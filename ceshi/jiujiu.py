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

num1 = 1

while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print(num2, end=" * ")
        print(num1, end=" = ")
        print(num1 * num2, end=" ")
        num2 += 1
    num1 += 1
    print()
