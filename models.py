import datetime
import pymysql
from config import *


# 数据库信息（请按实际情况修改）
def db_info():
    db = pymysql.connect(
        host=get_mysql_host(),
        port=get_mysql_port(),
        user=get_mysql_user(),
        password=get_mysql_password(),
        database=get_mysql_database(),
        charset=get_mysql_charset()
    )
    return db


# 排序查询数据库里的学生准考证号和姓名
def getstudents():
    # 打开数据库连接
    db = db_info()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM students ORDER BY priority,zkzh"
    # print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # print(results)
        # 关闭数据库连接
        db.close()
        return results
    except:
        # 关闭数据库连接
        db.close()
        return False


# 保存cookie到数据库
def setCookie(zkzh, cookie):
    # 打开数据库连接
    db = db_info()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    cookies_timeout = datetime.datetime.now() + datetime.timedelta(minutes=5)
    sql = "UPDATE students SET cookies='%s',cookies_timeout='%s' WHERE zkzh='%s'" % (cookie, cookies_timeout, zkzh)
    # print(sql)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 发生错误时回滚
        db.rollback()
        # 关闭数据库连接
        db.close()
        return False


# 查询数据库中的Cookie
def getCookie(zkzh):
    # 打开数据库连接
    db = db_info()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM students WHERE zkzh=" + zkzh
    # print(sql)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # zkzh = row[0]
            # name = row[1]
            # email = row[2]
            # priority = row[3]
            cookies = row[4]
            cookies_timeout = row[5]
        # 关闭数据库连接
        db.close()
        return [cookies, cookies_timeout]
    except:
        # 关闭数据库连接
        db.close()
        return False


# 查询数据库中的Cookie
def getname_email(zkzh):
    # 打开数据库连接
    db = db_info()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM students WHERE zkzh=" + zkzh
    # print(sql)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # zkzh = row[0]
            name = row[1]
            email = row[2]
            # priority = row[3]
            # cookies = row[4]
            # cookies_timeout = row[5]
        # 关闭数据库连接
        db.close()
        return [name, email]
    except:
        # 关闭数据库连接
        db.close()
        return False


# 查询数据库中学生的考期和订阅情况
def getexam_month(zkzh):
    # 打开数据库连接
    db = db_info()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM students WHERE zkzh=" + zkzh
    # print(sql)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # zkzh = row[0]
            # name = row[1]
            # email = row[2]
            # priority = row[3]
            # cookies = row[4]
            # cookies_timeout = row[5]
            exam_month = row[6]
        # 关闭数据库连接
        db.close()
        if exam_month not in [1,4,7,10]:
            print("\nexam_month的值不正确，请检查数据表数据！")
            input("回车以退出")
            exit(1)
        return exam_month
    except:
        # 关闭数据库连接
        db.close()
        return False


# 设置数据库中学生的考期和订阅情况
def setexam_month(zkzh, exam_month):
    # 打开数据库连接
    db = db_info()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "UPDATE students SET exam_month=%d WHERE zkzh='%s'" % (exam_month, zkzh)
    # print(sql)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 发生错误时回滚
        db.rollback()
        # 关闭数据库连接
        db.close()
        return False
