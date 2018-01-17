#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: accounts.py

@time: 2018/1/7 21:58

@desc:通过配置文件获取数据的保存方式，读取或者保存变化的数据

'''
import json
from model import db_handler
from conf import setting


def load_current_balance(account_id):
	'''
	获取保存在数据库中的帐号的信息
	return account balance and other basic info
	:param account_id:
	:return:
	'''
	db_path = db_handler.db_handler(setting.DATABASE)
	account_file = '%s\%s.json' % (db_path, account_id)
	with open(account_file) as f:
		acc_data = json.load(f)
		return acc_data


def dump_account(account_data):
	'''
	after update transaction or account data,dump it back to file db
	更新数据库的内容，持久化保存到文件
	:param account_data:
	:return:
	'''

	db_path = db_handler.db_handler(setting.DATABASE)
	account_file = '%s\%s.json' % (db_path, account_data["id"])
	with open(account_file, 'w') as f:
		json.dump(account_data, f)
	return True
