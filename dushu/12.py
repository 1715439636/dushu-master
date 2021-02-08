import smtplib
import os


# 发件人邮箱账号
my_sender = os.getenv('MAIL_USERNAME')
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
my_pass = os.getenv('MAIL_PASSWORD')
# 收件人邮箱账号
my_user = 'wei.tong@dianrong.com'

#
# sender = 'quanweiru@163.com'
#
# receivers = ['quanweiru@hotmail.com']

message = """From: From Person <quanweiru@163.com>

To: To Person <quanweiru@hotmail.com>

Subject: SMTP e-mail test



This is a test e-mail message.

"""

try:

    smtpObj = smtplib.SMTP('smtp.163.com')

    smtpObj.login(my_sender, my_pass)  # XXX为用户名，******为密码

    smtpObj.sendmail(my_sender, my_user, message)

    smtpObj.quit()

    print ("Successfully sent email")

except Exception:

    print ( "Error: unable to send email")