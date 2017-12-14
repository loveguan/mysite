#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2017/11/30 8:08

@desc:

'''
auth_user=''
auth_pass=''
with open('auth','r') as f:
	for i in f:
		if i.startswith('user'):
			auth_user=i.lstrip('user=').replace('\'','').strip()
		elif i.startswith('passwd'):
			auth_pass=i.strip('passwd=').replace('\'','').strip()
print(auth_user)
print(auth_pass)