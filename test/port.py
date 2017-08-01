#!/usr/bin/python
# -*- coding: utf-8 -*-

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



socket.setdefaulttimeout(1)
# 线程列表
threads = []
# 获取时间
stamp = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))


# 端口扫描函数

def socket_port(ip, port):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #  返回连接结果，成功的话返回为０，失败返回ｅｒｒｎｏ的值
        # 这里要注意的是下边的函数里边的为(ip, port)一个整体
        result = s.connect_ex((ip, port))
        if result == 0:
            print('[ OK  ] ip: %s, port: %d is open' % (ip, port))
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            tt = "check port sucess!"
            logfile = "ok" + "-" + stamp + ".log"
            f = open(logfile, 'a+')
            f.write(now + "  " + ip + ":" + str(port) + "  " + tt + "\n")
            f.close()
        else:
            print('[ERROR] ip: %s, port: %d close ' % (ip, port))
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            tt = "check port failed!"
            logfile = "error" + "-" + stamp + ".log"
            f = open(logfile, 'a+')
            f.write(now + "  " + ip + ":" + str(port) + "  " + tt + "\n")
            f.close()
    except:
        print(u"端口扫描异常")


def ip_scan(ip, port_range):
    # 输入ｉｐ地址后，扫描在范围内的端口占用情况
    try:
        start_time = time.time()
        # 处理分解字符串
        for port in port_range.strip('(').strip(')').split(','):
            t = threading.Thread(target=socket_port, args=(ip, int(port)))
            # 将线程加入线程列表
            threads.append(t)
            t.start()
        # 线程加ｊｏｉｎ
        for t in threads:
            t.join()
        end_time = time.time()
        print(u'[*] %s扫描完成，总共用时：　%.2f 秒' % (ip, (end_time - start_time)))
        send_Mail()
    except:
        print(u"端口扫描出错")

# 解析文本函数
def parse_ip():
    for line in open('ip'):
        if line != '\n':
            ip, port = line.replace('\n', '').split(':')
            ip_scan(ip, port)

# 发送邮件函数
def send_Mail():
    sender = 'zhouguanjie2005@163.com'
    receiver = 'zhouguanjie2005@163.com'
    subject = 'python email test'
    smtpserver = 'smtp.163.com'
    username = 'zhouguanjie2005@163.com'
    password = 'zhou789128'
    msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()



if __name__ == '__main__':
    parse_ip()
