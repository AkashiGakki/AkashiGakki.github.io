---
title: Python 上手指南之条件、循环
date: 2019-11-6
category: Python
tags: Python
thumbnail: /images/asuka/asu-4.jpg

---

### 条件、循环及其他语句

> 需要了解的列表推导式、字典推导式、`lambda` 匿名函数和关键字 `yield`。

<!-- more -->

#### `print` 和 `import`

- 打印多个参数

使用逗号分隔可以打印多个参数

```python
>>> print('age: ', 22)
age:  22
```

(类似于 `Java` 中的字符串连接符 `+`)

- 导入时重名

一般导入

```python
import somemodule
from somemodule import somefunction, antherfunction
from somemodule import *
```

当模块方法重名时，需要导入时指定别名，使用 `as`

```python
import math as foobar
res = foobar.sqrt(4)
```

或：

```python
from math import sqrt as foobar
res = foobar(4)
```

#### 赋值魔法

- 序列解包(可迭代对象解包)

```python
>>> x, y, z = 1, 2, 3
>>> print(x, y, z)
1 2 3
>>> values = 4, 5, 6
>>> values
(4, 5, 6)
```

利用这个特性，我们还可以实现快速的元素值交换：

```python
x, y = 1, 2
print(x, y)

x, y = y, x
print(x, y)
```

输出：

```python
1 2
2 1
```

#### `if`

```python
if something:
    do something
elif antherthing:
    do something
else:
    do something
```

#### `while`

```python
while condition:
    do something
```

#### `for`

```python
for some in somethings:
    pass
```

#### 迭代字典

```python
for key in item:
    print(key, item[key])
```

或

```python
for key value in item.items():
    print(key, value)
```

#### 迭代工具

- 索引获取

```python
name = ['akashi', 'asuka', 'gakki']
for i in range(len(name)):
    print(name[i])
```

- 并行迭代

`zip` 将两个序列“缝合”，返回一个适合迭代的对象

```python
name = ['akashi', 'asuka', 'gakki']
age = [22, 21, 30]

for name, age in zip(name, age):
    print(name, ':', age)
```

输出：

```python
akashi : 22
asuka : 21
gakki : 30
```

- 迭代同时获取索引和元素

函数 `enumerate`

```python
name = ['akashi', 'asuka', 'gakki']

for index, value in enumerate(name):
    print(index, value)
```

输出：

```python
0 akashi
1 asuka
2 gakki
```

#### 列表推导式

快速生成列表

```python
res = [x**2 for x in range(10)]
print(res)
```

输出：

```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### 字典推导式

快速生成字典

```python
name = ['akashi', 'asuka', 'gakki']
age = [22, 21, 30]

res = {name: age for name, age in zip(name, age)}
print(res)
```

输出：

```python
{'akashi': 22, 'asuka': 21, 'gakki': 30}
```

或

```python
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = {k:str(v) for k, v in enumerate(seq) if v % 2 == 0}
print(res)
```

输出：

```python
{1: '2', 3: '4', 5: '6', 7: '8'}
```

#### 匿名函数 `lambda`

定义一个只使用一次的函数

```python
func = lambda x, y: x + y
res = func(2, 3)
print(res)
```

输出： `5`

#### `yield`

可以将函数执行的中间结果返回但不结束程序

```python
def func(n):
    while n:
        yield n
        n -= 1

if __name__ == "__main__":
    for i in func(4):
        print(i)
```

输出：

```python
4
3
2
1
```

#### `map()`

遍历序列，对序列中的每一个元素进行操作，创建一个新的序列，结果返回新序列的对象，需传入一个函数操作：

```python
def func(x, y):
    return x + y

seq1 = [1, 2, 3]
seq2 = [4, 5, 6]

res = list(map(func, seq1, seq2))
print(res)
```

输出：

```python
[5, 7, 9]
```

或

```python
seq = [1, 2, 3]
res = list(map(lambda x: x**2, seq))
print(res)
```

输出：

```python
[1, 4, 9]
```

#### `filter()`

对序列中的元素进行筛选，返回符合条件的序列的对象，也需要传入函数操作：

```python
seq = [1, 2, 3]
res = list(filter(lambda x: x>1, seq))
print(res)
```

输出：

```python
[2, 3]
```

#### `reduce()`

累计函数，在 `python2` 中是内置函数，`python3` 中需要从 `functools` 模块中导入

返回一个操作最终的值，需要传入一个操作的函数

```python
from functools import reduce

seq = [1, 2, 3]
res = reduce(lambda x, y: x + y, seq)
print(res)
```

输出： `6`
