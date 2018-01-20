#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: client.py

@time: 2018/1/17 20:58

@desc:

'''

import socket
import os

sk = socket.socket()
addr = ('localhost', 80)
sk.connect(addr)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
while True:

	inp = input(">>").strip()
	if not inp.count('|'):
		if inp == 'exit':
			print('客户端退出！！！')
			break
		else:
			print(inp)
			cmd = inp
			name = ''
			size = '1'
			file_info = "%s|%s|%s" % (cmd, name, size)
			sk.send(bytes(file_info, 'utf8'))
			message = sk.recv(1024)
			sk.send(bytes('ack!!!', 'utf8'))
			size = int(str(message, 'utf8'))
			has_recv = 0
			mes_rec = bytes()
			while has_recv != size:
				recv = sk.recv(1024)
				mes_rec += recv
				has_recv += len(recv)

			print(str(mes_rec, 'gbk'))
			continue
	else:
		try:
			cmd, name = inp.split('|')
			cmd = cmd.strip()
			name = name.strip()
		except Exception:
			print('输入错误，请重新输入help函数')
			continue

		if cmd == "put" and name is not '':
			path = os.path.join(BASE_DIR, name)
			size = os.stat(path).st_size
			file_info = "%s|%s|%s" % (cmd, name, size)
			sk.send(bytes(file_info, 'utf8'))
			sk.recv(1024)
			with open(path, 'rb') as f:
				has_read = 0
				while has_read != size:
					send_da = f.read(1024)
					sk.send(send_da)
					has_read += len(send_da)
				print('发送成功')
		elif cmd == 'get' and name is not '':
			down_path = os.path.join(BASE_DIR, 'download', name)
			size = '00'
			file_info = "%s|%s|%s" % (cmd, name, size)
			sk.send(bytes(file_info, 'utf8'))
			recv = sk.recv(1024)
			size = int(str(recv, 'utf8'))
			# 如果返回的文件大小为0，则说明文件不存在
			if size == 0:
				print('文件不存在！！！')
				continue
			print(size)
			sk.send(bytes('ok', 'utf8'))
			f = open(down_path, 'ab')

			has_recv = 0
			while has_recv != size:
				recv = sk.recv(1024)
				f.write(recv)
				has_recv += len(recv)
			f.close()
			print("接收完成！！！")

		elif cmd.strip() == 'cd':
			size = '1'
			file_info = "%s|%s|%s" % (cmd, name, size)
			sk.send(bytes(file_info, 'utf8'))
			message = sk.recv(1024)
			print(message)
			sk.send(bytes('ack!!!', 'utf8'))
			message = sk.recv(1024)
			print(str(message, 'utf8'))
		else:
			print('输入错误，请重新输入help函数查看用法')
			continue

sk.close()
