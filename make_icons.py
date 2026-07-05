from PIL import Image, ImageDraw

def make_icon(size, path, maskable=False):
    img = Image.new("RGB", (size, size), "#b5502e")
    d = ImageDraw.Draw(img)
    pad = size * 0.30 if maskable else size * 0.18
    # simple shoe silhouette: sole + upper, drawn with basic shapes
    w, h = size, size
    cx, cy = w / 2, h / 2
    sole_y0 = cy + h * 0.10
    sole_y1 = cy + h * 0.22
    d.rounded_rectangle(
        [pad, sole_y0, w - pad, sole_y1],
        radius=(sole_y1 - sole_y0) / 2,
        fill="#f4ede6",
    )
    upper_pts = [
        (pad + w * 0.04, sole_y0),
        (pad + w * 0.04, cy - h * 0.10),
        (pad + w * 0.16, cy - h * 0.22),
        (w - pad - w * 0.10, cy - h * 0.18),
        (w - pad, cy - h * 0.02),
        (w - pad, sole_y0),
    ]
    d.polygon(upper_pts, fill="#f4ede6")
    lace_x0 = pad + w * 0.22
    lace_x1 = w - pad - w * 0.16
    for i in range(3):
        y = cy - h * 0.14 + i * (h * 0.09)
        d.line([(lace_x0, y), (lace_x1, y - h * 0.02)], fill="#b5502e", width=max(1, int(size * 0.018)))
    img.save(path, "PNG")

make_icon(192, "icons/icon-192.png")
make_icon(512, "icons/icon-512.png")
make_icon(512, "icons/icon-512-maskable.png", maskable=True)
print("done")
