#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: main.py

@time: 2018/1/5 22:10

@desc:

'''

from model import auth
from model import logger
from model import accounts
from model import transaction
from model import zhuangshiqi

user_data = {
	'account_id': None,
	'is_authenticated': False,
	'account_data': None
}

access_logger = logger.logger('access')
trans_logger = logger.logger('transaction')


@zhuangshiqi.login
def account_info(user_data):
	print(user_data)


@zhuangshiqi.login
def repay(user_data):
	print(user_data)
	account_data = accounts.load_current_balance(user_data['account_id'])
	current_balance = '''--------- BALANCE INFO --------
		Credit :    %s
    	Balance:    %s''' % (account_data['credit'], account_data['balance'])

	print(current_balance)
	back_flag = False
	while not back_flag:
		repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
		if len(repay_amount) > 0 and repay_amount.isdigit():
			print('ddd 000')
			new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
			if new_balance:
				print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
		else:
			print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)
		if repay_amount == 'b':
			back_flag = True


@zhuangshiqi.login
def withdraw(user_data):
	account_data = accounts.load_current_balance(user_data['account_id'])
	current_balance = '''------------BALANCE INFO-----------
			Credit:     %s
			Balance:    %s
	''' % (account_data['credit'], account_data['balance'])
	print(current_balance)
	back_flag = False
	while not back_flag:
		draw_amount = input("\033[33;1mInput draw amount:\033[0m")
		if len(draw_amount) > 0 and draw_amount.isdigit():
			print(draw_amount)
			new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', draw_amount)
			if new_balance:
				print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))
		else:
			print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % draw_amount)
		if draw_amount == 'b':
			back_flag = True


@zhuangshiqi.login
def transfer(user_data):
	pass


@zhuangshiqi.login
def pay_check(user_data):
	pass


@zhuangshiqi.login
def logout(user_data):
	pass


def interactive(user_data):
	menu = u'''
	   ------- Oldboy Bank ---------
	   \033[32;1m1.  账户信息
	   2.  还款(功能已实现)
	   3.  取款(功能已实现)
	   4.  转账
	   5.  账单
	   6.  退出
	   \033[0m'''
	menu_dic = {
		'1': account_info,
		'2': repay,
		'3': withdraw,
		'4': transfer,
		'5': pay_check,
		'6': logout,
	}
	exit_flag = False
	while not exit_flag:
		print(menu)
		user_option = input(">>:").strip()
		if user_option in menu_dic:
			menu_dic[user_option](user_data)
		else:
			print("\033[31;1mOption does not exist!\033[0m")

	print(menu)


def main():
	acc_data = auth.acc_login(user_data, access_logger)
	if user_data['is_authenticated'] == True:
		user_data['account_data'] = acc_data
		interactive(user_data)
	# repay(user_data)
