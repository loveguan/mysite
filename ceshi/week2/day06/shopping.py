#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: shopping.py

@time: 2017/8/27 21:27

@desc:  购物车程序

'''

# 商品列表
procuct_list = [['book', 30], ['bike', 300], ['cat', 3000], ['coffee', 35], ]
# 初始资金
Totle_money = 5000
# 购买列表
buy_list = []

while True:
    # enumerate方法转换
    for i in enumerate(procuct_list, start=1):
        print(i)
    # 输入选择
    choice = input('what do you want to buy: >>')
    #  判断输入的格式是否为数字
    if not choice.isdigit():
        continue
    # 判断剩余的资金是否可以购买东西
    if Totle_money - procuct_list[int(choice) - 1][1] > 0:
        Totle_money = Totle_money - procuct_list[int(choice) - 1][1]
        msg = """
        you have buied %s,your money %i
        """ % (procuct_list[int(choice) - 1][0], Totle_money)
        buy_list.append(procuct_list[int(choice) - 1][0])
        print(msg)
    else:
        print('lest money %i,you can not buy %s' % (Totle_money, procuct_list[int(choice) - 1][0]))

    while True:

        choice_continue = input('do you want to continue(y/n): >>')
        if choice_continue in ['y', 'n','Y','N']:
            break
    #  判断是否继续进行
    if choice_continue == 'n':
        print('bye')
        print(buy_list)
        break
