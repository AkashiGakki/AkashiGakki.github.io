---
title: 四、操作列表
date: yyyy-mm-dd
category: Python
tags:
    - python
    - 入门

---

#### 四、操作列表

##### 4.1 遍历整个列表

- 遍历
```python
mangicians = ['alice', 'david', 'carolina']

for mangician in mangicians:
    print(mangician)
```

<!--more-->

##### 4.2 避免缩进错误

> `Python`根据缩进来判断代码行与前一个代码行的关系

- 缩进
    - 忘记缩进
        - 报错
        - 逻辑错误
    - 不必要的缩进
        - 报错
    - 循环后不必要的缩进
        - 逻辑错误
    - 遗漏了冒号
        - 语法错误
        - `for`语句末尾的冒号告诉`Python`下一行是循环的第一行
    
##### 4.3 创建数值列表

- 使用函数`range()`
    - 从指定的第一个值开始，到指定的第二个值结束，不包含第二个值
```python
for value in range(1, 5):
    print(value)
```

- 使用`range()`创建数字列表——使用`list()`转换为列表
    - 使用`list()`转换为列表
    ```python
    numbers = list(range(1, 5))
    print(numbers)
    ```
    输出：
    > [1, 2, 3, 4]
    - 指定步长
        - 打印1~10内的偶数：
    ```python
    numbers = list(range(2, 11, 2))
    print(numbers)
    ```
    - 练习
        - 打印1~10内的平方
        ```python
        squares = []
        for value in range(1, 11):
            square = value ** 2
            squares.append(square)
        print(squares)
        ```
        - 优化
            - 使用临时变量会让代码更易读，而在其他情况下，只会让代码无谓地变长；
            - 首先考虑编写清晰易懂且能完成所需功能的代码；
            - 审核时，再考虑更高效的方法。
        ```python
        squares = []
        for value in range(1, 11):
            squares.append(value ** 2)
        print(squares)
        ```
- 统计计算
    - 最大值`max()`、最小值`min()`、总和`sum()`
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))
```
- 列表解析
    - 解析列表将`for`循环和创建新元素的代码合并成一行，并自动附加新元素
```python
"""
列表解析
"""
squares = [value ** 2 for value in range(1, 11)]
print(squares)
```

##### 4.4 使用列表的一部分

- 切片
    - 处理列表的部分元素
    ```python
    """
    打印从第1个开始，到第4个为止，不包括第4个(下标从0开始)
    """
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    
    print(players[0:3])
    ```
    - 如果没有指定第一个索引，将从列表开头开始
    ```python
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    """
    打印从列表开头开始，到第5个为止，不包括第5个(下标从0开始)
    """
    print(players[:4])
    ```
    - 如果省略终止索引，将终止于列表末尾
    ```python
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    """
    打印从第2个开始，到列表末尾为止
    """
    print(players[1:])
    ```
    - 负数索引返回离列末尾相应距离的元素
    ```python
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    """
    打印从最后3个开始，到列表末尾为止
    """
    print(players[-3:])
    ```
- 遍历切片
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

for player in players[:3]:
    print(player.title())
```
- 复制列表
    - 复制列表，可以创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（`[:]`）

> 理解两个例子的差异

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)

print(friend_foods)
```
输出：
![](http://ww1.sinaimg.cn/large/9c62a0cfly1g51kix6u17j20r801imx7.jpg)

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
"""
    本质上是将friend_foods关联到了包含在my_foods的列表，两个变量都是指向了同一个表。所以分别对两个变量操作，列表都会发生变化，且两个变量的值是相同的
"""
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)

print(friend_foods)
```
输出：
![](http://ww1.sinaimg.cn/large/9c62a0cfly1g51kiemhohj20r801m0st.jpg)

##### 4.5 元组

> 一系列不可修改的元素，不可变的列表被称为元组

- 定义和遍历
    - 尝试修改元组会报错
```python
dimensions = (200, 50)
print(dimensions)

for dimension in dimensions:
    print(dimension)
```

- 修改元组变量
    - 虽然不能修改元组的元素，但可以给存储元组的变量赋值（重新定义元组）
```python
dimensions = (200, 50)

dimensions = (400, 100)
for dimension in dimensions:
print(dimension)
```
如果需要存储一组值在程序的整个生命周期内都不变，可以使用元组。
