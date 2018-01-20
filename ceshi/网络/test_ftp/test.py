
#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2018/1/19 7:56

@desc:

'''
import os

"""


a='adbbb '
ret=a.split(' ')
print(len(ret))
import os
BASE_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),'upload','test','test')
CUR_DIR=BASE_DIR
print(BASE_DIR)

b="..\\..\\aabb"
# print(b.startswith('..'))
# c=b.replace("..\\","")
# print(c)
c=""
while b.startswith('..'):
	c = b.replace("..\\","",1)
	print(c)
	CUR_DIR=os.path.dirname(CUR_DIR)
	b=c

print(CUR_DIR)
print(c)

print(os.sep)

c="sdads/daddas"
print(c.index('/'))
print(c.__contains__('/')
"""
BASE_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),'download')
print(BASE_DIR)



