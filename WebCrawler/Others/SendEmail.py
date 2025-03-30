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


# info 메일에 첨부파일 첨가하고 싶으면
# import smtplib
# from email.mime.text import MIMEText
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart

# text = "메일 내용입니다"
# msg = MIMEMultipart()
# msg['Subject'] ="이것은 메일제목"
# msg['From'] = '보내는자이메일'
# msg['To'] = '받는자이메일또는이름'
# msg.attach(MIMEText(text))
# print(msg.as_string())

# #원하는 파일 rb로 오픈
# with open('보낼파일경로', 'rb') as 파일:
#   part = MIMEBase('application', 'octet-stream')
#   part.set_payload(파일.read())

# #파일 base64 인코딩
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', 'attachment; filename="경로제외보낼파일명"')
# msg.attach(part)

# s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
# s.starttls()
# s.login( '네이버아이디' , '비번' ) 
# s.sendmail( '보내는사람', '받는사람', msg.as_string() ) 
# s.close()