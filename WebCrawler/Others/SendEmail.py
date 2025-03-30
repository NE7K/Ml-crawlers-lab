# note smtp 사용
import smtplib
from email.mime.text import MIMEText
 
# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

text = os.getenv('context')
msg = MIMEText(text) 
 
msg['Subject'] = os.getenv('title')
msg['From'] = os.getenv('email')
msg['To'] = os.getenv('post')
print(msg.as_string())
 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls() #TLS 보안 처리
s.login( os.getenv('id') , os.getenv('pw') ) # 네이버로그인
s.sendmail( '발송자이메일', '수신자이메일', msg.as_string() )
s.close()