"""
@author:Clay_Guo
@time:2020/2/3 19:54
@filename:03列表_1.py
"""

list1 = ['abcd', 123, 3.14, False, complex(1, 2)]
list2 = ['cdef', 456, True]

print(list1)
print(list1[0])  # 输出列表第一个元素
print(list1[0:2])  # 输出列表从第一个元素到列表第二个元素
print(list1[2:])  # 输出列表从第三个元素到最后一个元素
print(list1 * 2)  # 列表复制输出
print(list1 + list2)  # 链接列表

list3 = ['Clay_Guo', '软件工程', False, 123]
print(list3)
print(list3[2])
list3[2] = True
print(list3[2])

list4 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
print(list4[-1::-1])  # 最后一位为-1表示逆序输出
