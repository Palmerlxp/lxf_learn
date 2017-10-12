#practise 转译符
print('''n=123
f=456.789
s1=\'Hello,world\'
s2=\'Hello,\\'Adam\\'\'
s3=r\'Hello,"Bart"\'
s4=r\'\'\'Hello,
lisa!\'\'\'''')

print('n=123')
print('f=456.789')
print('s1=\'Hello,world\'')
print('s2=\'Hello,\\\'Adam\\\'\'')
print('s3=r\'Hello,"Bart"\'')
print('s3=r\'Hello,\"Bart\"\'')
print('s4=r\'\'\'Hello,\nLisa!\'\'\'')



#practise \\
n = 123
f = 456.789
s1 = "'Hello, world'"
s2="'Hello,\'Adam\''"
s3="r'Hello,\"Bart\"'"
s4 = "r'''Hello,\nLisa!'''"
print('n =',n,'\nf =',f,'\ns1 =',s1,'\ns2 =',s2,'\ns3 =',s3,'\ns4 =',s4)


#practi list
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', '-', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

print(L[0][0],"\n"+L[1][1],"\n"+L[2][2])

print(L[0][0],'\n'+L[1][1],'\n'+L[2][2])

#practise %%
s1=72
s2=85
p=(s2-s1)/s2*100
print('小明的成绩提升比率是：''%.1f%%'%(p))

#practise if-elif
height=1.75
weight=80.5
bim=weight/(height*height)
if bim<18.5:
    print('过轻')
elif 18.5<bim<25:
    print('正常')
elif 25<bim<28:
    print('过重')
elif 28<bim<32:
    print('肥胖')
else:
    print('严重肥胖')

#practice---dict/set
#tuple in dict
s0={'dict_item1':(1,2,3)}
s1={'dict_item':(1,[2,3])}
print(s0)
print(s1)
#set
# s=set((1,2,3))
# print(s)

#area_of_circle()
def area_of_circle(r):
    pi=3.14
    area=pi*r**2  #area=pi*r*r
    return area
r1=12.34
r2=9.08
r3=73.1
s1=area_of_circle(r1)
s2=area_of_circle(r2)
s3=area_of_circle(r3)
print('s1=',s1)
print('s2=',s2)
print('s3=',s3)

#practise hex()函数
n1=255
n2=1000
print(str(hex(n1)),'\n',str(hex(n2)))

print(hex(n1),hex(n2))

print("255的16进制数为:",hex(255))
print("1000的16进制数为:",hex(1000))

#practise函数-quadratic(a,b,c)
# import math
#
# a=int(input('请输入a:'))
# b=int(input('请输入b:'))
# c=int(input('请输入c:'))

# def quadratic(a,b,c):
#     if(b*b-4*a*c)<0 or a==0:
#         return 'No value'
#     else:
#         x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
#         x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
#         return x1,x2
#
# x1,x2=quadratic(a,b,c)
# print(quadratic(a,b,c))

#var_args练习
# def hello(greeting,*args):
#     if (len(args)==0):
#         print('%s!'%greeting)
#     else:
#         print('%s,%s!'%(greeting,','.join(args)))
#
# print(hello('Hi'))

#杨辉三角：
#把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangeles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
n=0
for i in triangeles():
    print(i)
    n+=1
    if n==10:
        break

print(L)

#map()函数，将不规范的英文名字变为首字母大写，其他小写的规范名字
L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name[0].upper()+name[1:].lower()
#str.upper()方法将字符串中的小写字母转为大写字母
#str.lower()方法转换字符串中所有大写字符为小写
print(list(map(normalize,L1)))

#编写一个pord()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3*5*6*9=',prod([3,5,6,9]))
print(prod([3,5,6,9]))

#利用map()和reduce()编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce
def str2float(s):
    import math
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    L=s.split('.')
    return reduce(lambda x,y:x*10+y,map(char2num,L[0]+L[1]))/math.pow(10,len(L[1]))
print('str2float(\'123,456\')=',str2float('123.456'))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# def is_palindrome(n):
#     return lambda num:str(num)==str(num)[::-1]
#
# output=filter(is_palindrome,range(1,1000))
# print(list(output))

def circuitNumber(n):
    s=str(n)
    return s == s[::-1]
output=filter(circuitNumber,range(1,1000))
print(list(output))



#操作文件和目录

import os
# 利用os模块编写一个能实现dir -l输出的程序
def dir_l():
    list = [x for x in os.listdir('.')]
    for x in list:
        print(x)

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def get_file_paths_by_key(path, key):
     for x in os.listdir(path):
         x_path = os.path.join(path, x)
         if os.path.isfile(x_path):
             if key in os.path.split(x_path)[1]:
                 print(os.path.relpath(x_path))
         elif os.path.isdir(x_path):
             get_file_paths_by_key(x_path, key)
             get_file_paths_by_key('.', 'hhh.Python3')
