---
title: Python编程 - 文件和异常
date: 2019-7-23
category:
    - Python
tags:
    - python

---

#### 十、文件和异常

##### 10.1 从文件中读取数据

- 读取整个文件

<!--more-->

首先要创建一个文本文件(`pi_digits.txt`)，用于存储圆周率`PI`小数点后30位

![PI](http://ww1.sinaimg.cn/large/9c62a0cfly1g58ebuy544j20zk044dg5.jpg)

读取：

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

![读取](http://ww1.sinaimg.cn/large/9c62a0cfly1g58eca0be8j20r80320t5.jpg)

- 读取流程

    - `open()`函数
        - 打开文件
        - 它接收一个参数：要打开文件的名称
        - 返回一个表示文件的对象

    - 关键字`with`
        - 不再需要访问文件后将其关闭，`Python`会在合适的时候自动将其关闭
        
    - `read()`方法
        - 读取文件的全部内容，并存储为字符串
        
注意：可以使用`rstrip()`删除字符串末尾空白字符

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```

- 文件路径

    - 相对文件路径
    在`Linux`和`OS X`中
    ```python
    with open('text_files/filename.text') as file_object:
    ```
    在`Windows`中，在文件路径中使用的是反斜杠(`\`)而不是斜杆(`/`)
    ```python
    with open('text_files\filename.text') as file_object:
    ```

    - 绝对文件路径
    在`Linux`和`OS X`中类似于
    ```python
    file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
    with open(file_path) as file_object:
    ```
    在`Windows`中，在文件路径中使用的是反斜杠(`\`)而不是斜杆(`/`)
    ```python
    file_path = 'C:\Users\ehmatthes\other_files\text_files\finename.txt'
    with open(file_path) as file_object:
    ```

- 逐行读取

```python
filename= 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
```

去掉多余空行：

```python
filename= 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

- 创建一个包含文件各行内容的列表

```python
filename= 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

方法`readlines()`从文件读取每一行，并将其存储在一个列表中。

- 使用文件内容

```python
filename= 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

注意：`strip()`删除字符串两端的空格；读取文本文件时，文件被解析成字符串，如果是数字并且需要作为数值使用，就必须使用函数`int()`将其转换为整数，或者使用`float()`将其转换为浮点数。

##### 10.2 写入文件

- 写入空文件

```python
filename = 'programming.txt'

with open(filename, 'w') as f_object:
    f_object.write("akashi")
```

`open()`传入的第二个实参：

    - `r`读取模式
        - 只读模式，默认为只读模式打开文件
    - `w`写入模式
        - 如果指定文件已存在，返回的文件会覆盖之前的文件内容
    - `a`附加模式
        - 不会在返回文件对象时覆盖原来文件内容
    - `r+`读取和写入文件
    
注意：`Python`只能将字符串写入文件，要将数值数据存储到文本文件中，必须先使用函数`str()`将其转换为字符串格式。

```python
filename = 'programming.txt'

with open(filename, 'w') as f_object:
    f_object.write("21")
```

`or`

```python
filename = 'programming.txt'

with open(filename, 'w') as f_object:
    f_object.write(str(21))
```

- 写入多行

```python
filename = 'programming.txt'

with open(filename, 'w') as f_object:
    f_object.write("akashi\n")
    f_object.write("asuka\n")
```

- 附加到文件

```python
filename = 'programming.txt'

with open(filename, 'a') as f_object:
    # f_object.write("akashi\n")
    # f_object.write("asuka\n")
    f_object.write("gakki\n")
```

你会发现之前存储的两个字符串依然存在，没有被覆盖。

##### 10.3 异常

- 处理`ZeroDivisionError`异常

![zero](http://ww1.sinaimg.cn/large/9c62a0cfly1g58n3xmi6hj20r80340t7.jpg)

- 使用`try-except`代码块

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- 使用异常避免奔溃

> 发生错误时，如果程序还有工作没有完成，妥善处理错误就尤其重要。

异常处理可以让程序接着运行，用户看到的是一条友好的错误消息，程序也不至于奔溃。

```python
print("Give me two numbers, and I'll divide them.")
print("\nEnter 'q' to quit.")

while True:
    first_number = input("\nFirst nmuber: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
```

 - 处理`FileNotFoundError`异常
 
 ```python
 filename = 'asuka.txt'
 
 try:
 with open(filename) as f_obj:
    contents = f_obj.read()
 except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
 ```
 
 - 分析文本

    - 使用`split()`方法分割字符串，默认以空格拆分，也可以传入参数进行拆分
    
```python
filename = 'programming.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
```

 - 决定报告哪些错误
 
 > 并非每次捕获错误都需要告诉用户。使用`pass`语句可以像没发生过一样让代码继续运行。
 
 ```python
 try:
    --snip--
except FileNotFoundError:
    pass
else:
    --snip--
```
 
 ##### 10.4 存储数据
 
 - 使用`json.dump()`和`json.load()`
 
 存储：
 
 ```python
 import json
 
 number = [2, 3, 5, 7, 9, 11, 13]
 
 filename = 'number.json'
 with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
```

函数`json.dump()`接收两个实参，要存储的数据以及可用于存储数据的文件对象。

读取：

```python
import json

filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```
 
 - 保存和读取用户生成的数据
 
 ```python
import json

# 如果之前存储了用户名，就加载它
# 否则，就提示输入并存储它

filename = 'username.json'

try:
with open(filename) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + " !")
else:
    print("Welcome back " + username.title() + " !")
```
 
 - 重构

> 将代码划分成一系列完成具体工作的函数，这样的过程被称为重构。重构让代码更清晰，更易于理解，更容易扩展。

```python
import json

def greet_user():
    """ 问候用户，并指明名字 """
    username = get_stored_username()
    if username:
        print("Welcome back " + username.title() + " !")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + " !")

def get_stored_username():
    """ 如果存取了用户名，就获取它 """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """ 未存储用户名，提示用户输入用户名，并存储 """
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

greet_user()
```
