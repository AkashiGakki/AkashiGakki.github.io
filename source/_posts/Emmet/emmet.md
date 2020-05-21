---
title: Emmet 使用指南
date: 2019-7-30
category:
    - 杂项
tags: 
    - 杂项
    - 开发技巧
thumbnail: /images/bg-12.jpg

---

#### `Emmet` 使用指南

> `Emment` 是一个可以极大程度提高前端开发效率的工具。它提供了一种十分简练的语法规则，生成对应的 `HTML` 结构和 `CSS` 代码。

<!-- more -->

##### 语法规则

> 首先，你需要记住的是键入缩写后使用 `Tab` 键进行自动补全，生成完整的 `HTML` 标签。

- 输入 `!` 或者 `html:5` 按下 `tab` 键就可以生成一个基本的 `HTML` 结构：

```html
<!DOCTYPE html>
<!-- 语言设置 -->
<html lang="en">
<head>
    <!-- 默认字符集 -->
    <meta charset="UTF-8">
    <!-- 设置默认缩放 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 兼容IE8设置 -->
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

当然，一个最简单的文档结构还可以更简化：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Emmet</title>
</head>
<body>
    
</body>
</html>
```

接下来，便可以进行更多的探索，以下以 `E` 指代一个 `HTML` 标签，通过 `Emmet` 语法，可以实现：

```js
E 代表HTML标签。
E#id 代表id属性。
E.class 代表class属性。
E[attr=foo] 代表某一个特定属性。
E{foo} 代表标签包含的内容是foo。
E>N 代表N是E的子元素。
E+N 代表N是E的同级元素。
E^N 代表N是E的上级元素。
```

一个比较综合的例子：

```js
#page>div.logo+ul#navigation>li*5>a{Item $}
```

按下 `tab` 你就会得到：

```html
<div id="page">
    <div class="logo"></div>
    <ul id="navigation">
        <li><a href="">Item 1</a></li>
        <li><a href="">Item 2</a></li>
        <li><a href="">Item 3</a></li>
        <li><a href="">Item 4</a></li>
        <li><a href="">Item 5</a></li>
    </ul>
</div>
```

##### 基础用法

###### 元素(标签)

> 键入标签名称，按下 `tab` 键，就会得到对应的标签元素。

```js
div
```

```html
<div></div>
```

```js
h3
```

```html
<h3></h3>
```

###### `class`

> 使用点(`.`)生成 `class` 属性。

```js
div.page
```

```html
<div class="page"></div>
```

```js
p.info
```

```html
<p class="info"></p>
```

```js
.header
```

```html
<div class="header"></div>
```

注意：默认不写前面的标签会自动生成一个 `div` 标签。

###### `id`

> 使用 `#` 生成 `id` 标签。

```js
div.footer
```

```html
<div id="footer"></div>
```

一个比较复杂的例子：

```js
div#header+div.page+div#footer.class1.class2.class3
```

```html
<div id="header"></div>
<div class="page"></div>
<div id="footer" class="class1 class2 class3"></div>
```

###### `a`

> 使用 `:` 可以生成一些特殊的属性。

```html
a:link      =>          <a href="http://"></a>
a:blank     =>          <a href="http://" target="_blank" rel="noopener noreferrer"></a>
inp         =>          <input type="text" name="" id="">
input       =>          <input type="text">
input:b 或者 input:button       =>          <input type="button" value="">
input:c 或者 input:checkbox     =>          <input type="checkbox" name="" id="">
input:email                     =>          <input type="email" name="" id="">
input:f 或者 input:file         =>          <input type="file" name="" id="">
input:h 或者 input:hidden       =>          <input type="hidden" name="">
input:p 或者 input:password     =>          <input type="password" name="" id="">
input:r                        =>          <input type="radio" name="" id="">
input:s 或者 input:submit       =>          <input type="submit" value="">
form                 =>          <form action=""></form>
form:get             =>          <form action="" method="get"></form>
form:post            =>          <form action="" method="post"></form>
label                =>          <label for=""></label>
select               =>          <select name="" id=""></select>
select:d             =>          <select name="" id="" disabled="disabled"></select>
bq                   =>          <blockquote></blockquote>
btn 或者 button       =>          <button></button>
btn:d                =>          <button disabled="disabled"></button>
btn:r                =>          <button type="reset"></button>
btn:s                =>          <button type="submit"></button>
```

###### 子标签生成

> 使用 `>` 生成子标签。

```js
div>ul>li
```

```html
<div>
    <ul>
        <li></li>
    </ul>
</div>
```

###### 同级标签生成

> 使用 `+` 生成同级标签。

```js
div+p+bq
```

```html
<div></div>
<p></p>
<blockquote></blockquote>
```

###### 父级标签生成

> 使用 `^` 生成父级标签。

```js
div+div>p>span+em 
```

```html
<div></div>
<div>
    <p><span></span><em></em></p>
</div>
```

一个实例：

```js
div+div>p>span+em^bq
```

```html
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```

更复杂一点的用法：

```js
div+div>p>span+em^^^bq
```

```html
<div></div>
<div>
    <p><span></span><em></em></p>
</div>
<blockquote></blockquote>
```

###### 乘法

> 使用 `*` 生成多个标签。

```js
ul>li*3
```

```html
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

###### 分组

> 使用 `()` 进行分组。

```js
div>(header>ul>li*2>a)+footer>p
```

```html
<div>
    <header>
        <ul>
            <li><a href=""></a></li>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>
```

一个比较复杂的例子：

```js
(div>dl>(dt+dd)*3)+footer>p
```

```html
<div>
    <dl>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
    </dl>
</div>
<footer>
    <p></p>
</footer>
```

###### 属性

> 使用 `[]` 自定义属性

```js
a[href='#' data-title='customer' target='_blank']
```

```html
<a href="#" data-title="customer" target="_blank"></a>
```

###### 编号

> 使用 `$` 进行编号

```js
ul>li.item$*3
```

```html
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
</ul>
```

可以$连续使用多个用零填充数字：

```js
ul>li.item$$$*3
```

```html
<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
</ul>
```

使用 `@` 修改器，可以改变编号起始值。

`@N` 改变起始值：

```js
ul>li.item$@3*5
```

```html
<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>
```

###### 文本

> 使用 `{}` 添加文本。

```js
a{Click me}
```

```html
<a href="">Click me</a>
```

##### 进阶用法

###### 随机填充文本

> 在开发的过程中，常有需要一些文本填充位置占位。 `Emmet` 内置了 `Lorem Ipsum` 功能来实现。`loremN` 或者 `lipsumN` ，`N` 表示生成的单词数，正整数。

```js
lorem
```

```html
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas iusto, incidunt, est facilis quisquam possimus, aliquid provident aperiam sunt numquam a et. Asperiores distinctio explicabo quibusdam accusamus nesciunt, eius autem!
```

```js
(p>lorem4)*3
```

或者：

```js
p*3>lorem4 
```

```html
<p>Lorem ipsum dolor sit.</p>
<p>Voluptatibus cumque quisquam facere!</p>
<p>Error incidunt fugiat explicabo?</p>
```


