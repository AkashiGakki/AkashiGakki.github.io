---
title: 九、类
date: yyyy-mm-dd
category:
    - Python
tags:
    - python

---

#### 九、类

##### 9.1 创建和使用类

```python
class Dog():

    def __init__(self, name, age):
        """ 初始化属性name和age """
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟蹲下 """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ 模拟打滚 """
        print(self.name.title() + " rolled over!")

```

<!--more-->

- 方法`__init__()`

类中的函数被称为方法，`__init__()`是一个特殊的方法，每当根据类创建新的实例时，`Python`就会自动运行它。为了区别，放过名称开头和末尾各有两个下划线，方法的形参`self`必不可少！！！还必须位于其他形参的前面。它是指向实例本身的一个引用，让实例能够访问类中的属性和方法。`self`不用传递实参，由程序自动传入。

- 创建实例

```python
my_dog = Dog("kii", 6)

print(my_dog.name.title())
print(my_dog.age)
```

- 访问属性

    - 通过点(`.`)访问

```python
Object.attribute
```

- 调用方法

```python
Object.function_name()
```

- 创建多个实例

```python
my_dog = Dog("kii", 6)
your_dog = Dog("chip", 5)
```

##### 9.2 使用类和实例

> 类可以用来模拟现实世界中的很多场景，创建好类以后，大部分的时间都使用根据类创建的实例上。

```python
class Car:

    def __init__(self, make, model, year):
        """ 初始化汽车属性 """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """ 返回汽车信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

- 给属性指定默认值

> 类中的每个属性都必须有初始值，哪怕这个值是`0`或者空字符串。可以在`__init__()`中指定属性的初始值，这样就无需它初始值的形参。

```python
class Car:

    def __init__(self, make, model, year):
        """ 初始化汽车属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ 返回汽车信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ 打印汽车里程 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
```

- 修改属性的值

    - 直接修改属性的值

    ```python
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    ```

    - 通过方法修改属性的值
    
    ```python
    class Car:
    
        def __init__(self, make, model, year):
            """ 初始化汽车属性 """
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
        
        def get_descriptive_name(self):
            """ 返回汽车信息 """
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()
        
        def read_odometer(self):
            """ 打印汽车里程 """
            print("This car has " + str(self.odometer_reading) + " miles on it.")
        
        def update_odometer(self, mileage):
            """ 更新汽车里程 """
            self.odometer_reading = mileage
    
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    
    my_new_car.update_odometer(230)
    my_new_car.read_odometer()
    ```
    
    - 通过方法对属性的值进行递增
    
    ```python
    class Car:
    
        def __init__(self, make, model, year):
            """ 初始化汽车属性 """
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
        
        def get_descriptive_name(self):
            """ 返回汽车信息 """
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()
        
        def read_odometer(self):
            """ 打印汽车里程 """
            print("This car has " + str(self.odometer_reading) + " miles on it.")
        
        def update_odometer(self, mileage):
            """ 更新汽车里程 """
            self.odometer_reading = mileage
        
        def increment_odometer(self, miles):
            """ 更新汽车里程特定的量 """
            self.odometer_reading += miles
    
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    
    
    my_new_car.update_odometer(230)
    my_new_car.increment_odometer(100)
    my_new_car.read_odometer()
    ```

##### 9.3 继承

> 类的编写并非都要从空白开始，可以使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新的类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

- 子类方法`__init__()`

> 创建子类的实例时，首先是给父类的所有属性赋值。

```python
class Car:

    def __init__(self, make, model, year):
        """ 初始化汽车属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ 返回汽车信息 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ 打印汽车里程 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ 更新汽车里程 """
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """ 更新汽车里程特定的量 """
        self.odometer_reading += miles

class ElectricCar(Car):
    """ 电动车 """
    def __init__(self, make, model, year):
        """ 初始化父类属性 """
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

`super()`是一个特殊函数，将父类和子类关联起来。父类也称为超类(`superclass`)。

- 给子类定义属性和方法

```python
class ElectricCar(Car):
    """ 电动车 """
    def __init__(self, make, model, year):
        """ 初始化父类属性 """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """ 电池容量 """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

- 重写父类的方法

> 在子类里面定义一个和父类同名的方法，可以对父类方法进行重写。这样，`Python`将不会考虑父类的这个方法，而只关注在子类中定义的相应的方法。

- 将实例作用属性

> 类的代码过多（属性和方法），可以抽出类的部分，作为一个独立的类提取出来，进行细化拆分。

```python

class ElectricCar(Car):
    """ 电动车 """
    def __init__(self, make, model, year):
        """ 初始化父类属性 """
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        """ 电池容量 """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

##### 9.4 导入类

- 导入单个类

```python
from car import Car
```

语法：

```python
from module_name import class_name
```

- 从一个模块中导入多个类

```python
from module_name import class_name1, class_name2
```

- 导入整个模块

```python 
import module_name
```

注意：在导入整个模块后，使用必须通过模块访问。例如：`module_name.class_name`

```python
import car

my_car = car.Car('audi', 'a4', 2016)
```

- 导入模块中的所有类

```python
from module_name import *
```
