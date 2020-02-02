"""
@author:Clay_Guo
@time:2020/2/2 12:32
@filename:demo2.py
"""
# f-string使用练习

A = "Try your best"
B = "Give up"
C = "Just do it"
print("There are some choice for you:")
print(f"A:{A}")
print(f"B:{B}")
print(f"C:{C}")
print("please choose your choice:", end=" ")
choice = input()
if choice == "A":
    print(f"{A}")
elif choice == "B":
    print(f"{B}")
elif choice == "C":
    print(f"{C}")
else:
    print("Please choose from {A,B,C}")