import models
import time
from reponsed_check import reponsed_check
from log import log
from e_Mail import Mail
from config import *
from models import setexam_month


def sentScores():
    students = models.getstudents()
    if students == False:
        msg = "获取学生名单时数据库报错，程序终止！请检查数据库配置和数据库状态！"
        log(get_admin_zkzh(), msg)
        ret = Mail(get_admin_zkzh(), 1, msg, '')
        if ret:
            log(get_admin_zkzh(), "邮件发送成功")
        else:
            log(get_admin_zkzh(), "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
        exit(1)
    elif students == ():
        return True
    else:
        for s in students:
            zkzh = str(s[0]).strip()
            name = str(s[1]).strip()
            exam_month = s[6]
            if exam_month not in [1,4,7,10]:
                msg = "exam_month的值不正确，请检查数据表数据！"
                log(get_admin_zkzh(), msg)
                input("回车以退出")
                exit(1)
            elif exam_month != get_admin_exam_month():
                continue
            if zkzh == get_admin_zkzh():
                time.sleep(1)
                continue
            else:
                while True:
                    print("\n准考证：%s，姓名：%s\n"%(zkzh,name))
                    response = reponsed_check(zkzh, name)
                    # 查询到新成绩后处理
                    if response != 504:
                        time.sleep(10)
                        break
        return True
