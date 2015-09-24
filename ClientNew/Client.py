__author__ = 'Happyli'

import socket


#客户端要做的是连接服务端的地址和端口号

clientsk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsk.connect(('127.0.0.1', 9999))

namelist = [b'Happy',b'Lisa',b'Week']

data = clientsk.recv(1024)
print(data.decode('utf-8'))
for name in namelist:
    clientsk.send(name)
    data = clientsk.recv(1024)
    print(data.decode('utf-8'))
clientsk.send(b'exit')
clientsk.close()