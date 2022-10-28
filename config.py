from configparser import *
import os

# 读取ini文件
def read_cf():
    if os.path.isfile("config.ini") is False:
        print("\n配置文件config.ini不存在，请根据config.ini.example创建！")
        input("回车以退出")
        exit(1)
    cf = RawConfigParser()
    cf.read("config.ini", encoding="utf8")
    return cf


# 获取数据库配置
def get_mysql_host():
    cf = read_cf()
    try:
        mysql_host = cf.get("mysql", "host").strip('"')
    except NoSectionError:
        print("\n[mysql]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nhost不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return mysql_host


def get_mysql_port():
    cf = read_cf()
    try:
        mysql_port = cf.get("mysql", "port").strip('"')
        mysql_port = int(mysql_port)
    except NoSectionError:
        print("\n[mysql]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nport不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return mysql_port


def get_mysql_user():
    cf = read_cf()
    try:
        mysql_user = cf.get("mysql", "user").strip('"')
    except NoSectionError:
        print("\n[mysql]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nuser不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return mysql_user


def get_mysql_password():
    cf = read_cf()
    try:
        mysql_password = cf.get("mysql", "password").strip('"')
    except NoSectionError:
        print("\n[mysql]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nexam_month不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return mysql_password


def get_mysql_database():
    cf = read_cf()
    try:
        mysql_database = cf.get("mysql", "database").strip('"')
    except NoSectionError:
        print("\n[mysql]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\ndatabase不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return mysql_database


def get_mysql_charset():
    cf = read_cf()
    try:
        mysql_charset = cf.get("mysql", "charset").strip('"')
    except NoSectionError:
        print("\n[mysql]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\ncharset不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return mysql_charset


# 获取邮件系统设置
def get_email_host():
    cf = read_cf()
    try:
        email_host = cf.get("email", "host").strip('"')
    except NoSectionError:
        print("\n[email]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nhost不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return email_host


def get_email_passwd():
    cf = read_cf()
    try:
        email_passwd = cf.get("email", "passwd").strip('"')
    except NoSectionError:
        print("\n[email]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\npasswd不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return email_passwd


def get_email_from_addr():
    cf = read_cf()
    try:
        email_from_addr = cf.get("email", "from_addr").strip('"')
    except NoSectionError:
        print("\n[email]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nfrom_addr不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return email_from_addr


def get_email_from_addr_name():
    cf = read_cf()
    try:
        email_from_addr_name = cf.get("email", "from_addr_name").strip('"')
    except NoSectionError:
        print("\n[email]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nfrom_addr_name不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return email_from_addr_name


def get_email_admin_addr():
    cf = read_cf()
    try:
        email_admin_addr = cf.get("email", "admin_addr").strip('"')
    except NoSectionError:
        print("\n[email]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nadmin_addr不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return email_admin_addr


# 获取管理员设置
def get_admin_zkzh():
    cf = read_cf()
    try:
        admin_zkzh = cf.get("admin", "zkzh").strip('"')
    except NoSectionError:
        print("\n[admin]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nzkzh不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return admin_zkzh


def get_admin_name():
    cf = read_cf()
    try:
        admin_name = cf.get("admin", "name").strip('"')
    except NoSectionError:
        print("\n[admin]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nname不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return admin_name


def get_admin_exam_month():
    cf = read_cf()
    try:
        admin_exam_month = cf.get("admin", "exam_month").strip('"')
        admin_exam_month = int(admin_exam_month)
        if admin_exam_month not in [1,4,7,10]:
            print("\nexam_month的值不正确，请检查config.ini文件")
            input("回车以退出")
            exit(1)
    except NoSectionError:
        print("\n[admin]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nexam_month不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    return admin_exam_month


# 设置要检查新成绩的考期
def set_admin_exam_month(mon):
    mon = "\"" + str(mon) + "\""
    cf = read_cf()
    try:
        cf.set("admin", "exam_month", mon)
        cf.write(open("config.ini", "w", encoding="utf8"))
        return True
    except NoSectionError:
        print("\n[admin]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nexam_month不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
