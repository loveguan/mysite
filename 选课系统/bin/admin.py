#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: admin.py

@time: 2018/1/29 10:13

@desc:

'''
import os
import sys

BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)
sys.path.append(BASEDIR)

from src.service import admin_service


def execute():
	admin_service.main()


if __name__=="__main__":
	execute()