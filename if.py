#1/usr/bin/env python3
# -*- coding:utf-8 -*-

# print absolute value of an integer:
a=100
if a>=0:
    print(a)
else:
    print(-a)

#practise if语句

age=20
if age>=18:
    print('your age is',age)
    print('adult')


age=3
if age>=18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

#elif做更细致的判断
age=3
if age>=18:
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')

if 2:
    print('True')

#if 和 input
s=input('birth:')
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')



