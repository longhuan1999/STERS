import smtplib
import models
from email.mime.text import MIMEText
from email.utils import formataddr
from log import log
from config import *

frmt = "%Y-%m-%d %H:%M:%S"


def signupMail(zkzh, signup_info):
    ret = True
    admin_zkzh = get_admin_zkzh()
    admin_addr = get_email_admin_addr()
    from_addr_name = get_email_from_addr_name()
    from_addr = get_email_from_addr()
    host = get_email_host()
    passwd = get_email_passwd()
    try:
        if zkzh != admin_zkzh:
            to_addr = models.getname_email(zkzh)[1]
            to_addr_name = models.getname_email(zkzh)[0]
            logmsg = "给%s的邮箱%s发送注册成功信息" % (to_addr_name, to_addr)
            log(admin_zkzh, logmsg)
        elif zkzh == admin_zkzh:
            to_addr = admin_addr
            to_addr_name = "管理员"
            logmsg = "给%s的邮箱%s发送注册成功信息" % (to_addr_name, to_addr)
            log(admin_zkzh, logmsg)
        msgtext = signup_info
        msg = MIMEText(msgtext, 'html', 'utf-8')
        msg['From'] = formataddr([from_addr_name, from_addr])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([to_addr_name, to_addr])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "注册成功"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(from_addr, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(from_addr, [to_addr, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


def ipLocationMail(msg):
    ret = True
    admin_zkzh = get_admin_zkzh()
    admin_addr = get_email_admin_addr()
    from_addr_name = get_email_from_addr_name()
    from_addr = get_email_from_addr()
    host = get_email_host()
    passwd = get_email_passwd()
    try:
        msgtext = 'IP地址归属查询接口异常:\n%s' % (msg)
        msg = MIMEText(msgtext, 'plain', 'utf-8')
        msg['From'] = formataddr([from_addr_name, from_addr])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["管理员", admin_addr])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "IP地址归属查询接口异常"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(from_addr, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(from_addr, [admin_addr, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


def rebackTimeMail(zkzh, rebackTime):
    ret = True
    admin_zkzh = get_admin_zkzh()
    admin_addr = get_email_admin_addr()
    from_addr_name = get_email_from_addr_name()
    from_addr = get_email_from_addr()
    host = get_email_host()
    passwd = get_email_passwd()
    try:
        to_addr = admin_addr
        to_addr_name = "管理员"
        if zkzh != admin_zkzh:
            msgtext = '在查询%s的成绩时检测到504，官方自考成绩查询入口已关闭，将在 %s 重试' % (zkzh, rebackTime.strftime(frmt))
        elif zkzh == admin_zkzh:
            msgtext = '检测到504，官方自考成绩查询入口已关闭，将在 %s 重试' % (rebackTime.strftime(frmt))
        log(zkzh, msgtext)
        msg = MIMEText(msgtext, 'plain', 'utf-8')
        msg['From'] = formataddr([from_addr_name, from_addr])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([to_addr_name, to_addr])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "检测到504，官方自考成绩查询入口已关闭"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(from_addr, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(from_addr, [to_addr, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


def nextTimeMail(zkzh, nextTime, response):
    ret = True
    admin_zkzh = get_admin_zkzh()
    admin_addr = get_email_admin_addr()
    from_addr_name = get_email_from_addr_name()
    from_addr = get_email_from_addr()
    host = get_email_host()
    passwd = get_email_passwd()
    try:
        to_addr = admin_addr
        to_addr_name = "管理员"
        if zkzh != admin_zkzh:
            msgtext = '在查询%s的成绩时检测到 %s，官方自考成绩查询入口异常，将在 %s 重试' % (zkzh, str(response), nextTime.strftime(frmt))
        elif zkzh == admin_zkzh:
            msgtext = '检测到 %s，官方自考成绩查询入口异常，将在 %s 重试' % (str(response), nextTime.strftime(frmt))
        msg = MIMEText(msgtext, 'plain', 'utf-8')
        msg['Subject'] = "检测到 %s，官方自考成绩查询入口异常" % (str(response))  # 邮件的主题，也可以说是标题
        log(zkzh, msgtext)

        msg['From'] = formataddr([from_addr_name, from_addr])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([to_addr_name, to_addr])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        server = smtplib.SMTP_SSL(host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(from_addr, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(from_addr, [to_addr, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


def Mail(zkzh, code, msg, content):
    admin_zkzh = get_admin_zkzh()
    admin_addr = get_email_admin_addr()
    from_addr_name = get_email_from_addr_name()
    from_addr = get_email_from_addr()
    host = get_email_host()
    passwd = get_email_passwd()
    if zkzh != admin_zkzh:
        to_addr = models.getname_email(zkzh)[1]
        to_addr_name = models.getname_email(zkzh)[0]
    elif zkzh == admin_zkzh:
        to_addr = admin_addr
        to_addr_name = "管理员"
    ret = True
    try:
        if msg == "似乎有新成绩了":
            msgtext = '<html><p>返回码 %s<br>\n%s<br>详细内容：</p>\n%s\n</html>' % (str(code), msg, content)
            msg = MIMEText(msgtext, 'html', 'utf-8')
        else:
            msgtext = '在查询%s的成绩时，返回码 %s\n%s详细内容：\n%s' % (zkzh, str(code), msg, content)
            msg = MIMEText(msgtext, 'plain', 'utf-8')
            to_addr = admin_addr
            to_addr_name = "管理员"
        log(zkzh, msgtext)
        msg['From'] = formataddr(["endless小龙的自考成绩查询系统", from_addr])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([to_addr_name, to_addr])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        if msg == "似乎有新成绩了":
            msg['Subject'] = "似乎有新成绩了!" % (str(code))  # 邮件的主题，也可以说是标题
        else:
            msg['Subject'] = "返回码 %s" % (str(code))  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(from_addr, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(from_addr, [to_addr, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret