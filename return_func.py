def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


def countL():
    return map(lambda j : lambda : j * j , range(1, 4))#return list(map(lambda j: lambda: jj, range(1, 4)))

# lambda: j*j表示，g函数，无参数，返回j*j；lambda j: lambda: j*j表示f函数，有参数j，返回函数g。
# 使用高阶函数map，遍历range(1,4)，并想f函数传递每个值，最后返回Iterator，并转换为list。

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
