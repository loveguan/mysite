
#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2017/11/30 20:54

@desc:
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

'''


import time

# print(help(time))
# #时间戳，秒数
# print(time.time())
# convert seconds since Epoch to UTC tuple，根据时区显示和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
# print(time.gmtime())
# convert seconds since Epoch to local time tuple，将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
# print(time.localtime())  # 本地时间
# struck_time=time.localtime()
# convert time tuple to string according to format specification
# print(time.strftime('%Y-%m-%d %H:%M:%S',struck_time))
# parse string to time tuple according to format specification
# print(time.strptime('2017-12-01 16:35:54','%Y-%m-%d %H:%M:%S'))
# convert time in seconds to string
# print(time.ctime(1121122221))
# print(time.ctime())
# print(time.mktime(time.localtime()))
# print(help(time.mktime))
# a=time.localtime()
# print(time.mktime(time.localtime()))
# # 从字符串中取出时间
# a=time.strptime('2017-12-01 16:35:54','%Y-%m-%d %H:%M:%S')
# print(a.tm_hour)