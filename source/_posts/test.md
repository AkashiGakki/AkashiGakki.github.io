---
title: 十一、测试代码
date: yyyy-mm-dd
category:
    - Python
tags:
    - python
    
---

#### 十一、代码测试

##### 11.1 测试函数

> 学习测试之前，需要有测试的代码。下面编写一个简单的函数。

<!--more-->

`name_function.py`

```python
def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name
```

`names.py`

```python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("Please give me a last name: :")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("Full name: " + formatted_name)
```

- 单元测试和测试用例

> `Python`标准库中的模块`unittest`提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情况z下的行为都符合要求。

- 可通过的测试

> 创建测试用例的语法需要一段时间才能习惯，但测试用例创建以后，再添加针对函数的单元测试就很简单了。

为函数编写测试用例，可先导入模块`unittest`以及要测试的函数，再创建一个继承 `unittest.TestCase`的类，并编写一系列方法对函数行为的不同方面进行测试。

`test_name_function.py`

```python
import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ 测试name_function.py """

    def test_name_function(self):
        formatted_name = get_formatted_name('akashi', 'sai')
        self.assertEqual(formatted_name, 'akashi sai')

unittest.main()
```

运行：

![test](http://ww1.sinaimg.cn/large/9c62a0cfly1g5aog9loarj20r803ojrf.jpg)

首先，导入了`unittest`模块和测试函数；创建一个NameTestCase的类，可以随便命名，需要继承`unittest.TestCase`；编写函数测试，注意，在测试函数中，所有`test_`打头的方法都会自动运行。

之后使用了一个断言方法，`unittest`类的功能之一。断言方法用来核实得到的结果是否与期望的结果一致。

- 不能通过的测试

修改函数，让其可以出来中间名。先故意不做判断让其一般情况不能通过，查看结果。

```python
def get_formatted_name(first, middle, last):
    full_name = first + " " + middle + " " + last
    return full_name
```

传入的值不变，查看输出：

![error](http://ww1.sinaimg.cn/large/9c62a0cfly1g5aoujn0g3j20r80awmzj.jpg)

其中，`E`指出测试用例中有一个单元测试导致了错误。

- 测试未通过时怎么办

> 测试未通过，意味着编写的代码有错，因此需要修改导致测试不能通过的代码，而不是修改测试。

`name_function.py`

```python
def get_formatted_name(first, last, middle = ''):
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name
```

这样，根据不同的情况，有中间名和没有，函数都可以进行处理了，测试就自然可以通过了。

- 添加新测试

再添加一个测试，用来测试包含中间名的。这时就会发现继续添加函数测试就十分简单和方便了。

```python
import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ 测试name_function.py """

    def test_name_function(self):
        formatted_name = get_formatted_name('akashi', 'sai')
        self.assertEqual(formatted_name, 'akashi sai')

    def test_middle_name_function(self):
        """ 测试包含中间名的姓名 """
        formatted_name = get_formatted_name('portgas', 'ace', 'D')
        self.assertEqual(formatted_name, 'portgas D ace')

unittest.main()
```

![test](http://ww1.sinaimg.cn/large/9c62a0cfly1g5api5vfflj20r804odg8.jpg)

##### 11.2 测试类

- 各种断言方法

方法 | 用途
--- | ---
`assertEqual(a, b)` | 核实 `a == b`
`assertNotEqual(a, b)` | 核实 `a != b`
`assertTrue(x)` | 核实 `x` 为 `True`
`assertFalse(x)` | 核实`x`为`False`
`assertIn(item, list)` | 核实`item`在`lisst`中
`assertNotIn(item, list)` | 核实`item`不在`list`中

- 一个要测试的类

`sruvey.py`

```python
class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []


    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print("- " + response)
```

编写简单的使用程序

`language_survey.py`

```python
from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

- 测试`AnonymousSurvey`类

`test_survey.py`

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

unittest.main()
```

当用户提供三个答案时：

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
```

当然，我们还可以继续提高效率。

- 方法`setUp()`

> `unittest.TestCase`类包含方法`setUp()`，让我们只需创建这些对象一次，并在每个测试方法中使用它们。如果在`TestCast`类中包含了方法 `setUp()`，`Python`会先运行它，然后再运行各个以`test_`打头的方法。

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):

        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```

注意：运行测试用例时，每完成一个单元测试，`Python`都打印一个字符：通过测试时打印一个句点(`.`)；测试引发错误时打印一个`E`；测试导致断言失败打印一个`F`。
