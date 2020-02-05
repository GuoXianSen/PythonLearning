"""
@author:Clay_Guo
@time:2020/2/4 14:30
@filename:03列表_2.py
"""

"""
将输入的句子中的单词逆序输出
words = input().split(" ")
print(words)
words = words[-1::-1]
print(words)
sentense = ' '.join(words)
print(sentense)
"""
list1 = [1, 2, 3, 4, 5]
print(max(list1))

list2 = [{'name': 'Clay_Guo'}]
print(list2)

list3 = [123, 456, 'alex']
list4 = []
list4.extend(list3)
list4.extend(list2)
print(list3)
print(list4)
list4.append(list1)
print(list4)

print("===========================================================")
# 列表内置方法append和extend的区别

list5 = [{'name': 'Clay_Guo', 'age': 20, 'sex': 'male'}]
list6 = [{'name': 'Ding_luyao', 'age': 20, 'sex': 'male'}]
list7 = [{'name': 'Ma_wei', 'age': 20, 'sex': 'male'}]
list8 = []
list8.append(list7)
list8.append(list6)
list8.append(list5)
print("list8 = ", list8)
print("list8[0] = ", list8[0])
list8.clear()
list8.extend(list5)
list8.extend(list6)
list8.extend(list7)
print("list8 = ", list8)
print("list8[0] = ", list8[0])
