#! /usr/bin/env python
# encoding=utf-8

import smtplib
from email.mime.text import MIMEText

mailto_list = ['715278509@qq.com']           #收件人(列表)
mail_host = "smtp.126.com"            #使用的邮箱的smtp服务器地址
mail_user = "zingly"                           #用户名
mail_pass = "##########"                             #密码
mail_postfix = "126.com"                     #邮箱的后缀

# mailto_list = ['zingly@126.com']
# mail_host = 'smtp.qq.com'
# mail_user = '715278509'
# mail_postfix = 'qq.com'

def send_mail(to_list, sub, content):
    me="circumstance"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False
# for i in range(5):                             #发送五封，不过会被拦截的。。。
if send_mail(mailto_list, "明天有空一起吃晚饭吗？？？？", "因为今天下雨，所以我问你这个问题。"):  #邮件主题和邮件内容
    print("done!")
else:
    print("failed!")
