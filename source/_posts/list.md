---
title: 三、列表简介
date: yyyy-mm-dd
category: Python
tag:
    - python
    - 入门

---

#### 三、列表

##### 3.1 什么是列表

列表由一系列按特定的顺序排列的元素组成。用`[]`来表示，并用逗号来分隔其中的元素。

```python
bicycles = ['trek', 'cannondale', 'redine', 'specialized']
print(bicycles)
```

<!--more-->

输出：

![list](http://ww1.sinaimg.cn/large/9c62a0cfly1g45a9naj3rj20r801kglq.jpg)

- 访问列表元素

```python
bicycles = ['trek', 'cannondale', 'redine', 'specialized']
print(bicycles[0])
```

列表是有序集合，因此要访问列表的任何元素，只需要将元素位置的索引传入即可。

- 索引从`0`而不是`1`开始

```python
bicycles = ['trek', 'cannondale', 'redine', 'specialized']
print(bicycles[1])
print(bicycles[-1])
```

第一个列表元素的索引为`0`；通过将索引指定为`-1`，可以返回最后一个列表元素。

输出：

![返回最后一个元素](http://ww1.sinaimg.cn/large/9c62a0cfly1g45ahs7wajj20r801odfp.jpg)

##### 3.2 修改、添加和删除元素

- 修改列表元素

```python
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)
```

- 在列表中添加元素

    - 在列表末尾添加元素
        - `append()`
    ```python
    motocycles = ['honda', 'yamaha', 'suzuki']
    print(motocycles)

    motocycles[0] = 'ducati'
    print(motocycles)

    motocycles.append('honda')
    print(motocycles)
    ```
    - 在列表中插入元素
        - `insert()`
        ```python
        motocycles = ['honda', 'yamaha', 'suzuki']
        print(motocycles)
        
        motocycles.insert(0, 'ducati')
        print(motocycles)
        ```
- 从列表中删除元素

    -  使用`del`语句删除元素
    ```python
    motocycles = ['honda', 'yamaha', 'suzuki']
    print(motocycles)
    
    del motocycles[0]
    print(motocycles)
    ```
    - 使用方法`pop()`删除元素
        - 方法`pop()`可以删除列表末尾的元素，并且你可以接着使用它的值
    ```python
    motocycles = ['honda', 'yamaha', 'suzuki']
    print(motocycles)
    
    poped_motocycles = motocycles.pop()
    print(motocycles)
    print(poped_motocycles)
    ```
    - 弹出列表中任何位置处的元素
        - 在括号中指定要删除的元素的索引，可以使用`pop()`来删除列表中任何位置的元素
    ```python
    motocycles = ['honda', 'yamaha', 'suzuki']
    print(motocycles)
    
    next_motocycles = motocycles.pop(1)
    print(motocycles)
    print(next_motocycles)
    ```
    - 根据值删除元素
        - `remove()`
        - 使用`remove()`删除元素时，也可以接着使用它的值
        - 方法`remove()`只删除第一个指定的值，如果该值在列表中出现多次，就需要使用循环判断
    ```python
    mark = 'ducati'
    motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(motocycles)
    
    motocycles.remove(mark)
    print(mark)
    print(motocycles)
    ```

##### 3.3 组织列表

- 使用方法`sort()`对列表进行永久性排序
    - 按字母顺序排序
    - 方法`sort()`的修改是永久性的，无法恢复到原来的排序
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

'''
反转列表
'''
cars.sort(reverse=True)
print(cars)

```
    
- 使用函数`sorted()`对列表进行临时排序
    - `sorted()`可以按特定的顺序显示列表元素，同时不影响它们在列表中原始排列顺序
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list: ")
print(cars)

```
- 倒序打印列表
    - `reverse()`永久性的修改了排列的列表元素，但可以随时恢复，只需再次调用`reverse()`即可
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)
```
- 确定列表的长度
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(len(car))
```
- 避免索引错误
    - 当发生索引错误找不到解决办法时，可以尝试将列表或其长度打印出来
