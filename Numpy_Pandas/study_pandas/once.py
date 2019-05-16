import pandas as pd

name = ['IP', 'app', 'daytime', 'platform', 'channel_type', 'channel', 'user_id',
		'device_id', 'system_version', 'brand', 'model', 'version', 'event_id', 'para']
# 如果不是csv(默认逗号分隔)的文件  就需要加sep指定分隔符，否则会分割出\t, 要设定header=None,否则默认使用第一行的数据当做列名
f1 = pd.DataFrame(pd.read_csv('/Users/yuanfang/Desktop/download/logs/1/2/3/2/2019/03/27/1/logs12405.log',
							  sep='\t', header=None, names=name))

f2 = pd.DataFrame(pd.read_csv('/Users/yuanfang/Desktop/download/logs/1/2/3/2/2019/03/27/3/logs12405.log',
							  sep='\t', header=None, names=name))


#注册
register = f1.groupby('event_id')['user_id'].count()

# print(register)

#启动
start = f2.groupby('event_id')['user_id'].count()
# print(start)

#推荐位id
# f3 = pd.Series(p).value_counts()
# f3 = f2['para'].groupby(f2['event_id']).value_counts()
# p = [i.split(',')[1] for i in f3['para']]

#修改某列的值 DataFrame类型用的是apply  Series用的是str.split()
f2['para'] = f2['para'].apply(lambda x:x.split(',')[1])
f3 = f1.groupby('event_id')['para'].value_counts()

print(f3)
# print(f2['para'].split(',')[1])

#内容分类点击
print('='*50)




