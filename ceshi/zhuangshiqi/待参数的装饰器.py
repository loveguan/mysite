#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 待参数的装饰器.py

@time: 2017/11/28 8:04

@desc:

'''

import time

def time_logger(flag=0):
	def show_time(func):
		def wrapper(*args,**kwargs):
			star_time=time.time()
			func(*args,*kwargs)
			end_time=time.time()
			if flag:
				print('记录到日志中去')
		return wrapper
	return show_time


@time_logger(3)
def add(*args,**kwargs):
	time.sleep(1)
	sum=0
	for i in args:
		sum+=i
	print(sum)

add(1,5,7,8)