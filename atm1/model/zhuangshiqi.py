#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: zhuangshiqi.py

@time: 2018/1/9 15:49

@desc:

'''

from model import auth
from model import main


def login(func):

	'''检查是否通过了登录验证，没有则登录验证！！！！'''

	def wrap(user_data):
		print('zhuangshiqi')
		if user_data['account_id'] is not None:
			print('已经认证')
			func(user_data)
		else:
			print('你未认证，请输入认证信息！！！！')
			acc_data = auth.acc_login(main.user_data, main.access_logger)
			if user_data['is_authenticated'] == True:
				user_data['account_data'] = acc_data
				print('认证通过！！！')
				func(user_data)
	return wrap
