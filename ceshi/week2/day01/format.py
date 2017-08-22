#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: format.py

@time: 2017/8/22 22:14

@desc: 格式化输出

'''

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

msg = '''
-----------------info of %s ---------------
Name: %s
Age: %s
Job: %s
Salary: %s
-----------------end------------------------
''' % (name, name, age, job, salary)

print(msg)
