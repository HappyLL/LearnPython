__author__ = 'Happyli'


import socket

#面向UDP的服务器进程 流协议 SOCK_DGRAM
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',9999))
#服务端用recvfrom 来接收数据 和对方的IP和端口地址
while True:
    data,addr = server.recvfrom(1024)
    print('%s:%s' % addr)
