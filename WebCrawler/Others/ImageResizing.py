#note image resize import - how to use ? > pip install Pillow
from PIL import Image
#note image insert list
import os

#info 이미지 흑백으로 열려면 .convert('L)
# img = Image.open('Images/photo1.jpg').convert('L')
# img.thumbnail((500, 2500))
# img.save(r'Images/photo{i}')

# insert list
filepath = os.getcwd()
dir = os.listdir(filepath + '/Images')
print(dir)

# 예를 들어서 파일 100만개를 전부다 리사이징하고 싶을 때
# for i in range(100):
#     img = Image.open(f'Images/photo{i}.jpg')
#     img.thumbnail((500, 2500))
#     img.save(f'Imgaes/new_photo{i}.jpg')
    

#info 이미지 리사이즈해서 담아두면 화질 깨짐
# img = img.resize((300,500))

#info 이미지 리사이즈 비율 유지 > 가상의 박스를 만들어서 그 안에다가 사진을 넣는다는 느낌
# img.thumbnail((300, 500))

# img = img.crop((50,50, 150,150))


#info images quality 0 ~ 95, high = best quality | if .png > use quantize option 
#info maybe png > jpg : open(jpg) save(jpg)
#info progressive=True > 이미지 웹상에서 빠르게 불러오기
# img.save('Images/new_photo1.jpg', quality=75, progressive=True)

