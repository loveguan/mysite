#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 条件变量.py

@time: 2018/1/27 16:26

@desc:wait acquire release

'''
import threading
from random import randint
import time

class Producer(threading.Thread):

	def run(self):
		global L
		while True:
			val = randint(1, 100)
			print('生产者', self.name, "Append" + str(val), L)
			if lock_con.acquire():
				L.append(val)
			lock_con.notify()
			lock_con.release()
			time.sleep(3)

class Consumer(threading.Thread):

	def run(self):
		global L
		while True:
			print('ok1')
			lock_con.acquire()
			if len(L)<1:
				lock_con.wait()
			print('ok!!!!!')
			print('消费者', self.name, "del" + str(L[0]),L)
			while len(L)>0:
				del L[0]
			lock_con.release()
			time.sleep(0.25)

if __name__ == '__main__':

	L = []
	# 注意这把锁
	lock_con = threading.Condition()
	threads = []
	threads.append(Consumer())
	for i in range(5):
		threads.append(Producer())
	# threads.append(Consumer())

	for t in threads:
		t.start()

