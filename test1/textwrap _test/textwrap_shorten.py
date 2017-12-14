#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: textwrap_shorten.py.py

@time: 2017/11/13 20:44

@desc:截取一部分字符串，剩余的省略号表示

'''

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
orignal = textwrap.fill(dedented_text, width=50)
print('Original:\n')
print(orignal)

shortened = textwrap.shorten(orignal, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)
print('\nShortend:\n')
print(shortened_wrapped)
