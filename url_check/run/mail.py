#!/usr/bin/env python

# encoding: utf-8

'''

@author: JOJ

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: zhouguanjie@qq.com

@software: JOJ

@file: mail.py

@time: 2018/1/17 9:50

@desc:

'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from conf import setting

sender = setting.mail_config['sender']
username = setting.mail_config['username']
password = setting.mail_config['password']
reciver = setting.reciver
subject = '链路测试消息'

def mail(Flag_err, logger_type):
	message = '链路测试正常'
	if Flag_err:
		log_path = "%s\log\%s" % (setting.BASE_DIR, setting.LOG_TYPES[logger_type])
		message="Error!!!!!!!!!!\n\r"
		with open(log_path) as f:
			for line in f:
				message +=  line

	send_mail(message)


def send_mail(message):
	msg = MIMEText(message, 'plain', 'utf-8')
	# 中文需参数‘utf-8’，单字节字符不需要
	msg['Subject'] = Header(subject, 'utf-8')
	msg['To'] = ','.join(reciver)
	smtp = smtplib.SMTP()
	smtp.connect('smtp.139.com')
	smtp.login(username, password)
	smtp.sendmail(sender, reciver, msg.as_string())
	smtp.quit()
