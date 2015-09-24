__author__ = 'Happyli'


import socket
import threading
import time

def tcplink(sock,addr):
    print('there is new client %s:%s connected' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024).decode('utf-8')
        time.sleep(5)
        if data and data != 'exit':
            data = 'Hello '+data
            sock.send(data.encode('utf-8'))
        else:
            break
    sock.close()
    print('there is old client %s:%s closed ' % addr)

# 服务端程序需要利用socket绑定当前的服务端监听端口和对应的IP地址(客户端用socket建立连接时需要知道服务端的地址和端口)
serversk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversk.bind(('127.0.0.1',9999))
# 监听的最大个数
serversk.listen(5)
# 服务端利用socket 使得该进程绑定(对应的端口 和 IP地址) 然后服务端程序对该端口进行监听 且当有客户端根据该端口和ip
# 通过socket建立连接时 则当前的服务器与客户端建立连接 且每一个客户端他的socket 和 address
# 都不相同 所以我们根据此 创建不同的线程来处理每个客户端的数据请求
print('waiting for connection ....')
while True:
    sock, addr = serversk.accept()
    nthread = threading.Thread(target=tcplink,args=(sock,addr))
    nthread.start()






