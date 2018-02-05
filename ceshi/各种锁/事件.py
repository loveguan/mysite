#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 事件.py

@time: 2018/1/28 21:32

@desc: 根据event执行

'''
import threading
import time


class Boss(threading.Thread):
	def run(self):
		print("boss :jiaban")
		event.is_set() or event.set()
		time.sleep(3)
		print("boss: xiabanle ")
		event.set()


class Worker(threading.Thread):
	def run(self):
		print("1",self.name, event.is_set())
		event.wait()
		print("2",self.name, event.is_set())
		print('woker daomei jiaban')
		time.sleep(1)
		event.clear()
		print(self.name,event.is_set())
		event.wait()
		print("3",'worker: xiabanle')


if __name__ == "__main__":
	event = threading.Event()
	event2=threading.Event()
	print(event,event2)
	threads = []
	for i in range(5):
		threads.append(Worker())
	threads.append(Boss())
	for t in threads:
		t.start()
