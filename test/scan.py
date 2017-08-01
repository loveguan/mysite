"""
@version: ??
@author: Guanjie Zhou
@license: Apache Licence
@file: dis_port_threading.py
@time: 17-5-27 上午8:21
"""

import socket
import threading
import time
import smtplib
from email.mime.text import  MIMEText
from email.header import Header


sender = '15063176713@139.com'
receiver = ['15063176713@139.com' ]
subject = 'error,链路不通'
smtpserver = 'smtp.163.com'
username = '15063176713@139.com'
password = 'zhou789099'
message = 'nadiadlad,你是我电话'
msg = MIMEText(message, 'plain', 'utf-8')
# 中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
# msg['To'] = ','.join(receiver)
smtp = smtplib.SMTP()
smtp.connect('smtp.139.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()