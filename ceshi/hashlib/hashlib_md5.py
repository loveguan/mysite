#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: hashlib_md5.py

@time: 2017/12/3 20:49

@desc:

'''
import  hashlib
from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())
# This example uses the hexdigest() method instead of digest() because the output is formatted so it can be printed clearly. If a binary digest value is acceptable, use digest().
print(h.digest())


