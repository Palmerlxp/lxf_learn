#1/usr/bin/env python3
# -*- coding:utf-8 -*-

print ('hello,world')


print('''line
line1
line3''')

print(r'''line1
line2
line3''')

import math

a=int(input('请输入a:'))
b=int(input('请输入b:'))
c=int(input('请输入c:'))
def quadratic(a,b,c):
    if(b*b-4*a*c)<0 or a==0:
        return 'No value'
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1,x2

x1,x2=quadratic(a,b,c)
print(quadratic(a,b,c))