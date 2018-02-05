#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: client.py.py

@time: 2018/1/22 14:45

@desc:

'''

import socket
ip_port = ('127.0.0.1',8009)
sk = socket.socket()
sk.connect(ip_port)
while True:
    data = sk.recv(1024)
    print('receive:',str(data,'utf8'))
    inp = input('please input:')
    sk.sendall(bytes(inp,'utf8'))
    if inp == 'exit':
    	break
sk.close()