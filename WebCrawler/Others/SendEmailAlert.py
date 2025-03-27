#info smtp 방식 사용

import smtplib
from email.mime.text import MIMEText

# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()
 
text = "메일 내용입니다"
msg = MIMEText(text) 
 
msg['Subject'] ="이것은 메일제목"
msg['From'] = os.getenv('id')
msg['To'] = os.getenv('poset')
print(msg.as_string())
 
s = smtplib.SMTP( '네이버smtp주소' , 포트번호 ) 
s.starttls() #TLS 보안 처리
s.login( os.getenv('id') , os.getenv('pw') ) #네이버로그인
s.sendmail( os.getenv('email'), os.getenv('post'), msg.as_string() )
s.close()