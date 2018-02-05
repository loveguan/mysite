#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 信号量.py

@time: 2018/1/27 15:59

@desc:

'''

import threading, time


class myThread(threading.Thread):

	def run(self):
		if semaphore.acquire():
			print(threading.current_thread())
			print(self.name)
			time.sleep(0.6)
			semaphore.release()


if __name__ == "__main__":
	# 锁
	semaphore = threading.BoundedSemaphore(5)
	threads = []
	for i in range(100):
		threads.append(myThread())
	for i in threads:
		i.start()
