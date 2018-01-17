#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: logger.py.py

@time: 2018/1/17 10:34

@desc:

'''

import logging
from conf import setting


def logger(log_type):
	# create logger
	logger = logging.getLogger(log_type)
	# 这个登记必须要有
	logger.setLevel(setting.LOG_LEVEL)
	# create console screen
	ch = logging.StreamHandler()
	ch.setLevel(setting.LOG_LEVEL)
	# create file save
	log_file = "%s/log/%s" % (setting.BASE_DIR, setting.LOG_TYPES[log_type])
	fh = logging.FileHandler(log_file)
	fh.setLevel(setting.LOG_LEVEL)
	# create formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	# add formatter to ch and fh
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)
	# add ch and fh to logger
	logger.addHandler(ch)
	logger.addHandler(fh)
	return logger
