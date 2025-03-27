#note image resize import - how to use ? > pip install Pillow
from PIL import Image

img = Image.open('Images/photo1.jpg')
#info 이미지 리사이즈해서 담아두면 화질 깨짐
img = img.resize((300,500))

img.save('Images/new_photo1.jpg')