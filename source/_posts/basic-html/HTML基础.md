---
title: HTML基础
date: 2019-3-28 20:57:33
category:
    - 前端
    - HTML
thumbnail: /images/bg-2.jpg
layout: about
tags: 
    - HTML
    - 入门教程
    - 前端
grammar_cjkRuby: true

---


### 一、准备工作
---

#### 1.1 开发工具的选择

> 一款好用的编辑器可以让你在撸代码的过程中事半功倍。

- [`VS Code`](https://code.visualstudio.com/)
- [`Sublime text`](https://www.sublimetext.com/)

<!--more-->

==**注意：** 配合`Emmet`自动补全使用，效果更佳。==

#### 1.2 浏览器的选择

> 推荐开发者常用的开发与测试浏览器。

- `Chrome`
- `Firefox`

#### 1.3 HTML实例

- 什么是HTML？

> `HTML` 指的是`超文本标记语言`: `HyperText Markup Language`

```html
<!DOCTYPE html> <!-- 声明这是一个html文档 -->
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>标题</title>
</head>
<body>

	<h1>这里是一个文章标题</h1>
	<p>这里是一个段落</p>

</body>
</html>
```

- 解析
    - `<!DOCTYPE html>` 声明为 `HTML5` 文档
    - `<html>` 是 `HTML` 页面的根元素
    - `<head>` 包含了文档的元`（meta）`数据，如 `<meta charset="utf-8">` 定义网页编码格式为 `utf-8`。
    - `<title>` 描述了文档的标题
    - `<body>` 包含了可见的页面内容
    - `<h1>` 定义一个大标题
    - `<p>` 定义一个段落

### 二、HTML基础
---

#### 2.1 标签（元素）

> 像`<body></body>`这些叫做标签，也称作元素。

```html 
<body>

	<h1>这里是一个文章标题</h1>
	<p>这里是一个段落</p>

</body>
```

#### 2.2 属性

- 实例
    - `HTML` 链接由 `<a>` 标签定义。链接的地址在 `href` 属性中指定

```html
    <a href="https://akashi_sai.gitee.io/"></a>
```
- `eg.`
```html
    <div id="idname" class="classname" name="value"></div>
```

#### 2.3 常用标签

##### 2.3.1 `div`

- 块级元素，独占一行，用于组合其他`HTML`元素的容器。

```html
<div>
    <div>这里是一个容器</div>
</div>
```

##### 2.3.2 `span`

- 内联元素，从左到右排列，可用于文本的容器。

```html
    <span>文本的容器</span>
```

##### 2.3.3 `h1~h6`

- 标题，`<h1>`定义最大标题，`<h6>`定义最小标题。

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Hello</h1>
    <h2>Hello</h2>
    <h3>Hello</h3>
    <h4>Hello</h4>
    <h5>Hello</h5>
    <h6>Hello</h6>
</body>
</html>
```

- 注释，以`<!--`开始，以`-->`结束。

```html
<body>
    <div>
        <!-- 这里是注释内容 -->
    </div>
</body>
```

==**注意：** 良好的注释习惯，可以提高代码的可读性。==

##### 2.3.4 `p`

- 段落，可以将文档分割成若干段落。

```html
    <p>这里是一个段落</p>
    <p>这里是另一个段落</p>
```

##### 2.3.5 `a`

- 链接，可以用来设置超文本链接。

```html
    <a href="https://akashi_sai.gitee.io/"></a>
```

##### 2.3.6 `img`

- 图像，`src` 指 `"source"`。源属性的值是图像的 `URL` 地址。

```html
    <img src="../logo.png" alt="这是一张logo图片">
```

##### 2.3.7 列表

- 无序列表，`ul` > `li`

```html
    <ul>
		<li>Item</li>
		<li>Item</li>
	</ul>
```

- 有序列表，`ol` > `li`

```html
    <ol>
		<li>first item</li>
		<li>second item</li>
	</ol>
```

##### 2.3.8 表格 `table`

- 表格由 `<table>` 标签来定义。每个表格均有`若干行`（由 `<tr>` 标签定义），每行被分割为`若干单元格`（由 `<td>` 标签定义）。字母 `td` 指表格数据`（table data）`，即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

```html
    <table>
        <tr>
            <th>表头1</th>
            <th>表头2</th>
        </tr>
        <tr>
            <td>第一行第一列</td>
            <td>第一行第二列</td>
        </tr>
        <tr>
            <td>第二行第一列</td>
            <td>第二行第二列</td>
        </tr>
    </table>
```

##### 2.3.9 表单 `form`

```html
    <form action="#">
        <fieldset>
        	value: <input type="text">
    	    <button type="submit">Submit</button>
        </fieldset>
    </form>
```

- `input`

```html 
    <input type="text" placeholder="这里是一个输入框">
```

- `button`

```html
    <button>这是一个提交按钮</button>
```

- `textarea`

```html
    <textarea rows="10" cols="30">
        这里是一个文本框
    </textarea>
```

##### 2.3.10 头部

- `<head>`
> `<head>` 元素包含了所有的头部标签元素。在 `<head>`元素中你可以插入脚本`（scripts）`, 样式文件（CSS），及各种meta信息。可以添加在头部区域的元素标签为: `<title>`, `<style>`, `<meta>`, `<link>`, `<script>`.

```html 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
```

- `<title>`

> 定义了不同文档的标题.
```html
<title>Document</title>
```

- `<link>`

> 定义了文档与外部资源之间的关系。通常用于链接到样式表.

```html
<head>
    <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

- `<style>`

> 定义了HTML文档的样式文件引用地址。
```html
<head>
    <style type="text/css">
        body {background-color:yellow}
        p {color:blue}
    </style>
</head>
```

-  `<meta>`

> 描述了一些基本的元数据。元数据也不显示在页面上，但会被浏览器解析。
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
```

`fin`
