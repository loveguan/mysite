#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: identifier.py

@time: 2018/1/31 17:27

@desc:

'''
from lib import commons
import os
import pickle


class Nid:

	def __init__(self, role, db_path):
		"""

		:param role:  角色
		:param db_path:  放置路径
		"""

		role_list = [
			'admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', 'student'
		]

		if role not in role_list:
			raise Exception('用户校色错误，选项为：%s' % ','.join(role_list))
		self.role = role
		self.uuid = commons.create_uuid()
		self.db_path = db_path

	def __str__(self):
		return self.uuid

	def get_obj_by_uuid(self):
		for name in os.listdir(self.db_path):
			if name == self.uuid:
				return pickle.load(open(os.path.join(self.db_path, self.uuid), 'rb'))


class AdminNid(Nid):
	def __init__(self, db_path):
		super(AdminNid, self).__init__('admin', db_path)


class SchoolNid(Nid):
	def __init__(self, db_path):
		super(SchoolNid, self).__init__('school', db_path)


class TeacherNid(Nid):
	def __init__(self, db_path):
		super(TeacherNid, self).__init__('teacher', db_path)


class ClassedNid(Nid):
	def __init__(self, db_path):
		super(ClassedNid, self).__init__('classes', db_path)

class CourseNid(Nid):
	def __init__(self,db_path):
		super(CourseNid,self).__init__('course',db_path)
class couseToteacherNid(Nid):
	def __init__(self,db_path):
		super(couseToteacherNid,self).__init__('course_to_teacher',db_path)
