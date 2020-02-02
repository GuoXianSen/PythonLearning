# PythonLearning
>Recording my learning process
>
>记录自己学习Python的过程

## 准备工作

### macOS

### Windows

### Linux

### 可以选用的编辑器

|     编辑器名称     |       支持平台        |
| :----------------: | :-------------------: |
|      Pycharm       | Windows，Linux，macOS |
|     Notepad++      | Windows，Linux，macOS |
|   Sublime Text3    | Windows，Linux，macOS |
|        IDLE        | Windows，Linux，macOS |
|        Vim         |     Linux，macOS      |
| Visual Studio Code | Windows，Linux，macOS |



## 第一个程序

Python中不需要加上任何的标点符号，它是一种解释型的编程语言，下面就是一个我们学习Python的第一个程序，也就是Python的输出语句。

```python
print("I Love Python3")
```





## 注释和#号

程序里面写上注释是非常重要的，注释可以告诉我们的这一段程序的作用是什么，方便我们日后对自己程序进行修改。同时，如果程序中我们有一段代码临时不想使用，我们可以用注释来禁用这段代码。在Python中我们可以使用`#`来进行注释。例如下面的程序：

```python
# This is my first attempt

print("I Love Python3")
```



## 数字和数学计算

每一种编程语言都包含处理数字和进行数学计算的方法，Python也不例外。下面就是Python中的一些常用的数学运算符号：

| 运算符号 |   表示含义   |
| :------: | :----------: |
|    +     |     加号     |
|    -     |     减号     |
|    *     |     乘号     |
|    /     |     除号     |
|    %     |    求余数    |
|    >     |    大于号    |
|    ＜    |    小于号    |
|    ==    |    等于号    |
|   \>=    |  大于等于号  |
|    <=    | 小于与等于号 |

```python
# These are some samples

print("The price is ",33+15)
print("The price is ",66-13)

print("The result is ",32*7)
print("The result is ",40/5)

print()
```



## 变量





## 字符串和文本



### %格式化字符串

%格式化字符串是python最早的，也是能兼容所有版本的一种字符串格式化方法，在一些python早期的库中，建议使用%格式化方式，他会把字符串中的格式化符按顺序后面参数替换，格式是



### f-string

f-string，亦称为格式化字符串常量，是Python3.6新引入的一种字符串格式化方法，该方法源于PEP 498 – Literal String Interpolation，主要目的是使格式化字符串的操作更加简便。f-string在形式上是以 f 或 F 修饰符引领的字符串（f'xxx' 或 F'xxx'），以大括号 {} 标明被替换的字段；f-string在本质上并不是字符串常量，而是一个在运行时运算求值的表达式：

#### demo1

```python
# 使用f-string进行字符串的格式化

name = "alex"
print(f'my name is {name}')
```

#### demo2

```python
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
```



### format格式化







## 数据类型

### 列表

### 元组

### 字典






## 模块
+ 什么是模块
+ 如何引用
## 类
+ 类的基本概念
+ 类的使用方法
## 爬虫
+ 使用正则表达式
+ 利用第三方库BeautifulSoup
+ 利用Requests 



## JSON

 

## 参考资料

+ “笨方法”学Python3
+ 菜鸟教程
+ 廖雪峰的官网
+ Python官方文档