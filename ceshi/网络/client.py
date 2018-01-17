#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: client.py

@time: 2018/1/15 20:56

@desc:

'''

import socket

sk = socket.socket()
addr = ('localhost', 80)
sk.connect(addr)

while 1:
	# 编码
	inp = input(">>")
	if inp == 'exit': break
	sk.send(bytes(inp, 'utf-8'))
	rec = sk.recv(1024)
	print(str(rec, 'utf-8'))
sk.close()
