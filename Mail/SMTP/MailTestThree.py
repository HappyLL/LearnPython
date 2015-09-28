__author__ = 'Happyli'


pwd = 'zjq545529689'
#以html格式作为邮件内容发送(发送要推送的网址等)

import smtplib
from email.mime.text import MIMEText

from_addr = '545529689@qq.com'
from_pwd = pwd

to_addr = '3045138377@qq.com'

smtp_addr = 'smtp.qq.com'

sd_msg = MIMEText('<html><body><h1>Hello</h1><p><a href = "mail.qq.com">mail.qq.com</a></p></body></html>','html','utf-8')
sd_msg['From'] = from_addr
sd_msg['To'] = to_addr
sd_msg['Subject'] = 'LearnPython'

server = smtplib.SMTP()
server.connect(smtp_addr,25)
server.login(from_addr,from_pwd)
server.sendmail(from_addr,to_addr,sd_msg.as_string())
server.quit()






























