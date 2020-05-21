---
title: Python 上手指南之字典
date: yyyy-mm-dd
category: Python
tags: Python
thumbnail: /images/asuka/asu-3.jpg

---

### 字典

> 通过名称来访问其各个值的数据结构 `-` `映射`。字典是 `Python` 中唯一的内置映射类型。

<!-- more -->

#### `dict`

使用 `dict` 从其他映射或键值对序列创建字典

```python
>>> items = [('name', 'akashi'), ('age', 22)]
>>> d = dict(items)
>>> d
{'name': 'akashi', 'age': 22}
>>> d['name']
'akashi'
```

或者

```python
>>> dict(name='akashi', age=22)
{'name': 'akashi', 'age': 22}
```

#### 基本的字典操作

使用 | 描述
--- | ---
`len(item)` | 返回字典 `item` 包含的项数
`item[key]` | 返回与键 `key` 相关联的值
`item[key] = vlue` | 将值 `vule` 关联到 `key`
`del item[key]` | 删除键为 `key` 的项
`key in item` | 检查字典 `item` 是否包含键为 `key` 的项

#### 字典方法

方法 | 使用 | 描述
--- | --- | ---
`clear` | `adict.clear()` | 删除所有的字典项
`copy` | `adict.copy()` | 浅复制
`keys` | `adict.keys()` | 获取字典的键
`values` | `adict.values()` | 获取字典的值
`items` | `adict.items()` | 获取字典的键值对
`get` | `adict.get(k)` | 返回 `k` 对应的值，如果没有，返回 `None`
`get` | `adict.get(k, alt)` | 返回 `k` 对应的值，如果没有，返回 `alt`
`pop` | `adict.pop(key)` | 弹出指定的键向关联的值，并从字典中删除
`popitem` | `adict.popitem()` | 随机弹出一个字典项，并从字典中删除
`setdefault` | `adict.setdefault(key, value)` | 获取与指定键相关联的值，如果不存在，在字典中添加指定的键值对
`update` | `adict.update(otherdict)` | 使用一个字典项更新另一个字典

1. `clear()`

删除所有的字典项

```python
item = {
    'name': 'akashi',
    'age': 22
}

print(item)
item.clear()
print(item)
```

输出：

```python
{'name': 'akashi', 'age': 22}
{}
```

2. `copy()`

浅复制

```python
item = {
    'name': 'akashi',
    'age': 22,
    'list': [1, 2]
}

copy_item = item.copy()
item['addr'] = 'local'
copy_item['name'] = 'asuka'
copy_item['list'].append(3)
print(item)
print(copy_item)
```

输出：

```python
{'name': 'akashi', 'age': 22, 'list': [1, 2, 3], 'addr': 'local'}
{'name': 'asuka', 'age': 22, 'list': [1, 2, 3]}
```

当替换副本中的值时，原件不受影响，而如果修改副本中的值(就地修改而不是替换)，原件也会发生变化

深复制

```python
from copy import deepcopy

item = {
    'name': 'akashi',
    'age': 22,
    'list': [1, 2]
}

copy_item = deepcopy(item)
item['addr'] = 'local'
copy_item['name'] = 'asuka'
copy_item['list'].append(3)
print(item)
print(copy_item)
```

输出：

```python
{'name': 'akashi', 'age': 22, 'list': [1, 2], 'addr': 'local'}
{'name': 'asuka', 'age': 22, 'list': [1, 2, 3]}
```

3. `keys()`

获取字典中的键

```python
item = {
    'name': 'akashi',
    'age': 22,
}
print(item.keys())
```

输出：

```python
dict_keys(['name', 'age'])
```

4. `values()`

获取字典中的值

```python
item = {
    'name': 'akashi',
    'age': 22,
}
print(item.values())
```

输出：

```python
dict_values(['akashi', 22])
```

5. `items()`

获取字典中的键值

```python
item = {
    'name': 'akashi',
    'age': 22,
}
print(item.items())
```

输出：

```python
dict_items([('name', 'akashi'), ('age', 22)])
```

6. `get()`

获取字典中的值

```python
item = {
    'name': 'akashi',
    'age': 22,
}

print(item.get('name'))
```

输出： `akashi`

当指定的键不存在时，会输出 `None`

不存在时，指定默认值

```python
item = {
    'name': 'akashi',
    'age': 22,
}

print(item.get('nickname', 'asuka'))
```

输出： `asuka`

7. `pop()`

从字典中弹出一个值

```python
item = {
    'name': 'akashi',
    'age': 22,
}

print(item.pop('name'))
print(item)
```

输出：

```python
akashi
{'age': 22}
```

8. `popitem()`

从字典中随机弹出一个键值对

因为字典里面是无序的，弹出的值是随机的

```python
item = {
    'name': 'akashi',
    'age': 22,
}

print(item.popitem())
print(item)
```

输出： 

```python
('age', 22)
{'name': 'akashi'}
```

9. `setdefault()`

与 `get()` 类似，获取指定的键关联的值，但不同的是，如果不存在，会在字典中添加指定的键值对

```python
item = {
    'name': 'akashi',
    'age': 22,
}

print(item.setdefault('addr', 'local'))
print(item)
```

输出：

```python
local
{'name': 'akashi', 'age': 22, 'addr': 'local'}
```

10. `update()`

更新字典，有则替换，没有则添加

```python
item = {
    'name': 'akashi',
    'age': 22,
}

up_item = {
    'age': 21,
    'addr': 'local'
}

item.update(up_item)
print(item)
```

输出：

```python
{'name': 'akashi', 'age': 21, 'addr': 'local'}
```
