# 把下载好的逐日卫星图合成为 S02（8.5 秒，24fps，1920×1080）。
# 片中位置 0:01.5–0:10.0；素材内第 7.9 秒（片中 0:09.4）定格在最后一天。
# 用法：python3 make_satellite.py <卫星图文件夹> <字体文件夹> <输出文件夹>
import os
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC, FONTS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)

FPS = 24
W, H = 1920, 1080
SW, SH = 3840, 2160                     # source frames
BBOX = (23, 97, 32, 113)                # lat_min, lon_min, lat_max, lon_max
WEIXIN = (105.05, 27.84)                # lon, lat (county seat, Zhaxi)

TOTAL = 204                             # 8.5 s
FADE_IN = 6
PLAY_START = 7                          # first frame that advances the year
FREEZE = 190                            # 7.92 s into the clip = 0:09.4 in the film
ZOOM_START, ZOOM_END, ZOOM_MAX = 60, FREEZE, 3.0

days = sorted(f for f in os.listdir(SRC) if f.endswith(".jpg"))
assert len(days) >= 2, "no satellite frames found"


def src_xy(lon, lat):
    return ((lon - BBOX[1]) / (BBOX[3] - BBOX[1]) * SW, (BBOX[2] - lat) / (BBOX[2] - BBOX[0]) * SH)


WX, WY = src_xy(*WEIXIN)


def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def view_box(f):
    """Crop box in source pixels for output frame f (slow push towards Weixin)."""
    if f <= ZOOM_START:
        z = 1.0
    else:
        t = min(1.0, (f - ZOOM_START) / (ZOOM_END - ZOOM_START))
        z = 1.0 + (ZOOM_MAX - 1.0) * ease_out_cubic(t)
    cw, ch = SW / z, SH / z
    # Interpolate the centre from the frame centre to Weixin, then keep the box inside the image.
    k = (z - 1.0) / (ZOOM_MAX - 1.0)
    cx = SW / 2 + (WX - SW / 2) * k
    cy = SH / 2 + (WY - SH / 2) * k
    x0 = min(max(cx - cw / 2, 0), SW - cw)
    y0 = min(max(cy - ch / 2, 0), SH - ch)
    return x0, y0, x0 + cw, y0 + ch


def day_index(f):
    if f < PLAY_START:
        return 0
    span = FREEZE - PLAY_START
    return min(len(days) - 1, round((f - PLAY_START) * (len(days) - 1) / span))


mono = ImageFont.truetype(os.path.join(FONTS, "IBMPlexMono-Light.ttf"), 24)
mono_small = ImageFont.truetype(os.path.join(FONTS, "IBMPlexMono-Light.ttf"), 15)
sans = ImageFont.truetype(os.path.join(FONTS, "NotoSansCJKsc-Regular.otf"), 30)
sans_big = ImageFont.truetype(os.path.join(FONTS, "NotoSansCJKsc-Regular.otf"), 44)
sans_small = ImageFont.truetype(os.path.join(FONTS, "NotoSansCJKsc-Light.otf"), 16)
mono_en = ImageFont.truetype(os.path.join(FONTS, "IBMPlexMono-Light.ttf"), 19)
WHITE = (242, 242, 238, 230)
SOFT = (242, 242, 238, 190)


def shadowed(layer):
    """Two dark halos (tight + wide) so thin white type reads even over white cloud."""
    a = layer.split()[3]
    out = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    for radius, alpha in ((16, 130), (3, 230)):
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        sh.putalpha(a.filter(ImageFilter.MaxFilter(3)).point(lambda v, al=alpha: v * al // 255).filter(ImageFilter.GaussianBlur(radius)))
        out.alpha_composite(sh)
    out.alpha_composite(layer)
    return out


def scrim(box, opacity=0.42, blur=46):
    """Soft dark pad behind a text block; box = (x0, y0, x1, y1) in output pixels."""
    pad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(pad).rounded_rectangle(box, radius=40, fill=(8, 10, 12, int(255 * opacity)))
    return pad.filter(ImageFilter.GaussianBlur(blur))


def label_layer(date_text, frozen, box):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((64, 52), date_text, font=mono, fill=WHITE)
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    base.alpha_composite(scrim((24, 30, 300, 110), opacity=0.30, blur=28))
    if frozen:
        x0, y0, x1, y1 = box
        px = (WX - x0) / (x1 - x0) * W
        py = (WY - y0) / (y1 - y0) * H
        r = 17
        d.ellipse([px - r, py - r, px + r, py + r], outline=WHITE, width=2)
        # Leader line straight down from the ring to a text block sitting on the clear, dark ground below the cloud edge.
        line_end = py + 150
        d.line([(px, py + r + 4), (px, line_end)], fill=WHITE, width=2)
        tx, ty = px + 16, line_end - 6
        d.text((tx, ty), "威信", font=sans, fill=WHITE)
        d.text((tx, ty + 46), "年均 218 个雨日", font=sans_big, fill=WHITE)
        d.text((tx, ty + 104), "218 rain days a year, on average", font=mono_en, fill=SOFT)
        base.alpha_composite(scrim((24, H - 110, 1500, H - 30), opacity=0.30, blur=28))
        d.text((64, H - 86), "影像：NASA Worldview（VIIRS 逐日真彩色）｜雨日：中国气象局 1991–2020 气候平年值，日降水量 ≥0.1 毫米",
               font=sans_small, fill=SOFT)
        d.text((64, H - 60), "Imagery: NASA Worldview (VIIRS daily true colour) · Rain days: CMA 1991–2020 normals, ≥0.1 mm of precipitation",
               font=mono_small, fill=SOFT)
    base.alpha_composite(shadowed(layer))
    return base


tmp_l = os.path.join(OUT, "_frames_labels")
tmp_c = os.path.join(OUT, "_frames_clean")
os.makedirs(tmp_l, exist_ok=True)
os.makedirs(tmp_c, exist_ok=True)
cache = {}
for f in range(TOTAL):
    i = day_index(f)
    if i not in cache:
        cache.clear()
        cache[i] = Image.open(os.path.join(SRC, days[i])).convert("RGB")
    box = view_box(min(f, FREEZE))
    frame = cache[i].resize((W, H), Image.LANCZOS, box=box)
    if f < FADE_IN:
        frame = Image.blend(Image.new("RGB", (W, H), (0, 0, 0)), frame, (f + 1) / FADE_IN)
    frame.save(os.path.join(tmp_c, f"{f:04d}.png"))
    date_text = days[i][:10].replace("-", ".")
    labelled = frame.convert("RGBA")
    if f >= FADE_IN - 1:
        labelled.alpha_composite(label_layer(date_text, f >= FREEZE, box))
    labelled.convert("RGB").save(os.path.join(tmp_l, f"{f:04d}.png"))

for frames, name in [(tmp_l, "S02_satellite_year.mp4"), (tmp_c, "S02_satellite_year_clean.mp4")]:
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
                    "-i", os.path.join(frames, "%04d.png"),
                    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p",
                    os.path.join(OUT, name)], check=True)
    for fn in os.listdir(frames):
        os.remove(os.path.join(frames, fn))
    os.rmdir(frames)
print("first day:", days[0], "last day:", days[-1], "frames:", len(days))
