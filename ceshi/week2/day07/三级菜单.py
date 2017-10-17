#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 三级菜单.py

@time: 2017/9/22 8:18

@desc:

'''

caidan = {
	'山东': {
		'威海': ['乳山', '环翠', '经区', '环翠', '临港'],
		'烟台': ['海阳', '栖霞', '莱阳', '莱山']
	},
	'河南': {
		'郑州': ['zheng1', 'zhegn2']
	},
	'湖北': {
		'武汉': ['hankou', 'jiujiang']
	},

}
# 设置初始的列表
current_layer = caidan
# 设置一个列表，每循环一次，加入一个
parent_layer = []
while True:

	for i in current_layer:
		print(i)
	choice = input('>>>').strip()
	if len(choice) == 0: continue
	if choice in current_layer:
		if type(current_layer) == list:
			print('list')
		else:
			if current_layer[choice]:
				parent_layer.append(current_layer)
				current_layer = current_layer[choice]
	elif choice == 'b':
		if parent_layer:
			current_layer = parent_layer.pop()
	else:
		print('无此项！！！')
