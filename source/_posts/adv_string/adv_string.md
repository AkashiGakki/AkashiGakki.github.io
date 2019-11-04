---
title: Python 上手指南之字符串
date: yyyy-mm-dd
category: Python
tags: Python
thumbnail: /images/asuka/asu-2.jpg

---

#### 字符串

> 字符串的基本操作和方法。

<!-- more -->

##### 设置字符串的格式

```python
>>> "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)
'3 1 4 2'
```

```python
me = 'my name is {name}'.format(name='akashi')
print(me)
```

##### 基本操作

序列的基本操作(索引、切片、乘法、成员资格检查、长度、最小值、最大值)都适用于字符串

但是，字符串是不可变的，所有的元素赋值和切片赋值都是非法的。

##### 字符串方法

方法 | 使用 | 描述
--- | --- | ---
`center` | `astring.center(w)` | 返回一个字符串，长度为 `w`，在两边填充字符(默认为空格)，让字符串居中
`count` | `astring.count(item)` | 返回 `item` 出现的次数
`lower` | `astring.lower()` | 返回均为小写字母的字符串
`upper` | `astring.upper()` | 返回均为大写的字符串
`title` | `astring.title()` | 字符串单词首字母大写，返回结果
`find` | `astring.find(item)` | 返回 `item` 第一次出现时的下标
`join` | `astring.join(sequence)` | 将两个字符串元素合并，并返回结果
`replace` | `astring.replace(old, new)` | 将指定子串全部替换为另一个字符串返回
`split` | `astring.split(schar)` | 在 `schar` 位置将字符串分割为子串
`strip` | `astring.strip()` | 删除字符串开头和末尾的空白

1. `center()`

字符串居中

```python
>>> x = 'string'
>>> x.center(10)
'  string  '
>>> x.center(20, '=')
'=======string======='
```

2. `count()`

计算字符出现个数

```python
>>> x = 'akashi'
>>> x.count('a')
2
```

3. `lower()`

字符串转换成小写

```python
>>> x = 'AKASHI'
>>> x.lower()
'akashi'
```

类似还有

字符串转换成大写 - `upper()`

```python
>>> x = 'asuka'
>>> x.upper()
'ASUKA'
```

首字母大写

```python
>>> x = 'gakki'
>>> x.title()
'Gakki'
```

4. `find()`

在字符串中查找子串，如果存在，返回第一次出现的第一个字符的索引，否则返回 `-1`

```python
>>> x = 'akashi'
>>> x.find('ka')
1
```

注：值匹配一次，返回第一次的下标

类似还有 

`index()`、`rindex()`、`rfind()`

5. `join()`

合并序列元素

```python
>>> x = 'akashi'
>>> '-'.join(x)
'a-k-a-s-h-i'
>>> seq = ['akashi', 'asuka', 'gakki']
>>> sep = '+'
>>> sep.join(seq)
'akashi+asuka+gakki'
```

注：目的是将一个列表合并为一个字符串，可以指定中间的拼接字符。

6. `split()`

将字符串拆分为序列

```python
>>> x = '1+2+3+4'
>>> x.split('+')
['1', '2', '3', '4']
```

注：和 `join()` 相反，`split()` 用于拆分字符串为列表。

7. `replace()`

替换字符串

```python
>>> x = 'akashi'
>>> x.replace('kashi', 'suka')
'asuka'
```

注：替换的是所有的字符串中出现的子串，一次执行替换全部。

8. `strip()`

取出字符串开始和结尾的空白

```python
>>> x = '  akahsi '
>>> x.strip()
'akahsi'
```

类似还有

`lstrip()`、`rstrip()`

##### 判断字符串是否满足特定的条件

方法以 `is` 打头，判断为真返回 `True`，否则返回 `False`

方法 | 使用 | 描述
--- | --- | ---
`isalnum()` | `astring.isalnum()` | 检查字符串中字符是否都是字母或数
`isalpha()` | `astring.isalpha()` | 检查字符串字符是否都是字母
`isdigit()` | `astring.isdigit()` | 检查字符串字符是否都是数字
`islower()` | `astring.islower()` | 检查字符串字符是否都是小写
`isupper()` | `astring.isupper()` | 检查字符串字符是否都是大写
