from PIL import Image
from pathlib import Path

# 1) 여기만 네 표지 파일명으로 바꿔줘 (원본 파일을 프로젝트 루트에 잠깐 두자)
SRC = Path("asset/covers/originals/selected_001_original.jpg")



# 2) 결과 파일명 (asset/covers/ 아래로 저장)
DST = Path("asset/covers/selected_001.jpg")


TARGET_W = 900  # 웹용 가로폭(픽셀). 800~1000 사이면 충분히 선명함

img = Image.open(SRC).convert("RGB")
w, h = img.size
if w > TARGET_W:
    new_h = int(h * (TARGET_W / w))
    img = img.resize((TARGET_W, new_h), Image.LANCZOS)

DST.parent.mkdir(parents=True, exist_ok=True)
img.save(DST, format="JPEG", quality=78, optimize=True, progressive=True)

print("Saved:", DST)