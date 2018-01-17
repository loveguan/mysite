#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: account_sample.py.py

@time: 2018/1/5 23:12

@desc:

'''

import json

import os
import sys
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import setting


acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}
path_name="%s\db\%s\%s" %(setting.BASE_DIR,"accounts",'1234.json')
print(path_name)
# f = open(path_name,'w')
f = open(path_name)
# json.dump(acc_dic,f)

account_data = json.load(f)
print(account_data)