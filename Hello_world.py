#1/usr/bin/env python3
# -*- coding:utf-8 -*-

# name=input('please enter your name:')
# print('hello,',name)
#
#
# t=input('please enter a time:')
# if t>='3':
#     print('eat')
# else:
#     print('not eat')
#
# char=input()
# # try input [1,2,3]
# print(isinstance(char,str))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

