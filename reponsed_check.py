import datetime
import random
import time
from e_Mail import rebackTimeMail, nextTimeMail
from log import log
from score_requests import selectScore
from config import *

frmt = "%Y-%m-%d %H:%M:%S"


# 根据自考日程检查当前是否在查询新成绩的时间段内并返回本次考期
def exam_day():
    thisyear = datetime.datetime.now().strftime("%Y-")
    timenow = datetime.datetime.now()
    score_check_days_str = ["01-25 09:00:00", "02-25 21:00:00", "04-25 09:00:00", "05-25 21:00:00", "07-25 09:00:00",
                            "08-25 21:00:00", "10-25 09:00:00", "11-25 21:00:00"]
    score_check_days = []
    for i in score_check_days_str:
        i = datetime.datetime.strptime(thisyear + i, "%Y-%m-%d %H:%M:%S")
        score_check_days.append(i)
    exam_month = get_admin_exam_month()
    if exam_month == 1:
        if score_check_days[0] <= timenow < score_check_days[1]:
            return score_check_days[0].strftime("%Y年%m月")
        else:
            return False
    elif exam_month == 4:
        if score_check_days[2] <= timenow < score_check_days[3]:
            return score_check_days[2].strftime("%Y年%m月")
        else:
            return False
    elif exam_month == 7:
        if score_check_days[4] <= timenow < score_check_days[5]:
            return score_check_days[4].strftime("%Y年%m月")
        else:
            return False
    elif exam_month == 10:
        if score_check_days[6] <= timenow < score_check_days[7]:
            return score_check_days[6].strftime("%Y年%m月")
        else:
            return False


# 自考成绩查询接口关闭时计算下次恢复时间
def rebackTime_def():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timenow = datetime.datetime.now()
    time1 = datetime.datetime.strptime(today + " 00:00:00", frmt)
    time2 = datetime.datetime.strptime(today + " 09:00:00", frmt)
    time3 = datetime.datetime.strptime(today + " 12:00:00", frmt)
    time4 = datetime.datetime.strptime(today + " 21:00:00", frmt)
    time5 = datetime.datetime.strptime(today + " 00:00:00", frmt) + datetime.timedelta(days=1)
    if time1 <= timenow < time2:
        rebackTime = time2
    elif time2 <= timenow < time3:
        rebackTime = nextTime_def()
    elif time3 < timenow <= time4 or time4 < timenow < time5:
        rebackTime = time2 + datetime.timedelta(days=1)
    return rebackTime


# 未查询到新成绩时延迟10-15分钟重试
def nextTime_def():
    start = datetime.datetime.now() + datetime.timedelta(minutes=10)
    start = start.strftime(frmt)
    end = datetime.datetime.now() + datetime.timedelta(minutes=15)
    end = end.strftime(frmt)
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + random.random() * (etime - stime)
    ptime = int(ptime)
    randomDate = time.strftime(frmt, time.localtime(ptime))
    randomDate = datetime.datetime.strptime(randomDate, frmt)
    return randomDate


def reponsed_check(zkzh, name):
    new_exam_day = exam_day()
    if new_exam_day is False:
        logmsg = "当前查询新成绩的考期为%s月\n" % get_admin_exam_month()
        logmsg += "当前不在查询新成绩的时间段内，等待中...\n查询新成绩的时间段：\n01月25日09:00——02月25日21:00\n04月25日09:00——05月25日21:00\n07月25日09:00" \
                  "——08月25日21:00\n10月25日09:00——11月25日21:00 "
        log(zkzh, logmsg)
        while True:
            time.sleep(1)
            new_exam_day = exam_day()
            if new_exam_day is False:
                continue
            else:
                break
    response = selectScore(zkzh, name, new_exam_day)  # 查询一次新成绩
    # 自考成绩查询接口关闭时处理
    if response == 504:
        rebackTime = rebackTime_def()
        ret = rebackTimeMail(zkzh, rebackTime)
        if ret:
            log(zkzh, "邮件发送成功")
        else:
            log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
        while True:
            time.sleep(1)
            if datetime.datetime.now() < rebackTime:
                continue
            else:
                return 504
    # 自考成绩查询接口异常或未查询到新成绩时处理
    elif response in [301, 302, 303, 304, 307, 400, 401, 403, 404, 500, 503] or response == "无新成绩记录":
        nextTime = nextTime_def()
        if response == "无新成绩记录":
            if zkzh != get_admin_zkzh():
                msgtext = '无新成绩记录，跳过'
                log(zkzh, msgtext)
                return response
            else:
                msgtext = '暂无新成绩记录，将在 %s 重试' % (nextTime.strftime(frmt))
                log(zkzh, msgtext)
        else:
            if zkzh != get_admin_zkzh():
                ret = nextTimeMail(zkzh, nextTime, response)
                if ret:
                    log(zkzh, "邮件发送成功")
                else:
                    log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
                    return response
            ret = nextTimeMail(zkzh, nextTime, response)
            if ret:
                log(zkzh, "邮件发送成功")
            else:
                log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
        while True:
            time.sleep(1)
            if datetime.datetime.now() < nextTime:
                continue
            else:
                return False
    # 查询到新成绩后处理
    elif response == 200:
        return 200
