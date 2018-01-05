#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 计算器.py

@time: 2017/12/17 14:56

@desc:

'''

import re

input_string = "1 +2 * ( (60-30 +(40/5) * (9 - 2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3)/ (16-3*2) )"
# input_string = "1 - 2 * ( (60-30 +(-40/5) * (9 - 2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# input_string = "1 - 2 * ( 3+8*4 )"
# input_string = "1+2 * 8"


# 检查输入的内容是否合规
def check_number(s):
	ret = True
	if re.search(r'[z-zA-Z]]', s):
		ret = False
	return ret


# 查看括号的数量
def check_kuohao(s):
	ret = True
	if len(re.findall(r'\(', s)) == len(re.findall(r'\)', s)):
		ret = False
	return ret


# 格式化字符串
def format_str(s):
	s = s.replace(' ', '')
	s = s.replace('--', '+')
	s = s.replace('+-', '-')
	return s


def mul_div(s):
	while re.findall('[*/]', s):
		str_div = re.search('\d+\.?\d*[*/]\d+\.?\d*', s).group()
		fuhao = re.search('[*/]', str_div).group()
		listl = str_div.split(fuhao)
		if fuhao == '/':
			result1 = float(listl[0]) / (float(listl[1]))
		else:
			result1 = float(listl[0]) * (float(listl[1]))
		s = s.replace(str_div, str(result1))
	return s


def add_sub(x):
	while re.findall('[+-]', x):
		str_div = re.search('\d+\.?\d*[+-]\d+\.?\d*', x).group()
		fuhao = re.search('[+-]', str_div).group()
		listl = str_div.split(fuhao)
		if fuhao == '-':
			result1 = float(listl[0]) - (float(listl[1]))
		else:
			result1 = float(listl[0]) + (float(listl[1]))
		x = x.replace(str_div, str(result1))
	return x


# 执行检查并且格式化字符串

check_kuohao(input_string)
ret = check_number(input_string)
input_string = format_str(input_string)
print(input_string)
result=0
if ret:
	while re.findall('\(', input_string):
		strr = re.search('\(([^()]+)\)', input_string)
		str1=strr.group(1)
		str3=strr.group()
		print(str1)
		print(str3)
		# str1 = re.search('\(([^()]+)\)', input_string).group(1)
		str2 = mul_div(str1)
		str2 = add_sub(str2)
		input_string = input_string.replace(str3, str2)
	else:
		result=mul_div(input_string)
		result=add_sub(result)
	print(result)


