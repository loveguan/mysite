#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: jiujiu.py

@time: 2017/8/22 20:39

@desc: 九九乘法表

'''

# 设置初始值

num1 = 1

while num1 <= 9:
    num2 = 1
    while num2 <= num1:

        #  通过end把默认的换行符替换为其他需要的这里为*和=等，分步输出如下
        '''print(num2, end=" * ")
        print(num1, end=" = ")s
        print(num1 * num2, end="\t")
        '''
        #  \t用来使输出对齐
        print(str(num2) + '*' + str(num1) + "=" + str(num1 * num2), end='\t')
        num2 += 1
    num1 += 1
    # 循环到最后换行
    print()

