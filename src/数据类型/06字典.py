"""
@author:Clay_Guo
@time:2020/2/3 19:55
@filename:06字典.py
"""

dict1 = {'name': 'Clay_Guo', 'age': 20, 'city': '江苏常州', 'hometown': '江苏淮安'}
print(dict1)

dict2 = {'name': 'Clay_Guo', 'age': 20, 'city': '江苏常州'}
print(dict2['name'])

dict2['hobby'] = 'football'
print(dict2)
del dict2['hobby']  # 删除一个一个键值对
dict2.clear()  # 清空字典
print(dict2)

dict = {'Name': 'Alex', 'Age': 7, 'Name': 'Clay_Guo'}

print("dict['Name']: ", dict['Name'])  # 输出Clay_Guo



