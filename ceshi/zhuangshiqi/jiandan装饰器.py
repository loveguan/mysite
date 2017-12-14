#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: jiandan装饰器.py

@time: 2017/11/28 7:50

@desc:

'''

import time

def show_time(func):
	def wrapper():
		start_time=time.time()
		func()
		end_time=time.time()
		print('spend %s'%(end_time-start_time))

	return  wrapper

@show_time
def foo():
	print('hello foo')
	time.sleep(3)


foo()
