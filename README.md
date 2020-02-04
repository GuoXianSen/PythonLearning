# PythonLearning

[TOC]



>Recording my learning process
>
>记录自己学习Python的过程

## 准备工作

俗话说”工欲善其事，必先利其器“，在学习Python之前，我们也需要安装好所需的工具，以下是常见三个操作系统Python的安装教程：

### macOS

[下载地址](https://www.python.org/downloads/)

### Windows

[下载地址](https://www.python.org/downloads/)

### Linux

[下载地址](https://www.python.org/downloads/)

点击到下载地址之后，选择你自己操作系统所对应的版本下载安装即可。

### 可以选用的编辑器

|     编辑器名称     |       支持平台        |
| :----------------: | :-------------------: |
|      Pycharm       | Windows，Linux，macOS |
|     Notepad++      | Windows，Linux，macOS |
|   Sublime Text3    | Windows，Linux，macOS |
|        IDLE        | Windows，Linux，macOS |
|        Vim         |     Linux，macOS      |
| Visual Studio Code | Windows，Linux，macOS |

笔者所使用的是`Pycharm专业版（2018.3.4 x64）`，大家可以自行选择适合自己的编译器

## 第一个程序

Python中不需要加上任何的标点符号，因此相比其他的编程语言，看起来也非常的简洁。它是一种解释型的编程语言，下面就是一个我们学习Python的第一个程序，也就是Python的输出语句。在进行数据的时候，我们使用到的语句是`print`。示例如下：

```python
print("I Love Python3")
```





## 注释

程序里面写上注释是非常重要的，注释可以告诉我们的这一段程序的作用是什么，方便我们日后对自己程序进行修改。同时，如果程序中我们有一段代码临时不想使用，我们可以用注释来禁用这段代码。

### 单行注释

在Python中我们可以使用`#`来进行注释。例如下面的程序：

```python
# This is my first attempt

print("I Love Python3")
```

### 多行注释

在Python中也有另外一种可以进行多行注释的方法，也就是使用两个`"""`来进行注释，示例如下

```python
"""
@author:Clay_Guo
@time:2020/2/3 19:53
@filename:01数字.py
"""
```





## 数据类型

Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

```python
counter = 100  # 整型
mile = 100.0  # 浮点型
name = "Clay_Guo"  # 字符串类型

print(counter)
print(mile)
print(name)
```

**多变量赋值**

python中可以进行多个变量的赋值，如下所示：

```python
# 多变量赋值
a = b = c = 100
print(a, b, c)

d, e, f = 100, 100.0, "Just do it"
print(d, e, f)
```



Python3中有**六个标准的数据类型**：

+ Number（数字）
+ String（字符串）
+ List（列表）
+ Tuple（元组）
+ Set（集合）
+ Dictionary（字典）

Python3中的六个标准数据类型中：

+ **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
+ **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

### 数字

#### 定义

Python3支持**int**、**float**、**bool**和**complex（复数）**

python3里面只有一种整型类型int，表示为长整型，没有python2中的Long

使用Python内置的`type()`函数可以查看变量的类型

```python
a = 100
b = 3.14
c = "Hello World"
d = True
e = 1+3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```

此外我们还可以使用`isinstance()`来判断

```python
e = 20
print(isinstance(e, int))
print(isinstance(e, float))
```

`type()`和`isinstance()`的区别：

+ `type()`不会认为子类是一种父类类型。
+ `isinstance()`会认为子类是一种父类类型。

**注意：** *在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。*例如：

```python
a = 1 + True
```

如果打印a的结果，将会输出2



**注意：**当你指定一个值时，Number 对象就会被创建，我们也可以使用`del`来将变量进行删除，如下所示

```python
a = 100
b = 3.14
c = True

del a,b,c
```

当你进行删除之后，变量就不存在了！



#### 数学运算

每一种编程语言都包含处理数字和进行数学计算的方法，Python也不例外。下面就是Python中的一些常用的数学运算符号：

| 运算符号 |    表示含义    |
| :------: | :------------: |
|    +     |      加号      |
|    -     |      减号      |
|    *     |      乘号      |
|    /     |      除号      |
|    //    | 取商的整数部分 |
|    %     |     求余数     |
|    >     |     大于号     |
|    ＜    |     小于号     |
|    ==    |     等于号     |
|   \>=    |   大于等于号   |
|    <=    |  小于与等于号  |

```python
# These are some samples
# 数学运算
print("求加法：", 33 + 15)
print("求减法：", 66 - 13)

print("求乘法：", 32 * 7)
print("求除法：", 40 / 5)
print("求商的整数部分：", 40//3)
print("求余数：", 30 % 4)
print("求阶乘：", 5**100)

```

**注意：**

- 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
- 2、一个变量可以通过赋值指向不同类型的对象。
- 3、数值的除法包含两个运算符：**/**返回一个浮点数，**//** 返回一个整数。
- 4、在混合计算时，Python会把整型转换成为浮点数。

Python还支持复数，复数由实数部分和虚数部分构成，可以用`a + bj`，或者`complex(a,b)`表示， 复数的实部a和虚部b都是浮点型

### 字符串

#### 定义

Python中的字符串，就是用`'`或者`"`括起来的内容，在我们开头的第一个程序中，用`print`所打印出来的就是字符串，同时我们也可以使用`\`来转义特殊字符

字符串的截取的语法如下：

**变量[头下标:尾下标]**

范围是左闭右开，索引值以0位开始位置，-1位最后一位

![](https://www.runoob.com/wp-content/uploads/2013/11/o99aU.png)

```python
name = "Clay_Guo"
print(name[0:4])
# 输出结果为Clay
# 注：name[0:4]为切片，也就是取出从name下标为0的字符到下标为3的字符（一共四个字符，左闭右开）
```

Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：

```python
print("This a \nhacker")
"""
上面字符的输出结果就是
This a 
hacker
"""
```

如果想要将`\`输出的话，我们就需要在字符串前面加上`r`：

```python
print(r"This a \nhacker")
```

这样就不会显示转义的效果

另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 **"""..."""** 或者 **'''...'''** 跨越多行。

**注意：**

+ 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
+ 和其C语言不同，Python的字符串是**不能改变**的，即不能通过索引来改变字符，这点千万注意！
+ 字符串可以用`+`运算符连接在一起，用`*`运算符重复。
+ Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。

### 列表  

#### 定义

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 **[]** 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：

> 变量[头下标:尾下标]

索引值从0开始，-1为末尾最后一个元素

![](https://www.runoob.com/wp-content/uploads/2013/11/list_slicing1.png)

加号 **+** 是列表连接运算符，星号 ***** 是重复操作。如下实例：

```python
list1 = ['abcd', 123, 3.14, False, complex(1, 2)]
list2 = ['cdef', 456, True]

print(list1)
print(list1[0])  # 输出列表第一个元素
print(list1[0:2])  # 输出列表从第一个元素到列表第二个元素
print(list1[2:])  # 输出列表从第三个元素到最后一个元素
print(list1 * 2)  # 列表复制输出
print(list1 + list2)  # 链接列表
```

注意：

与字符串不一样的是列表中的元素是可以进行修改的

```python
list3 = ['Clay_Guo','软件工程' , False , 123]
print(list3)
print(list3[2])
list3[2] = True
print(list3[2])
```

修改后，list3[2]的值变为了True

List（列表） 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。

**注意：**

- 1、List写在方括号之间，元素用逗号隔开。
- 2、和字符串一样，list可以被索引和切片。
- 3、List可以使用+操作符进行拼接。
- 4、List中的元素是可以改变的。

Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：

![](https://www.runoob.com/wp-content/uploads/2013/11/python_list_slice_2.png)

如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：

```python
list4 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]print(list4[-1::-1])  # 最后一位为-1表示逆序输出  
```

  逆序输出句子中的单词：

```python
# 将输入的句子中的单词逆序输出
words = input().split(" ")
print(words)
words = words[-1::-1]
print(words)
sentense = ' '.join(words)
print(sentense)
```

#### 访问列表中的值



#### 更新列表



#### 删除列表元素



#### 列表内置函数



#### 列表内置方法



### 元组

#### 定义

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 **()** 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：



可以把字符串看做是一种特殊的元组，元组中的元素也是不可以进行修改的，但是他可以包括可以修改的元素，比如List列表

#### 内置方法

### 集合

#### 定义

集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 **{ }** 或者 **set()** 函数创建集合，注意：创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典。

创建格式：

```python 
parame = {value01,value02,...}
或者
set(value)
```

### 字典

#### 定义

字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 **{ }** 标识，它是一个无序的 **键(key) : 值(value)** 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

**注意：**

- 1、字典是一种映射类型，它的元素是键值对。

- 2、字典的关键字必须为不可变类型，且不能重复。

- 3、创建空字典使用 **{ }**。

#### 访问字典里的值

我们可以通过将所要访问的值的键放到括号中，示例如下：

```python
dict1 = {'name': 'Clay_Guo', 'age': 20, 'city': '江苏常州'}

print(dict1['name'])
# 输出name所对应的值Clay_Guo
```

#### 修改字典

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

```python
dict1 = {'name': 'Clay_Guo', 'age': 20, 'city': '江苏常州'}
# 增加新的键值对
dict1['hobby'] = '打篮球'

# 修改字典内容
dict1['age'] = 21
```



#### 删除字典元素

能删单一的元素也能清空字典，清空只需一项操作。

显示删除一个字典用del命令，如下实例：

```python
dict1 = {'name': 'Clay_Guo', 'age': 20, 'city': '江苏常州'}
del dict1['name']  # 删除一个一个键值对
dict1.clear()  # 清空字典
```

#### 字典键的特性

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

```python
dict = {'Name': 'Alex', 'Age': 7, 'Name': 'Clay_Guo'}
 
print ("dict['Name']: ", dict['Name'])
# 输出Clay_Guo
```

2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

```python
dict = {['Name']: 'Clay_Guo', 'Age': 7}
 
print ("dict['Name']: ", dict['Name'])
```



#### 字典内置函数



#### 字典内置方法



## 字符串格式化



### %格式化字符串

%格式化字符串是python最早的，也是能兼容所有版本的一种字符串格式化方法，在一些python早期的库中，建议使用%格式化方式，他会把字符串中的格式化符按顺序后面参数替换，格式是

```python
print("My name is %s" % "alex")
```



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

format也是一种字符串格式化的方法





## 函数

### 参数

+ 形参
+ 实参

`*args`的用法：当传入的参数个数未知，且不需要知道参数名称时。



### 内置函数

`sum()`函数

`sum()`用于求和，其参数是一个列表  

```python
sum([1,2,3])
```

这样便会输出结果为：6

## 文件




## 模块
+ 什么是模块
+ 如何引用
## 类
+ 类的基本概念
+ 类的使用方法
## 爬虫
+ 使用正则表达式
+ 利用第三方库`BeautifulSoup`
+ 利用`Requests `

详情请看：[传送门](https://github.com/GuoXianSen/Python_Spyder)

如果您觉的我写的内容还不错，那么欢迎点一个**star**

## JSON

 

## 参考资料

+ 《“笨方法”学Python3》
+ [菜鸟教程](https://www.runoob.com/python3/)
+ 廖雪峰的官网
+ CSDN相关博客
+ Python官方文档