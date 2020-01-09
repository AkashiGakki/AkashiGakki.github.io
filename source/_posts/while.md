---
title: 七、用户输入和while循环
date: yyyy-mm-dd
category:
    - Python
tags:
    - python
    - 入门
    
---

#### 七、用户输入和`while`循环

##### 7.1 `input`函数

- `input`

> 函数`input()`让程序暂停运行，等待用户输入一些文本。获取用户输入后，`Python`将其存储在一个变量中，以方便使用。

<!--more-->

```python
name = input("Please enter your name: ")

print("Hello, " + name.title() +  "!")
```

注意：`input()`接收一个参数，即要向用户显示的提示或说明。

```python
prompt = "If you tell ue who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print("\nHello! " + name.title() + "!")
```

- 使用`int()`来获取数值输入

```python
age = input("How old are you? ")
age = int(age)

print(age >= 18)
```

- 求模运算符

> 可以通过是否被`2`整除判断奇偶。

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")

number = int(number)

if number % 2 == 0:
    print("\nThe nubmer " + str(number) + " is even.")
else:
    print("\nThe nubmer " + str(number) + " is odd.")
```

##### 7.2 `while`循环

- 使用`while`循环

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

- 让用户选择何时退出

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

- 使用标志

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    
    else:
        print(message)
```

- 使用`break`退出循环

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)
```

- 使用`continue`继续下一次循环

```python
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

##### 7.3 使用`while`循环处理列表和字典

- 在列表之间移动元素

```python
unconfirmed_users = ['akashi', 'asuka', 'gakki']

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nconfirmed users: ")
print(confirmed_users)
```

- 删除包含特定值的所有列表元素

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

- 使用用户输入来填充字典

```python
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    age =input("How old are you? ")

    responses[name] = age

    repeat = input("next? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n=== Poll Results ===")
print(responses)
```
