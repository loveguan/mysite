#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 递归锁1.py

@time: 2018/1/26 21:14

@desc:设置锁的粒度在最小处

'''

import threading
import time

mutex = threading.RLock()


class MyThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		self.fun1()
		time.sleep(1)
		self.fun2()

	def fun1(self):
		mutex.acquire()
		print(mutex)
		print("I am 1 %s,get res:  %s---%s" % (self.name, 'resa', time.time()))
		# time.sleep(0.3) # 加这句才能显示出死锁的效果
		mutex.acquire()
		print("I am 1 %s,get res:  %s---%s" % (self.name, 'resb', time.time()))
		mutex.release()
		mutex.release()

	def fun2(self):
		mutex.acquire()
		print("I am 2 %s,get res:  %s---%s" % (self.name, 'resb', time.time()))
		# time.sleep(0.2)
		mutex.acquire()
		print("I am 2 %s,get res:  %s---%s" % (self.name, 'resa', time.time()))
		mutex.release()
		mutex.release()


if __name__ == "__main__":
	print("start---------------------%s" % time.time())
	for i in range(0, 10):
		my_thread = MyThread()
		my_thread.start()
