#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: server.py

@time: 2018/1/22 14:44

@desc:

'''

import socketserver
class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		conn = self.request
		client_addr = self.client_address
		print(client_addr)
		conn.sendall(bytes('duoxiancheng','utf8'))
		Flag = True
		while Flag:
			data = conn.recv(1024)
			if str(data,'utf8') == 'exit':
				Flag = False
			conn.sendall(data)

if __name__=='__main__':
	server=socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
	server.serve_forever()