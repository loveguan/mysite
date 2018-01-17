#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: cmd_client.py

@time: 2018/1/16 12:32

@desc:

'''

import socket

sk = socket.socket()
addr = ('localhost', 80)
sk.connect(addr)

while 1:
	inp = input(">>")
	if inp == 'exit': break
	# 发送执行的命令
	sk.send(bytes(inp, 'utf8'))
	# 获取要接收的数据的长度
	data_len = int(str(sk.recv(1024), 'utf8'))
	# 解决粘包问题
	sk.send(bytes("ok,数据长度收到！！！",'utf8'))
	# 接收数据
	data = bytes()
	while data_len != len(data):
		data += sk.recv(1024)
	# window默认的编码格式为dbk
	print(str(data, 'gbk'))
