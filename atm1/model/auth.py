#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: auth.py

@time: 2018/1/5 22:44

@desc:

'''

import os
from conf import setting
from model import logger
from model import db_handler
import time
import json


def acc_auth(account, password):
	'''

	:param account:
	:param password:
	:return:
	验证用户名和密码，通过返回json字符串信息
	'''
	db_path = db_handler.db_handler(setting.DATABASE)
	account_file = '%s\%s.json' % (db_path, account)
	if os.path.isfile(account_file):
		with open(account_file) as f:
			account_data = json.load(f)
			if account_data['password'] == password:
				exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
				if time.time() > exp_time_stamp:
					print(
						"\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
				else:
					return account_data
			else:
				print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data, log_obj):
	'''

	:param user_data:
	:param log_obj:
	:return:
	验证逻辑，设置重试的次数，为user_data赋值
	'''
	retry_count = 0
	while user_data['is_authenticated'] is not True and retry_count < 3:
		account = input("\033[32;1maccount:\033[0m").strip()
		password = input("\033[32;1mpassword:\033[0m").strip()
		auth = acc_auth(account, password)
		if auth:
			user_data['account_id'] = account
			user_data['is_authenticated'] = True
			return auth
		retry_count += 1
	else:
		log_obj.error("account [%s] too many login attempts" % account)
		exit()
