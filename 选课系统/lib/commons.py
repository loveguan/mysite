#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: commons.py

@time: 2018/1/31 17:33

@desc:

'''

import uuid


def create_uuid():
	return str(uuid.uuid1())
