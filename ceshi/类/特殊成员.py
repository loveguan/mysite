#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 特殊成员.py

@time: 2018/1/11 15:25

@desc:

'''

'''
class Foo:
	def __init__(self,name,age):
		self.name = name
		# self.age = age
		self.__age=age # 私有外部不可以访问
	def show(self):
		return self.__age

obj = Foo('xiaoming',9)
print(obj.name)
# print(obj.__age)  # error
print(obj.show())
'''

"""
# 私有方法和属性只有类本身可以访问，继承的类也不可以访问，外部不可以直接访问
class F:
	def __init__(self):
		self.ge = 123
		self.__gene = 1234
	def show(self):
		print(self.__gene)


class S(F):
	def __init__(self, name):
		self.name = name
		self.__age = 19
		super(S, self).__init__()


	def show(self):
		print(self.name)
		print(self.__age)
		print(self.ge)
		super(S,self).show()
		# print(self.__gene)


s = S("xiaoming")
s.show()
"""

"""
class  Foo:
	# 对象初始话使用
	def __init__(self,name,age):
		self.name=name
		self.age=age

	# 对象（）或者类（）（）自动执行对象加括号
	def __call__(self, *args, **kwargs):
		print('class call ')
# 	string 格式化字符串，自定义输出格式
	def __str__(self):
		s = "%s %d" %(self.name,self.age)
		return s
	# int(对象)
	def __int__(self):
		return 1111



foo=Foo('name',18)
print(foo,type(foo))
# int对象调用
# a=int(foo)
# print(a)
# foo()
# Foo()()
i=str(foo)
print(i)
print(foo.__dict__)
print(Foo.__dict__)
"""
"""
class Foo:
	def	__init__(self,name,age):
		self.name=name
		self.age=age
	# 	这里是自定义的方法
	def __add__(self, other):
		# return self.age+other.age
		return Foo(self.name,other.age)

obj1=Foo('xiaoming',30)
obj2=Foo('dagang',30)
a=obj1+obj2
print(a)
print(a.name,a.age)
"""
"""
class Foo:
	def	__init__(self,name,age):
		self.name=name
		self.age=age
		self.value=100

obj=Foo('xiaoming',30)
# dict
print(obj.__dict__)
print(Foo.__dict__)
"""
"""
静态私有变量还是只能在类的内部访问
class Foo:
	__v='123'
	def __init__(self):
		pass
	def show(self):
		return Foo.__v
	@staticmethod
	def stat():
		return Foo.__v
	v1=__v
# print(Foo.show()) # 错误不是静态方法
print(Foo.stat())
# print(Foo.__v) cuowu
print(Foo.v1)
ret=Foo().show()
print(ret)
ret1 = Foo().stat()
print(ret1)

"""
"""
私有方法，只能在类内部使用
class Foo:
	def __f1(self):
		return 123
	def f2(self):
		r = self.__f1()
		return r

obj = Foo()
# print(obj.__f1) # 错误静态方法只能内部访问
print(obj.f2())
"""
"""
# __int__方法  __str__方法，对象调用，返回值给对象
class Foo:
	def __init__(self):
		self.name='joj'
	def __int__(self):
		return 111
	def __str__(self):
		return 'alex'

obj = Foo()
print(obj,type(obj))
# int对象，自动执行对象的__int__方法，并将返回值赋值给int对象
r =int(obj)
print(r)
# str对象，自动执行str方法，发挥至赋值给str对象
i=str(obj)
print(i)
print(obj.name)
print(obj)
"""

"""
__str__方法
class Foo:
	def __init__(self,n,a):
		self.name=n
		self.age=a
	def __str__(self):
		return '%s-%s' %(self.name,self.age)
obj = Foo('joj',32)
print(obj) #print(str(obj))  obj中的__str__,并获取其返回的值

"""
"""
class Foo:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def __add__(self,other):
		return Foo(self.name,other.age) #拼接一个新的

	def __del__(self):
		print('析构方法') #对象被销毁时，自动执行

obj1 = Foo('alex',19)
obj2 = Foo('eirc',66)
r=obj1+obj2 #两个对象想加的时，自动执行第一个对象的__add__方法，并将第二个对象当作参数传入
print(r,type(r))
print(r.name,r.age)

"""

"""
class Foo:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __getitem__(self, item):
		return item+10
	def __setitem__(self, key, value):
		print(key,value)
	def __delitem__(self, key):
		print(key)
li = Foo('alex',18)
print(li)
r=li[8] #通过这种方式调用，自动执行li对象的类中的__getitem__方法，8当作参数传递给item
print(r)
li[100]='addas' #diaoyong setitem method

del li[999]
"""
"""
class Foo:
	def __init__(self,name,age):
		self.name = name
		self.age =age
	def __getitem__(self, item):
		if type(item) ==slice:
			print('qiepian')
			print(item.start)
			print(item.stop)
			print(item.step)
		else:

			print('suo yin')
	def __setitem__(self, key, value):
		print(key,value)
	def __delitem__(self, key):
		print(key)
li=Foo('alex',19)
li[123]
li[1:4:2]
li[1:3]=[11,12]
del li[1:3]

"""
"""
class Foo:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def __iter__(self):
		return iter([1,2,4])

li = Foo('ldi',18)
type(li)
for i in li:
	print(i)
	
	"""


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
"""
class myType(type):
	# def __init__(self,*args,**kargs):
	# 	print('1223')
	def __call__(self, *args, **kwargs):
		print('etdd')

class Foo(object,metaclass=myType):
	def __init__(self):
		print('fu')
	def func(self):
		print('ok')

foo = Foo()
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






