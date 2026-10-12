# 下载一年的逐日卫星真彩色影像（NASA GIBS 公开数据），隔一天取一张，结束日固定为定格那一天。
# 用法：python3 get_year.py 2024-03-04 183 out
#   第 1 个参数：结束日（定格帧），第 2 个参数：张数，第 3 个参数：输出文件夹
# 需要：Python 3 和 Pillow（pip install pillow）
import sys, os, datetime, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

end = datetime.date.fromisoformat(sys.argv[1])
count = int(sys.argv[2])
out = sys.argv[3]
os.makedirs(out, exist_ok=True)

W, H = 3840, 2160                      # 16:9，留出推镜头的余量
BBOX = (23, 97, 32, 113)               # 北纬 23–32°、东经 97–113°（WMS 1.3.0 的 EPSG:4326 先纬度后经度）
LAYERS = ["VIIRS_SNPP_CorrectedReflectance_TrueColor",
          "VIIRS_NOAA20_CorrectedReflectance_TrueColor",
          "MODIS_Aqua_CorrectedReflectance_TrueColor"]   # 前一颗卫星缺图就换下一颗
URL = ("https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap"
       "&VERSION=1.3.0&LAYERS={L}&STYLES=&FORMAT=image/jpeg&CRS=EPSG:4326"
       "&BBOX={b[0]},{b[1]},{b[2]},{b[3]}&WIDTH={w}&HEIGHT={h}&TIME={t}")

def black_ratio(im):
    h = im.convert("L").histogram()
    return sum(h[:8]) / sum(h)

def fetch(day):
    path = os.path.join(out, day.isoformat() + ".jpg")
    if os.path.exists(path):
        return day, "cached"
    for layer in LAYERS:
        tmp = path + ".part"
        for attempt in range(4):
            try:
                urllib.request.urlretrieve(URL.format(L=layer, b=BBOX, w=W, h=H, t=day.isoformat()), tmp)
                break
            except Exception:
                if attempt == 3:
                    raise
        im = Image.open(tmp).convert("RGB")
        if black_ratio(im) < 0.25:
            os.replace(tmp, path)
            return day, layer
    os.replace(tmp, path)
    return day, "gappy:" + layer

days = [end - datetime.timedelta(days=2 * i) for i in range(count)][::-1]
with ThreadPoolExecutor(max_workers=6) as pool:
    for day, layer in pool.map(fetch, days):
        print(day.isoformat(), layer, flush=True)
