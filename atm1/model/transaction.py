#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: transaction.py

@time: 2018/1/7 22:30

@desc:

'''
from conf import setting
from model import accounts


def make_transaction(log_obj, account_data, tran_type, amount, **others):
	amount = float(amount)
	if tran_type in setting.TRANSACTION_TYPE:
		interest = amount * setting.TRANSACTION_TYPE[tran_type]['interest']
		old_balance = account_data['balance']
		if setting.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
			new_balance = old_balance + amount + interest
		elif setting.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
			new_balance = old_balance - amount - interest
			# check credit
			if new_balance < 0:
				print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
			               [%s]''' % (account_data['credit'], (amount + interest), old_balance))
				return
		account_data['balance'] = new_balance

		accounts.dump_account(account_data)
		log_obj.error("account:%s   action:%s    amount:%s   interest:%s" %
					  (account_data['id'], tran_type, amount, interest))
		return account_data
	else:
		print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)
