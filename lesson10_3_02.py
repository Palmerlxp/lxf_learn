
import os# 引入包

file_list=[]# 声明一个空列表，用以添加文件

def list_files(dir):# 获取当前目录下的所有文件，包含子文件夹
    for x in os.listdir(dir):# 遍历当前目录
        path=os.path.join(dir,x)# 将当前目录下的所有文件和文件夹加上完整路径
        if os.path.isdir(path):# 如果当前遍历路径为文件夹
            list_files(path)# 递归
        else:# 如果当前遍历路径不为目录（不是文件夹就是文件呗，还能是啥）
            file_list.append(path)# 将该文件添加至列表

def filter_files(reg_str):# 筛选文件，使用传入的字符规则进行筛选
    for x in file_list:
        if reg_str in os.path.split(x)[1]:# os.path.split(x)[1]代表仅获取文件名（包含扩展名），如果文件名包含指定字符
            print(x)

def get_current_dir():# 获取当前文件的绝对路径
    return os.path.abspath('.')

def main():
    current_path=get_current_dir()
    list_files(current_path)
    filter_files('les')

# 执行入口
if __name__=='__main__':
    main()


# Practice_02:
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

def search_file(key_words, path = '.'):
    work_path = path
    for l in os.listdir(path):  # 遍历当前目录下所有文件和目录名
        if os.path.isdir(l):
            search_file(key_words, path = os.path.join(work_path, l))
        else:
            if l.find(key_words) != -1:
                print(os.path.join(work_path, l))

if __name__ == '__main__':
    search_file('.py')

