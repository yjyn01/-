import bbt_analyze
import config
from collections import Counter
from config import engine


def save_data(self):
	save_event(self, '1', self.registevent)
	save_event(self, '2', self.startevent)
	save_event(self, '5', self.content)
	save_event(self, '18', self.title)
	save_event(self, '20', self.expert)
	save_event(self, '33', self.payevent)
	save_event(self, '40', self.registevent)
	save_event(self, '41', self.live)
	save_event(self, '43', self.startuv)
	save_event(self, '44', self.page)
	save_event(self, '45', self.startnouser)

	# 付费成功的影片
	payrate = Counter(self.mediauser)
	for media, court in payrate.items():
		save_platrate(self, '48', media, '1', court)
	# 未付费的影片
	playrate = Counter(self.playUser)
	for media, court in playrate.items():
		save_platrate(self, '48', media, '0', court)

	# 变成字典计数每个元素出现的次数
	recommend = Counter(self.recomlist)
	for para, court in recommend.items():
		save_recommend(self, '3', court, para)


def save_event(self, count_id, event):
	bbt_analyze.save_alldate(self, count_id, event)


def save_recommend(self, count_id, recomend, para):
	bbt_analyze.save_recommdate(self, count_id, recomend, para)

#留存率
def save_rate(self, count_id, twostartuser, registuser):
	olduser = list(set(twostartuser) & set(registuser))
	try:
		self.rate = len(olduser) / self.register * 100
		bbt_analyze.save_alldate(self, count_id, self.rate)
	except Exception as e:
		self.mylog.debug('被除数不能为0', e)


def save_platrate(self, court_id, media, vip, court):
	bbt_analyze.save_vipdate(self, court_id, media, vip, court)

# print('次日留存率为:%.2f%%' % (rate))

#保存付费率
def save_payrate(self):
	bbt_analyze.find2_date(self, self.thedate)
	with engine.connect() as db:
		for media,rate in dict(zip(self.rea,self.reb)).items():
			bbt_analyze.save_mediarate(self, media, rate, db)
	db.close()



#导出excel
def getExcel(self):
	bbt_analyze.find_date(self, self.thedate)


	# df = pd.DataFrame({'事件ID': [],
	# 				   '事件名称': ['累计注册用户', '日活', '次日留存率', '注册事件', '启动事件',
	# 							'首页推荐位点击', '内容分类点 击', '专题展示', '专家展示'],
	# 				   'key': [], '消息数量': [self.allregist, self.live, self.rate, self.registevent, self.startevent,
	# 									   self.recommend, self.content, self.title, self.expert], '独立用户数': []})
	# df.to_excel(config.root + thedate + '.xlsx')
