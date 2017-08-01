#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import dns.rdtypes
import dns.resolver
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sys.path.append('E:\PycharmProjects\mysite\test')
import answer
import os
import logging
import time

# 日志路径
log_path = os.path.join('/script/url_check', 'log.txt')
print(log_path)
# 获取时间
stamp = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
file_name = 'error' + '-' + stamp + '.txt'
# 错误日志路径
error_log_path = os.path.join('url_check', file_name)
# error_log_path = os.path.join('/script/url_check', file_name)
print(error_log_path)
# 日志文件
logging.basicConfig(filename=log_path, level=logging.INFO)
# 错误日志文件
logging.basicConfig(filename=error_log_path, level=logging.ERROR)


# 比较url获取的运营商的ip与记录的ip是否相同
def diff(url, ip, changjia):
    # 根据运行商，url对应获取ip
    res_ip = answer.ip_source.get(changjia).get(str(url), -1)
    if str(ip) in res_ip:
        print('[ OK ] %s %s ip is %s OK!!!' % (str(changjia), str(url), str(ip)))
        logging.info('[ OK ] %s %s ip is %s OK!!!' % (str(changjia), str(url), str(ip)))
    else:
        # 记录日志，如有问题
        print('[ ERROR ] %s %s ip is %s ERROE!!!' % (str(changjia), str(url), str(ip)))
        logging.info('[ ERROR ] %s %s ip is %s ERROR!!!' % (str(changjia), str(url), str(ip)))
        # 错误日志，每天一个一个文件
        file_error = open(error_log_path, 'a+')
        file_error.write('[ ERROR ] %s %s ip is %s ERROR!!! \n' % (str(changjia), str(url), str(ip)))


# 解析ip与url函数
def URL2IP(changjia, dip):
    for oneurl in urllist.readlines():
        url = str(oneurl.strip())[7:]

        try:
            my_resolver = dns.resolver.Resolver()
            my_resolver.nameservers = [socket.gethostbyname(dip)]
            ans = my_resolver.query(url, 'A')
            for i in ans.response.answer:
                for ip in i.items:
                    diff(url, ip, changjia)
        except:
            print("this URL 2 IP ERROR ")


# 发送邮件函数
def send_Mail():
    sender = '15063176713@139.com'
    receiver = ['15063176713@139.com', 'zhouguanjie@qq.com', 'zhouguanjie2005@163.com']
    subject = '**域名测试**'
    smtpserver = 'smtp.139.com'
    username = '15063176713@139.com'
    password = 'zhou789099'
    message = '域名解析测试正常！！!'
    # 如果存在err.log信息，读取error日志里边的文件
    # print(os.path.getsize(error_log_path))
    if os.path.exists(error_log_path):
        file_object = open(error_log_path)
        message = file_object.read()
        file_object.close()
    msg = MIMEText(message, 'plain', 'utf-8')
    # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.139.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


# source = {'liantong': '202.102.152.3',
#           'dianxin': '219.150.32.132',
#           'yidong': '211.141.16.99',
#           }
# # 遍历运营商执行文件
# for i in source.keys():
#     logging.info("\n--------------%s parse--------------------\n" % (i))
#     urllist = open("/script/url_check/urllist.txt", "r")
#     URL2IP(i, source[i])
#     urllist.close()
# # 发送邮件
# send_Mail()
# # 日志分割线
# print("----------------- %s complete! ------------------ \n" % (stamp))
# logging.info("----------------- %s complete! ------------------ \n" % (stamp))

try:

# 源列表
    source = {'liantong': '202.102.152.3',
              'dianxin': '219.150.32.132',
              # 'yidong':[]
              }

    # 遍历运营商执行文件
    for i in source.keys():
        urllist = open("urllist.txt", "r")
        URL2IP(i, source[i])
        urllist.close()
    # 发送邮件
    send_Mail()
    # 日志分割线
    print("----------------- %s complete! ------------------ \n" % (stamp))
    logging.info("----------------- %s complete! ------------------ \n" % (stamp))
except:
    print("ERROR !")
