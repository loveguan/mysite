#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: initialize_service.py

@time: 2018/1/31 17:06

@desc:

'''
from src.models import Admin


def initialize():
	try:
		user = input("请输入初始化的用户名；")
		pwd = input("请输入初始化密码：")
		obj = Admin(user, pwd)
		print(obj.nid)
		print(obj)
		print(obj.nid.get_obj_by_uuid())
		obj.save()
		return True

	except Exception as e:
		print(e)


def main():
	show = """
	1. 初始化管理员帐号
	"""

	choice_dict = {

		'1': initialize
	}
	while True:
		print(show)
		choice = input('请输入操作选项：')
		if choice not in choice_dict:
			print('错误，请重新输入！！！')
		func = choice_dict[choice]
		ret = func()
		print(ret)
		if ret:
			print('操作成功')
		else:
			print('操作失败，请重新操作！！！')
