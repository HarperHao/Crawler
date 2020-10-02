import pytesseract
from PIL import Image

# 加载图片
img = Image.open('yzm1.jpg')
# 识别文字
str = pytesseract.image_to_string(img)
print(str)
