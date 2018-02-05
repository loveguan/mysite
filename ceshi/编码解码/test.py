#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2018/1/17 20:31

@desc:

'''

a='hello,你好，周'
# 编码方式一
# b=bytes(a,'utf8')
b=a.encode('utf8')
print(b)
# 解码 方式一
# print(str(b,'utf8'))
# 解码方式二
print(b.decode('utf8'))
