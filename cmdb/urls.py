#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/6/22 15:05
# @Author  : joj
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from cmdb import views


urlpatterns = [
    url(r'^index/', views.index),
]