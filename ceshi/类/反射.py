#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 反射.py

@time: 2018/1/14 20:06

@desc:

'''

"""

# 对象反射（getattr，setattr）
class Foo:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def show(self):
		return "%s-%s" %(self.name,self.age)
	def __int__(self):
		return 'int'
	def __str__(self):
		return  'uuu'

obj =Foo('alex',18)
print(obj)

# getattr
# hasattr
# setattr
# delattr

# 通过字符串的形式操作对象中的成员

func =getattr(obj,'show')
print(func)
ret=func()
print(ret)
# 判断是否存在值
print(hasattr(obj,'name'))
# 设置对象的一个值
setattr(obj,'k1','v1')
print(getattr(obj,'k1'))
print(obj.name)
# 删除对象的一个值
delattr(obj,'name')
# print(obj.name)

"""

"""
# 类反射

class Foo:
	stat = '123'
	def __init__(self,name,age):
		self.name=name
		self.age=age
# 通过字符串的形式操作对象（类）中的成员
r=getattr(Foo,'stat')
print(r)
"""

"""
# 模块反射

import S2

# 通过字符串的形式调用模块中的属性
print(getattr(S2,'NAME'))
print(getattr(S2,'func')())

# 引入模块中的class
print(getattr(S2,'Foo'))
cls=getattr(S2,'Foo')
obj = cls()
print(obj.name)
"""


