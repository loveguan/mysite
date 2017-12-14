#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: 多层装饰器.py

@time: 2017/11/28 8:11

@desc:

'''


def makebold(fn):
	def wrapper():
		return "<b>" + fn() + "</b>"

	return wrapper


def makeitalic(fn):
	def wrapper():
		return "<i>" + fn() + "</i>"

	return wrapper


@makebold
@makeitalic

def hello():
	print("hello alvin")


hello()