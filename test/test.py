#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/7/7 7:04
# @Author  : joj
# @Site    : 
# @File    : test.py
# @Software: PyChar

# import dns.resolver
# import dns.rdtypes
# import socket
#
# my_resolver = dns.resolver.Resolver()
# my_resolver.nameservers=[socket.gethostbyname('218.201.96.130')]
# ans= my_resolver.query('www.baidu.com','A')
# for i in ans.response.answer:
#     for j in i.items:
#         print(j)


'''
import logging
import os
import time

# 获取时间
stamp = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
file_name = 'error' + '-' + stamp + '.txt'
#错误日志路径dddd
error_log_path=os.path.join('E:\PycharmProjects\mysite\\test',file_name)
print(error_log_path)
logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
logging.debug('this is a message')
logging.basicConfig(filename=error_log_path, level=logging.ERROR)
logging.error('addaddaaaddddd11fsdffsfssfsffe23323223233232')
# logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
# logging.debug('this is a message')
print(os.path.getsize(error_log_path))
os.remove()
'''

'''
count = 0

while True:
	it = input('Entre quit: ')
	if it == 'quit':
		break
	count = count + 1
	if count % 3 > 0:
		continue
	print('please input quit!')

print('success')

'''


class MyClass(object):
	def __init__(self, name='unser', color='black'):
		print('contructor is called with params: %s ,%s' % (name, color))
		self.__name = name
		self.__color = color

	def __del__(self):
		print('Destructor is called for %s!' % self.__name)


inst = MyClass('Joojo', 'White')
print(inst.__name) #  类之外的代码无法访问私有成员
del inst
