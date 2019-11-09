---
title: Python 上手指南之再谈抽象
date: yyyy-mm-dd
category: Python
tags: Python
thumbnail: /images/asuka/asu-6.jpg

---

### 再谈抽象

> 封装、继承和多态。

<!-- more -->

#### 封装

> 对外部隐藏有关对象工作原理的细节。

封装指的是向外隐藏不必要的细节，让你无需知道对象内部的细节就可以使用它。

假设我们有一个名为 `OpenObject` 的类，存在 `set_name()` 和 `get_name()` 方法：

```python
>>> o = OpenObject()
>>> o.set_name('akashi')
>>> o.get_name()
'akashi'
```

具体实现：

```python
class Person:
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
```

这是属于方法上的封装，还可以在属性上进行封装，让外部不能访问

#### 再谈隐藏

将属性定义为私有，私有属性不能从对象外部进行访问，而只能通过存取器方法(`get_name` 和 `set_name`)访问

通常在 `python` 中，更常见的做法是使用特性(`property`)来替代存取器

让方法和属性设置为私有的，可以在名称前以两个下划线打头，例如：`self.__name = name`

然而在 `python` 中并没有真正支持私有化，使用 `_类名__方法名` 这种方式依然可以在外部访问，但是隐藏就是我们对外部发出的信号，让外部不要访问，所有开发中我们不应这样做

在 `python` 中，单下划线开始的成员变量叫保护变量，只有类对象（即类实例）和子类对象自己能访问到这些变量，需通过类提供的接口进行访问

双下划线开始的成员变量叫私有变量，只有类对象自己可以访问，连子类对象也不可以访问


#### 继承

> 基于通用类创建出专用类，子类是对父类的扩充。

继承可以达到代码和功能复用的目的，并且子类可以对父类进行功能上的扩充。

```python
class Children(Person):
    pass
```

要确定一个类是否是另一个类的子类，可以使用内置方法 `issubclass`

```python
>>> issubclass(Children, Person)
True
```

如果你有一个类，想知道他的基类，可以访问其特殊属性 `__bases__`

```python
>>> Children.__bases__
```

同样，确定对象是否是特定类的实例，可以使用 `isinstance`

```python
>>> s = Children()
>>> isinstance(s, Children)
True
```

##### 多个超类

`Python` 是支持多继承的，然而，除非万不得已，否则应该避免使用多重继承，因为在有些情况下，它可能带来意外的 “并发症”

#### 多态

> 可对不同类型的对象执行相同的操作，表现在方法的重载和覆写、对象的向上转型。

多态意味着 `多种形态`，我认为是最重要的原则，这意味着你不知道变量指向的是那种对象，也可以对其执行操作，且操作的行为会随对象的类型而表现出不同

如：

```python
>>> 'abc'.count('a')
1
>>> [1, 2, 'a'].count('a')
1
```

像这样，方法 `count` 对于字符串和列表都可以使用，根据对象的不同做出不同的表现，这就是多态

相反，在使用时，我们只需要知道对象有 `count` 这个方法就可以了，它会根据不同的对象有不同的表现方式

另一个例子就是内置的运算符：

```python
>>> 1 + 2
3
>>> 'akashi' + 'sai'
akashisai
>>> [1, 2] + [3, 4, 5]
[1, 2, 3, 4, 5]
```

在实现时，是依赖于对象的向上转型，使多态发生作用，这一点在静态类型语言中表现更为明显，以 `Java` 为例：

```java
Shape rect = new Rectangle()
Shape cir = new Circle()
rect.draw()
cir.draw()
```

#### 接口和内省

> (`Java` 单继承的局限、与多态相关)

接口这一概念与多态相关，处理多态对象时，我们只关心其接口(协议对外暴露的方法和属性。在 `Python` 中，不显示地指定对象必须包含哪些方法才能用作参数。不会像 `Java` 和 `Go` 那样显示编写接口，而是假定对象能够完成你要求它完成的任务，如果不能完成，程序将失败。

#### 抽象基类

> 利用抽象基类可以实现对子类覆写方法的控制。

`Python` 在多态上几乎都只依赖于鸭子类型(如果走起来像鸭子，叫起来像鸭子，那么它就是鸭子)，然而官方也通过引入模块 `abc` 提供了抽象基类的支持，抽象基类是不能实例化的类，子类需要实现抽象基类的所有抽象方法。

```python
from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass
```

```python
class Herring(Talker):
    def talk(self):
        print("Blub.")
```
