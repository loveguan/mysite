#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 队列.py

@time: 2018/1/28 21:58

@desc:

'''

import threading
import time
import queue
from random import randint


class Producer(threading.Thread):
	def run(self):
		while True:
			if qu.qsize() < 5:
				a = randint(1, 99)
				print('producer', a)
				qu.put(a)


class Consumer(threading.Thread):
	def run(self):
		while True:
			if qu.qsize() > 0:
				print('consumer!!!', qu.get())


if __name__ == '__main__':
	qu = queue.Queue()
	threads = []
	for i in range(5):
		threads.append(Producer())
	threads.append(Consumer())
	for t in threads:
		t.start()
