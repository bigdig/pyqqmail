#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
import time
import yaml
from email.mime.text import MIMEText

with open('mail.yaml') as f:
    mail = yaml.load(f)

mailto_list = mail['mailto_list']
smtp_host = mail['smtp_host']
smtp_ssl_port = mail['smtp_ssl_port']
mail_user = mail['mail_user']
mail_pass = mail['mail_pass']
mail_postfix = mail['mail_postfix']

def send_mail(sub, content):  #to_list：收件人；sub：主题；content：邮件内容
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"  
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(mailto_list)  
    try:
        s = smtplib.SMTP_SSL()  
        s.connect(smtp_host+':'+str(smtp_ssl_port))  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  #发送邮件
        s.close()  
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'：邮件发送成功'  
    except Exception, e:  
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'：邮件发送失败'  
        print str(e)

if __name__ == '__main__':
    send_mail('test', 'test')