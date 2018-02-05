#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: setting.py

@time: 2018/1/31 16:58

@desc:

'''

import os



BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASEDIR, 'db', 'admin')
COURSE_DB = os.path.join(BASEDIR, 'db', 'course')
COURSE_TO_TEACHER_DB = os.path.join(BASEDIR, 'db', 'course_to_teacher')
CLASSES_DB = os.path.join(BASEDIR, 'db', 'classes')

STUDENT_DB = os.path.join(BASEDIR, 'db', 'student')
TEACHER_DB = os.path.join(BASEDIR, 'db', 'teacher')
SCHOOL_DB = os.path.join(BASEDIR, 'db', 'school')