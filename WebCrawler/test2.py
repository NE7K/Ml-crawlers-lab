# note rename
import os
# note copy file
import shutil

FileList = os.listdir('testFile')

# for i in os.listdir('testFile'):
#     os.rename(f'testFile/{i}', f'testFile/a{i}')

# note 절대경로 = r
for i in os.listdir('testFile'):
    shutil.copy(f'testFile/{i}', f'testFile2/{i}')
    
# 경로 합치기
os.path.join()

# 지금 경로
os.getcwd()