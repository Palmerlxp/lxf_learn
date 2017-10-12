#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#判断一个对象是可迭代对象，方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('abc',Iterable))#str是否可迭代
print(isinstance([1,2,3],Iterable))#list是否可迭代
print(isinstance(123,Iterable))#整数是否可迭代

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print(i,value)
d=[(1,1),(2,4),(3,9)]
for x,y in d:
    print(x,y)



a=12 * '甲乙丙丁戊己庚辛壬癸'
b=10 * '子丑寅卯辰巳午未申酉戌亥'
print(a)
print(b)
for i in range(0,60):
    print (a[i]+b[i])