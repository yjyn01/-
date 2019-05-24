# -*- coding: UTF-8 -*-

import bbt_analyze
import re
import os
import bbt_save

file = bbt_save


class Analyze:
	def __init__(self, year, month, day, path, platform, app_id, channel_type, channel, mylog):
		self.mylog = mylog
		self.year = year
		self.month = month
		self.day = day
		self.path = path
		self.thedate = self.year + self.month + self.day
		self.platform = platform
		self.app_id = app_id
		self.chanelType = channel_type
		self.channel = channel
		self.today = re.compile(
			r'%s/%s/%s/%s/%s/%s/%s' % (app_id, platform, channel_type, channel, year, month, day))
		if self.day.isdigit():
			self.twoday = re.compile(
				r'%s/%s/%s/%s/%s/%s/%s' % (app_id, platform, channel_type, channel, year, month, str(int(day) + 1)))
		#注册事件
		self.registevent = 0
		#注册用户
		self.register = 1
		#累计注册用户量
		self.allregist = 0
		self.registuser = []
		#启动事件
		self.startevent = 0
		#启动app的独立用户(uv)
		self.startuv = 0
		self.startUvUser = []
		#启动app访客数
		self.startnouser = 0
		self.startNoUser = []
		#累计访客数
		self.allnouser = 0
		#日活(启动去重)
		self.live = 0
		self.liveuser = []
		#次日继续使用的
		self.twostart = 0
		self.twostartuser = []
		self.rate = 0
		self.recomlist = []
		#内容分类点击
		self.content = 0
		#专题展示(pv)
		self.title = 0
		#专家展示(pv)
		self.expert = 0
		## 全部页面PV之和
		self.page = 0
		self.payUser = []
		self.mediauser = []
		#付费用户
		self.payevent = 0
		self.rea = []
		self.reb = []
		#累计付费用户
		self.allpay = 0
		#播放节目数
		# self.playnum = 0
		self.playUser = []

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
				bbt_analyze.startUvEvent(self, f)
				bbt_analyze.startNouser(self, f)


			elif event[0].endswith('/3'):
				bbt_analyze.recommendEvent(self, f)

			elif event[0].endswith('/5'):
				bbt_analyze.contentEvent(self, f)

			elif event[0].endswith('/18'):
				bbt_analyze.titleEvent(self, f)

			elif event[0].endswith('/20'):
				bbt_analyze.expertEvent(self, f)

			elif event[0].endswith('/24'):
				bbt_analyze.playEvent(self, f)

			elif event[0].endswith('/32'):
				bbt_analyze.pageEvent(self, f)

			elif event[0].endswith('/33'):
				bbt_analyze.payEvent(self, f)

		# 判断日期是否有日的参数，如果有统计
		if self.day.isdigit():
			for f in twofile:
				event = os.path.split(f)
				if event[0].endswith('/2'):
					bbt_analyze.retentRate(self, f)
		file.save_rate(self, '42', self.twostartuser, self.registuser)

	def run(self):
		self.checkday_files(self.path)
		file.save_data(self)
		file.save_payrate(self)
		file.getExcel(self)
