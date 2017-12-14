#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: caidan-v1.1.py

@time: 2017/10/23 20:54

@desc:

'''
d = dict()

f = open('caidan.txt', 'r+', encoding='utf-8')

# zha
for i in f.readlines():
	d.update(eval(i))
print(d)
list_zi = []
pro_dict = d
liebiao=[]
while True:
	if pro_dict:
		print('城市列表为：')
		for x in pro_dict:
			print(x)
	else:
		print('到底了！！！')
	choice = input('请输入你选择的城市，b后退到上一级,a添加:')
	if choice in pro_dict:
		list_zi.append(pro_dict)
		pro_dict = pro_dict[choice]
		liebiao.append(d[choice])
		print(liebiao)
	elif choice == 'b':
		if list_zi:
			pro_dict = list_zi.pop()

	elif choice in ['a', 'A']:
		choice1 = input('输入要添加的城市 ：')
		pro_dict[choice1] = {}

	elif choice in ['q', 'Q']:
		print(pro_dict)
	else:
		print('输入错误，请重新输入！！！')
