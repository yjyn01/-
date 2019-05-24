# -*- coding: UTF-8 -*-


import os

from sqlalchemy import create_engine

name = ['IP', 'app', 'daytime', 'platform', 'channel_type', 'channel', 'user_id',
		'device_id', 'system_version', 'brand', 'model', 'version', 'event_id', 'para', 'vip']

root = '/Users/yuanfang/Desktop/document/study_project/Numpy_Pandas/result/'
# root = '/home/lxq/Numpy_Pandas/result/'


cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(cur_path, 'logs')

handle_type = 't'  # t-timehandler 每日生成一个  f - filehandler固定大小生成日志文件，目前配置521M
formatter = True  # True日志中将带有时间信息， False将直接写入日志，无格式


class dbConfig(object):
	DIALECT = 'mysql'
	DRIVER = 'mysqldb'
	USERNAME = 'hswjMysqlTest'
	PASSWORD = 'eagle*Mysql;Test@20181211'
	HOST = '39.98.197.224'
	PORT = '3306'
	DATABASE2 = 'analyze'
	DB_URI2 = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE2)


conn = dbConfig()
engine = create_engine(conn.DB_URI2)

sql_allcount = "insert into t_count(" \
				 "app_id," \
				 "platform_id," \
				 "channel_type_id," \
				 "channel," \
				 "count_id," \
				 "count," \
				 "count_date) " \
				 "values (%s, %s, %s, %s, %s, %s, %s )"

# 推荐位
sql_recommcount = "insert into t_count(" \
				  "app_id," \
				  "platform_id," \
				  "channel_type_id," \
				  "channel," \
				  "para," \
				  "count_id," \
				  "count," \
				  "count_date) " \
				  "values (%s, %s, %s, %s, %s, %s, %s, %s )"

# 付费和未付费的影片
sql_vipcount = "insert into t_payment_media(" \
				  "count_id," \
				  "para," \
				  "vip," \
				  "count," \
				  "count_date) " \
				  "values (%s, %s, %s, %s, %s )"

#付费率
sql_payratecount = "insert into t_payment_rate(" \
				  "para," \
				  "rate," \
				  "count_date)" \
				  "values (%s, %s, %s)"

#展示累计注册
sql_lookconut = "SELECT sum(count) as count from t_count where count_id='40' and count_date <= %s"

sql_paymedia = '''
			SELECT a.cnt / b.cnt as rate, a.para as para, b.para as para1, a.cnt, b.cnt from 
			(SELECT para, vip, sum(count) cnt FROM t_payment_media where count_date <= '%s' and vip = 1 GROUP BY vip,para) a,
			(SELECT para, vip, sum(count) cnt FROM t_payment_media where count_date <= '%s' and vip = 0 GROUP BY vip,para) b
			WHERE a.para = b.para'''