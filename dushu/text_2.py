# -*- coding: UTF-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import formataddr
import pandas as pd
from pyspark.sql import SQLContext
from pyspark import SparkContext, HiveContext

import zipfile

# 发件人邮箱账号
my_sender = os.getenv('MAIL_USERNAME')
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
my_pass = os.getenv('MAIL_PASSWORD')
# 收件人邮箱账号
my_user = 'wei.tong@dianrong.com'



sc = SparkContext(appName = "baidu_touci")
sqlContext = HiveContext(sc)

data = sqlContext.sql("select lender_id ,portfolio_amount,principal,yesterday_cnt , 7day_cnt, log_time from dw.f_principle_active_user_num  where  substr(log_time,1,10) = date_add(current_date(),-1)  " ).collect()
saved = pd.DataFrame(data,columns = ["用户ID" ,"持有债权总额","充提差","T-1活跃用户数" , "7天活跃用户数", "日期"])
saved.to_csv('T-1_active_user_num.csv',encoding = "utf-8",index=False)

f = zipfile.ZipFile('T-1_active_user_num.zip', 'w', zipfile.ZIP_DEFLATED)
f.write('T-1_active_user_num.csv')
f.close()

sender = 'dataautosend@dianrong.com'
receivers = ['wei.tong@dianrong.com' ] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# ,'minjie.chen@dianrong.com'],'yunchao.lu@dianrong.com' ,'minjie.chen@dianrong.com','yunchao.lu@dianrong.com'
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = formataddr(("dataautosend", 'dataautosend@dianrong.com'))
message['To'] =  formataddr(("wei.tong", 'wei.tong@dianrong.com'))
# message['To'] =  formataddr(("yunchao.lu", 'yunchao.lu@dianrong.com'))
# message['To'] =  formataddr(("minjie", 'minjie.chen@dianrong.com'))
subject = "T-1天活跃用户数据"
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('Hi，附件是T-1天活跃用户数据，包括计活跃用户aid、持有债权总额、充提差、T-1活跃用户数、7天用户登录次数,日期;',  'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
part = MIMEApplication(open('T-1_active_user_num.zip','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="T-1_active_user_num.zip")
message.attach(part)
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"







