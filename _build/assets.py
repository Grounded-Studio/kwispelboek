"""Builds images, favicons, OG images and the Nunito woff2 subset for the site."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from fontTools import subset

SITE = Path(__file__).resolve().parent.parent
SHOTS = Path(sys.argv[1])
APP = Path(r"C:\huisdierlogboek\assets")
IMG = SITE / "assets" / "img"
FONTS = SITE / "assets" / "fonts"

# Screenshots -> webp, 540px wide
for lang in ("nl", "en"):
    for n in ("today", "pets", "profile", "health", "agenda", "add", "party", "card", "done"):
        im = Image.open(SHOTS / f"{n}_{lang}.png").convert("RGB")
        im = im.resize((540, round(540 * im.height / im.width)), Image.LANCZOS)
        im.save(IMG / f"{n}-{lang}.webp", quality=84, method=6)

# Icons
icon = Image.open(APP / "branding" / "app_icon.png").convert("RGB")
def rounded(im, size, radius_frac=0.225):
    im = im.resize((size, size), Image.LANCZOS).convert("RGBA")
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size * 4, size * 4), radius=int(size * 4 * radius_frac), fill=255)
    im.putalpha(mask.resize((size, size), Image.LANCZOS))
    return im
rounded(icon, 256).save(IMG / "icon.webp", quality=90)
rounded(icon, 512).save(SITE / "icon-512.png")
rounded(icon, 192).save(SITE / "icon-192.png")
icon.resize((180, 180), Image.LANCZOS).save(SITE / "apple-touch-icon.png")
rounded(icon, 48).save(SITE / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
rounded(icon, 32).save(SITE / "favicon-32.png")

# Fonts: Nunito latin subset as woff2
unicodes = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2190-2193,U+2212"
for w in ("Regular", "SemiBold", "Bold", "ExtraBold", "Black"):
    subset.main([str(APP / "fonts" / f"Nunito-{w}.ttf"), f"--unicodes={unicodes}", "--flavor=woff2",
                 f"--output-file={FONTS / f'nunito-{w.lower()}.woff2'}", "--layout-features=*"])

# OG images 1200x630
CREAM, INK, TERRA, SAGE, SAND = "#F2F6F9", "#1C2B36", "#2B7A9E", "#3FA36C", "#DCEEF6"
def font(w, s): return ImageFont.truetype(str(APP / "fonts" / f"Nunito-{w}.ttf"), s)
copy = {
    "nl": ("Vaccinaties, ontworming & medicijnen", "op tijd, voor elk huisdier.", "Binnenkort · Android"),
    "en": ("Vaccinations, deworming & medication", "on time, for every pet.", "Coming soon · Android"),
}
names = {"nl": "Kwispelboek", "en": "Wagbook"}
for lang, (l1, l2, pill) in copy.items():
    og = Image.new("RGB", (1200, 630), CREAM)
    d = ImageDraw.Draw(og)
    d.ellipse((-260, 330, 420, 1010), fill=SAND)
    d.ellipse((900, -220, 1400, 280), fill="#FFF1D6")
    og.paste(rounded(icon, 132), (70, 108), rounded(icon, 132))
    d.text((66, 262), names[lang], font=font("Black", 88), fill=INK)
    d.text((72, 372), l1, font=font("SemiBold", 32), fill="#5B6B78")
    d.text((72, 414), l2, font=font("SemiBold", 32), fill="#5B6B78")
    f = font("ExtraBold", 26)
    tw = d.textlength(pill, font=f)
    d.rounded_rectangle((70, 478, 70 + tw + 52, 530), radius=26, fill=TERRA)
    d.text((96, 486), pill, font=f, fill="white")
    shot = Image.open(SHOTS / f"today_{lang}.png").convert("RGB")
    w = 300; h = round(w * shot.height / shot.width)
    shot = shot.resize((w, h), Image.LANCZOS)
    frame = Image.new("RGB", (w + 24, h + 24), INK)
    fmask = Image.new("L", frame.size, 0)
    ImageDraw.Draw(fmask).rounded_rectangle((0, 0, *frame.size), radius=46, fill=255)
    smask = Image.new("L", shot.size, 0)
    ImageDraw.Draw(smask).rounded_rectangle((0, 0, *shot.size), radius=36, fill=255)
    frame.paste(shot, (12, 12), smask)
    og.paste(frame, (800, 40), fmask)
    og.save(IMG / f"og-{lang}.jpg", quality=88)
print("ok")
