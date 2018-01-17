#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2018/1/9 22:56

@desc:
多重继承的时候是先左边，在一直找到底，再右边，执行对象的时候要知道self是谁
'''

class BaseRequest:
	def __init__(self):
		print('baserequest init')


class RequestHandler(BaseRequest):
	def __init__(self):
		print('requesthandler init')
		BaseRequest.__init__(self)
	def server_forever(self):
		print('request handler server_forever')
		self.process_request()
	def process_request(self):
		print('requesthandler process_request')

class Minx:
	def process_request(self):
		print('minx process_request')

class Bar(Minx,RequestHandler):
	pass

obj = Bar()
obj.server_forever()