#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2017/12/21 8:39

@desc:

'''
import re
a=31+31
# ret = re.search('\d\*\d',a).group()

# ret=re.search('\d+', str(a))
ret=re.search('\d+\.?\d*[+]\d+\.?\d*',str(a))
# ret=re.search('\d+\.?\d*\+\d+\.?\d*', str(a)).group()
print(ret)