# -*- coding: UTF-8 -*-

import pandas as pd
import config
from config import engine


# 今日注册用户
def registUser(self, files):
	f1 = pd.DataFrame(pd.read_csv(files, sep='\t', header=None, names=config.name))
	# 简化时间至年月日
	f1['daytime'] = pd.to_datetime(f1['daytime']).dt.normalize()
	# register = f1.drop_duplicates('user_id', 'first')['event_id'].count()
	a = f1['user_id'].unique()
	for i in a:
		if i not in self.registuser:
			self.registuser.append(i)
			self.register += 1


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


# 启动事件(pv)
def startEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	start = f1.groupby('event_id')['user_id'].count().reset_index(name='count')['count'][0]
	self.startevent += start


# 启动事件(uv)
def startUvEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	user = f1.groupby('event_id')['user_id'].unique().reset_index(name='count')['count'][0]
	for i in user:
		if i not in self.startUvUser:
			self.startUvUser.append(i)
			self.startuv += 1


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


# 全部页面PV之和
def pageEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	page = f1['event_id'].count()
	self.page += page


# 累计访客数(启动app的独立访客数总)
def startNouser(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	# unique返回的是list可以迭代 count直接出的是一个数不可迭代
	device = f1.groupby('event_id')['device_id'].unique().reset_index(name='count')['count'][0]
	for i in device:
		if i not in self.startNoUser:
			self.startNoUser.append(i)
			self.startnouser += 1


# 累计付费用户数(33事件)
def payEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	f1['para'] = f1['para'].apply(lambda x: x.split(',')[0])
	user = f1.groupby('event_id')['user_id'].unique().reset_index(name='count')['count'][0]
	media = f1.groupby('user_id')['para'].unique().reset_index(name='count')['count']
	#付费成功的节目
	for one in media:
		for v in one:
			self.mediauser.append(v)
	#付费用户(去重)
	for i in user:
		if i not in self.payUser:
			self.payUser.append(i)
			self.payevent += 1



# 用户地区分布


# 节目付费率
def playEvent(self, file):
	f1 = pd.DataFrame(pd.read_csv(file, sep='\t', header=None, names=config.name))
	f1['para'] = f1['para'].apply(lambda x: x.split(',')[0])
	# 取非vip的数
	f2 = f1.groupby('vip').get_group(0)
	media = f2.groupby('user_id')['para'].unique().reset_index(name='count')['count'][0:]
	for one in media:
		for v in one:
			self.playUser.append(v)


# 保存数据
def save_alldate(self, count_id, count):
	scount = str(count)
	with engine.connect() as db:
		try:
			sql = config.sql_allcount % (
				self.app_id, self.platform, self.chanelType, self.channel, count_id, scount, self.thedate)
			db.execute(sql)
		except Exception as e:
			self.mylog.debug(e)
		db.close()


# 保存数据2
def save_recommdate(self, count_id, count, para):
	scount = str(count)
	with engine.connect() as db:
		try:
			sql = config.sql_recommcount % (
				self.app_id, self.platform, self.chanelType, self.channel, "'" + para + "'", count_id, scount,
				self.thedate)
			db.execute(sql)
		except Exception as e:
			self.mylog.debug(e)
		db.close()

#观看节目时间付费以及非付费
def save_vipdate(self, count_id, para, vip, count):
	scount = str(count)
	with engine.connect() as db:
		try:
			sql = config.sql_vipcount % (count_id, "'" + para + "'", vip, scount, self.thedate)
			db.execute(sql)
		except Exception as e:
			self.mylog.debug(e)
		db.close()

#观看节目的付费率
def save_mediarate(self, media, rate, db):
	try:
		sql = config.sql_payratecount % ("'" + media + "'", rate, self.thedate)
		db.execute(sql)
	except Exception as e:
		self.mylog.debug(e)


# 查询数据
def find_date(self, thedate):
	with engine.connect() as db:
		try:
			sql = config.sql_lookconut % (thedate)
			data = db.execute(sql).fetchall()
			for i, row in enumerate(data):
				a = row['count']

			self.allregist += int(a)

		except Exception as e:
			self.mylog.debug(e)
		db.close()

#节目付费情况查询
def find2_date(self, thedate):
	with engine.connect() as db:
		try:
			sql = config.sql_paymedia % (thedate,thedate)
			data = db.execute(sql).fetchall()
			for i, row in enumerate(data):
				para = row['para']
				rate = row['rate']
				self.rea.append(para)
				self.reb.append(rate)
		except Exception as e:
			self.mylog.debug(e)
		db.close()