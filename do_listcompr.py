#1/usr/bin/env python3
# -*- coding:utf-8 -*-

#生成[1*1，2*2，3*3,...10*10]
print(list(range(1,11)))

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

#简化版
l=[x*x for x in range(1,11)]
print(l)

#for循环后面还可加if判断
l0=[x*x for x in range(1,11) if x%2==0]
print(l0)

#两层循环，可以生成全排列
l1=[m+n for m in 'ABC' for n in 'XYZ']
print(l1)

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名
import os
l2=[d for d in os.listdir('.')]#os.listdir可以列出文件和目录
print(l2)
