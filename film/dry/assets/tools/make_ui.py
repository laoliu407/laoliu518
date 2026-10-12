# 生成《干》的界面素材：计数器、片名、片尾卡。
# 所有 PNG 都是 1920×1080 全画幅，透明底（片尾卡为黑底），放到剪辑时间线上不用再对位。
# 用法：python3 make_ui.py <字体文件夹> <输出文件夹>
import os
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080

SERIF = os.path.join(FONTS, "NotoSerifSC-Regular.ttf")
SERIF_BOLD = os.path.join(FONTS, "NotoSerifSC-SemiBold.ttf")
SANS = os.path.join(FONTS, "NotoSansCJKsc-Regular.otf")
SANS_LIGHT = os.path.join(FONTS, "NotoSansCJKsc-Light.otf")
MONO = os.path.join(FONTS, "IBMPlexMono-Light.ttf")
MONO_REG = os.path.join(FONTS, "IBMPlexMono-Regular.ttf")

UI_WHITE = (242, 242, 238)
AMBER = (227, 168, 87)
CARD_BG = (13, 15, 17, 255)


def font(path, size):
    return ImageFont.truetype(path, size)


def with_shadow(layer, radius=6, alpha=90):
    """Soft dark halo so thin white type stays readable over bright fog."""
    a = layer.split()[3]
    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    shadow.putalpha(a.point(lambda v: v * alpha // 255).filter(ImageFilter.GaussianBlur(radius)))
    base = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    base.alpha_composite(shadow)
    base.alpha_composite(layer)
    return base


def text_right(draw, right_x, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((right_x - w, y), text, font=fnt, fill=fill)


def text_center(draw, cy, text, fnt, fill, cx=W / 2):
    l, t, r, b = draw.textbbox((0, 0), text, font=fnt)
    draw.text((cx - (r - l) / 2 - l, cy - (b - t) / 2 - t), text, font=fnt, fill=fill)


MONTHS = {
    "JAN": "一月", "FEB": "二月", "AUG": "八月", "OCT": "十月", "DEC": "十二月",
}

# Counter block anchored bottom-right: 64px from the right edge, 56px from the bottom.
RIGHT = W - 64
BOTTOM = H - 56


def counter_layer(month, number, opacity=0.88):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fill = UI_WHITE + (int(255 * opacity),)
    f_label = font(SANS_LIGHT, 22)
    f_num = font(MONO, 48)
    f_en = font(MONO, 15)
    text_right(d, RIGHT, BOTTOM - 22, f"{month} · RAIN DAY", f_en, fill)
    text_right(d, RIGHT, BOTTOM - 86, f"{number:03d}", f_num, fill)
    text_right(d, RIGHT, BOTTOM - 118, f"{MONTHS[month]}｜雨日", f_label, fill)
    return with_shadow(layer)


def sun_layer():
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fill = AMBER + (240,)
    text_right(d, RIGHT, BOTTOM - 178, "日照 +0.001 小时", font(SANS, 26), fill)
    text_right(d, RIGHT, BOTTOM - 146, "SUNSHINE +0.001 HRS", font(MONO, 15), fill)
    return with_shadow(layer)


for month, number in [("JAN", 1), ("FEB", 31), ("AUG", 131), ("AUG", 132),
                      ("DEC", 207), ("DEC", 217), ("DEC", 218)]:
    counter_layer(month, number).save(os.path.join(OUT, f"counter_{month}_{number:03d}.png"))
sun_layer().save(os.path.join(OUT, "counter_FEB_sun.png"))

# October run: 164 -> 183 at 24fps. 6-frame fade in, 19 jumps across 3.5s,
# hold 1s, 8-frame fade out (matches 1:53.5–1:58.3 in the cut).
FPS = 24
frames_dir = os.path.join(OUT, "_oct_frames")
os.makedirs(frames_dir, exist_ok=True)
fade_in, run, hold, fade_out = 6, 84, 24, 8
total = fade_in + run + hold + fade_out
cache = {}
for i in range(total):
    if i < fade_in:
        n, op = 164, (i + 1) / fade_in
    elif i < fade_in + run:
        n, op = 164 + min(19, int((i - fade_in) * 19 / run) + 1), 1.0
    elif i < fade_in + run + hold:
        n, op = 183, 1.0
    else:
        n, op = 183, 1 - (i - fade_in - run - hold + 1) / fade_out
    key = n
    if key not in cache:
        cache[key] = counter_layer("OCT", n)
    frame = cache[key].copy()
    frame.putalpha(frame.split()[3].point(lambda v, o=op: int(v * o)))
    frame.save(os.path.join(frames_dir, f"{i:04d}.png"))

subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
                "-i", os.path.join(frames_dir, "%04d.png"),
                "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le",
                os.path.join(OUT, "counter_OCT_164-183.mov")], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
                "-i", f"color=c=0x00FF00:s={W}x{H}:r={FPS}",
                "-framerate", str(FPS), "-i", os.path.join(frames_dir, "%04d.png"),
                "-filter_complex", "[0][1]overlay=shortest=1,format=yuv420p",
                "-c:v", "libx264", "-crf", "12", "-preset", "slow",
                os.path.join(OUT, "counter_OCT_164-183_green.mp4")], check=True)
for f in os.listdir(frames_dir):
    os.remove(os.path.join(frames_dir, f))
os.rmdir(frames_dir)

# Title: 干 / DRY, centred a little above the middle of the frame.
title = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(title)
text_center(d, H / 2 - 30, "干", font(SERIF_BOLD, 112), UI_WHITE + (255,))
f_dry = font(MONO_REG, 26)
spaced = "D R Y"
text_center(d, H / 2 + 62, spaced, f_dry, UI_WHITE + (235,))
with_shadow(title, radius=10, alpha=110).save(os.path.join(OUT, "title_gan_DRY.png"))


def card(lines):
    """lines: list of (text, font, rgba, gap_after); rgba None keeps the line's space but draws nothing."""
    img = Image.new("RGBA", (W, H), CARD_BG)
    d = ImageDraw.Draw(img, "RGBA")
    heights = []
    for text, fnt, _, gap in lines:
        l, t, r, b = d.textbbox((0, 0), text, font=fnt)
        heights.append((b - t, gap))
    total_h = sum(h + g for h, g in heights)
    y = (H - total_h) / 2
    for (text, fnt, rgba, gap), (h, _) in zip(lines, heights):
        if rgba is not None:
            text_center(d, y + h / 2, text, fnt, rgba)
        y += h + gap
    return img


WHITE = UI_WHITE + (255,)
SOFT = UI_WHITE + (170,)
DIM = (150, 156, 162, 255)
f46, f20 = font(SERIF, 46), font(SERIF, 20)

line1 = [("威信县 · 年均 218 个雨日", f46, WHITE, 14),
         ("Weixin County · 218 rain days a year, on average", f20, SOFT, 0)]
line2 = [("县级非物质文化遗产 · 干辣椒制作", f46, WHITE, 14),
         ("County-level Intangible Cultural Heritage · Making Dried Chili", f20, SOFT, 0)]

# card_facts_1 keeps line 1 exactly where it sits on card_facts_2, so a straight cut between them does not jump.
both = card(line1[:1] + [(line1[1][0], f20, SOFT, 64)] + line2)
first_only = card(line1[:1] + [(line1[1][0], f20, SOFT, 64)] + [(t, f, None, g) for t, f, _, g in line2])
first_only.save(os.path.join(OUT, "card_facts_1.png"))
both.save(os.path.join(OUT, "card_facts_2.png"))

f52, f22 = font(SERIF_BOLD, 52), font(SERIF, 22)
card([("由雷大卷辣椒面制作", f52, WHITE, 16),
      ("Made by Thunder Roll Chili", f22, SOFT, 0)]).save(os.path.join(OUT, "card_brand.png"))

print("done")
