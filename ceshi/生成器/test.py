#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2017/11/30 16:10

@desc:

'''

def f():
	print('ok')
	yield 1

	print('1')
	yield 2

d=f()
print(d)
print(next(d))
print(d)
next(d)