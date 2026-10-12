# 把 ChatGPT 出的 3:2 关键帧处理成"纪录片底片"，再交给 Grok 生成视频。
# 做的事：裁成 16:9 → 放大到 1920×1080 → 去掉过度锐化和 HDR 感 → 略降饱和与对比。
# 不加噪点：颗粒留到剪辑时统一加，否则视频模型会把噪点当成纹理，生成蠕动的颗粒。
# 用法：python3 doc_look.py 输入图片 输出图片 [裁切的垂直位置 0–1，默认 0.5 居中]
import sys
import numpy as np
from PIL import Image, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
vpos = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5

im = Image.open(src).convert("RGB")
w, h = im.size
ch = round(w * 9 / 16)
if ch < h:
    top = round((h - ch) * vpos)
    im = im.crop((0, top, w, top + ch))
im = im.resize((1920, 1080), Image.LANCZOS)

# 1) Kill sharpening halos and "clarity": a light blur blended back in.
soft = im.filter(ImageFilter.GaussianBlur(1.1))
im = Image.blend(im, soft, 0.55)

a = np.asarray(im).astype(np.float32) / 255.0

# 2) Gentle global contrast reduction around mid-grey, with highlights rolled off a little.
a = 0.5 + (a - 0.5) * 0.90
a = np.where(a > 0.80, 0.80 + (a - 0.80) * 0.65, a)

# 3) Desaturate about 15% (luma-preserving).
luma = (0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2])[..., None]
a = luma + (a - luma) * 0.85

Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)).save(dst)
