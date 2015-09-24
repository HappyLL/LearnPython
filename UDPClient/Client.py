__author__ = 'Happyli'


import socket
# UDP 不需要建立连接 只需要知道目标地址 和端口即可
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(b'udp send',('127.0.0.1',9999))