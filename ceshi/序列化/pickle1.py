#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: pickle1.py

@time: 2018/1/4 17:17

@desc:http://www.cnblogs.com/yuanchenqi/articles/5732581.html

'''


import pickle

dic={'name':'alvin','age':23,'sex':'male'}

f=open('序列化对象pickle','wb')
pickle.dump(dic,f)

f=open('序列化对象pickle','rb')
data=pickle.load(f)
print(data)
