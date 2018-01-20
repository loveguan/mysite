#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: cmd_server.py

@time: 2018/1/16 12:32

@desc:

'''

import socket
import subprocess

sk = socket.socket()
addr = ('localhost', 80)
sk.bind(addr)
sk.listen(3)

while 1:
	conn, add = sk.accept()
	# 新的客户端连接进来后，堵塞等待客户端发送数据
	msg = "新的连接%s" % str(add)
	print(msg)
	while 1:
		try:
			rec = conn.recv(1024)
		except Exception:
			conn.close()
			print('客户端已经断开，等待新的连接！！！')
			break
		if not rec:
			print('客户端退出！！！')
			break

		# 编码为utf8格式
		str1 = str(rec, 'utf8')
		# 执行命令行的方式，返回值由于在window执行，window编码格式为gbk
		com = subprocess.Popen(str1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# 得到stdout和stderror的元组
		ret1 = com.communicate()
		# 获取数据,判断输出错误是否存在，存在的话将错误信息赋值给data
		if ret1[1]:
			err_str = ret1[1]
			# 赋值给error 给 data，解码为gbk
			data = err_str
		# data = bytes(err_str, 'gbk')
		else:
			data = ret1[0]
		# 获取数据的长度
		lenth = len(data)
		# 发送数据的长度给客户端
		conn.send(bytes(str(lenth), 'utf8'))
		# 解决粘包(服务端客户端同时设置)
		conn.recv(1024)
		# 发送返回值
		conn.send(data)

sk.close()
