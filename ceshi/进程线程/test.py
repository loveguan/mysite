#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2018/1/24 22:38

@desc:

'''
class a:
	def __init__(self):
		print('chushihua')
		print(self)
	def c(self):
		print('ceshi')

class b(a):
	def __init__(self):
		a.__init__(self)
		a.c(self)

b=b()
print(b)

