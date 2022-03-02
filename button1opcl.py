import socket
import struct
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
host=('10.0.0.25',8000)
try:
   s.connect(host)
except socket.error:
    print('Failed to creat socket')
    sys.exit()
print('socket created')
bulb1=":BP01\r\n".encode()
bulb2=":BP00\r\n".encode()
for i in range(1000):
    s.sendall(bulb1)
    time.sleep(1)
    data=s.recv(1024)
    print(data)
    if data==b':BP01;BPOK\r\n\r\n->':
        s.sendall(bulb2)
        time.sleep(1)
        data2=s.recv(1024)
        print(data2)
    i=i+1
    print(i)