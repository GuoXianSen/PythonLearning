"""
@author:Clay_Guo
@time:2020/2/3 19:53
@filename:01数字.py
"""

# 数字类型
a = 100
b = 3.14
c = True
d = 1 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))

e = 20
print(isinstance(e, int))
print(isinstance(e, float))

print(True + 1)

# 数学运算
print("求加法：", 33 + 15)
print("求减法：", 66 - 13)

print("求乘法：", 32 * 7)
print("求除法：", 40 / 5)
print("求商的整数部分：", 40 // 3)
print("求余数：", 30 % 4)
print("求阶乘：", 5 ** 100)

# 删除不再使用的变量
a = 100
b = 3.14
c = True

del a, b, c

a = complex(1, 2)
print(a)
