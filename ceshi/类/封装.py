#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 封装.py

@time: 2018/1/14 22:43

@desc:

'''
class F1:
	def __init__(self):
		self.name=123

class F2:
	def __init__(self,a):
		self.ff=a
class F3:
	def __init__(self,b):
		self.dd=b

f1=F1()
f2=F2(f1)
f3=F3(f2)
print(f3)
print(f3.dd)
print(f3.dd.ff)
print(f3.dd.ff.name)