---
title: 五、if条件语句
date: yyyy-mm-dd
category: Python
tags:
    - python
    - 入门
    
---

#### 五、`if`语句

##### 5.1 一个简单的示例

```python
cars = ['audi', 'bmw', 'subaru', 'tuyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

<!--more-->

##### 5.2 条件测试

> 每条`if`语句的核心都是一个值为`True`或`False`的表达式，这种表达式被称为条件测试。

- 检查是否相等
    - 使用`==`符号

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52uu5bzscj20r802aq44.jpg)

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52uuidpebj20r802cwfu.jpg)

注意：一个等号是陈述（赋值），两个等号是发问（判断是否相等）。

- 不考虑大小写

> 在`Python`中检查是否相等时区分大小写，那如何判断是不考虑区分大小写呢？

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52uy6odslj20r802ejsv.jpg)

转换为小写比较：
![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52uymbzzcj20r803u416.jpg)

注意：原来的值不会发生改变。

- 检查是否不相等
    - 使用`!=`符号
```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')
    
```
- 检查多个条件
    - 使用`and`检查多个条件
        - ![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52v9g94uej20r8036jtn.jpg)
        - ![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52vcejw5gj20r80360uz.jpg)
        
    - 使用`or`检查多个条件
        - ![](http://ww1.sinaimg.cn/large/9c62a0cfly1g52vef4js5j20r805e0wp.jpg)
    
- 检查特定值是否包含
    - 使用`in`
- 检查特定值是否不包含
    - 使用`not in`
    
- 布尔表达式

> 布尔表达式，即条件测试的别名。结果要么为`True`，要么`False`。

```python
game_active = True
can_edit = False
```

##### 5.3 `if-elif-else`结构

```python
age = 12

if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')
```

##### 5.4 使用`if`语句处理列表

- 检查特殊元素
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
print('Adding ' + requested_topping + '.')

print('\nFinished making your pizza!')
```

- 确定列表不为空
```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')

    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
```
