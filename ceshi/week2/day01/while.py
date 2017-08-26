# !/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: while.py

@time: 2017/8/26 22:03

@desc: while使用

'''

_user = 'joj'
_passwd = 'guan'
flag_auth = False  # 标志位用来判断循环完成后后续对的执行过程
counter = 0 # 计数器

while counter < 3:
    username = input('username:')  #输入用户名
    passwd = input('password:')    #输入密码
    if username == _user and passwd == _passwd:
        print('welcome %s login....' % (username))
        break  # 跳出，中断
    else:
        print("Invalid username or passwd!")
    counter += 1
    if counter == 3: # 输入三次后还想玩的话，counter计数清零
        choice = input('Do you continue,y/n:')
        if choice == 'y':
            counter = 0
else:  # 这个else只有在for循环正常退出的时候，才执行，否则不执行
    print("帐号被锁定！！！")
