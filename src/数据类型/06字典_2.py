"""
@author:Clay_Guo
@time:2020/2/4 19:11
@filename:06字典_2.py
"""

dict = {'name': 'Clay_Guo', 'age': 20, 'sex': 'male'}
print(dict)

print('name' in dict)

print(list(dict.values()))  # 输出包含字典中所有值的列表
print(len(dict))

dict1 = dict.copy()
print('dict1=', dict1)
