# 利用os模块编写一个能实现dir -l输出的程序--bear方法

import os,sys

def main():
    if len(sys.argv)!=3:
        print('usage: ./test.Python3 [dir] [-command]')
        sys.exit(1)
    option=sys.argv[1]
    command=sys.argv[2]
    if option=='dir' and command=='--':
        for x in os.listdir('.'):
            print(x)
if __name__=='__main__':
    main()


# import os
#
# # Practice_01: 利用os模块编写一个能实现dir -l输出的程序。
#
# def dir_l():
#     f = sorted([x for x in os.listdir('.') if os.path.isdir(x)])
#     for x in f:
#         print(x)
#
# if __name__ == '__main__':
#     dir_l()
