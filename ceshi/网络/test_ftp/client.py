#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: client.py

@time: 2018/1/18 17:03

@desc:

'''
"""
import socket
import os

BASE_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),'upload')
CURRENT_DIR=BASE_DIR
CHG_DIR=''

addr=('localhost',80)
sk=socket.socket()
sk.connect(addr)

# 命令中要处理的文件的大小
file_size=''
# 命令中要处理的文件名
file_name=''


while True:

	inp=input(">>")

	if len(inp.split(" "))==1:
		inp=inp+" "
	# 分割字符串
	cmd,file_name=inp.split(' ')
	# 去掉多于的空格
	cmd=cmd.strip()
	file_name=file_name.strip()
	if cmd=='cd':
		# 只有cd命令，不带切换目录，默认到根目录
		if file_name=='':
			CHG_DIR=BASE_DIR
		# ..后退的情况
		elif file_name.startswith("..\\"):
			while file_name.startswith('..'):
				rep_name = file_name.replace("..\\", "", 1)
				CURRENT_DIR = os.path.dirname(CURRENT_DIR)
				file_name = rep_name
			CHG_DIR=os.path.join(CURRENT_DIR,file_name)
		else:
			CHG_DIR=os.path.join(CURRENT_DIR,file_name)
		# 处理流程
		file_info="%s|%s|%s|%s" %(cmd,file_name,file_size,CHG_DIR)
		# 发送相关的信息
		sk.send(bytes(file_info,'utf8'))
		ret=str(sk.recv(1024),'utf8')
		size,ret_code=ret.split('|')
		# 判断切换成功后把当前目录改为切换的目录
		if int(ret_code)==1:
			CURRENT_DIR=CHG_DIR
		print(CURRENT_DIR)
	elif cmd=="exit":
		break
	else:
		# 命令执行通道
		pass

"""

import socket
import os

addr = ('localhost', 80)
sk = socket.socket()
sk.connect(addr)

# 命令中要处理的文件的大小
file_size = ''
# 命令中要处理的文件名
file_name = ''

first_rev = sk.recv(1024)
BASE_DIR = str(first_rev, 'utf8')
CURRENT_DIR = BASE_DIR
CHG_DIR = ''

# 上传文件存放路径
save_path_name = 'download'
UP_DOWN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), save_path_name)

while True:
	log_msg='实现ftp上传下载!!!支持命令：dir，cd，cd..，get name,put name'
	print(log_msg)
	inp = input(">>")
	if len(inp.strip()) == 0:
		print('请输入有效的命令！！！')
		continue
	if len(inp.split(" ")) == 1:
		inp = inp + " "
	# 分割字符串
	cmd, file_name = inp.split(' ')
	# 去掉多余的空格
	cmd = cmd.strip()
	file_name = file_name.strip()
	if cmd == 'cd':
		"""
		# 只有cd命令，不带切换目录，默认到根目录
		if file_name=='':
			CHG_DIR=BASE_DIR
		# ..后退的情况
		elif file_name.startswith("..\\"):
			while file_name.startswith('..'):
				rep_name = file_name.replace("..\\", "", 1)
				CURRENT_DIR = os.path.dirname(CURRENT_DIR)
				file_name = rep_name
			CHG_DIR=os.path.join(CURRENT_DIR,file_name)
		else:
			CHG_DIR=os.path.join(CURRENT_DIR,file_name)
		"""

		# 处理流程
		file_info = "%s|%s|%s" % (cmd, file_name, file_size)
		# 发送相关的信息
		sk.send(bytes(file_info, 'utf8'))
		ret = str(sk.recv(1024), 'utf8')
		size, CHG_DIR, ret_code = ret.split('|')
		# 判断切换成功后把当前目录改为切换的目录
		if int(ret_code) == 1:
			CURRENT_DIR = CHG_DIR
		else:
			print('目录不存在！！！！')
		# print(CURRENT_DIR)
	elif cmd == "exit":
		break
	elif cmd == 'put':

		if file_name:
			file_name_local = os.path.join(UP_DOWN_DIR, file_name)
			if os.path.exists(file_name_local):
				# 获取上传文件的大小
				file_size = os.stat(file_name_local).st_size
				file_info = "%s|%s|%s" % (cmd, file_name, str(file_size))
				# 信息给server
				sk.send(bytes(file_info, 'utf8'))
				# 阻塞等待server的确认信息，防止粘包
				ret = str(sk.recv(1024), 'utf8')
				with open(file_name_local, 'rb') as f:
					has_send = 0
					while has_send != file_size:
						file_read = f.read(1024)
						sk.send(file_read)
						has_send += len(file_read)
				# 根据server的返回消息确认上传是否成功
				if str(sk.recv(1024), 'utf8') == 'ok':
					print('发送完成！！！！')
				else:
					print('上传出错，请重传！！！')
			else:
				print("%s dose not exise!!!!" % file_name)
		else:
			print('error,usage: put filename!!!!')
			continue
	elif cmd == 'get':
		if file_name:
			file_size = ''
			file_info = "%s|%s|%s" % (cmd, file_name, str(file_size))
			# 信息给server
			sk.send(bytes(file_info, 'utf8'))
			# 阻塞等待server的确认信息，防止粘包
			ret = str(sk.recv(1024), 'utf8')
			file_size, ret_code = ret.split('|')
			if int(ret_code):
				print("%s 文件不存在！！！" % file_name)
				continue
			else:
				sk.send(bytes('ok', 'utf8'))
				file_size = int(file_size)
				file_name_local = os.path.join(UP_DOWN_DIR, file_name)
				has_recv = 0
				with open(file_name_local, 'ab') as f:
					while has_recv != file_size:
						data = sk.recv(1024)
						f.write(data)
						has_recv += len(data)

				print('%s 接受完成！！ ' % file_name)
		else:
			print('usage: get filename')
	else:
		# 命令执行通道
		file_info = "%s|%s|%s" % (cmd, file_name, file_size)
		sk.send(bytes(file_info, 'utf8'))
		# 获取
		msg_ret1 = str(sk.recv(1024), 'utf8')
		message_size, err_flag = msg_ret1.split('|')
		sk.send(bytes('I ok!!', 'utf8'))
		print(err_flag)
		print(message_size)
		if int(err_flag):
			print('错误的不存在的命令！！！！')
		message_size = int(message_size)
		# 发送过来的为二进制，重点
		msg_ret2 = bytes()
		while len(msg_ret2) != message_size:
			msg_ret2 += sk.recv(1024)
		print('执行完成！！！！')
		print(str(msg_ret2, 'gbk'))
