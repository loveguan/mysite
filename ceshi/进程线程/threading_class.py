#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: threading_class.py

@time: 2018/1/24 22:26

@desc:

'''
import threading


class myThreading(threading.Thread):
	def __init__(self, n):
		threading.Thread.__init__(self)
		self.num = n

	def run(self):
		print(threading.current_thread())
		print('running number is %s' % self.num)


if __name__ == '__main__':
	t1 = myThreading(1)
	t2 = myThreading(2)
	t1.start()
	# t2.start()
	t1.run()
	print(threading.current_thread())