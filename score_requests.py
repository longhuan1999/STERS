import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import models
from tableProcess import tableProcess
from config import get_admin_exam_month
from log import log
import gzip
from io import BytesIO
from e_Mail import Mail
import datetime


# https://www.jseea.cn/webfile/examination/selflearning/
# https://sdata.jseea.cn/tpl_front/score/practiceScoreList.html
# https://sdata.jseea.cn/tpl_front/score/allScoreList.html
def toZiKao(zkzh):
    url = "https://www.jseea.cn/webfile/examination/selflearning/"
    headers = {
        'Host': 'www.jseea.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': 1,
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': 1,
    }

    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(url=url, headers=headers)
    try:
        logmsg = "尝试访问：" + url
        log(zkzh, logmsg)
        response = opener.open(request)
        cookie_str = ""
        for item in cookie:
            cookie_str += item.name + "=" + item.value + ";"
        cookie = cookie_str.rstrip(";")
        logmsg = url + "的Cookie：\n" + cookie
        log(zkzh, logmsg)
        models_return = models.setCookie(zkzh, cookie)
        if models_return != True:
            msg = "保存%s的Cookie时数据库报错，程序终止！请检查数据库配置和数据库状态！" % zkzh
            log(zkzh, msg)
            ret = Mail(zkzh, 1, msg, '')
            if ret:
                log(zkzh, "邮件发送成功")
            else:
                log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
            exit(1)
        return cookie
    except urllib.error.HTTPError as e:
        msg = 'code: ' + str(e.code) + '\n'
        msg += 'reason: ' + e.reason + '\n'
        msg += 'headers: {\n' + str(e.headers) + '}\n'
        log(zkzh, msg)
        ret = Mail(zkzh, e.code, msg, '')
        if ret:
            log(zkzh, "邮件发送成功")
        else:
            log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
        return e.code


def toSelectScore(zkzh, cookie):
    url = "https://sdata.jseea.cn/tpl_front/score/practiceScoreList.html"
    headers = {
        'Host': 'sdata.jseea.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.jseea.cn/webfile/examination/selflearning/',
        'DNT': 1,
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': 1,
        'Cache-Control': 'max-age=0'
    }

    cookie1 = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie1)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(url=url, headers=headers)
    try:
        logmsg = "尝试访问：" + url
        log(zkzh, logmsg)
        response = opener.open(request)
        cookie_str = cookie + ";"
        for item in cookie1:
            cookie_str += item.name + "=" + item.value + ";"
        cookie = cookie_str.rstrip(";")
        logmsg = url + "的Cookie：\n" + cookie
        log(zkzh, logmsg)
        models_return = models.setCookie(zkzh, cookie)
        if models_return != True:
            msg = "保存%s的Cookie时数据库报错，程序终止！请检查数据库配置和数据库状态！" % zkzh
            log(zkzh, msg)
            ret = Mail(zkzh, 1, msg, '')
            if ret:
                log(zkzh, "邮件发送成功")
            else:
                log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
            exit(1)
        return cookie
    except urllib.error.HTTPError as e:
        msg = 'code: ' + str(e.code) + '\n'
        msg += 'reason: ' + e.reason + '\n'
        msg += 'headers: {\n' + str(e.headers) + '}\n'
        log(zkzh, msg)
        if e.code == 504:
            return 504
        else:
            ret = Mail(zkzh, e.code, msg, '')
            if ret:
                log(zkzh, "邮件发送成功")
            else:
                log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")


def selectScore(zkzh, name, new_exam_day):
    cookie = models.getCookie(zkzh)
    if cookie == False:
        msg = "获取%s的Cookie时数据库报错，程序终止！请检查数据库配置和数据库状态！" % zkzh
        log(zkzh, msg)
        ret = Mail(zkzh, 1, msg, '')
        if ret:
            log(zkzh, "邮件发送成功")
        else:
            log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
        exit(1)
    if cookie[0]:
        if cookie[1] <= datetime.datetime.now() or ";" not in cookie[0]:
            cookie = toZiKao(zkzh)
            cookie = toSelectScore(zkzh, cookie)
        else:
            cookie = cookie[0]
    else:
        cookie = toZiKao(zkzh)
        cookie = toSelectScore(zkzh, cookie)
    # 如果cookie返回值为以下错误代码，返回到main循环检查
    if cookie in [301, 302, 303, 304, 307, 400, 401, 403, 404, 500, 503, 504]:
        return cookie
    url = 'https://sdata.jseea.cn/tpl_front/score/allScoreList.html'
    params = {
        'zkzh': zkzh,
        'ksmx': name
    }
    headers = {
        'Host': 'sdata.jseea.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://sdata.jseea.cn',
        'DNT': 1,
        'Connection': 'keep-alive',
        'Referer': 'https://sdata.jseea.cn/tpl_front/score/practiceScoreList.html',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': 1,
    }
    data = bytes(urllib.parse.urlencode(params), encoding='utf8')
    #print(cookie)
    #print(type(cookie))
    print(params)
    print(data)
    try:
        logmsg = "尝试访问：" + url + "\n准考证：%s，姓名：%s"%(zkzh,name)
        log(zkzh, logmsg)
        request = urllib.request.Request(url, data)
        for i in headers:
            request.add_header(i, headers[i])
        print(request.__dict__)
        response = urllib.request.urlopen(request)
        htmls = response.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        #print(htmls)
        #print(response.getcode())
        htmls = tableProcess(htmls)
        log(zkzh, htmls)
        if new_exam_day not in htmls:
            return "无新成绩记录"
        else:
            exam_month = models.getexam_month(zkzh)
            if exam_month == get_admin_exam_month():
                Mail(zkzh, 200, "似乎有新成绩了", htmls)
                if exam_month == 10:
                    exam_month = 1
                else:
                    exam_month += 3
                models.setexam_month(zkzh, exam_month)
            return 200

    except urllib.error.HTTPError as e:
        msg = 'code: ' + str(e.code) + '\n'
        msg += 'reason: ' + e.reason + '\n'
        msg += 'headers: {\n' + str(e.headers) + '}\n'
        log(zkzh, msg)
        ret = Mail(zkzh, e.code, msg, '')
        if ret:
            log(zkzh, "邮件发送成功")
        else:
            log(zkzh, "邮件发送失败，请检查邮件和数据库配置以及数据库状态")
        return e.code
