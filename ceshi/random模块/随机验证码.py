#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 随机验证码.py

@time: 2017/12/2 21:56

@desc:

'''
import random


def v_code():
	code = ''
	for i in range(5):
		if 1 == random.choice([1, 2]):
			add = random.randrange(10)
		else:
			add = chr(random.randrange(65, 91))
		code += str(add)
	print(code)

v_code()