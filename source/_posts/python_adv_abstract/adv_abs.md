---
title: Python 上手指南之抽象
date: 2019-11-7
category: Python
tags: Python
thumbnail: /images/asuka/asu-5.jpg

---

### 抽象

> 抽象可以节省人力，更重要的是，抽象是程序能够被人理解的关键所在。

<!-- more -->

#### 自定义函数

现在，如果我们需要计算一个裴波那契序列，我们编写如下面的代码：

```python
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)
```

这样，我们得到了一个数列

```python
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

现在需求变了，我们需要用户可以指定序列的长度，再次编写如下代码：

```python
fibs = [0, 1]
num = int(input('How many Fibonacci numbers do you want?\n'))
for i in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)
```

现在，已经像是一个可用的程序的样子了，但是我们需要写出的代码是可以复用的，我们便会想到把它封装在一个自定义的函数里面

```python
def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result


if __name__ == "__main__":
    res = fibs(10)
    print(res)
```

这样，以后只需要直接调用函数 `fibs()` 就可以轻松获得序列了。

这是一个函数定义的过程，也是问题抽象的过程。

#### 参数魔法

##### 位置参数

函数参数传入的位置是有区别的，如下面的实例：

```python
def hello(greeting, name):
    print('{}, {}!'.format(greeting, name))

if __name__ == "__main__":
    hello('Hello', 'akashi')
```

输出： `Hello, akashi!`

如果我们传入参数的位置发生了变化，结果也会发生变化：

```python
hello('akashi', 'Hello')
```

输出：`akashi, Hello!`

程序并不能按照我们的意图执行，它不知道参数的正确位置，需要我们传入时就规定好位置

##### 关键字参数和默认值

想要程序知道参数的正确位置，可以使用关键字参数

```python
hello(name='akashi', greeting='Hello')
```

这样，指明了关键字，就可以不按位置传递参数

如果直接在定义函数中规定默认参数的值，调用时可以不用传递，但传入即会覆盖默认的参数

##### 收集参数

- 通过 `*` 可以传入一个元组

```python
def print_params(*params):
    print(params)

if __name__ == "__main__":
    print_params(1, 2, 3)
```

输出：`(1 2 3)`

当收集的元组参数在中间位置时，需要指定后续参数：

```python
def in_the_middle(x, *y, z):
    print(x, y, z)

if __name__ == "__main__":
    in_the_middle(1, 2, 3, 4, z=5)
```

输出： `1 (2, 3, 4) 5`

- 通过 `**` 可以传入一个字典

```python
def print_params(**params):
    print(params)

if __name__ == "__main__":
    print_params(x=1, y=2, z=3)
```

输出：

```python
{'x': 1, 'y': 2, 'z': 3}
```

##### 分配参数

相反，也可以用于分配参数

```python
def add(x, y):
    print(x+y)

if __name__ == "__main__":
     params_1 = (1, 2)
    params_2 = [3, 4]
    add(*params_1)
    add(*params_2)
```

字典同理

#### 递归

递归，简单来说就是一个函数自己调用自己。递归函数一般包含两个条件：`基线条件`和`递归条件`

基线条件：针对最小问题的解，满足条件时，函数直接返回一个值

递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分

下面来看几个例子：

##### 阶乘

> 计算 `n` 的阶乘，公式为 `1x2x...x(n-1)xn`

```python
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
```

基线条件：`1` 的阶乘为 `1`
递归条件：对于一个大于 `1` 的数字 `n`，其阶乘为 `(n-1)*n`

那么，满足这两个条件，可以实现为：

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

##### 幂

> 计算 `x` 的 `n` 次幂，`x*x*x...`(`n`次)

```python
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result
```

基线条件：任何数字 `x`，它的 `0` 次幂为 `1`
递归条件：当 `n>0` 时，`x` 的 `n` 次幂为 `x` 乘以 `x` 的 `n-1` 次幂，即 `power(x, n-1)*x`

那么，满足这两个条件，可以实现为：

```python
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
```

##### 二分查找

定义两个指针用来确定搜索范围(`lower`, `upper`)，不断折中缩小范围，如果两指针(上限和下限)相同，则指向的位置就是数字所在的位置，将数字返回

```python
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1

    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

if __name__ == "__main__":
   seq = [34, 67, 8, 123, 4, 100, 95]
   seq.sort()
   print(seq)
   res = search(seq, 34)
   print(res)
```

输出：

```python
[4, 8, 34, 67, 95, 100, 123]
2
```
