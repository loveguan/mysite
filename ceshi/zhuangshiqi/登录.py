#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 登录.py

@time: 2017/11/29 21:58

@desc:

'''

# 认证状态
login_status = False
# 用户名密码
auth_user=''
auth_passwd=''

# 用户名密码获取函数
def get_auth(fi='jingdong'):
	global auth_passwd
	global auth_user
	with open(fi, 'r') as f:
		# 获取用户名和密码
		for i in f:
			if i.startswith('user'):
				auth_user = i.lstrip('user=').replace('\'', '').strip()
			elif i.startswith('passwd'):
				auth_passwd = i.strip('passwd=').replace('\'', '').strip()


def login(auth_type='jingdong'):
	def wap(fun):
		def wrapper():
			global login_status
			global auth_passwd
			global auth_user
			if login_status == False:
				if auth_type == 'jingdong':
					print('jingdong ok')
					# 获取用户名密码
					get_auth('jingdong')
				elif auth_type == 'weixin':
					# 获取用户名密码
					get_auth('weixin')
					print('other auth,weixin!!')
				# 输入用户名和密码
				username = input('username: ')
				password = input('password: ')
				if auth_user == username and auth_passwd == password:
					print('renzheng pass')
					login_status = True
					fun()
				else:
					print('error')
				# 	清空认证信息
				auth_user=''
				auth_passwd=''
			else:
				print('yi jing denglu !')
				fun()

		return wrapper

	return wap


@login(auth_type='jingdong')
def home():
	print('welcome to home page')


@login(auth_type='weixin')
def finance():
	print('welcome to finance page')

@login()
def book():
	print('welcome to book page')


# home()
# print(auth_user)
# print(auth_passwd)
# finance()
book()