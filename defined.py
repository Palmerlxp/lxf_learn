#1/usr/bin/env python3
# -*- coding:utf-8 -*-
#x=input('please enter a number:')

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

#def 函数的调用//默认参数必须指向不变的对象：age,city就是默认的参数
def enroll(name,gender,age=8,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('xiaolu','F')
enroll('bob','M',7)
enroll('adam','M',city='tianjing')

#默认参数必须指向不变的对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L
print(add_end())


#可变参数：在参数前面加一个*  //a^2+b^2+c^2+...
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

print(calc(1,2,3))
print(calc(1,3,5,7))

#如果要限制关键字参数的名字，命名关键字参数需要一个特殊的分隔符*，*后面的参数被视为命名关键字参数
#命名关键字参数必须传入参数名
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('xiaolu',25,'lovebear',city='Beijing',job='tester')

#命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city='Beijing',job):
    print(name,age,city,job)
person('xiaolu',25,job='tester')


#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

f1(1,2)

f1(1,2,c=3)

f1(1,2,3,'a','b')

f1(1,2,3,'a','b',x=99)

f1(1,2,3,'a','b',x='bear')

f2(1,2,d=88,ext=None)

args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
f1(*args,**kw)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

#进行修改-commit


