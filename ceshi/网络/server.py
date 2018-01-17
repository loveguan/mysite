#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: server.py

@time: 2018/1/15 20:53

@desc:socket rec接收到的回车不会执行，会一直阻塞等待，当客户端断开连接后rec收到的为空，解除阻塞状态

'''

"""
import socket

sk = socket.socket()
print(sk)
addr = ('localhost', 80)
sk.bind(addr)
sk.listen(3)
print('waiting!!!')
conn, addr = sk.accept()
print(conn)

while 1:
	rec = conn.recv(1024)
	# 解码
	print(addr)
	if not rec:
		conn.close()
		print('开始等待新的连接！！！')
		conn,addr=sk.accept()
		continue
	print('...'+str(rec, 'utf-8'))
	inp = input(">>")
	# conn.send(bytes(inp,'utf-8'))

sk.close()

"""

import socket

sk = socket.socket()
addr = ('localhost', 80)
sk.bind(addr)
sk.listen(3)

while 1:
	conn, add = sk.accept()
	print(add)
	while 1:
		print(add)

		try:
			rec = conn.recv(1024)
		except Exception:
			print('客户端断开连接！！！')
			break
		if not rec:
			# conn.close()
			print('等待新的连接！！！')
			break
		print('....' + str(str(rec, 'utf-8')))
		conn.send(rec)
sk.close()


