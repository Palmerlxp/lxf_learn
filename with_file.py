f=open('/Users/labuser/Desktop/google-Python3-exercises/NOTICE.txt','r')
print("文件名为：",f.name)

# print(f.read())

for line in f.readlines():
    print(line.strip())
f.close()
f=open('/Users/labuser/Desktop/test.txt','r',encoding='gbk')
print(f.read())
f=open('/Users/labuser/Desktop/test.txt','w')
f.write('Hello,world!')
f.close()

with open('/Users/labuser/Desktop/test.txt','w')as f:
    f.write('Hello,world!')

# with open('/Users/labuser/Desktop/test.txt','r') as f:
#     with open('/Users/labuser/Desktop/test-2.txt','w+') as s:
#         for i in f.readlines():
#             s.write(i.replace('hello','hi'))

from datetime import datetime
with open('/Users/labuser/Desktop/test.txt','w') as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y-%m-%d'))
with open('/Users/labuser/Desktop/test.txt','r') as f:
    s=f.read()
    print('open for read...')
    print(s)
with open('/Users/labuser/Desktop/test.txt','rb') as f:
    s=f.read()
    print('open as binary for read...')
    print(s)