import numpy as np
import pandas as pd

'''
s = pd.Series([1, 3, 5,np.nan , 6, 8])
print(s)

dates = pd.date_range('20190419', periods=6)
df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list('ABCDE'))

print(df)

a = pd.Timestamp('20190419')
b = pd.Series(1,index=list(range(5)), dtype=float)
c = np.array([3]*4, dtype=int)
e = pd.Categorical(["test", "train", "test", "train"])
print(e)


df2 = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(5)), dtype='float32'),
                   'D': np.array([3] * 5, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train","aaaa"]),
                   'F': 'foo'})

print(df2.dtypes)
print(df2.head())

dates = pd.date_range('20190419', periods=6)
df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list('ABCDE'))
print(df)
print('\n','==============')
print(df.apply(np.cumsum))

'''
series = pd.Series([1,2,3,4],['London', 'Hongkong', 'Americe', 'Loma'])
series2 = pd.Series([1,3,5,6],['London','Accra','Americe','de'])
print(series - series2)


