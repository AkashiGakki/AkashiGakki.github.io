---
title: 六、字典
date: yyyy-mm-dd
category: 
    - Python
tags: 
    - python
    - 入门
---

#### 六、字典

##### 6.1 使用字典

> 在`Pyhton`中，字典是一系列`键-值`对。

<!--more-->

- 字典

    - `键-值`对
    - 用花括号`{}`表示
    - 键和值之间用冒号`:`分隔
    - 键值对之间用逗号`,`分隔
    
```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

- 添加`键-值`对

> 字典是一种动态结构，可随时在其中添加键值对。

```python
alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

输出：
```python
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

- 先创建一个空字典

```python
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
```

- 修改字典中的值

```python
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

alien_1['color'] = 'yellow'
print(alien_1)
```

输出：
```python
{'color': 'yellow', 'points': 5}
```

- 删除键值对

    - 使用`del`语句将相对应的键值对彻底删除
    - 必须指定要删除的字典名和键
    
```python
alien_1 = {'color': 'green', 'points': 5}

del alien_1['points']
print(alien_1)
```

输出：
```python
{'color': 'green'}
```

##### 6.2 遍历字典

- 遍历所有的键值对

    - 使用方法`items()`

```python
user_0 = {
    'username': 'Akashi',
    'age': 21,
    'sex': 'male'
}

for key, value in user_0.items():
    print('\nkey:' + key)
    print('value:' + str(value))
```

注意：即便遍历字典时，键值对的返回顺序也与存储顺序不同，`Python`不关心键值对的存储顺序，而只跟踪键和值之间的关联关系。

- 遍历字典中所有的键

    - 使用方法`keys()`
    
```python
user_0 = {
    'username': 'Akashi',
    'age': 21,
    'sex': 'male'
}

for key in user_0.keys():
    print(key.title())
```

注意：将代码中`for key in user_0.keys():`替换为`for key in user_0:`输出不变。

> 显式地使用方法`keys()`可以让代码更容易理解，当然也可以省略。

- 按顺序遍历字典中所有的键

    - 要以特定的顺序返回元素，一种办法是在`for`循环中对返回的键进行排序
    - 使用`sorted()`来获得按特定顺序排列的键列表的副本

```python
user_0 = {
    'username': 'Akashi',
    'age': 21,
    'sex': 'male'
}

# 按字母顺序排列
for key in sorted(user_0.keys()):
    print(key)
```

- 遍历字典中所有的值

    - 使用方法`values()`
    ```python
    user_0 = {
        'username': 'Akashi',
        'age': 21,
        'sex': 'male'
    }

    for value in user_0.values():
        print(value)

    ```
    - 剔除重复项，使用集合`set()`
    ```python
    user_0 = {
        'username': 'Akashi',
        'age': 21,
        'sex': 'male'
    }
    
    for value in set(user_0.values()):
        print(value)
    ```

##### 6.3 嵌套

- 字典列表

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

- 在字典中存储列表

```python
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())
```

- 在字典中存储字典

```python
users = {
    'akashi': {
        'name': 'akashi',
        'age': 21,
        'sex': 'male'
    },

    'asuka': {
        'name': 'asuka',
        'age': 20,
        'sex': 'female'
    }
}

for username, user_info in users.items():
    print('\nUsername: ' + username)

    print('\tAge: ' + str(user_info['age']))
    print('\tSex: ' + user_info['sex'])
```

