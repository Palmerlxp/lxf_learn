height=input('身高：')
weight=input('体重：')
h=float(height)
w=float(weight)
bmi=w/(h*h)  #bmi=w/h**2 另一种平方的写法
if bmi<18.5:
    print('过轻')
elif bmi>18.5 and bmi<25:
    print('正常')
elif bmi>25 and bmi<28:
    print('过重')
elif bmi>28 and bmi<32:
    print('肥胖')
else:
    print('严重肥胖')

#other way
height=1.75
weight=80.5
BMI=weight/height/height
if BMI<18.5:
    print('过轻')
elif BMI<25:
    print('正常')
elif BMI<28:
    print('过重')
elif BMI<32:
    print('肥胖')
else:
    print('严重肥胖')




