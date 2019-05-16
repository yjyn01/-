# -*- coding: UTF-8 -*-


import os

from sqlalchemy import create_engine

name = ['IP', 'app', 'daytime', 'platform', 'channel_type', 'channel', 'user_id',
		'device_id', 'system_version', 'brand', 'model', 'version', 'event_id', 'para']

root = '/Users/yuanfang/Desktop/document/study_project/Numpy_Pandas/result/'
# root = '/home/lxq/Numpy_Pandas/result/'


cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(cur_path, 'logs')

handle_type = 't'  # t-timehandler 每日生成一个  f - filehandler固定大小生成日志文件，目前配置521M
formatter = True   # True日志中将带有时间信息， False将直接写入日志，无格式

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

sql_save_count = "insert into t_count(" \
				 "app_id," \
				 "platform_id," \
				 "channel_type_id," \
				 "channel," \
				 "count_id," \
				 "count," \
				 "count_date) " \
				 "values (%s, %s, %s, %s, %s, %s, %s )"


sql2_save_count = "insert into t_count(" \
				 "app_id," \
				 "platform_id," \
				 "channel_type_id," \
				 "channel," \
				 "para," \
				 "count_id," \
				 "count," \
				 "count_date) " \
				 "values (%s, %s, %s, %s, %s, %s, %s, %s )"



sql_look_conut = "SELECT sum(count) as count from t_count where count_id='30' and count_date <= %s"
