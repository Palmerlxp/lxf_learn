#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('xiaolu',25,'lovebear',city='Beijing',job='tester')


def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi')
hello('Hi','Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')
names = ('Bart', 'Lisa')
hello('Hello', *names)

