#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: for.py

@time: 2017/8/26 21:41

@desc:  for循环的使用！！！

'''

_user = 'joj'
_passwd = 'guan'
flag_auth = False  # 标志位用来判断循环完成后后续对的执行过程

for i in range(3):
    username = input('username:')
    passwd = input('password:')
    if username == _user and passwd == _passwd:
        print('welcome %s login....' % (username))
        break  # 跳出，中断
    else:
        print("Invalid username or passwd!")
else:  # 这个else只有在for循环正常退出的时候，才执行，否则不执行
    print("帐号被锁定！！！")
