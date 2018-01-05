#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: json1.py

@time: 2018/1/4 17:12

@desc:

'''

import json


dic={'name':'joj','age':'32','sex':'male'}

print(type(dic))

# j=json.dumps(dic)
# print(type(j))


f = open('序列化对象','w')
# f.write(j)
# f.close()
json.dump(dic,f)  # 等价于上边的注释掉的

f=open('序列化对象')
data=json.load((f))
print(data)

# http://www.cnblogs.com/yuanchenqi/articles/5732581.html