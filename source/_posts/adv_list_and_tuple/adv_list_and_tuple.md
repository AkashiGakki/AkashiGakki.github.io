---
title: Python 上手指南之列表
date: yyyy-mm-dd
category: Python
tags: Python
thumbnail: /images/bg-43.jpg

---

#### 列表

> 列表的基本操作和方法。

<!-- more -->

##### `list`

> 因为不能像修改列表一样修改字符串，有些情况需要字符串来创建列表。

```python
res = list('Hello')
print(res)
```

输出：`['H', 'e', 'l', 'l', 'o']`

序列的运算：

运算名 | 运算符 | 说明
--- | --- | ---
索引 | `[]` | 获取序列中的某个元素
连接 | `+` | 将序列连接在一起
重复 | `*` | 重复 `N` 次连接
成员 | `in` | 序列中是否有某元素
长度 | `len` | 序列元素个数
切片 | `[:]` | 取出序列的一部分

##### 基本的列表操作

1. 修改列表：给元素赋值

```python
res = [1, 2, 3, 4]
print(res)

res[1] = 5
print(res)
```

输出：

```python
[1, 2, 3, 4]
[1, 5, 3, 4]
```

2. 删除元素

使用 `del` 语句可以实现列表中元素删除。

```python
res = [1, 2, 3, 4]
print(res)

del res[1]
print(res)
```

输出：

```python
[1, 2, 3, 4]
[1, 3, 4]
```

3. 给切片赋值

- 赋值

```python
res = list('akashi')
print(res)

res[1:] = list('rashi')
print(res)
```

输出：

```python
['a', 'k', 'a', 's', 'h', 'i']
['a', 'r', 'a', 's', 'h', 'i']
```

- 替换序列，改变序列长度

```python
res = list('akashi')
print(res)

res[1:] = list('suka')
print(res)
```

输出：

```python
['a', 'k', 'a', 's', 'h', 'i']
['a', 's', 'u', 'k', 'a']
```

- 不替换原有元素的情况下插入元素

```python
res = [1, 5]
print(res)

res[1:1] = [2, 3, 4]
print(res)
```

输出：

```python
[1, 5]
[1, 2, 3, 4, 5]
```

- 删除切片

```python
res = [1, 2, 3, 4, 5]
print(res)

res[1:4] = []
print(res)
```

输出：

```python
[1, 2, 3, 4, 5]
[1, 5]
```

- 指定步长

`[start:stop:step]`

注：`start` 缺省默认从头开始，`stop` 缺省默认至列表结尾，`step` 缺省默认为 `1`

```python
res = [1, 2, 3, 4, 5]
print(res)

num = res[::2]
print(num)
```

输出：

```python
[1, 2, 3, 4, 5]
[1, 3, 5]
```

- 序列反转

```python
res = [1, 2, 3, 4, 5]
num = res[::-1]
print(num)
```

输出：

```python
[5, 4, 3, 2, 1]
```

##### 列表方法

方法名 | 用法 | 说明
--- | --- | ---
`append` | `alist.append(item)` | 在列表末尾添加一个新元素
`clear` | `alist.clear()` | 就地清空列表的内容
`copy` | `alist.copy()` | 复制列表
`count` | `alist.count(item)` | 返回 `item` 在列表中出现的次数
`extend` | `alist.extend(otherlist)` | 同时将多个值附加到列表末尾
`index` |  `alist.index(item)` | 返回 `item` 第一次出现时的下标
`insert` | `alist.insert(i, item)` | 在列表的第 `i` 个位置插入一个元素
`pop` | `alist.pop()` | 删除并返回列表中最后一个元素
`pop` | `alist.pop(i)` | 删除并返回列表中第 `i` 个位置的元素
`del` | `del alist[i]` | 删除列表中第 `i` 个位置的元素
`remove` | `alist.remove(item)` | 从列表中移除第一次出现的 `item`
`reverse` | `alist.reverse()` | 将列表元素倒序排列
`sort` | `alist.sort()` | 将列表元素排序

1. `append()`

用于将一个对象附加到列表末尾

```python
lst = [1, 2, 3]
lst.append(4)
print(lst)
```

输出：

```python
[1, 2, 3, 4]
```

2. `clear()`

就地清空列表的内容

```python
lst = [1, 2, 3]
lst.clear()
print(lst)
```

输出：

```python
[]
```

3. `copy()`

复制列表

```python
a = [1, 2, 3]
b = a.copy()
b[1] = 4

print(a)
print(b)
```

输出：

```python
[1, 2, 3]
[1, 4, 3]
```

等效于

```python
a = [1, 2, 3]
b = a[:]
```

常规复制只是将另一个名称关联到了列表，本质上还是同一个列表。

4. `count()`

计算指定的元素在列表中出现的次数

```python
lst = [1, 1, 2, 3]
res = lst.count(1)
print(res)
```

输出： `2`

5. `extend()`

同时将多个值附加到列表末尾

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
```

输出：

```python
[1, 2, 3, 4, 5, 6]
```

6. `index()`

在列表中查找指定的值第一次出现的索引

```python
name = ['akashi', 'asuka', 'asuka']
print(name.index('asuka'))
```

输出： `1`

7. `insert()`

用于将一个对象插入列表

```python
lst = [1, 2, 3, 5]
lst.insert(3, 4)
print(lst)
```

输出：

```python
[1, 2, 3, 4, 5]
```

8. `pop()`

从列表中删除一个元素(末尾为最后一个元素)，并返回这一个元素

```python
lst = [1, 2, 3, 4]
print(lst.pop())
```

输出： `4`

注：`push` 和 `pop` 是普遍接受的两种栈操作，但是 `Python` 没有提供 `push`，可以使用 `append` 代替。

9. `remove()`

删除第一个为指定值的元素

```python
lst = [1, 1, 2, 3]
lst.remove(1)
print(lst)
```

输出：

```python
[1, 2, 3]
```

10. `reverse()`

按相反的顺序排列列表中的元素

```python
lst = [1, 2, 3]
lst.reverse()
print(lst)
```

输出：

```python
[3, 2, 1]
```

11. `sort()`

用于对列表就地排序

```python
lst = [4, 6, 2, 1, 3, 5]
lst.sort()
print(lst)
```

输出：

```python
[1, 2, 3, 4, 5, 6]
```

因为是就地排序，修改了列表而不返回任何的值，如果像下面这样，就是得到一个 `None`

```python
x = [2, 1, 4, 3]
y = x.sort()
print(y)
```

输出： `None`

想要获取排序后的列表的副本，可以使用函数 `sorted()`

```python
x = [2, 1, 4, 3]
y = sorted(x)
print(y)
```

12. 高级排序

方法 `sort()` 接受两个可选参数：`key` 和 `reverse`

参数 `key` 可以设置为一个用于排序的函数(可以是自定义函数)：

```python
name = ['akashi', 'asuka', 'gakki']
name.sort(key=len)
print(name)
```

参数 `reverse` 指定为 `True` 或 `False`，指出是否按相反顺序排序。

#### 元组：不可修改的序列

> 元组也是序列，与列表的差别在于不可修改。

使用逗号分隔，自动创建一个元组

- 创建

```python
>>> 1, 2, 3
(1, 2, 3)
```

- 表示一个值的元组

```python
>>> 4,
(4,)
```

##### `tuple`

```python
res = tuple('123')
print(res)
```

输出：

```python
('1', '2', '3')
```

元组操作与列表大体一致，也有切片

元组用作映射中的键(以及集合的成员)，而列表不行。
