#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: tongbusuo.py

@time: 2018/1/26 20:51

@desc:

'''

import time
import threading

def addNum():
	global num
	temp=num
	print('ok')
	time.sleep(0.1)
	num=temp-1

num=100

thread_list=[]

for i in range(100):
	t=threading.Thread(target=addNum())
	t.start()
	thread_list.append(t)
# for t in thread_list:
# 	t.join()

print('Result:',num)