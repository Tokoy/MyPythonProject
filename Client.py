#-*-coding:utf-8-*-
import sys,socket,threading,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接：
s.connect(('localhost',9999))
# 接收欢迎消息：
print s.recv(1024)
while True:
  data=raw_input()
  s.send(data)
  print s.recv(1024)
