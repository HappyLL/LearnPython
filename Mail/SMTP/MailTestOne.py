__author__ = 'Happyli'


#所以当我们在发送邮件时 首先要知道当前的源邮件地址 目标邮件地址 要知道当前的邮件传输代理(即smtp服务器地址)
#通过连接 和 验证 即可发送邮件
#该例子是向目标地址发送文本内容
pwd = 'zjq545529689'
# import time
# from email.mime.text import MIMEText
# #MIMEText表示邮件的文本格式
# msg = MIMEText('send by 十三姨夫.', 'plain', 'utf-8')
#
# # 输入Email地址和口令:
# from_addr = '545529689@qq.com'
# # shisanyifu1987@sina.com
# password = '********'
# # 输入收件人地址:
# to_addr = ['362493352@qq.com','3045138377@qq.com','617745699@qq.com']
# # 输入SMTP服务器地址:
# smtp_server = 'smtp.qq.com'
#
# import smtplib
# server = smtplib.SMTP() # SMTP协议默认端口是25
# server.connect(smtp_server)
# #server.set_debuglevel(1)
#
# server.login(from_addr, password)
# num = 0
# while True:
#     server.sendmail(from_addr, to_addr, msg.as_string())
#     num = num + 1
#     print('the num %d mail has sended to %s ' % (num,to_addr))
#     time.sleep(60)
# server.close()

# class email.mime.text.MIMEText(_text[, _subtype[, _charset]])：MIME文本对象，其中_text是邮件内容，_
# subtype邮件类型，可以是text/plain（普通文本邮件），html/plain(html邮件),  _charset编码，可以是gb2312等等。
import time
import smtplib
from email.mime.text import MIMEText

sd_msg = MIMEText('send by 十三姨夫',_subtype='plain',_charset='utf-8')

from_addr = '545529689@qq.com'
from_pwd = pwd

to_addr = '3045138377@qq.com'
#MTA(SMTP服务器地址)
smtp_addr = "smtp.qq.com"

#类似于创建一个Socket 并与对应的地址建立连接
smtp = smtplib.SMTP()
smtp.connect(smtp_addr)
#另一种与smtp服务器连接的方法
#smtp = smtplib.SMTP(smtp_addr,25)

#当当前的进程与smtp端连接成功后 然后需要的smtp的身份验证
smtp.login(from_addr,from_pwd)

#发送信息 注意要将当前的信息转化为字符创
smtp.sendmail(from_addr,to_addr,sd_msg.as_string())
smtp.quit()










































