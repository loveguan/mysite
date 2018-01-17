#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: setting.py

@time: 2018/1/5 22:19

@desc:

'''

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
	'engine': 'file_storage',
	'name': 'accounts',
	'path': "%s\db" % BASE_DIR
}

LOG_LEVEL = logging.INFO

LOG_TYPES = {
	'transaction': 'transaction.log',
	'access': 'access.log'
}

TRANSACTION_TYPE = {
	'repay': {'action': 'plus', 'interest': 0},
	'withdraw': {'action': 'minus', 'interest': 0.05},
	'transfer': {'action': 'minus', 'interest': 0.05},
	'consume': {'action': 'minus', 'interest': 0},

}
