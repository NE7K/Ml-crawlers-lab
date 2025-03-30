# note smtp 사용
import smtplib
from email.mime.text import MIMEText
 
# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# info html import
from email.mime.multipart import MIMEMultipart

# .env file load
load_dotenv()

# info html 기반 email 보내려고 할 때
msg = MIMEMultipart('alternative')
내용 = """
<h4> 테스트임 ㄷㄷ </h4>
<button> 버튼 띠 </button>
"""
part1 = MIMEText(내용, "html")
msg.attach(part1)

# info 그냥 텍스트만 보내려고 할 때
# text = os.getenv('context')
# msg = MIMEText(text) 
 
msg['Subject'] = os.getenv('title')
msg['From'] = os.getenv('email')
msg['To'] = os.getenv('post')
print(msg.as_string())
 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls() #TLS 보안 처리
s.login( os.getenv('id') , os.getenv('pw') ) # 네이버로그인
s.sendmail( os.getenv('email'), os.getenv('post'), msg.as_string() )
s.close()