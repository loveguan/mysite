#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 增删查.py

@time: 2017/12/14 15:47

@desc:

'''


import configparser
# 由于时空，所以没有啥文件
config = configparser.ConfigParser()

print(config.sections())
# 读取文件后会有结果
config.read('example.ini')
print(config.sections())

# 显示见是否存在
print('buteb' in config)
print('bitbucket.org' in config)

# 获取值
print(config['bitbucket.org']['user'])
print(config['DEFAULT']['Compression']) #yes

print(config['topsecret.server.com']['ForwardX11']) #no

# 获取键值，默认都包括default的值
for key in config['bitbucket.org']:
	print(key)

# 获取键值
print(config.options('bitbucket.org')) # ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
print(config.items('bitbucket.org')) #  [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]
# 获取具体键的值
print(config.get('bitbucket.org','compression'))

#---------------------------------------------删,改,增(config.write(open('i.cfg', "w")))
#  添加一个
# config.add_section('yuan')
# 删除一项
# config.remove_section('topsecret.server.com')
# 删除一个键值
config.remove_option('bitbucket.org','user')
# 设置键值
config.set('bitbucket.org','k1','11111')
# 写入到文件
config.write(open('example.ini', "w"))