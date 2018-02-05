#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 递归锁-2.py

@time: 2018/1/26 21:36

@desc:

'''
import threading

import time


class Account:
	def __init__(self, name,money):
		self.name=name
		self.balance = money
		self.lock=threading.RLock()

	def withdraw(self, num):
		print(self.name,'3', self.lock)
		self.lock.acquire()
		print(self.name,'1',self.lock)
		self.balance -= num
		time.sleep(3)
		self.lock.release()
		print(self.name,"5",self.lock)

	def repay(self, num):
		print(self.name,'4', self.lock)
		self.lock.acquire()
		print(self.name,"2",self.lock)
		self.balance += num
		time.sleep(0.1)
		self.lock.release()
		print(self.name,"6",self.lock)


def transer(_from, to, count):
	_from.withdraw(count)
	time.sleep(2)
	to.repay(count)

def b(_from, to, count):
	_from.withdraw(count)
	time.sleep(1)
	to.repay(count)



a1=Account('alex',1000)
a2=Account('xiaohu',2000)
thread_list=[]
t1=threading.Thread(target=transer,args=(a1,a2,200))
t2=threading.Thread(target=b,args=(a1,a2,100))
thread_list.append(t1)
thread_list.append(t2)
t1.start()
t2.start()
for t in thread_list:
	t.join()
print(a1.balance)
print(a2.balance)

