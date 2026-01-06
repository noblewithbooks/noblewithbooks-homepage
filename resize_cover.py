from PIL import Image
from pathlib import Path

# 1) 원본 이미지 경로
SRC = Path("asset/kpipa/kpipa-kbook-author-02_original.jpg")

# 2) 결과 이미지 경로
DST = Path("asset/kpipa/kpipa-kbook-author-02.jpg")

TARGET_W = 900  # 웹용 가로폭(픽셀)

img = Image.open(SRC).convert("RGB")
w, h = img.size
if w > TARGET_W:
    new_h = int(h * (TARGET_W / w))
    img = img.resize((TARGET_W, new_h), Image.LANCZOS)

DST.parent.mkdir(parents=True, exist_ok=True)
img.save(DST, format="JPEG", quality=85, optimize=True, progressive=True)

print("Saved:", DST)
