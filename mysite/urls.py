"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cmdb import views
from cmdb import urls
from django.conf.urls import include,url
from mysite.activator import process
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 动态路由
    url('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))/(?P<id>(\d+))/$', process),
    url ('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\d+))/$', process),
    url ('^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
    url ('^(?P<app>(\w+))/$', process, {'function': 'index'}),
    # 引入分组，在各自的app下边建立url列表，自己处理自己的
    # url(r'^cmdb/', include("cmdb.urls")),
    # url(r'^index/', views.index),
    # url(r'^test/', views.test),
]
