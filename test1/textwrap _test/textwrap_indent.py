#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: textwrap_indent.py.py

@time: 2017/11/13 16:14

@desc:每一行前边加字符

'''

import textwrap
from textwrap_example import sample_text

dedentd_text=textwrap.dedent((sample_text))
wrapped= textwrap.fill(dedentd_text,width=50)
wrapped+='\n\nSecond paragraph after a blank line.'
final=textwrap.indent(wrapped,'>')
print('Quoted block:\n')
print(final)