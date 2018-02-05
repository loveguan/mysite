#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: admin_service.py

@time: 2018/1/31 22:38

@desc:

'''

from src.models import School
from src.models import Teacher
from src.models import Course
from src.models import Classes
from src.models import course_to_teacher


def show_choice():
	show = """
	        1. 创建学校
	        2. 查看学校
	        3. 创建老师
	        4. 创建课程
	        5. 查看课程
	        6. 创建老师课程对应关系
	        7. 创建班级
	        8. 查看老师
	    """
	print(show)


def create_school():
	name = input('请输入学校的名称')
	obj = School(name)
	obj.save()


def show_school():
	print('===========学校============')
	school_list = School.get_all_list()
	for obj in school_list:
		print(obj.schoolName)


def create_teacher():
	name = input('请输入教师的姓名：')
	level = input('输入教师的级别：')
	obj = Teacher(name, level)
	obj.save()


def show_teacher():
	print('老师信息如下：')
	teacher_list = Teacher.get_all_list()
	for obj in teacher_list:
		print('老师为%s,级别是%s' % (obj.teacherName, obj.teacherLevel))


def create_course():
	print('=============创建课程===============')
	school_list = School.get_all_list()
	for k, obj in enumerate(school_list, 1):
		print(k, obj)

	sid = input("请选择学校：")
	sid = int(sid)
	school_obj = school_list[sid - 1]
	print(type(school_obj.nid))
	name = input('请输入课程名称：')
	price = input('请输入课程价格：')
	period = input('请输入课程周期：')
	obj = Course(name, price, period, school_obj.nid)
	obj.save()
	print('课程【%s】创建成功' % name)
	print(obj)


def show_course():
	print('=========课程===========')
	course_list = Course.get_all_list()
	for item in course_list:
		print(item)


def create_course_teacher():
	print("请输入课程信息")
	course_list = Course.get_all_list()
	for key, obj2 in enumerate(course_list, 1):
		print(key, obj2)
	inp2 = input('请输入选择的号码：')
	inp2 = int(inp2)
	course = course_list[inp2 - 1]
	print('你选择的课程信息为：%s' % (course,))
	print('老师信息如下：')
	teacher_list = Teacher.get_all_list()
	for key, obj1 in enumerate(teacher_list, 1):
		print(key, obj1)
	inp1 = input("请输入选择的号码：")
	inp1 = int(inp1)
	teacher = teacher_list[inp1 - 1]
	print("选择的老师为：%s" % (teacher,))
	obj = course_to_teacher(course, teacher)
	obj.save()
	print('【%s,%s】创建成功' % (course, teacher))
	print(obj)


def create_class():
	# 获取老师
	teacher_list = Teacher.get_all_list()
	print(teacher_list)
	for key, i in enumerate(teacher_list, 1):
		print(key, i)
	tid = input('请输入教师的编号：')
	tid = int(tid)
	teacher_id = teacher_list[tid - 1].nid
	print(type(teacher_id))
	print(teacher_id)
	print(teacher_id.uuid)
	name = input('请输入班级的名称:')
	price = input('输入价格：')
	# 获取学校
	school_list = School.get_all_list()
	for key, i in enumerate(school_list, 1):
		print(key, i)
	sid = input('请输入学校id：')
	sid = int(sid)
	school_id = school_list[sid - 1].nid

	obj = Classes(name, price, school_id, teacher_id)
	obj.save()
	print(obj)


def main():
	choice_dict = {
		'0': show_choice,
		'1': create_school,
		'2': show_school,
		'3': create_teacher,
		'4': create_course,
		'5': show_course,
		'6': create_course_teacher,
		'7': create_class,
		'8': show_teacher,
	}

	while True:
		show_choice()
		inp = input('请输入选项：')
		if inp not in choice_dict:
			print('选项错误，请重新选择！！！')
			continue

		func = choice_dict[inp]
		result = func()
# print(result)
