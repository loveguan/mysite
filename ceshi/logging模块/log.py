#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: log.py

@time: 2017/12/13 21:17

@desc:同时输出到屏幕和文件中

'''

import logging

logger=logging.getLogger()

#  创建一个handler，输出到日志
fh = logging.FileHandler('test1.log')
# 再创建一个handler，用于输出到控制台
ch=logging.StreamHandler()
# 设置格式
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
# 设置日志的级别
logger.setLevel(logging.DEBUG)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')