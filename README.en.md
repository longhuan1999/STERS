> As the second testing project during `Django` study, this project will not be maintained for the time being, and will only be used as my study record.

# 自考成绩订阅（STERS）
Self taught examination results subscription

#### Description
This is a project written in `Python` that is used to automatically check and obtain new scores of self-taught examination and send them by email. This is the main part of the program.

#### Software Architecture

1. Steps.py is the program entry.
2. reponsed_ Check.py is used to control the process of checking whether new scores of self-taught examination are published and querying new scores.
3. score_ Requests.py is used to query the results from the official website. The default is Jiangsu. Other regions can modify it according to the actual situation.
4. Tableprocess.py is used to process transcripts obtained from the official website.
5. Sendscores.py is used to get the list of students in the database, so that you can query and send them transcripts.
6. Mmodels.py is used to access the database. If you are not using MySQL or do not create the database according to the SQL file, you may need to customize it.
7. Config.py is used to read and modify the configuration file config.ini.
8. Config.ini includes database configuration, mail configuration and other related configurations.
9. e_ Mail.py is used to send all kinds of mail.
10. Log.py is used to generate logs.

#### Installation

1. Environment: Python 3.9
2. Dependent package installation: pip3 install -r requirements.txt
3. Create database: Create or customize database according to SQL file. You may need to modify models.py . When I developed, I used MySQL 8.0, database (utf8mb4, utf8mb4_general_ci）：steris_ Students, data table: Students

#### Instructions

1.  Create the configuration file config.ini according to config.ini.example
2. Start: python3 main.py