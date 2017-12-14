#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: textwrap_indent_predicate.py.py

@time: 2017/11/13 17:16

@desc: 重新排版，根据条件添加字符串

'''

import textwrap
from textwrap_example import sample_text

def should_indent(line):
	print('Indent {!r}?'.format(line))
	return len(line.strip())%2==0

dedented_text=textwrap.dedent(sample_text)
wrapped=textwrap.fill(dedented_text,width=50)
final=textwrap.indent(wrapped,'EVEN',predicate=should_indent)

print('\nQuoted block:\n')
print(final)