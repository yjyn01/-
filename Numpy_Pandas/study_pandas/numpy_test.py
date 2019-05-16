# from numpy import *

'''
# 生成对角矩阵
print(eye(4))

# a = np.array([1,2,3])
a = np.array([[1,2],[3,4]])

#ndmin生成最小维度 一个[ ] 就是一个维度
b = np.array([1,  2,  3,4,5], ndmin=2)
# dtype可以设置数组的数据类型 如bool 、int 、 float 、complex
c = np.array([1,2,3,4], dtype = bool)

# dt = np.dtype('i8')
dt = np.dtype([('age', np.int32)])
d = np.array([(10,),(20,),(30)], dtype=dt)
print(d)
# 类型字段名可以用于存取实际的 age 列
print(d['age'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
s = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(s)

z = np.arange(24)
q = z.reshape(2,3,4)
print(q.ndim)

x = np.empty([2,3], dtype = int, order='C')
print(x)


x = np.zeros((4,), dtype=[('x','i8'),('y','i8')])
print(x)

s = b'hello word'
a = np.frombuffer(s,dtype='S1')
print(a)
list = range(8)
it = iter(list)

a = np.fromiter(it, dtype=float)
a = np.linspace(1,10,10,dtype=int).reshape([1,10])
print(a)

a = np.arange(10)[slice(2,7,2)]
a = np.arange(10)[2:7:2]

print(a)

x = np.arange(32).reshape((8, 4))
print (x)
print('==================')
print(x[[1, 5, 7, 2]])

#tail()函数 像x轴复制1 ,y轴复制3
a = np.arange(6).reshape(2, 3)   #原始数组[[0 1 2]										
										# [3 4 5]]
for x in np.nditer(a.T):
	print(x, end=", ")
print('\n')

for x in np.nditer(a.T, order='C'):   #遍历顺序行序优先   0,1,2,3,4,5
for x in np.nditer(a.T, order='F'):  # 遍历顺序列序优先	0,3,1,4,2,5
	print(x, end=", ")
print('\n')

a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=2*x
print ('修改后的数组是：')
print (a)

a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('修改后的数组是：')
for x in np.nditer(a, flags =  ['external_loop'], order =  'C'):
   print (x, end=", " )
   
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

b = np.broadcast(x,y)
r,v = b.iters
print(next(r),next(v))
print(next(r),next(v))
'''

