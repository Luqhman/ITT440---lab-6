import socket
import os
import sys
import time
import errno
import math



s_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ""
port = 10000
try:
	s_sock.bind((host,port))
except socket.error as e:
	print(str(e))

print("Waiting for connection . .")
s_sock.listen(5)

while True:
	connec,address = s_sock.accept()
	connec.send(str.encode("Welcome to the calculator server\n"))
	data1 = connec.recv(2048)
	if data1 == 1:
		connec.send(str.encode("You choosing a log\n"))
		data2 = connec.recv(1024)
		answer = math.log(int(data2))
	elif data1 == 2:
		connec.send(str.encode("You choosing a Square root\n"))
		data2 = connec.recv(1024)
		answer = math.sqrt(int(data2))
	else:
		connec.send(str.encode("You choosing a Exponential\n"))
		data2 = connec.recv(1024)
		answer = math.exp(int(data2))
	if not data1:
		break

s_sock.close()



