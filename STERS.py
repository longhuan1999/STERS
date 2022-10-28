from reponsed_check import reponsed_check
from sentScores import sentScores
from config import *
from log import log


# 循环检查新成绩
def scoreDetect(zkzh, name):
    while True:
        response = reponsed_check(zkzh, name)

        if response == 200:
            # 若管理员的准考证查询新成绩公布，则查询发送其他同学的成绩
            sentScores()
            exam_month = get_admin_exam_month()
            if exam_month == 10:
                set_admin_exam_month(1)
                log(zkzh, "修改当前查询新成绩的考期为1月")
            else:
                set_admin_exam_month(exam_month+3)
                log(zkzh, "修改当前查询新成绩的考期为1月")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    zkzh = get_admin_zkzh()
    name = get_admin_name()
    # 使用管理员的准考证查询是否有新成绩公布
    scoreDetect(zkzh, name)
