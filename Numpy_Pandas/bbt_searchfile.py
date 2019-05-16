# -*- coding: UTF-8 -*-

import bbt_analyze
import re
import os
import pandas as pd
import config
from collections import Counter

class Analyze:
	def __init__(self, year, month, day, path, platform, app_id, channel_type, channel, mylog):
		self.mylog = mylog
		self.year = year
		self.month = month
		self.day = day
		self.path = path
		self.platform = platform
		self.app_id = app_id
		self.chanelType = channel_type
		self.channel = channel
		self.today = re.compile(
			r'%s/%s/%s/%s/%s/%s/%s' % (app_id, platform, channel_type, channel, year, month, day))
		if self.day.isdigit():
			self.twoday = re.compile(
				r'%s/%s/%s/%s/%s/%s/%s' % (app_id, platform, channel_type, channel, year, month, str(int(day) + 1)))
		self.registevent = 0
		self.register = 1
		self.allregist = 0
		self.registuser = []

		self.startevent = 0
		self.live = 0
		self.liveuser = []

		self.twostart = 0
		self.twostartuser = []
		self.rate = 0

		self.recomlist = []
		self.content = 0
		self.title = 0
		self.expert = 0

	# 昨日的文件
	def checkday_files(self, path):
		onefile = []
		twofile = []
		try:
			for maindir, subdir, all_file in os.walk(path):

				for filename in all_file:
					apath = os.path.join(maindir, filename)
					if self.today.search(apath) and apath.endswith('.log'):
						onefile.append(apath)

					if self.day.isdigit():
						if self.twoday.search(apath) and apath.endswith('.log'):
							twofile.append(apath)
					else:
						continue

		except Exception as e:
			self.mylog.debug('没有可统计的文件')

		if len(twofile) == 0:
			self.mylog.debug('没有确定的天数无法统计离存率')
		for f in onefile:
			event = os.path.split(f)  # 返回文件的路径和文件名
			# count_id = event[0].split('/')[-1]

			if event[0].endswith('/1'):
				bbt_analyze.registUser(self, f)
				bbt_analyze.registEvent(self, f)

			elif event[0].endswith('/2'):
				bbt_analyze.startUser(self, f)
				bbt_analyze.startEvent(self, f)

			elif event[0].endswith('/3'):
				bbt_analyze.recommendEvent(self, f)

			elif event[0].endswith('/5'):
				bbt_analyze.contentEvent(self, f)

			elif event[0].endswith('/18'):
				bbt_analyze.titleEvent(self, f)

			elif event[0].endswith('/20'):
				bbt_analyze.expertEvent(self, f)

		self.save_regist('1', self.registevent)
		self.save_daylive('2', self.startevent)
		self.save_content('5', self.content)
		self.save_titlevent('18', self.title)
		self.save_expertevet('20', self.expert)
		self.save_regist('30', self.register)
		self.save_daylive('31', self.live)
		if self.day.isdigit():
			for f in twofile:
				event = os.path.split(f)
				if event[0].endswith('/2'):
					bbt_analyze.retentRate(self, f)
		self.save_rate('32', self.twostartuser, self.registuser)

		recommend = Counter(self.recomlist)
		for para,court in recommend.items():
			self.save_recommend('3', court, para)

	def save_registevent(self, count_id, regisevent):
		bbt_analyze.save_date(self, count_id, regisevent)

	def save_startevent(self, count_id, start):
		bbt_analyze.save_date(self, count_id, start)

	def save_recommend(self, count_id, recomend, para):
		bbt_analyze.save2_date(self, count_id, recomend, para)

	def save_content(self, count_id, content):
		bbt_analyze.save_date(self, count_id, content)

	def save_titlevent(self, count_id, title):
		bbt_analyze.save_date(self, count_id, title)

	def save_expertevet(self, count_id, expert):
		bbt_analyze.save_date(self, count_id, expert)

	def save_regist(self, count_id, register):
		bbt_analyze.save_date(self, count_id, register)

	def save_daylive(self, count_id, live):
		bbt_analyze.save_date(self, count_id, live)

	def save_rate(self, count_id, twostartuser, registuser):
		olduser = list(set(twostartuser) & set(registuser))
		try:
			self.rate = len(olduser) / self.register * 100
			bbt_analyze.save_date(self, count_id, self.rate)
		except Exception as e:
			self.mylog.debug('被除数不能为0',e)

	# print('次日留存率为:%.2f%%' % (rate))

	def getExcel(self):
		thedate = self.year + self.month + self.day
		bbt_analyze.find_date(self, thedate)
		df = pd.DataFrame({'事件ID': [],
						   '事件名称': ['累计注册用户', '日活', '次日留存率', '注册事件', '启动事件',
									 '首页推荐位点击', '内容分类点击', '专题展示', '专家展示'],
						   'key':[],'消息数量':[self.allregist, self.live, self.rate, self.registevent, self.startevent,
									  self.recommend, self.content, self.title, self.expert],'独立用户数':[]})
		df.to_excel(config.root + thedate + '.xlsx')

	def run(self):
		self.checkday_files(self.path)
		# 生成excel文件
		# self.getExcel()
