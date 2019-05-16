# -*- coding: UTF-8 -*-

import pandas as pd
import config
import numpy as np
from config import engine


# #昨日注册
# def upregistUser(self, upfile):
# 	f1 = pd.DataFrame(pd.read_csv(upfile, sep='\t', header=None, names=config.name))
# 	f1['daytime'] = pd.to_datetime(f1['daytime']).dt.normalize()
# 	upregister = f1.drop_duplicates('user_id', 'first')['event_id'].count()
# 	self.upregister += upregister
# 	# b = f1[(f1['daytime'] == self.date)].user_id.unique()
# 	b = f1['user_id'].unique()
# 	for i in b:
# 		self.upregistuser.append(i)

# 今日注册用户
def registUser(self, files):
	f1 = pd.DataFrame(pd.read_csv(files, sep='\t', header=None, names=config.name))
	f1['daytime'] = pd.to_datetime(f1['daytime']).dt.normalize()

	# register = f1.drop_duplicates('user_id', 'first')['event_id'].count()
	a = f1['user_id'].unique()
	for i in a:
		self.registuser.append(i)
		self.register += 1


# print('当日注册用户量:%s' % self.register)

# 日活
def startUser(self, files):
	f1 = pd.DataFrame(pd.read_csv(files, sep='\t', header=None, names=config.name))
	# start = f1.drop_duplicates('user_id', 'first')['event_id'].count()
	user = f1['user_id'].unique()
	for i in user:
		if i not in self.liveuser:
			self.liveuser.append(i)
			self.live += 1


# 留存率
def retentRate(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	# start = f1.drop_duplicates('user_id', 'first')['event_id'].count()
	user = f1['user_id'].unique()
	for i in user:
		if i not in self.twostartuser:
			self.twostartuser.append(i)
			self.twostart += 1


# 注册事件
def registEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	register = f1.groupby('event_id')['user_id'].count().reset_index(name='count')['count'][0]
	self.registevent += register


# 启动事件
def startEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	start = f1.groupby('event_id')['user_id'].count().reset_index(name='count')['count'][0]
	self.startevent += start


# 首页推荐位点击事件
def recommendEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	# f1['para'] = f1['para'].apply(lambda x: x.split(',')[1])
	f2 = f1['para']
	for i in f2:
		self.recomlist.append(i)
	# f3 = f1.groupby('event_id')['para'].value_counts()




# 内容分类点击事件
def contentEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	content = f1.groupby('event_id')['user_id'].count().reset_index(name='count')['count'][0]
	self.content += content


# 专题展示pv(不去重）
def titleEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	title = f1.groupby('event_id')['user_id'].count().reset_index(name='count')['count'][0]
	self.title += title


# 专家展示pv
def expertEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	expert = f1.groupby('event_id')['user_id'].count().reset_index(name='count')['count'][0]
	self.expert += expert


# 保存数据
def save_date(self, count_id, count):
	count_date = self.year + self.month + self.day
	scount = str(count)
	with engine.connect() as db:
		try:
			sql = config.sql_save_count % (
					self.app_id, self.platform, self.chanelType, self.channel, count_id, scount, count_date)
			db.execute(sql)
		except Exception as e:
			self.mylog.debug(e)
		db.close()

#保存数据2
def save2_date(self, count_id, count, para):
	count_date = self.year + self.month + self.day
	scount = str(count)
	with engine.connect() as db:
		try:
			sql = config.sql2_save_count % (
				self.app_id, self.platform, self.chanelType, self.channel, "'"+para+"'", count_id, scount, count_date)
			db.execute(sql)
		except Exception as e:
			self.mylog.debug(e)
		db.close()


# 查询数据
def find_date(self, thedate):
	with engine.connect() as db:
		try:
			sql = config.sql_look_conut % (thedate)
			data = db.execute(sql)
			value = data.fetchall()
			for i, row in enumerate(value):
				a = row['count']

			self.allregist += int(a)

		except Exception as e:
			self.mylog.debug(e)
		db.close()