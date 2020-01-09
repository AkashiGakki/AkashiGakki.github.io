---
title: 二、数据类型
date: YYYY-MM-DD
category: Python
tag: 
    - python
    - 入门
    
---

#### 二、变量和简单数据类型

##### 2.1 变量

```python
message = "Hello Python World!"
print(message)
```

<!--more-->

这里我们添加了一个`message`的变量，变量存储了一个值为文本 `"Hello Python World!"`

```python
message = "Hello Python World!"

message = "Hello!"
print(message)
```

我们可以修改覆盖变量的值，`Python`将始终记录变量的最新值。这里的输出为`"Hello!"`

##### 2.2 变量的命名和使用

- 命名规则：
1. 变量只能包含`字母`、`数字`和`下划线`。变量名可以以字母或下划线开头，但不能以数字开头。
2. 变量名`不能包含空格`，可以使用下划线来分隔单词。
3. 不要将`Python``关键字`和`函数名`用作变量名。
4. 变量名应既`简短`又具有`描述性`。
5. 慎用小写字母`l`和大写字母`O`，因为容易和数字`1`和`0`混淆。

##### 2.3 字符串

> 字符串就是一系列字符，在`Python`中用引号括起来的都是字符串，其中引号可以使`单引号`也可以是`双引号`。

- 使用方法修改字符串的大小写

```python
name = "akashi"
print(name.title())
```

方法是`Python`可对数据执行的操作，在`name.title()`中通过点（`.`）来执行`title()`方法的操作。`title()`以首字母大写的方式显示每个单词。

1. 首字母大写
    - `title()`
2. 全部大写
    - `upper()`
3. 全部小写
    - `lower()`

```python
name = "akashi"

print(name.title())
print(name.upper())
print(name.lower())
```

输出：
```
Akashi
AKASHI
akashi
```

- 合并（拼接）字符串

`Python`中使用（`+`）来合并字符串。

```python
first_name = "akashi"
last_name = "sai"
full_name = first_name + last_name

message = "Hello, " + full_name.title() + "!"
print(message)
```

输出：
`Hello Akashisai!`

- 使用制表符或换行符添加空白

字符串`\n\t`让`Python`换到下一行，并在下一行添加一个制表符。

```python
print("Languages:\n\tPython\n\tC++\n\tJavaScript")
```

输出：
![制表符\换行符](http://ww1.sinaimg.cn/large/9c62a0cfly1g4568ijal0j20r804ywew.jpg)

- 删除空白

1. 剔除字符串末尾空白
    - `rstrip()`
2. 剔除字符串开头空白
    - `lstrip()`
3. 剔除字符串两端的空白
    - `strip()`

##### 2.4 数字

- 整数

加减乘除运算

![运算](http://ww1.sinaimg.cn/large/9c62a0cfly1g456vmfn3wj20r80acq3s.jpg)

乘方

![乘方](http://ww1.sinaimg.cn/large/9c62a0cfly1g456x2qgm7j20r8046dfr.jpg)

`Python`使用两个乘号表示乘方运算。

- 浮点数

`Python`将带小数点的数字都称作浮点数。在进行浮点运算时，`Python`通常会按照你期望的方式处理它。

![浮点运算](http://ww1.sinaimg.cn/large/9c62a0cfly1g457en1pqzj20r807aaa7.jpg)

但需要注意的是，结果包含的小数位数可能不确定。但其实所有的语言都存在这种问题。浮点数计算得到的是一个近似的值。

- 使用函数str()避免类型错误

```python
age = 21
message = "Happy " + age + "rd Birthday!"
print(message)
```
你可能认为，上面的代码会打印一条生日祝福语，但其实它会引发一个错误：

![类型错误](http://ww1.sinaimg.cn/large/9c62a0cfly1g457ntxjwjj20r80403z2.jpg)

这是一个类型错误，这意味着`Python`无法识别你使用的信息，为此，可调用函数`str()`将非字符串转换为字符串：

```python
age = 21
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

##### 2.5 注释

- 单行注释
    - 使用`#`进行单行注释
- 多行注释
    - 使用`"""`包含进行多行注释

```
# 这是一个单行注释

"""
这是
一个
多行注释
"""
```

##### 2.6 `Python`之禅

- `import this`
    - 避繁就简
    - 漂亮而优雅
    - 简单易懂
    - ……

![import this](http://ww1.sinaimg.cn/large/9c62a0cfly1g50kq81ddoj20qw0hw16s.jpg)
