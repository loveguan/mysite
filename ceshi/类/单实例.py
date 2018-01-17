#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 单实例.py

@time: 2018/1/14 22:48

@desc:

'''


class Foo:
	__v = None

	@classmethod
	def get_instance(cls):
		if cls.__v:
			return cls.__v
		else:
			cls.__v = Foo()
			return cls.__v


obj1 = Foo.get_instance()
obj2 = Foo.get_instance()
print(obj1,obj2)
