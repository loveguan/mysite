#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: initialize.py

@time: 2018/1/31 17:03

@desc:

'''
import os
import sys

BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
from src.service import initialize_service

def execute():
	initialize_service.main()


if __name__=='__main__':
	execute()

