# _*_coding:utf-8_*_
from django.db import models


# Create your models here.



class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class Colors(models.Model):
    colors = models.CharField(u'颜色', max_length=10)

    def __unicode__(self):
        return self.colors


class Ball(models.Model):
    color = models.OneToOneField("Colors")
    description = models.CharField(u'描述', max_length=10)

    def __unicode__(self):
        return self.description


class Clothes(models.Model):
    color = models.ForeignKey("Colors")
    description = models.CharField(u'描述', max_length=10)

    def __unicode__(self):
        return self.description

class Child(models.Model):
    name=models.CharField(u'姓名',max_length=10)
    favor=models.ManyToManyField('Colors')


