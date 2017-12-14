#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: os_scandir.py

@time: 2017/12/4 15:46

@desc:
scandir() returns a sequence of DirEntry instances for the items in the directory. The object has several attributes and methods for accessing metadata about the file.

'''

import os
import sys

#  设置默认的路径
if len(sys.argv)==1:
	root='D:\\pycharm_code\\mysite\\ceshi\\os模块'
else:
	root=sys.argv[1]
for entry in os.scandir(root):

	if entry.is_dir():
		typ = 'dir'
	elif entry.is_file():
		typ = 'file'
	elif entry.is_symlink():
		typ = 'link'
	else:
		typ = 'unknown'
	print('%s %s' %(entry.name,typ))