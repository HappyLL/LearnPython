__author__ = 'Happyli'



#当前邮件功能发送邮件的主题 发送邮件的地址 和 邮件寄到的目标地址
#且只要在当前的邮件文本上的 To From Subject 即可
pwd = 'zjq545529689'
















#发送邮件步骤: 确定 源地址 目标地址 MTA地址 连接MTA 验证身份 发送邮件

import smtplib
from email.mime.text import MIMEText

from_addr = '545529689@qq.com'
from_pwd = pwd

to_addr = '3045138377@qq.com'

smtp_addr = 'smtp.qq.com'

sd_msg = MIMEText('正在学习python','plain','utf-8')

sd_msg['From'] = from_addr
sd_msg['To'] = to_addr
sd_msg['Subject'] = 'Python'

server = smtplib.SMTP()
server.connect(smtp_addr)

server.login(from_addr,from_pwd)
server.sendmail(from_addr,to_addr,sd_msg.as_string())
server.quit()

