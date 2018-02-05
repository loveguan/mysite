#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 死锁.py

@time: 2018/1/26 21:03

@desc:

'''

import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()


class MyThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		self.fun1()
		self.fun2()

	def fun1(self):
		mutexA.acquire()
		print("I am %s,get res:  %s---%s" % (self.name, 'resa', time.time()))
		# time.sleep(0.1) # 加这句才能显示出死锁的效果
		mutexB.acquire()
		print("I am %s,get res:  %s---%s" % (self.name, 'resb', time.time()))
		mutexB.release()
		mutexA.release()

	def fun2(self):
		mutexB.acquire()
		print("I am %s,get res:  %s---%s" % (self.name, 'resa', time.time()))
		time.sleep(0.2)
		mutexA.acquire()
		print("I am %s,get res:  %s---%s" % (self.name, 'resb', time.time()))
		mutexA.release()
		mutexB.release()


if __name__ == "__main__":
	print("start---------------------%s" % time.time())
	for i in range(0, 10):
		my_thread = MyThread()
		my_thread.start()
