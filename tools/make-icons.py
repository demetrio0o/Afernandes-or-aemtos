"""Gera todos os ícones a partir de assets/logo.png.
Uso (precisa do Pillow):  python tools/make-icons.py
"""
from PIL import Image, ImageDraw
import os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logo = Image.open(os.path.join(root, "assets", "logo.png")).convert("RGBA")
logo = logo.crop(logo.getbbox())

def fit(canvas, frac):
    """Centraliza o logo ocupando 'frac' do lado do canvas."""
    s = canvas.size[0]
    k = s * frac / max(logo.size)
    l = logo.resize((max(1, round(logo.width * k)), max(1, round(logo.height * k))), Image.LANCZOS)
    canvas.alpha_composite(l, ((s - l.width) // 2, (s - l.height) // 2))
    return canvas

def rounded_white(size, frac):
    bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(bg).rounded_rectangle((0, 0, size - 1, size - 1), radius=int(size * .22), fill=(255, 255, 255, 255))
    return fit(bg, frac)

b = os.path.join(root, "build"); a = os.path.join(root, "assets")
os.makedirs(b, exist_ok=True)

# PC
icon = rounded_white(1024, .66)
icon.save(os.path.join(b, "icon.png"))
icon.save(os.path.join(b, "icon.ico"), sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])

# Android (@capacitor/assets)
Image.new("RGBA", (1024, 1024), (255, 255, 255, 255)).save(os.path.join(a, "icon-background.png"))
fit(Image.new("RGBA", (1024, 1024), (0, 0, 0, 0)), .50).save(os.path.join(a, "icon-foreground.png"))
only = Image.new("RGBA", (1024, 1024), (255, 255, 255, 255)); fit(only, .62)
only.save(os.path.join(a, "icon-only.png"))
for name, color in (("splash.png", (255, 255, 255, 255)), ("splash-dark.png", (0, 0, 0, 255))):
    fit(Image.new("RGBA", (2732, 2732), color), .30).save(os.path.join(a, name))
print("ok")
