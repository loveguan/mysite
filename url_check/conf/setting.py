#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: setting.py

@time: 2018/1/17 9:51

@desc:

'''
import logging
import os

ip = [
	  "120.220.251.39:10001",
	  "120.220.251.39:10002",
	  "120.220.251.39:10003",
	  "120.220.251.39:10004",
	  "120.220.251.38:11001",
	  "120.220.251.38:11002",
	  "120.220.251.38:11003",
	  "120.220.251.38:11004",
	  "120.220.251.38:11005",
	  "120.220.251.38:11006",
	  "120.220.251.38:11007",
	  "120.220.251.38:11008",
	  "120.220.251.38:12001",
	  "120.220.251.18:80",
	  "222.174.216.63:10001",
	  "222.174.216.63:10002",
	  "222.174.216.63:10003",
	  "222.174.216.63:10004",
	  "222.174.216.62:11001",
	  "222.174.216.62:11002",
	  "222.174.216.62:11003",
	  "222.174.216.62:11004",
	  "222.174.216.62:11005",
	  "222.174.216.62:11006",
	  "222.174.216.62:11007",
	  "222.174.216.62:11008",
	  "222.174.216.62:12001",
	  "60.212.191.157:10001",
	  "60.212.191.157:10002",
	  "60.212.191.157:10003",
	  "60.212.191.157:10004",
	  "60.212.191.156:11001",
	  "60.212.191.156:11002",
	  "60.212.191.156:11003",
	  "60.212.191.156:11004",
	  "60.212.191.156:11005",
	  "60.212.191.156:11006",
	  "60.212.191.156:11007",
	  "60.212.191.156:11008",
	  "60.212.191.156:12001",
	  "60.212.191.151:80",
	  "60.212.191.152:80",
	  "60.212.191.153:80",
	  "60.212.191.157:80",
	  "60.212.191.154:80",
	  "60.212.191.150:80",
	  "60.212.191.155:80",
	  "60.212.191.156:80",
	  "10.32.1.76:11001",
	  "10.32.1.77:11002",
	  "10.32.1.78:11003",
	  "10.32.1.79:11004",
	  "10.32.1.86:11005",
	  ]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# config log level DEBUG  INFO  WARNING
LOG_LEVEL = logging.WARNING

LOG_TYPES = {
	'check': 'check.log',
	'access': 'access.log'
}

mail_config={
	'sender':'15063176713@139.com',
	'smtpserver':'smtp.139.com',
    'username':'15063176713@139.com',
    'password':'zhou789099'
}

reciver=['15063176713@139.com','cuipeng@beiyang.com',]

