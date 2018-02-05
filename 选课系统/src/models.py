#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: models.py

@time: 2018/1/31 17:19

@desc:

'''
from config import setting
import os
import pickle
import time
from src import identifier


class BaseModel:

	def save(self):
		nid = str(self.nid)
		file_path = os.path.join(self.db_path, nid)
		# print(file_path)
		pickle.dump(self, open(file_path, 'wb'))


class Admin(BaseModel):
	db_path = setting.ADMIN_DB

	def __init__(self, username, passwd):
		"""

		:param username:
		:param passwd:
		"""
		self.nid = identifier.AdminNid(Admin.db_path)
		self.username = username
		self.password = passwd
		self.create_time = time.strftime('%Y-%m-%d')

	@staticmethod
	def login(user, pwd):
		for item in os.listdir(Admin.db_path):
			obj = pickle.load(open(os.path.join(Admin.db_path, item), 'rb'))
			if user == obj.username and pwd == obj.password:
				print('ok')
				return obj


class School(BaseModel):
	db_path = setting.SCHOOL_DB

	def __init__(self, name):
		self.nid = identifier.SchoolNid(School.db_path)
		self.schoolName = name
		self.income = 0

	def __str__(self):
		return self.schoolName

	@staticmethod
	def get_all_list():
		ret = []
		for item in os.listdir(School.db_path):
			obj = pickle.load(open(os.path.join(School.db_path, item), 'rb'))
			ret.append(obj)
		return ret


class Teacher(BaseModel):
	db_path = setting.TEACHER_DB

	def __init__(self, name, level):
		self.teacherName = name
		self.nid = identifier.TeacherNid(Teacher.db_path)
		self.teacherLevel = level
		self.__account = 0

	def __str__(self):
		return self.teacherName

	@staticmethod
	def get_all_list():
		ret = []
		for item in os.listdir(Teacher.db_path):
			obj = pickle.load(open(os.path.join(Teacher.db_path, item), 'rb'))
			ret.append(obj)
		return ret


class course_to_teacher(BaseModel):
	db_path = setting.COURSE_TO_TEACHER_DB

	def __init__(self, course, teacher):
		self.nid = identifier.couseToteacherNid(course_to_teacher.db_path)
		self.teacher = teacher
		self.course = course

	def __str__(self):
		return 'course:%s,teaceher:%s' % (self.course.courseName, self.teacher.teacherName)

	@staticmethod
	def get_all_list():
		ret = []
		for item in os.listdir(course_to_teacher.db_path):
			obj = pickle.load(open(os.path.join(course_to_teacher.db_path, item), 'rb'))
			ret.append(obj)
		return ret


class Classes(BaseModel):
	db_path = setting.CLASSES_DB

	def __init__(self, name, tuition, school_id, course_to_teacher_1ist):
		"""

		:param name:
		:param tuition:
		:param schoo_id:
		:param course_to_teacher_1ist:
		"""
		self.nid = identifier.ClassedNid(Classes.db_path)
		self.name = name
		self.tuition = tuition
		self.school_id = school_id
		self.courseToTeacherList = course_to_teacher_1ist

	def __str__(self):
		return "班级：%s；课程价格：%s,学校：%s,教师：%s" % (
			self.name, self.tuition, self.school_id.get_obj_by_uuid().schoolName,
			self.courseToTeacherList.get_obj_by_uuid().teacherName
		)


class Course(BaseModel):
	db_path = setting.COURSE_DB

	def __init__(self, name, price, period, school_id):
		self.nid = identifier.CourseNid(Course.db_path)
		self.courseName = name
		self.coursePeriod = period
		self.coursePrice = price
		self.schoolId = school_id

	def __str__(self):
		return "课程名：%s；课程价格：%s；课程周期：%s；所属学校：%s" % (
			self.courseName, self.coursePrice, self.coursePeriod, self.schoolId.get_obj_by_uuid().schoolName)

	@staticmethod
	def get_all_list():
		ret = []
		for item in os.listdir(Course.db_path):
			obj = pickle.load(open(os.path.join(Course.db_path, item), 'rb'))
			ret.append(obj)
			print(type(obj))
		return ret
