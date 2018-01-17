#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2017/8/20 18:59

@desc:

'''



"""
death_age = 80
age = input('your age:')
print('you can live for ',death_age-int(age),'years')
print('you can live for '+ str(death_age-int(age))+' years')
"""

#
# age_of_princal = 56
#
# gusess_age=int(input(">>:"))
# if gusess_age == age_of_princal:
#     print('ok!')
# else:
#     print('wrongs')


"""
class Foo:
	def __init__(self):
		self.name='a'
	def bar(self):
		# self是对象
		print('bar')
	@staticmethod
	def sta():
		print('123')
	@staticmethod
	def stat(a1,a2):
		print(a1,a2)
	@classmethod
	def classmd(cls):
		# cls 是类名
		print(cls)
		print('clasmd')
Foo.sta()
Foo.stat(1,2)
Foo().sta()
Foo.classmd()

"""
"""
class Foo:
	def __init__(self):
		self.name='a'
		self.name_list=['alex']
	def bar(self):
		print('bar')
	@property
	def perr(self):
		return 123
	@perr.setter
	def perr(self,val):
		print(val)
	@perr.deleter
	def perr(self):
		print('666')
obj = Foo()
print(obj.perr) # 获取值
obj.perr=45  # 赋值
del obj.perr  # 删除值

"""

class Pergination:
	def __init__(self,current_page):
		try:
			p=int(current_page)
		except:
			p=1

		self.page=p
	@property
	def start(self):
		val=(self.page-1)*10
		return val
	@property
	def end(self):
		val=self.page*10
		return val
li=[]
for i in range(1000):
	li.append(i)
while True:
	p=input('输入要查看的页码：').strip()
	obj = Pergination(p)
	print(li[obj.start:obj.end])

