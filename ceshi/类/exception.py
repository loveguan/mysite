#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: exception.py

@time: 2018/1/12 13:49

@desc:

'''

"""
while True:
	try:
		inp = input('请输入序号：')
		i=int(inp)
	except Exception as e:
		print(e)
		i=1
	print(i)
"""
"""
try:
	raise Exception('bu guole .....')
except Exception as e:
	print(e)
"""

"""

def db():
	return False

def index():
	try:
		inp = input('>>')
		int(inp)
		result= db()
		if not result:
			raise Exception('数据库处理错误！！！')
	except Exception as e:
		str_error=str(e)
		# 处理字符串并加上换行符
		str_error='%s%s' %(str_error,'\n')
		print(str_error)
		f = open('log','a')
		f.write(str_error)
		f.close()

index()

"""

"""
# 自定义异常类

class OldBoyError(Exception):
	def __init__(self,msg):
		self.message = msg
	def __str__(self):
		return self.message

# obj = OldBoyError('test')
# print(obj)

try:
	raise  OldBoyError('my wrong')
except OldBoyError as e:
	print(e)
"""


