#f菲薄拉起数列 1，1，2，3，5，8，13，21，34，...
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))

for n in fib(6):
    print(n)

#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通的函数，而是一个generator：
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

#捕获stopIteration的错误，返回值包含在StopIteration的value中
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
    print(g)
