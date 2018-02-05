#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: main.py

@time: 2018/1/17 9:54

@desc:

'''

from conf import setting
import threading
from run import ip_scan
from run import logger
from run import mail

# thread pool
threads = []

# 判断检查是否成功的标志
Flag_err = False

# get log devel from settting conf 日志格式（conf setting ）
loger_type = 'check'
# 获取logger对象
access_log = logger.logger(loger_type)


# 多线程调用执行ip_scan方法
def init():
	for line in setting.ip:
		line = line.strip()
		ip, port = line.split(":")
		t = threading.Thread(target=ip_scan.ip_scan, args=(ip, port, access_log))
		threads.append(t)
		t.start()

	for t in threads:
		t.join()


# 入口函数
def init_check():
	init()
	# mail loger_type define log path 根据标志位判断发送什么样的邮件
	mail.mail(Flag_err, loger_type)
	if Flag_err:
		print("\033[43;34m error,please read log!!!\033[0m")
	else:
		print("\033[42;33m It's ok!!!\033[0m")
