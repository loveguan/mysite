#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: subPress_test.py

@time: 2018/1/16 12:22

@desc:

'''

import subprocess

a = subprocess.Popen('dir1', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(a)
# # print(str(a.stdout.read(),'utf8'))
# print(str(a.stdout.read(),'gbk'))
ret=a.communicate()
print(str(ret[0],'gbk'))
if ret[1]:
	print(str(ret[1],'gbk'))