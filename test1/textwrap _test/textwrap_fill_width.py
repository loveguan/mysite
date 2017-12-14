#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: textwrap_fill_width.py.py

@time: 2017/11/13 16:09

@desc: 去掉之前的缩进整理新的格式，生成新的格式


'''

import  textwrap

from textwrap_example import sample_text

dedented_text=textwrap.dedent(sample_text).strip()
for width in [45,60]:
	print('{} Columns:\n'.format(width))
	print(textwrap.fill(dedented_text,width=width))
	print()