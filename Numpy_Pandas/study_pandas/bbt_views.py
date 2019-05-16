import pandas as pd
import numpy as np
import datetime

name = ['IP', 'app', 'daytime', 'platform', 'channel_type', 'channel', 'user_id',
		'device_id', 'system_version', 'brand', 'model', 'version', 'event_id', 'para']
# 如果不是csv(默认逗号分隔)的文件  就需要加sep指定分隔符，否则会分割出\t, 要设定header=None,否则默认使用第一行的数据当做列名
f1 = pd.DataFrame(pd.read_csv('/Users/yuanfang/Desktop/download/logs/1/2/3/2/2019/3/26/2/logs12405.log',
							  sep='\t', header=None, names=name))

f2 = pd.DataFrame(pd.read_csv('/Users/yuanfang/Desktop/download/logs/1/2/3/2/2019/3/27/2/logs12405.log',
							  sep='\t', header=None, names=name))
# 然后把默认的列名重命名


# 分批读取大数据  DataFrame没有这个方法
# 可以通过设置chunksize大小分批读入，也可以设置iterator=True后通过get_chunk选取任意行。
# chunk = df.get_chunk(2)
# 打印显示所有列
# pd.set_option('display.max_columns', None)


# print(a.shape)
# 分组以某列的数据为标准 去统计相对应的数量


# question1 :1、累计注册用户量：截止到某一时间点，累计注册用户数量(注册事件event_id=1)
f2['daytime'] = pd.to_datetime(f2['daytime']).dt.normalize()   #去掉时、分、秒 保留日期
register = f2[(f2['daytime'] == '2019-03-27')].event_id.count()

print('当日注册用户量:%s' %register)

# question2 :2、日活：过去一天启动过应用的用户数（去重），启动过一次的用户即视为活跃用户，包括新用户与老用户
# 将df2中的行添加到df1的尾部 ignore_index 会接上面的数据行号
# a = df.append(df2, ignore_index=True) '或者' a = pd.concat([df, df2], ignore_index=True)

# start = a.groupby(['datetime'])['event_id'].count()
# print(a)
# 这个drop_duplicate方法是对DataFrame格式的数据，去除特定列下面的重复行。返回DataFrame格式的数据。
start = f1.drop_duplicates('user_id', 'first')['event_id'].count()
print('当日启动用户量:%s' %start)


# question3 :3、次日留存：当日新增用户中次日继续使用应用的用户数/当日新增用户数*100%

# a = pd.isnull(res)
# b = res[a==False].reset_index(drop=True)

# 取出用户在五月之前的记录
# d_new = res[(res['datetime'] < '2019-05-01')].sort_values(by='datetime')
# d_all = pd.merge(d_new,res,how='left',on='event_id')
df = pd.concat([f1, f2], ignore_index=True)  # 把数据连接起来
df['daytime'] = pd.to_datetime(df['daytime']).dt.normalize()   #去掉时、分、秒 保留日期
new_user = []

def retention_rate(df):
	date = df[(df['daytime'] == '2019-03-27')].user_id.unique()  #取出当日注册的用户  加unique变成numpy.ndarray
	date2 = df[(df['daytime'] == '2019-03-28')].user_id.unique()
	for i in date:
		new_user.append(i)
	a = 0
	for user_id in date2:
		if user_id in new_user:
			a+=1
	rate = a/len(new_user)*100
	print('次日留存率为:%.2f%%'%(rate))

df = retention_rate(df)



