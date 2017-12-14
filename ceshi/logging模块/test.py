#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2017/12/8 8:02

@desc:这个是屏幕和文件输出二选一

'''

import logging
logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					datefmt='%a,%d %b %Y %H:%M:%S',
					# 如果不写filename，则为输出到屏幕
					filename='test.log',
					#  默认的是追加的模式
					filemode='a'
					)

logging.debug('dubug message')
logging.info('info message')
logging.warning('hello error')
logging.error('error message')
logging.critical('critical message')
