#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: ssh.py

@time: 2017/8/30 15:20

@desc:

'''
# 商品列表
procuct_list = [['book', 30], ['bike', 300], ['cat', 3000], ['coffee', 35], ]
# 初始资金
saving= input('input your money: ')
if saving.isdigit():
    Totle_money=int(saving)
# 购买列表
buy_list = []

while True:
    # enumerate方法，在前边加上序列号
    for i,v in enumerate(procuct_list, start=1):
        # 注意这里字符串的连接方式
        print(i ,'>>',v)
    # 输入选择
    choice = input('what do you want to buy: >>')
    #  判断输入的格式是否为数字
    if not choice.isdigit():
        continue
    # 判断剩余的资金是否可以购买东西
    choice = int(choice)
    if choice>0 and choice<len(procuct_list):
        if Totle_money - procuct_list[int(choice) - 1][1] > 0:
            Totle_money = Totle_money - procuct_list[int(choice) - 1][1]
            msg = """
            已经购买了%s,还剩 %i元
            """ % (procuct_list[int(choice) - 1][0], Totle_money)
            buy_list.append(procuct_list[int(choice) - 1][0])
            print(msg)
        else:
            print('余额不足，还有%i元,不够买 %s' % (Totle_money, procuct_list[int(choice) - 1][0]))
    else:
        print('wrong input!!!')

    while True:
        # 判断只有输入y，Y，N,n时候跳出循环
        choice_continue = input('do you want to continue(y/n): >>')
        if choice_continue in ['y', 'n', 'Y', 'N']:
            break
    # 判断是否继续进行
    if choice_continue == 'n' or choice_continue == 'N':
        print('购物完成！！！')
        # print默认为换行，可以使用其他的替代
        print('你已经购买了', end=':')
        for i in buy_list:
            print(i, end=',')

        print('\nleaving monney %d' %Totle_money)
        break
