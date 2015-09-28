__author__ = 'Happyli'

pwd = 'zjq545529689'
























# #发送附件
#
# import smtplib
# from email.mime.multipart import MIMEMultipart,MIMEBase
# from email.mime.text import MIMEText
# from email import encoders
#
# from_addr = '545529689@qq.com'
# from_pwd  = pwd
#
# to_addr = '3045138377@qq.com'
#
# smtp_addr = 'smtp.qq.com'
#
# sd_msg = MIMEMultipart()
# sd_msg['From'] = from_addr
# sd_msg['To'] = to_addr
# sd_msg['Subject'] = 'learnPython'
#
#
#
# with open('E:\\python\\test.png','rb') as f:
#     attch_msg = MIMEBase('application', 'octet-stream')
#     attch_msg.add_header('Content-Disposition','attachment',filename='test.png')
#     attch_msg.add_header('Content-ID','<0>')
#     attch_msg.set_payload(f.read())
#     encoders.encode_base64(attch_msg)
#     sd_msg.attach(attch_msg)
#
# #加上这一行 则邮件不带附件 且直接显示cid对应的内容
# sd_msg.attach(MIMEText('<html><body><img src = "cid:0"/></body></html>','html','utf-8'))
#
# server = smtplib.SMTP()
# server.connect(smtp_addr,25)
# server.login(from_addr,from_pwd)
# server.sendmail(from_addr,to_addr,sd_msg.as_string())
# server.close()














# 带附件发送
import time
import smtplib
from email.encoders import encode_base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase

from_addr = '18868803201@163.com'
from_pwd = '02256332'

to_addr = ['412542414@qq.com','3045138377@qq.com']
smtp_addr = 'smtp.163.com'

sd_msg = MIMEMultipart()
sd_msg['From'] = from_addr
#sd_msg['To'] = str(to_addr[0]),str(to_addr[1])
sd_msg['Subject'] = '请吃饭...请吃饭 '
sd_msg.attach(MIMEText('请吃饭...请吃饭......', 'plain', 'utf-8'))


# 读取时要用二进制格式
# with open('E:\\python\\test.png','rb') as f:
#     attach_msg = MIMEBase('application','octet-stream')
#     attach_msg.add_header('Content-Disposition','attachment',filename = 'test.png')
#     attach_msg.set_payload(f.read())
#     encode_base64(attach_msg)
#     sd_msg.attach(attach_msg)

server = smtplib.SMTP()
server.connect(smtp_addr, 25)
server.login(from_addr,from_pwd)
num = 0
while True:
    num = num + 1
    server.sendmail(from_addr,to_addr,sd_msg.as_string())
    print('the num %d mail has sended to %s ' % (num,to_addr))
    time.sleep(60)













