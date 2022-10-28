> 本项目作为学习`Django`时的第二个尝试的项目暂时不再维护，仅作本人的学习记录。当时`Python`会的不多，连类都不会写，全是函数...

# 自考成绩订阅（STERS）

#### 介绍
用`Python`写的一个用于自动检查和获取自考新成绩并通过邮件发送的项目，这是主要程序部分。

#### 软件架构

1. STERS.py为程序入口
2. reponsed_check.py是用来控制检查自考新成绩是否公布和查询新成绩的过程
3. score_requests.py用来向官网查询成绩，默认是江苏，其他地区根据实际情况修改（官网接口可能已发送变化）
4. tableProcess.py是用来处理从官网获取的成绩单
5. sentScores.py是用来获取数据库中的学生名单，以便查询并向他们发送成绩单
6. mmodels.py是用来访问数据库的，如果使用的不是mysql或者不按照sql文件创建数据库可能需要自定义
7. config.py是用来读取和修改config.ini配置文件的
8. config.ini包含了数据库配置、邮件配置和其他相关配置
9. e_Mail.py是用来发送各种邮件的
10. log.py是用来生成日志的

#### 安装教程

1.  环境：python3.9
2.  依赖包安装：pip3 install -r requirements.txt
3.  创建数据库：根据sql文件创建或者自定义数据库。可能需要修改models.py，开发时使用的是mysql 8.0，数据库（utf8mb4、utf8mb4_general_ci）：steris_students，数据表：students

#### 使用说明

1.  根据config.ini.example创建config.in配置文件
2.  启动：python3 main.py
