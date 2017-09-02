#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: shoppingv0.1.py

@time: 2017/9/2 19:44

@desc:

'''

# 商品列表
procuct_list = [['book', 30], ['bike', 300], ['cat', 3000], ['coffee', 35], ]

#循环查看输入的初始金额是否为数字
while True:
    # 输入初始金额
    saving= input('input your money: ')
    if saving.isdigit():
        Totle_money=int(saving)
        # 直到输入正确退出
        break
    else:
        print("输入错误，重新输入！")

# 已经购买列表
buy_list = []

while True:
    # enumerate方法，在前边加上序列号
    for i,v in enumerate(procuct_list, start=1):
        # 注意这里字符串的连接方式
        print(i ,'>>',v)
    # 判断购物车如有物品则打印输出
    if len(buy_list) > 0:
        print("购物车里已经有：", end='')
        for i in buy_list:
            print(i, end=' ')
    #  输出账户余额信息
    print('\n账户余额还有%d元' % (Totle_money))
    # 输入购买的物品
    choice = input('what do you want to buy，quit（q）: >>')
    #  if语句选择
    if choice.isdigit():
        choice=int(choice)
        # 判断剩余的资金是否可以购买东西
        if choice>0 and choice<len(procuct_list):
            if Totle_money - procuct_list[int(choice) - 1][1] > 0:
                Totle_money = Totle_money - procuct_list[int(choice) - 1][1]
                msg = """
                已经购买了%s,还剩 %i元
                """ % (procuct_list[int(choice) - 1][0], Totle_money)
                buy_list.append(procuct_list[int(choice) - 1][0])
                print(msg)
            else:
                print('余额不足，还剩%i元,不够买 %s' % (Totle_money, procuct_list[int(choice) - 1][0]))
        else:
            print("商品不存在，请重新输入！！！")
    # 输入q或者Q退出购物
    elif choice=='q' or choice== 'Q':
        # 如果有购物就打印购物单
        if len(buy_list)>0:
            print('购物完成！！！')
            # print默认为换行，可以使用其他的替代
            print('你已经购买了', end=':')
            for i in buy_list:
                print(i, end=',')

            print('\n账户余额%d元！！' %Totle_money)
        else:
            print('你未购买任何东西，欢迎下次光临！！！')
        # 跳出循环
        break
    else:
        print('错误的输入，请输入商品的编码！！！')
