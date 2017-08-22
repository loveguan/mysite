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

# 法一，判断输入的是否像整数
'''
if salary.isdigit():
    salary=int(salary)
else:
    print("you must input digest")
    exit("wrong,digest")
'''
#  法二 或者在这里可以适用%d来获取数字，如果传入的字符串不为数字则报错

msg = '''
-----------------info of %s ---------------
Name: %s
Age: %s
Job: %s
Salary: %d
-----------------end------------------------
''' % (name, name, age, job, salary)

print(msg)
