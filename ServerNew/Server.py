__author__ = 'Happyli'


# 该进程为服务器进程 对服务器进程编写需要注意
# 需要利用创建服务端的socket来绑定对应地址 和 端口 并监听
# 需要利用服务端的socket来接收来自客户端的连接
# 每有一个客户端链接 服务端需要创建一个线程来处理该客户端的请求

import socket
import threading
import time

#addr 包括当前客户端的IP 和客户端的端口
def doclientfunc(sock,addr):
    print('new client connection & addr is %s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        #阻塞
        data = sock.recv(1024)
        time.sleep(1)

        data = data.decode('utf-8')
        if not data or data == 'exit':
            break
        #print(data)
        sock.send(('Hello '+data).encode('utf-8'))

    sock.close()
    print('old client disconnection & addr is %s:%s' %addr)

serversk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversk.bind(('127.0.0.1', 9999))
serversk.listen(5)
print('Wating for connection')
while True:
    # 接收来自客户端的socket 和 地址
    sock, addr = serversk.accept()
    nwthread = threading.Thread(target=doclientfunc,args=(sock,addr))
    nwthread.start()

