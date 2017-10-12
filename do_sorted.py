students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
from operator import itemgetter

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(n):
    return n[0] #按名字排序：

def by_score(n):
    return n[1] #按成绩从高到低排序

L2=sorted(L,key=by_name)
print(L2)
L3=sorted(L,key=by_score,reverse=True)
print(L3)
