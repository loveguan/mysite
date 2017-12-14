#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 待参数的被装饰函数.py

@time: 2017/11/28 8:00

@desc:

'''


import time

def show_time(func):
	def wrapper(a,b):
		start_time=time.time()
		func(a,b)
		end_time=time.time()
		print('spend %s %s'%(end_time-start_time))
	return wrapper

@show_time
def add(a,b):
	time.sleep(4)
	print(a+b)

add(2,4)