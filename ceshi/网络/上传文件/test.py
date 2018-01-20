
#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: test.py

@time: 2018/1/18 9:44

@desc:

'''

import os
import subprocess

com = subprocess.Popen('cd \\', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(str(com.communicate()[0],'gbk'))