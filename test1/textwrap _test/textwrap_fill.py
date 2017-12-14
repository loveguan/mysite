#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: textwrap_fill.py.py

@time: 2017/11/13 15:53

@desc:

'''

import textwrap
# import textwrap_example
from textwrap_example import sample_text

print(textwrap.fill(sample_text, width=50))