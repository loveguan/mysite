#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: Example_reflect.py

@time: 2018/1/14 20:40

@desc:反射的应用

'''

import S2

while True:

	inp = input('>>')

	if hasattr(S2, inp):
		ret = getattr(S2, inp)
		print(ret())
	else:
		print('wrong!!')
