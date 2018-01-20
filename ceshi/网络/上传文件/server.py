#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: server.py

@time: 2018/1/17 20:57

@desc:

'''

import os
import socket
import subprocess
import sys

sk = socket.socket()
addr = ('localhost', 80)
sk.bind(addr)
sk.listen(3)
print('waiting')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
SEP = os.sep
file_upload_path = "%s%s%s" % (BASE_DIR, SEP, 'upload')
cur_path = file_upload_path
flag = True
while 1:
	conn, add = sk.accept()
	print('新的连接 %s' % (str(add)))
	while 1:
		try:
			rec = conn.recv(1024)
		except:
			conn.close()
			print('客户端已断开，等待新的连接！！！')
			flag = True
			cur_path = file_upload_path
			break
		if not rec:
			print('等待新的连接！！！')
			flag = True
			cur_path = file_upload_path
			break

		file_info = str(rec, 'utf8')
		cmd, name, size = file_info.split("|")
		# print(cmd)
		# print(name)
		# print(size)

		size = int(size)
		if cmd.strip() == "put" and name is not '':
			conn.send(bytes("ok!!!", 'utf8'))
			has_rec = 0
			file_path = os.path.join(BASE_DIR, 'upload', name)
			print(file_path)
			f = open(file_path, 'ab')
			while has_rec != size:
				recv = conn.recv(1024)
				f.write(recv)
				has_rec += len(recv)
			f.close()
		elif cmd.strip() == 'get' and name is not '':
			try:
				file_path = os.path.join(BASE_DIR, 'upload', name)
				file_size = os.stat(file_path).st_size
			except:
				# 文件不存在，返回文件大小为0
				file_size = 0
				conn.send(bytes(str(file_size), 'utf8'))
				continue
			conn.send(bytes(str(file_size), 'utf8'))
			conn.recv(1024)

			with  open(file_path, 'rb') as f:
				has_read = 0
				while file_size != has_read:
					send_data = f.read(1024)
					conn.send(send_data)
					has_read += len(send_data)
				print('发送完成！！！')
		elif cmd.strip() == 'cd' and name is not '':
			print(name)
			# 默认信息！！！
			mess = 'ok!!!'
			file_path = os.path.join(BASE_DIR, 'upload',name)

			try:
				os.chdir(file_path)
			except:
				mess='%s目录不存在' %name
				os.chdir(cur_path)
			cur_path = file_path
			print(os.curdir)
			file_size = 10
			conn.send(bytes(str(file_size), 'utf8'))
			conn.recv(1024)
			print(mess)
			conn.send(bytes(mess, 'utf8'))
		else:
			cmd = cmd.replace('\\', '').strip()
			print(cmd)
			os.chdir(cur_path)
			if flag:
				os.chdir(file_upload_path)
				flag = False
			if cmd == 'cd':
				os.chdir(file_upload_path)
				cur_path = file_upload_path
			com = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			# 得到stdout和stderror的元组
			ret1 = com.communicate()
			print(str(ret1[0], 'gbk'))

			if ret1[1]:
				message = bytes('命令不存在', 'gbk')
				print(message)
			elif cmd == 'cd':
				message = bytes('切换到根目录,upload！！！', 'gbk')
			else:
				message = ret1[0]

			size = len(message)
			conn.send(bytes(str(size), 'utf8'))
			conn.recv(1024)
			conn.send(message)
