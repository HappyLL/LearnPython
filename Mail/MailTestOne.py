__author__ = 'Happyli'


import time
from email.mime.text import MIMEText
msg = MIMEText('send by 十三姨夫.', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = '545529689@qq.com'
# shisanyifu1987@sina.com
password = '********'
# 输入收件人地址:
to_addr = ['362493352@qq.com','3045138377@qq.com','617745699@qq.com']
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

import smtplib
server = smtplib.SMTP() # SMTP协议默认端口是25
server.connect(smtp_server)
#server.set_debuglevel(1)

server.login(from_addr, password)
num = 0
while True:
    server.sendmail(from_addr, to_addr, msg.as_string())
    num = num + 1
    print('the num %d mail has sended to %s ' % (num,to_addr))
    time.sleep(60)
server.close()

