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

待补充...

#### 更新列表

待补充...

#### 删除列表元素

待补充...

#### 列表内置函数

待补充...

#### 列表内置方法

待补充...

### 元组

#### 定义

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 **()** 里，元素之间用逗号隔开。

元组中的元素类型也可以不相同：



可以把字符串看做是一种特殊的元组，元组中的元素也是不可以进行修改的，但是他可以包括可以修改的元素，比如List列表

#### 内置函数

待补充...

#### 内置方法

待补充...

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

待补充...

#### 字典内置方法

待补充...

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

### 定义

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。前面的学习中我们也了解到很多Python的内置函数，比如print()。同时我们也可以自己创建函数，这被叫做用户自定义函数。

### 定义一个函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

```python
def fun():
    print("Hello World!")
```

注意：

在我们定义函数之后，如果不调用函数的话，是不会有任何的效果的。

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

### 文件方法

#### open()方法

Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

**注意：**

使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

```pythohn
open(file, mode='r')
```

完整的语法格式是：

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

参数说明:

- file: 必需，文件路径（相对或者绝对路径）。
- mode: 可选，文件打开模式
- buffering: 设置缓冲
- encoding: 一般使用utf8
- errors: 报错级别
- newline: 区分换行符
- closefd: 传入的file参数类型
- opener:

mode 参数有：

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| t    | 文本模式 (默认)。                                            |
| x    | 写模式，新建一个文件，如果该文件已存在则会报错。             |
| b    | 二进制模式。                                                 |
| +    | 打开一个文件进行更新(可读可写)。                             |
| U    | 通用换行模式（**Python 3 不支持**）。                        |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

默认为文本模式，如果要以二进制模式打开，加上 **b** 。









注意：如果我们使用open的方式进行文件的打开，那么就必须在结束的时候加上close()语句来关闭文件，不然会一直消耗计算机内存。

#### with方法

除了用open()的方法进行文件打开，我们还可以使用with的方法进行文件的打开，这个方法不需要对文件进行close()，具体用法如下：

```python
with open("readme.txt","r") as f:
	print(f.read())
```




## 模块
+ 什么是模块
+ 如何引用
### OS模块

**os** 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：

| 序号 | 方法及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [os.access(path, mode)](https://www.runoob.com/python3/python3-os-access.html) 检验权限模式 |
| 2    | [os.chdir(path)](https://www.runoob.com/python3/python3-os-chdir.html) 改变当前工作目录 |
| 3    | [os.chflags(path, flags)](https://www.runoob.com/python3/python3-os-chflags.html) 设置路径的标记为数字标记。 |
| 4    | [os.chmod(path, mode)](https://www.runoob.com/python3/python3-os-chmod.html) 更改权限 |
| 5    | [os.chown(path, uid, gid)](https://www.runoob.com/python3/python3-os-chown.html) 更改文件所有者 |
| 6    | [os.chroot(path)](https://www.runoob.com/python3/python3-os-chroot.html) 改变当前进程的根目录 |
| 7    | [os.close(fd)](https://www.runoob.com/python3/python3-os-close.html) 关闭文件描述符 fd |
| 8    | [os.closerange(fd_low, fd_high)](https://www.runoob.com/python3/python3-os-closerange.html) 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 |
| 9    | [os.dup(fd)](https://www.runoob.com/python3/python3-os-dup.html) 复制文件描述符 fd |
| 10   | [os.dup2(fd, fd2)](https://www.runoob.com/python3/python3-os-dup2.html) 将一个文件描述符 fd 复制到另一个 fd2 |
| 11   | [os.fchdir(fd)](https://www.runoob.com/python3/python3-os-fchdir.html) 通过文件描述符改变当前工作目录 |
| 12   | [os.fchmod(fd, mode)](https://www.runoob.com/python3/python3-os-fchmod.html) 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。 |
| 13   | [os.fchown(fd, uid, gid)](https://www.runoob.com/python3/python3-os-fchown.html) 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。 |
| 14   | [os.fdatasync(fd)](https://www.runoob.com/python3/python3-os-fdatasync.html) 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。 |
| 15   | [os.fdopen(fd[, mode[, bufsize\]])](https://www.runoob.com/python3/python3-os-fdopen.html) 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象 |
| 16   | [os.fpathconf(fd, name)](https://www.runoob.com/python3/python3-os-fpathconf.html) 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。 |
| 17   | [os.fstat(fd)](https://www.runoob.com/python3/python3-os-fstat.html) 返回文件描述符fd的状态，像stat()。 |
| 18   | [os.fstatvfs(fd)](https://www.runoob.com/python3/python3-os-fstatvfs.html) 返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。 |
| 19   | [os.fsync(fd)](https://www.runoob.com/python3/python3-os-fsync.html) 强制将文件描述符为fd的文件写入硬盘。 |
| 20   | [os.ftruncate(fd, length)](https://www.runoob.com/python3/python3-os-ftruncate.html) 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。 |
| 21   | [os.getcwd()](https://www.runoob.com/python3/python3-os-getcwd.html) 返回当前工作目录 |
| 22   | [os.getcwdu()](https://www.runoob.com/python3/python3-os-getcwdu.html) 返回一个当前工作目录的Unicode对象 |
| 23   | [os.isatty(fd)](https://www.runoob.com/python3/python3-os-isatty.html) 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。 |
| 24   | [os.lchflags(path, flags)](https://www.runoob.com/python3/python3-os-lchflags.html) 设置路径的标记为数字标记，类似 chflags()，但是没有软链接 |
| 25   | [os.lchmod(path, mode)](https://www.runoob.com/python3/python3-os-lchmod.html) 修改连接文件权限 |
| 26   | [os.lchown(path, uid, gid)](https://www.runoob.com/python3/python3-os-lchown.html) 更改文件所有者，类似 chown，但是不追踪链接。 |
| 27   | [os.link(src, dst)](https://www.runoob.com/python3/python3-os-link.html) 创建硬链接，名为参数 dst，指向参数 src |
| 28   | [os.listdir(path)](https://www.runoob.com/python3/python3-os-listdir.html) 返回path指定的文件夹包含的文件或文件夹的名字的列表。 |
| 29   | [os.lseek(fd, pos, how)](https://www.runoob.com/python3/python3-os-lseek.html) 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效 |
| 30   | [os.lstat(path)](https://www.runoob.com/python3/python3-os-lstat.html) 像stat(),但是没有软链接 |
| 31   | [os.major(device)](https://www.runoob.com/python3/python3-os-major.html) 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。 |
| 32   | [os.makedev(major, minor)](https://www.runoob.com/python3/python3-os-makedev.html) 以major和minor设备号组成一个原始设备号 |
| 33   | [os.makedirs(path[, mode\])](https://www.runoob.com/python3/python3-os-makedirs.html) 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。 |
| 34   | [os.minor(device)](https://www.runoob.com/python3/python3-os-minor.html) 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。 |
| 35   | [os.mkdir(path[, mode\])](https://www.runoob.com/python3/python3-os-mkdir.html) 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。 |
| 36   | [os.mkfifo(path[, mode\])](https://www.runoob.com/python3/python3-os-mkfifo.html) 创建命名管道，mode 为数字，默认为 0666 (八进制) |
| 37   | [os.mknod(filename[, mode=0600, device\])](https://www.runoob.com/python3/python3-os-mknod.html) 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。 |
| 38   | [os.open(file, flags[, mode\])](https://www.runoob.com/python3/python3-os-open.html) 打开一个文件，并且设置需要的打开选项，mode参数是可选的 |
| 39   | [os.openpty()](https://www.runoob.com/python3/python3-os-openpty.html) 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。 |
| 40   | [os.pathconf(path, name)](https://www.runoob.com/python3/python3-os-pathconf.html) 返回相关文件的系统配置信息。 |
| 41   | [os.pipe()](https://www.runoob.com/python3/python3-os-pipe.html) 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写 |
| 42   | [os.popen(command[, mode[, bufsize\]])](https://www.runoob.com/python3/python3-os-popen.html) 从一个 command 打开一个管道 |
| 43   | [os.read(fd, n)](https://www.runoob.com/python3/python3-os-read.html) 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。 |
| 44   | [os.readlink(path)](https://www.runoob.com/python3/python3-os-readlink.html) 返回软链接所指向的文件 |
| 45   | [os.remove(path)](https://www.runoob.com/python3/python3-os-remove.html) 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。 |
| 46   | [os.removedirs(path)](https://www.runoob.com/python3/python3-os-removedirs.html) 递归删除目录。 |
| 47   | [os.rename(src, dst)](https://www.runoob.com/python3/python3-os-rename.html) 重命名文件或目录，从 src 到 dst |
| 48   | [os.renames(old, new)](https://www.runoob.com/python3/python3-os-renames.html) 递归地对目录进行更名，也可以对文件进行更名。 |
| 49   | [os.rmdir(path)](https://www.runoob.com/python3/python3-os-rmdir.html) 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。 |
| 50   | [os.stat(path)](https://www.runoob.com/python3/python3-os-stat.html) 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。 |
| 51   | [os.stat_float_times([newvalue\])](https://www.runoob.com/python3/python3-os-stat_float_times.html) 决定stat_result是否以float对象显示时间戳 |
| 52   | [os.statvfs(path)](https://www.runoob.com/python3/python3-os-statvfs.html) 获取指定路径的文件系统统计信息 |
| 53   | [os.symlink(src, dst)](https://www.runoob.com/python3/python3-os-symlink.html) 创建一个软链接 |
| 54   | [os.tcgetpgrp(fd)](https://www.runoob.com/python3/python3-os-tcgetpgrp.html) 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组 |
| 55   | [os.tcsetpgrp(fd, pg)](https://www.runoob.com/python3/python3-os-tcsetpgrp.html) 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。 |
| 56   | os.tempnam([dir[, prefix]]) **Python3 中已删除。**返回唯一的路径名用于创建临时文件。 |
| 57   | os.tmpfile() **Python3 中已删除。**返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。 |
| 58   | os.tmpnam() **Python3 中已删除。**为创建一个临时文件返回一个唯一的路径 |
| 59   | [os.ttyname(fd)](https://www.runoob.com/python3/python3-os-ttyname.html) 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。 |
| 60   | [os.unlink(path)](https://www.runoob.com/python3/python3-os-unlink.html) 删除文件路径 |
| 61   | [os.utime(path, times)](https://www.runoob.com/python3/python3-os-utime.html) 返回指定的path文件的访问和修改的时间。 |
| 62   | [os.walk(top[, topdown=True[, onerror=None[, followlinks=False\]]])](https://www.runoob.com/python3/python3-os-walk.html) 输出在文件夹中的文件名通过在树中游走，向上或者向下。 |
| 63   | [os.write(fd, str)](https://www.runoob.com/python3/python3-os-write.html) 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度 |
| 64   | [os.path 模块](https://www.runoob.com/python3/python3-os-path.html) 获取文件的属性信息。 |

## 面向对象

### 类

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