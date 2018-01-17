#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: ip_scan.py

@time: 2018/1/17 10:13

@desc:

'''

import socket
from run import main


def ip_scan(ip, port, log_type):
	'''

	:param ip:
	:param port:
	:param log_type: 传入log对象
	:return:
	'''
	try:
		addr = (ip, int(port))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = s.connect_ex(addr)
		if result == 0:
			# print('[ OK  ] ip: %s, port: %s is open' % (ip, port))
			# define log
			log_type.info('ip: %s, port: %s is open' % (ip, port))
		else:
			log_type.error('ip: %s, port: %s is closed' % (ip, port))
			main.Flag_err = True
	except Exception:
		print('端口扫描异常！！！！')
