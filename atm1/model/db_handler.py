#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: db_handler.py

@time: 2018/1/5 23:03

@desc:

'''


# 文本处理方式
def file_db_handle(conn_parms):
	db_path = '%s\%s' % (conn_parms['path'], conn_parms['name'])
	return db_path


def mysql_db_handle(conn_parms):
	pass


# 路由可以添加更多的存放数据的方式
def db_handler(conn_parms):
	if conn_parms['engine'] == 'file_storage':
		return file_db_handle(conn_parms)
	if conn_parms['engine'] == 'mysql':
		return mysql_db_handle(conn_parms)
