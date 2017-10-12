def f(n):
    return n*n
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

L=[]
for n in[1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))


from functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))


#str to int的函数
from functools import reduce
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))
print('0')
print(str2int('5'))
print(str2int('0123'))


#简化下
from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(char2num('2'))
print(str2int('2345'))


#利用map()和reduce()编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
def str2float(s):
    import math
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    L=s.split('.')#split()通过指定分隔符对字符串进行切片
    return reduce(lambda x,y:x*10+y,map(char2num,L[0]+L[1]))/math.pow(10,len(L[1]))
print('str2float(\'123,456\')=',str2float('123.456'))
#math.pow 表示x的y次方