import pandas as pd
import numpy as np


#文件后缀名任意,并不#文件后缀名任意,并不是csv的文件一定要是csv结尾
#  #一定要加上sep='\t',否则报错;
'''
read_csv的参数  nrows 显示多少行  usecols 使用多少列
'''

df = pd.read_csv('/Users/yuanfang/Desktop/work/test_date.csv',nrows=20)
a = pd.DataFrame(df)
# print(a.head())
# print(df.shape)
# print(df)
# print(df.head(10))
#获取二维表的维度,他是属性,返回数据是元组 
# print(df.shape)

#返回所有列名
# for i in df.columns:
# 	print(i)

#返回最后10条数据
# print(df.tail(10))

#得到第一行数据
# print(df.loc[0])


# print(df.groupby('name')['rate'].count())
# print(df.info())
# print(df.isnull())
#查看某列的唯一值
# print(df['region'].unique())

# print(df.values)
# print(df.fillna(value=0))

# print(df.ix[10:20, 0:3])
# print(df[df.index_num > 8])

# print(df.T)  数据转换

# print(df.sort_values(by='index_num',))
# Series = pd.Series([0,1,2,3,4,5])
#列和列的替换
# print(Series.replace([0,1,2,3,4,5],[11111,222222,3333333,44444,55555,666666]))

#通过标签来选择
# print(a.loc[1,'region'])

#通过位置来选择
# print(a.iloc[[1,3],[1,4]])
# print(a.iloc[1:3])
# a.loc[:,['name','rate']] = 6
# a.iloc[4,:]
# print(a)

#对缺失值进行填充
# print(a.fillna(value='叮当猫'))

#只能填any or all
# print(a.dropna(how='all',axis=0))

# 将a中的第三行以后的数据全部添加到a中  #在添加一次 20+18    如果a[:]就是40
# 若不指定ignore_index参数，则会把添加的数据的index保留下来，若ignore_index=Ture则会对所有的行重新自动建立索引。
# print(a.append(a[2:],ignore_index=False))

#用pd.date_range函数生成连续指定天数的的日期

date = {
	'date':pd.date_range('20190423', periods=10),
	'gender':np.random.randint(0,2,size=10),
	'height':np.random.randint(150,180,size=10),
	'weight':np.random.randint(40,60,size=10)
}
b = pd.DataFrame(date)
# c = b.groupby('gender').size()
# d = b.groupby('gender').sum()
# e = b.groupby('gender')['height'].mean()

# 对a中的gender进行重新编码分类，将对应的0，1转化为male，female
b['gender1'] = b['gender'].astype('category')
b['gender1'].cat.categories = ['male', 'female']
print(b)