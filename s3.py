#构造一个1，3，5....，99的列表，可以通过循环实现
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
print('list(L)=',L)

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,3,5,7,9))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

#OOP 面向对象编程——Object Oriented Programming
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'



bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())





