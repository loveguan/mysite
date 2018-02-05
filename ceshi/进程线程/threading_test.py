#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: threading_test.py

@time: 2018/1/22 21:34

@desc:

'''

import threading
import time


def music(n):
	print(threading.current_thread())
	for i in range(n):
		print('开始听音乐')
		time.sleep(2)
		print('听音乐结束！！！')


def movie(n):
	print(threading.current_thread())
	for i in range(n):
		print('开始看电视')
		time.sleep(3)
		print('看电视结束！！！')


threads = []
thread1 = threading.Thread(target=music, args=(2,))
thread2 = threading.Thread(target=movie, args=(2,))

threads.append(thread1)
threads.append(thread2)
# thread1.start()
# thread2.start()
print('start time %s' % time.time())
for i in threads:
	# setDaemon的用法是不必等待子线程结束，如果主线程结束的化，自动结束
	i.setDaemon(True)
	i.start()
thread2.join()
# 查看当前线程
print(threading.current_thread())
# 查看当前活跃线程的数量
print(threading.active_count())
print('end %s' % time.time())
