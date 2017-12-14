#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: os_directory.py

@time: 2017/12/4 16:28

@desc:

'''

import os

# 创建文件夹
dir_name = 'os_directories_example'
print('Creating', dir_name)
if not os.path.exists(dir_name):
	os.makedirs(dir_name)
else:
	print('exise')

# 创建文件
file_name = os.path.join(dir_name, 'example.txt')
print('Creating', file_name)

with open(file_name, 'wt')  as f:
	f.write('example')

print('cleaning up')

if os.path.exists(file_name):
	os.unlink(file_name)

if os.path.exists(dir_name):
	os.rmdir(dir_name)
