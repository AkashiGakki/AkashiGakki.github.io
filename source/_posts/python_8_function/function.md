---
title: Python编程 - 函数
date: 2019-7-21
category:
    - Python
tags:
    - python
    
---

#### 八、函数

##### 8.1 定义函数

```python
def greet_user():
    """ 显示问候 """
    print("Hello!")

#调用
greet_user()
```

<!--more-->

- 定义

    - 使用关键字`def`告诉`Python`定义一个函数
    - 函数名，如`greet_user()`，括号里面传参数
    - 定义以冒号结尾`:`

```python
def 函数名(形参):
    # 函数体
```

- 向函数传递信息

```python
def greet_user(username):
    """ 显示问候 """
    print("Hello, " + username.title() + " !")

#调用
greet_user(input("What's you name?"))
```

- 实参和形参

    - 在函数定义中，传入的变量是一个形参
    - 在函数的调用中，传递的变量是一个实参

##### 8.2 传递实参

- 位置实参
    
> 函数调用中的每一个实参都关联到函数定义中的一个形参，基于实参的顺序进行关联的方式被称为位置实参

```python
def describe_pet(animal_type, pet_name):
    """ 显示宠物信息 """
    print("\ntype: " + animal_type)
    print("name: " + pet_name)

describe_pet('hamster', 'harry')
```

注意：传入不同的实参可以对函数多次调用，实现复用；位置实参的顺序很重要，要与形参的位置相对应。

- 关键字实参

> 关键字实参是传递给函数一个键值对，将实参的名称和值关联起来，顺序便无关紧要了。

```python
def describe_pet(animal_type, pet_name):
    """ 显示宠物信息 """
    print("\ntype: " + animal_type)
    print("name: " + pet_name)

describe_pet(animal_type = 'hamster', pet_name = 'harry')
```

- 默认值

> 可以给每个形参指定默认值，在调用时如果没有出入实参，则使用默认值。

```python
def describe_pet(pet_name, animal_type = 'cat'):
    """ 显示宠物信息 """
    print("\ntype: " + animal_type)
    print("name: " + pet_name)

describe_pet('nieko')
```

注意：在定义函数时需将有默认参数的形参（无需传递实参的形参）放在形参列表的最后面，因为`Python`依然将需要传入的实参视为位置实参，位置错误会报“非默认参数跟随默认参数”的错误。

注意：在无默认值的情况下，形参和实参的位置和个数都需要一一对应，缺少传入实参也会报错。

- 避免实参错误

> 实参不匹配问题，仔细查看错误，在无默认值的情况下，必须为形参提供实参，并一一关联（位置关联或关键字关联）。

##### 8.3 返回值

- 返回简单值

    - `return`

```python
def get_formatted_name(first_name, last_name):
    """ 返回姓名 """
    full_name = first_name + " " + last_name
    return full_name.title()

person = get_formatted_name('akashi', 'sai')
print(person)
```

- 返回字典

> 函数可以返回任何类型的值，包括列表和字典等较为复杂的数据结构。

```python
def build_person(name, age = '', sex = ''):
    """ 返回一个字典，定义个人信息 """
    person = {
        'name': name,
        'age': age,
        'sex': sex
    }
    return person

person = build_person('akashi', 21, 'male')
print(person)
```

或者你也可以只传入`name`:

```python
person = build_person('akashi')
print(person)
```

- 结合使用函数和`while`循环

```python
def get_formatted_name(first_name, last_name):
    """ 返回姓名 """
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter'q' at any time to quit)")

    f_name = input("First name： ")
    if f_name == 'q':
    break

    l_name = input("Last name: ")
    if l_name == 'q':
    break

    person = get_formatted_name(f_name, l_name)
    print("\nHello, " + person + " !")
```

##### 8.4 传递列表

```python
def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)

username = ['akashi', 'asuka', 'gakki']
greet_users(username)
```

- 在函数中修改列表

```python
unprinted_designs = ['akashi', 'asuka', 'gakki']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop();

    print("Priint: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

重新组织：

```python
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Print model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['akashi', 'asuka', 'gakki']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)```
```

注意：重新梳理流程，提高效率，每个函数都只应负责一项具体的工作。

- 禁止函数修改列表

    - 将列表的副本传递给函数
    
```python
# 切片
function_name(list_name[:])
```

注意：除非有充分的理由需要传递副本，否则不推荐。考虑到效率，创建副本需要有时间和内存的开销。

##### 8.5 传递任意数量的实参

```python
def make_pizza(*toppings):
    """ 打印顾客点的配料 """
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

> 形参名`*toppings`中的星号让`Python`创建了一个名为`topping`的元组，并将收到的所有的值都封装到元组中。这样，无论多少个实参，都可以传递。

```python
def make_pizza(*toppings):
    """ 打印顾客点的配料 """
    print("\ntoppings list:")
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

- 结合使用位置实参和任意数量实参

```python
def make_pizza(size, *toppings):

    print("\ntoppings list:")
    print(size)
    for topping in toppings:
        print(topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

注意：函数定义时，先定义位置形参，将任意数量形参定义在最后。

- 使用任意数量的关键字实参

```python
def bulid_profile(name, age, **user_info):
    """ 创建一个空字典，存储用户信息 """
    profile = {}
    profile['name'] = 'akashi'
    profile['age'] = 21
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = bulid_profile('akashi', 21, sex = 'male', location = 'Chengdu')

print(user_profile)
```

> 形参名`**user_info`的两个星号让`Python`创建了一个`user_info`的空字典，并接收所有传入的键值对。

##### 8.6 将函数存储在模块中

> `import`允许在当前运行的程序文件中使用o模块中的代码。

- 导入整个模块

将之前编辑的文件创建为模块：

`pizza.py`
```python
def make_pizza(size, *toppings):

print("\ntoppings list:")
print(size)
for topping in toppings:
    print(topping)
```

创建`make_pizzas.py`并导入模块：

```python
# 导入模块
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

即：
```python
# 导入
import module_name

#使用
module_name.function_name()
```

- 导入特定的函数

```python
# 导入模块中的特定函数
from module_name import function_name

# 导入模块中的任意函数
from module_name import function_0, functon_1
```

- 使用`as`给函数指定别名

```python
from module_name import function_name as fn
```

- 使用`as`给模块指定别名

```python
import module_name as mn
```

- 导入模块中的所有函数

```python 
from module_name import *
```

注意：使用`*`导入模块中的所有函数
