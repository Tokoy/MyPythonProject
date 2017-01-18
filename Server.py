#-*-coding:utf-8-*-
import sys,threading,time,socket


def tcplink(conn,addr):
  print ('Accept new connection form {0}'.format(addr))
  conn.send('Welcome!')
  while True:
    data = conn.recv(1024)
    time.sleep(1)
    if data == 'exit' or not data:
      break
    else:
      conn.send('hi'+format(data))
  conn.close()
  print ('Connection from {0} closed.',format(addr))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立套接字
s.bind(('localhost',9999))
s.listen(5)
print 'Waiting for connection...'
while True:
  # 接受一个新连接
  conn,addr = s.accept()
  # 创建一个新线程处理TCP连接
  t = threading.Thread(target=tcplink, args=(conn, addr))
  t.start()
