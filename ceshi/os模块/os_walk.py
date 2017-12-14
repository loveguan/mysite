#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: os_walk.py

@time: 2017/12/4 14:46

@desc:遍历文件夹下的目录 和文件
This example shows a recursive directory listing

'''

import os
import sys

#  设置默认的路径
if len(sys.argv)==1:
	root='D:\\pycharm_code\\mysite\\ceshi\\os模块'
else:
	root=sys.argv[1]
# print(os.walk(root))
for dir_name,sub_dirs,files in os.walk(root):
	print(dir_name)
	# 在目录后边的名字加上斜线/
	sub_dirs=[ n + '/' for n in sub_dirs]
	#  将目录和文件放在一起
	contents=sub_dirs+files
	# 排序
	contents.sort()
	for c in contents:
		print(' {}'.format(c))

	print()
	# print(dir_name,sub_dirs,files)
