#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: hashlib_update.py

@time: 2017/12/3 21:40

@desc:

'''

import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
all_at_once = h.hexdigest()


# print(all_at_once)

def chunkize(size, text):
	"Return parts of the text in size-based increments."
	start = 0
	while start < len(text):
		chunk = text[start:start + size]
		yield chunk
		start += size
	return

h = hashlib.md5()
for chunk in chunkize(64, lorem.encode('utf-8')):
	h.update(chunk)
line_by_line = h.hexdigest()

print('All at once :', all_at_once)
print('Line by line:', line_by_line)
print('Same        :', (all_at_once == line_by_line))
