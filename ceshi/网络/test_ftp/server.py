#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: server.py.py

@time: 2018/1/18 17:03

@desc:

'''

"""
import socket
import os

# 初始的目录
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upload')
# 当前目录
CURRENT_DIR = BASE_DIR
# 消息
message = ''
# 文件大小
file_size = ''

sock = socket.socket()
addr = ('localhost', 80)
sock.bind(addr)
sock.listen(3)

while True:

	conn, addr = sock.accept()
	print(addr)
	print("当前连接：%s" % CURRENT_DIR)
	while True:

		try:
			recv = conn.recv(1024)
		except:
			print('客户端断开等待新的连接！！！')
			os.chdir(BASE_DIR)
			CURRENT_DIR = BASE_DIR
			break
		recv = str(recv, 'utf8')
		if not recv:
			print('客户端退出，等待新的连接！！！')
			CURRENT_DIR = BASE_DIR
			os.chdir(BASE_DIR)
			break
		cmd, name, size, chg_dir = recv.split('|')
		if cmd == 'cd':
			# 状态标识码
			ret_code = '1'
			try:
				# 切换到要切换的目录
				os.chdir(chg_dir)
				# 把目录改为当前切换到的目录
				CURRENT_DIR = chg_dir
			except:
				print('切换目录错误，目录不存在！！！')
				ret_code = '0'
			message = bytes("%s|%s" % (file_size, ret_code), 'utf8')
			conn.send(message)
			print(CURRENT_DIR)
		elif cmd=="get":
			print('put')
		elif cmd=="put":
			print('put')
"""

import socket
import os
import subprocess

# 初始的目录
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upload')
# 当前目录
CURRENT_DIR = BASE_DIR
# 消息
message = ''
# 文件大小
file_size = ''
# 反斜线分隔符
line_sep = os.sep

sock = socket.socket()
addr = ('localhost', 80)
sock.bind(addr)
sock.listen(3)

while True:

	conn, addr = sock.accept()
	conn.send(bytes(BASE_DIR, 'utf8'))

	print(addr)
	print("当前连接：%s" % CURRENT_DIR)
	while True:

		try:
			recv = conn.recv(1024)
		except:
			print('客户端断开等待新的连接！！！')
			os.chdir(BASE_DIR)
			CURRENT_DIR = BASE_DIR
			break
		recv = str(recv, 'utf8')
		if not recv:
			print('客户端退出，等待新的连接！！！')
			CURRENT_DIR = BASE_DIR
			os.chdir(BASE_DIR)
			break
		cmd, name, size = recv.split('|')
		name = name.strip()
		print(cmd, name)
		if cmd == 'cd':
			# 状态标识码
			ret_code = '1'
			# if
			if name == '':
				CHG_DIR = BASE_DIR
			# 判断是否有错误的输入有的话告警
			elif name.__contains__('/'):
				# 把name值取为一个不存在的值
				name = '1223233443refdfdf'
				CHG_DIR = os.path.join(CURRENT_DIR, name)
			# ..后退的情况
			elif name.startswith('..'):
				while name.startswith('..'):
					# 判断到根后的处理逻辑
					if CURRENT_DIR == BASE_DIR:
						# 将name赋值为空
						name = ''
						break
					rep_name = name[2:]
					if rep_name.startswith(line_sep) and len(rep_name) > 1:
						rep_name = rep_name[1:]
					CURRENT_DIR = os.path.dirname(CURRENT_DIR)
					name = rep_name
				CHG_DIR = os.path.join(CURRENT_DIR, name)
				# 去除最后边的\
				if CHG_DIR.endswith(line_sep):
					CHG_DIR = CHG_DIR[:-1]
				print(CHG_DIR)
			else:
				CHG_DIR = os.path.join(CURRENT_DIR, name)
				print(CHG_DIR)
			try:
				# 切换到要切换的目录
				os.chdir(CHG_DIR)
				# 把目录改为当前切换到的目录
				CURRENT_DIR = CHG_DIR
			except:
				print('切换目录错误，目录不存在！！！')
				ret_code = '0'
			message = bytes("%s|%s|%s" % (file_size, CURRENT_DIR, ret_code), 'utf8')
			conn.send(message)
			print(CURRENT_DIR)
		elif cmd == "get" and name is not None:
			file_save_path = os.path.join(BASE_DIR, name)
			if os.path.exists(file_save_path):
				file_size = os.stat(file_save_path).st_size
				ret_code = 0
				message = bytes("%s|%s" % (str(file_size), str(ret_code)), 'utf8')
				conn.send(message)
				# 放置粘包
				conn.recv(1024)
				has_send = 0
				with open(file_save_path, 'rb') as f:
					while has_send != file_size:
						data = f.read(1024)
						conn.send(data)
						has_send += len(data)
				print('%s 发送完成！！ ' %name)
			else:
				file_size = ''
				ret_code = '1'
				message = bytes("%s|%s" % (str(file_size), str(ret_code)), 'utf8')
				conn.send(message)
				print("等待新的命令！！！")
				# 跳出当前循环，执行下一个循环
				continue
		elif cmd == "put" and name is not None:
			file_save_path = os.path.join(BASE_DIR, name)
			print(file_save_path, size)
			conn.send(bytes("开始吧！！", 'utf8'))
			with open(file_save_path, 'wb') as f:
				has_recv = 0
				while has_recv != int(size):
					recv_file = conn.recv(1024)
					f.write(recv_file)
					has_recv += len(recv_file)
			if os.stat(file_save_path).st_size == int(size):
				print('ok,写入完成')
				# 回传客户端确认消息
				conn.send(bytes('ok', 'utf8'))
			else:
				print('error')

		else:

			err_flag = 0
			com = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			# 得到stdout和stderror的元组
			ret1 = com.communicate()
			if ret1[1]:
				message = ret1[1]
				err_flag = 1
			else:
				message = ret1[0]
			# 注意这里计算消息的长度，是二进制的长度
			message_size = len(message)
			# 发送要发送的大小和标志位（是否有错误的信息）
			msg_ret1 = "%s|%s" % (message_size, str(err_flag))
			conn.send(bytes(msg_ret1, 'utf8'))
			# 解决粘包
			conn.recv(1024)
			conn.send(message)
