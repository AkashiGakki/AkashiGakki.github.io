---
title: Python 解析库的使用
date: yyyy-mm-dd
category: 
    - Python
    - 工具
tags:
    - Python
    - 工具
thumbnail: /images/bg-40.jpg

---

#### `Python` 解析库的使用

> `lxml`、`Beautiful Soup` 和 `pyquery` 的使用。

<!-- more -->

##### `XPath`

###### `XPath` 常用规则

表达式 | 描述
--- | ---
`nodename` | 选取此节点的所有子节点
`/` | 从当前节点选取直接子节点
`//` | 从当前节点选取子孙节点
`.` | 选取当前节点
`..` | 选取当前节点的父节点
`@` | 选取属性

###### 实例引入

`eg`:

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item">
            <a href="link.html">item</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
```

###### 所有节点

使用 `//` 开头的 `XPath` 规则来匹配所有符合要求的节点

`eg`:

```python
import requests
from lxml import etree

url = 'https://akashigakki.github.io'
response = requests.get(url)
html = etree.HTML(response.text)
result = html.xpath('//div')
print(result)
```

###### 子节点

使用 `/` 匹配子节点

`eg`:

```python
import requests
from lxml import etree

url = 'https://akashigakki.github.io'
response = requests.get(url)
html = etree.HTML(response.text)
result = html.xpath('//div/span')
print(result)
```

###### 父节点

使用 `..` 匹配获取父节点

`eg`:

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item">
            <a href="link.html">item</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li/a/../@class')
print(result)
```

也可以通过 `parent::` 来获取

`eg`:

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item">
            <a href="link.html">item</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li/a/parent::*/@class')
print(result)
```

###### 属性匹配

使用 `@` 进行属性过滤

`eg`:

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li/a[@class="item"]')
print(result)
```

以上 `xpath` 只有 `class` 是 `item` 的 `a` 标签可以匹配到，结果只有一个节点。

###### 文本获取

使用 `text()` 进行文本获取

`eg`:

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li/a[@class="item"]/text()')
print(result)
```

###### 属性获取

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li/a/@href')
print(result)
```

###### 属性多值匹配

使用 `contains()` 函数

如果一个节点的 `class` 属性有两个值，那么就无法通过属性匹配来获取了：

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item li-first">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li[@class="item"]/a/@href')
print(result)
```

输出为 `[]`

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item li-first">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "item")]/a/@href')
print(result)
```

这种方式在某个节点的某个属性有多个值时经常用到。

###### 多属性匹配

使用 `and`

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item li-first" name="li">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "item") and @name="li"]/a/@href')
print(result)
```

其他运算符介绍：

运算符 | 描述 | 实例 | 返回值
--- | --- | --- | ---
`or` | 或 | `age=19 or age=20` | `true/false`
`and` | 与 | `age>19 and age<21` | `true/false`
`mod` | 计算除法的余数 | `5 mod 2` | 余数
`|` | 计算两个节点集 | `//book | //cd` | 返回所有拥有 `book` 和 `cd` 元素的节点集
`+` | 加法 | `6 + 4` | 对应值
`-` | 减法 | `6 - 4` | 对应值
`*` | 乘法 | `6 * 4` | 对应值
`div` | 除法 `8 div 4` | 对应值
`=` | 等于 | `age=19` | `true/false`
`!=` | 不等于 | `age!=19` | `true/false`
`<` | 小于 | `age<19` | `true/false`
`<=` | 小于等于 | `age<=19` | `true/false`
`>` | 大于 | `age>19` | `true/false`
`>=` | 大于等于 | `age>=19` | `true/false`


###### 按序选择

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item li-first" name="li">
            <a href="link.html">item_1</a>
            <a class="item">item_2</a>
        </li>
    </ul>
</div>
'''

html = etree.HTML(text)
result_1 = html.xpath('//li/a[last()]/text()')
result_2 = html.xpath('//li/a[position()=1]/text()')
print(result_1)
print(result_2)
```

具体参考 `http://www.w3cschool.com.cn/xpath/xpath_functions.asp`

##### `Beautiful Soup`

###### 基本用法

```python
import requests
from bs4 import BeautifulSoup

url = 'https://akashigakki.github.io/'
response = requests.get(url=url)
html = response.text

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify)
print(soup.title.string)
```

`Beautiful Soup` 在使用时依赖于解析器，它除了支持 `Python` 标准库中的 `HTML` 解析器外(`html.parser`)，还支持第三方解析器如 `lxml` 和 `xml` 等。

初始化时，把第二个参数设置为解析器，如 `soup = BeautifulSoup(html, 'lxml')`

###### 节点选择器

- 选择元素

```python
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
    <p class='item'>Akashi</p>
    <a href='https://example.com' class='site'>site_1</a>
    <a href='https://example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(soup.title.string)
print(soup.p)
```

输出：

```html
<title>The Title</title>
The Title
<p class="item">Akashi</p>
```

- 提取信息

(1) 获取节点名称

```python
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
    <p class='item'>Akashi</p>
    <a href='https://example.com' class='site'>site_1</a>
    <a href='https://example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)
```

输出： `title`

(2) 获取属性

```python
rom bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
    <p class='item'>Akashi</p>
    <a href='https://example.com' class='site'>site_1</a>
    <a href='https://example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.p.attrs)
print(soup.p.attrs['class'])
```

输出： 

```json
{'class': ['item']}
['item']
```

- 嵌套选择

```python
rom bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
    <p class='item'>Akashi</p>
    <a href='https://example.com' class='site'>site_1</a>
    <a href='https://example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
```

输出： `<title>The Title</title>`

- 关联选择

(1) 子节点和子孙节点

选取节点元素之后，如果想要获取它的直接子节点，可以调用 `contents` 属性

如果想要获取所有的子孙节点，可以使用 `children` 来获取

```python
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
<div>
    <p class='item'>Akashi</p>
    <a href='https://r1.example.com' class='site'>site_1</a>
    <a href='https://r2.example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.div.contents)
print(soup.div.children)
for item in soup.div.children:
    print(item)
```

输出：

```html
['\n', <p class="item">Akashi</p>, '\n', <a class="site" href="https://r1.example.com">site_1</a>, '\n', <a class="site" href="https://r2.example.com">site_2</a>, '\n']

<list_iterator object at 0x1018f5810>


<p class="item">Akashi</p>


<a class="site" href="https://r1.example.com">site_1</a>


<a class="site" href="https://r2.example.com">site_2</a>
```

(2) 父节点和祖先节点

如果想要获取某个节点元素的父节点，可以使用 `parent` 属性

如果想要获取所有的祖先节点，可以使用 `parents` 属性

(3) 兄弟节点

如果想要获取同级节点，可以使用 `netx_sibling` 获取下一个兄弟元素，`previous_sibling` 获取上一个兄弟元素

使用 `next_siblings` 返回所有后面的兄弟节点，使用 `previous_sibling` 返回所有前面的兄弟节点

(4) 提取信息

调用 `string` 和 `attrs` 等属性获得其文本和属性

###### 方法选择器

- `find_all()`

> 查询所有符合条件的元素

(1) `name`

```python
soup.find_all(name='li')
```

(2) `attrs`

```python
soup.find_all(attrs={
    'id': 'list-1'
})
```

```python
soup.find_all(id='list-`')
soup.fin_all(class_='element')
```

(3) `text`

```python
soup.find_all(text=re.compile('link'))
```

- `find`

> 匹配一个元素，参数与 `find_all` 一致

其他方法：

`find_parents()`、`find_parent()`、`find_next_sibling()`、`find_next_siblings()`、`find_previous_sibling()`、`find_previous_siblings()`

###### `CSS` 选择器

```python
# import requests
# from bs4 import BeautifulSoup

# url = 'https://akashigakki.github.io/'
# response = requests.get(url=url)
# html = response.text

# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify)
# print(soup.title.string)

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
<div>
    <p class='item'>Akashi</p>
    <a href='https://r1.example.com' class='site'>site_1</a>
    <a href='https://r2.example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.select('a'))
```

输出：

```html
[<a class="site" href="https://r1.example.com">site_1</a>, <a class="site" href="https://r2.example.com">site_2</a>]
```

- 嵌套选择

```python
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Title</title></head>
<body>
<div>
    <p class='item'>Akashi</p>
    <a href='https://r1.example.com' class='site'>site_1</a>
    <a href='https://r2.example.com' class='site'>site_2</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
for div in soup.select('div'):
    print(soup.select('a'))
```

- 属性获取

```python
soup = BeautifulSoup(html, 'lxml')
for a in soup.select('a'):
    print(a['class'])
    print(a.attrs['class'])
```

- 文本获取

```python
soup = BeautifulSoup(html, 'lxml')
for a in soup.select('a'):
    print(a.get_text())
    print(a.string)
```

##### `pyquery`

> 如果使用 `jQuery` 操作 `css` 选择器比较熟悉，那么使用起 `pyquery` 就会非常顺手了，因为它们的语法基本是一样的。

###### 初始化

```python
import requests
from pyquery import PyQuery as pq

url = 'https://akashigakki.github.io'
html = requests.get(url=url)
doc = pq(html.text)
print(doc('title'))
```

###### 基本 `css` 选择器

使用起来和 `jQuery` 完全相同，如：

```python
doc('#container .list li')
```

以上分别为 `id` 选择器、`class` 选择器和标签选择器。

###### 查找节点

- 需要查找子节点时，使用 `find()` 方法

`eg`:

```python
doc = pq(html)
items = doc('.list')
lis = items.find('li')
```

`find()` 方法会返回符合条件的所有子孙节点，如果只是查找子节点，可以使用 `children()`

`eg`:

```python
lis = items.children('.active')
```

- 使用 `parent()` 获取某个节点的父节点

`eg`:

```python
doc = pq(html)
items = doc('.list')
contaier = items.parent()
```

如果想获取所有祖先节点，使用 `parents()` 方法

`eg`:

```python
container = items.parents()
```

- 获取兄弟节点 `siblings()`

`eg`:

```python
doc = pq(html)
li = doc('.list')
print(li.siblings())
```

如果需要筛选，还可以继续传入参数：

```python
print(li.siblings('.active'))
```

###### 获取信息

- 获取属性

`eg`:

```python
doc = pq(html)
a = doc('.item a')
print(a.attr('href'))
print(a.attr.href)
```

以上两种方式都可以获取属性。

- 获取文本

使用 `text()` 来实现

`eg`:

```python
print(a.text())
```

也可以使用 `html()` 获取 `HTML` 文本

`eg`:

```python
print(a.html())
```

###### 节点操作

- `addClass` 和 `removeClass`

可以对节点进行动态修改

- `attr`、`text` 和 `html`

对节点的内容进行修改

- `remove()`

移除

###### 伪类选择器

`eg`:

```python
doc = pq(html)
li = doc('li:first-child')
li = doc('li:last-child')
li = doc('li:nth-child(2)')
```

依次选择了第一个 `li` 节点、最后一个 `li` 节点和第二个 `li` 节点。
