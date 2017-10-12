
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# dog=Dog()
# print(dog.run())
#
# cat=Cat()
# print(cat.run())

print(Dog())
print(Cat())


class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')



def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print(c.run())
print(a.run())

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
run_twice(Animal())

print(type(a))
print(isinstance(c,Cat))
print(isinstance(c,Animal))

print(isinstance(d,Dog) and isinstance(d,Animal))


import types

print('type(\'abc\')==str?', type('abc')==str)