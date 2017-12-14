#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: textwrap_hanging_indent.py.py

@time: 2017/11/13 20:38

@desc:首行和下边的行缩进不一样

'''

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text, initial_indent='', subsequent_indent=' ' * 4, width=50, ))
