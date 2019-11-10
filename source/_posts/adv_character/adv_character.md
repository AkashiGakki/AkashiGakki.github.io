---
title: Python 上手指南之特性、迭代器和生成器
date: yyyy-mm-dd
category: Python
tags: Python
thumbnail: /images/asuka/asu-7.jpg

---

### 特性、迭代器和生成器

> Python 中的魔法(特殊)方法。

<!-- more -->

首先，所有的类都将隐式的继承 `object` 类，如果没有指定超类，将直接继承它，否则将间接的继承它。

#### 构造函数

> 介绍的第一个魔法方法是构造函数，其实就是初始化方法，命名为 `__init__`。

构造函数将在对象创建后自动调用它们

```python
class Foobar:
    def __init__(self):
        self.somevar = 42

if __name__ == "__main__":
    f = Foobar()
    print(f.somevar)
```

或者，给构造函数添加参数

```python
class Foobar:
    def __init__(self, value=42):
        self.somevar = value
```

参数是可选的，可以使用默认的参数值，也可以传入指定的参数值，对原有的值进行覆盖

##### 重写

> 每一个类都有一个或多个超类，并从它们那里继承行为。

对于大多数的子类，重写构造函数时，必须调用超类的构造函数，否则可能无法正确的初始化对象

```python
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    
    def sing(self):
        print(self.sound)

if __name__ == "__main__":
    s = SongBird()
    s.eat()
```

这时，执行程序，你会发现无法正确的初始化对象，提示对象没有 `hungry` 属性

这是因为子类重写了构造函数，但是并没有初始化父类的构造函数

##### 调用未关联的超类构造函数

由于历史遗留问题，我们先介绍旧版 `Python` 的初始化方式：

```python
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'
    
    def sing(self):
        print(self.sound)
```

修改之后再次执行，会发现已经可正确的初始化了

但是在新式类中，我们应该避免这种初始化方式，而使用 `super`

##### 使用函数 `super`

使用 `super` 时通常不用提供任何参数

```python
class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    
    def sing(self):
        print(self.sound)
```

当然，如果子类没有重写构造函数，那么默认继承了父类的构造函数，可以直接使用

#### 元素访问

##### 基本的序列和映射协议

序列和映射基本上是元素的集合，要实现它们的基本行为，不可变对象需要实现2个方法，可变对象需要实现4个

- `__len__(self)`

返回集合包含的项数

- `__getitem__(self, key)`

返回与指定键相关联的值

- `__setitem__(self, key, value)`

以键相关联的方式存储值

- `__delitem__(self, key)`

当对象可变(且允许被删除时)，才需要实现

下面创建一个无穷序列

```python
def check_index(key):
    # 判断
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        # 初始化
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        # 获取
        check_index(key)
        try:
            # 如果元素已被修改，存储元素的值
            return self.changed[key]
        except KeyError:
            # 如果元素未被修改，计算出元素的值
            return self.start + key * self.step

    def __setitem__(self, key, value):
        # 修改
        check_index(key)
        self.changed[key] = value

if __name__ == "__main__":
    # 创建一个从1开始，步长为2的无穷序列
    s = ArithmeticSequence(1, 2)
    print(s[4])
```

这里我们没有实现 `__del__`，意味着不允许删除元素

##### 从 `list`、`dict`、`str`派生

快速实现一个序列和映射，可以从已有的基本序列和映射继承，通过重写魔法方法，实现一个新的序列或映射，例如：

实现一个计算器列表：

```python
class CounterList(list):
    def __init__(self, *args):
        super.__init__(*args)
        self.counter = 0
    
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
```

#### 特性

之前有介绍 `set` 和 `get` 的存取方法，是一种很重要的封装状态变量(属性)的方法。但我们没有办法将所有属性都提供存取方法，这是不现实的，所以我们采用另外一种方法 —— `property`。它可以隐藏存取方法，让所有属性看起来都一样。

> 通过存取方法定义的属性通常称为特性。

##### 函数 `property`

```python
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def get_size(self):
        return self.width, self.height

    def set_size(self, size):
        self.width, self.height = size

    size = property(get_size, set_size)

if __name__ == "__main__":
    r = Rectangle()
    r.width = 5
    r.height = 10
    print(r.size)
```

这样，`size` 属性依然受制于 `set` 和 `get` 执行计算，但是看起来就像普通属性一样

或者使用装饰器实现

```python
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    @property
    def size(self):
        return self.width, self.height
    
    @size.setter
    def size(self, size):
        self.width, self.height = size
    
if __name__ == "__main__":
    r = Rectangle()
    r.width = 5
    r.height = 10
    print(r.size)
```

##### 静态方法和类方法

静态方法和类方法在创建的过程中是分别包装在 `staticmethod` 和 `classmethod` 类的对象中的

静态方法的定义中，没有参数 `self`，可以直接通过类来调用

类方法的定义中包含类似于 `self` 的参数，通常被命名为 `cls`，对与类方法，也可以通过对象直接调用，但参数 `cls` 将自动关联到类

```python
class MyClass:
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('Tish is a class method of', cls)
    cmeth = classmethod(cmeth)

if __name__ == "__main__":
    m = MyClass()
    m.smeth()
    m.cmeth()
```

在引入装饰器(装饰器可以用于包装任何可调用的对象，并且可用于方法和函数)以后，还可以用于这样包装方法

```python
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    
    @classmethod
    def cmeth(cls):
        print('Tish is a class method of', cls)

if __name__ == "__main__":
    MyClass.smeth()
    MyClass.cmeth()
```

定义方法后，无需实例化，可以直接使用它们

更多装饰器实现，参考 [@property](https://www.liaoxuefeng.com/wiki/897692888725344/923030547069856)、[装饰器](https://www.liaoxuefeng.com/wiki/897692888725344/923030163290656)

##### `__getattr__`、`__setattr__`

- `__getattr__(self, name)`

在属性被访问而对象没有这样的属性时自动调用

- `__setattr__(self, name, value)`

试图给属性赋值时自动调用

使用上面的方法可以编写处理多个特性的代码，但是，在可能的情况下，还是使用函数 `property` 代替比较好(出于使用方式和效率的考虑)

#### 迭代器

> 迭代，意味着重复多次，就像循环那样，实现了 `__iter__` 的对象是可迭代的。

方法 `__iter__` 返回一个迭代器，它是包含方法 `__next__` 的对象，而调用方法时可以不提供任何参数。

在某些情况下，你可能只想逐个地获取值，而不是使用列表一次性获取，因为如果值很多，列表可能占用太多的内存，然而使用迭代器更通用、更简单、更优雅

```python
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

if __name__ == "__main__":
    fibs = Fibs()
    for f in fibs:
        print(f)
        if f > 100:
            break
```

实现了方法 `__iter__` 的对象是可迭代的，而实现方法 `__next__` 的对象是迭代器

```python
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    
    def __iter__(self):
        return self

if __name__ == "__main__":
    t = TestIterator()
    print(list(t))  
```

#### 生成器

> 生成器是一中使用普通函数语法定义的迭代器。

生成器使用 `yied` 语句进行创建，之前有简单介绍，也可以说包含 `yield` 语句的函数称作生成器

现在我们使用一个生成器展开一个嵌套列表：

```python
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2,], [3, 4], [5]]
print(list(flatten(nested)))
```

输出：

```python
[1, 2, 3, 4, 5]
```
