"""
@author:Clay_Guo
@time:2020/2/5 14:42
@filename:01读文件.py
"""
# 读取文件的两种方式

# f = open('readme.txt','r')
# print(type(f))
# print(f.read())
#
# f.close()


with open("readme.txt", "r") as f:
    print(f.read())
