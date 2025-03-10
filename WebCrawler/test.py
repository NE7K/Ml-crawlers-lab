import time
import datetime

resultTime = time.time()

resultTime2 = time.ctime(resultTime)

resultTime3 = time.localtime()

resultTime4 = time.strftime('%Y year %m month', resultTime3)

print(resultTime4)

name = 'kim'
print('%s 안녕하슈' %name)
print(f'헐러{name}걱')

datedate = datetime.datetime(2099, 9, 9)

print(datedate)