---
title: CSS基础
date: 2019-3-29 00:03:45
category: 
    - 前端
    - CSS
tags: 
    - 前端
    - 入门教程
    - CSS
thumbnail: /images/bg-3.jpg
grammar_cjkRuby: true

---


### 一、什么是CSS？
---

> CSS 指层叠样式表 (Cascading Style Sheets)， 用于控制网页的样式和布局。

<!-- more -->

#### 1.1 CSS基本语法

选择器 {
    属性: 值;
    属性: 值;
}

```css
body{
    background-color: red;
}
```

#### 1.2 CSS的三种引入方式

- 外部样式表(External style sheet)
    - 即`link`中的`href`属性，引用外部`css`文件

```html
<head>
     <link rel="stylesheet" href="./app.css">
</head>
```

- 内部样式表(Internal style sheet)
    - 在`head`中的`style`标签中引用

```html
<head>
    <style>
        body{
            background-color: red;
        }
    </style>
</head>
```

- 内联样式(Inline style)
    - 在标签中直接使用`style`属性

```html
<div style="background-color:red;">
      <p>Hello world!</p>
 </div>
```

##### 1.3 三种基础选择器

- 标签选择器
    - 直接接标签名
- `class`选择器
    - 以`.`开头，接`class`名
- `id`选择器
    - 以`#`开头，接`id`名

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
    body{
        background-color: red;
    }
    .box{
        margin: 10px;
        width: 100px;
        height: 100px;
        background-color: white;
    }
    #con{
        width: 50px;
        height: 50px;
        background-color: yellow;
    }
    </style>
</head>
<body>
    <div class="box"></div>
    <div id="con"></div>
</body>
</html>
```

### 二、常见属性
---

#### 2.1 `background`

> CSS 背景属性用于定义HTML元素的背景。

- `background-color`
    - 背景颜色
- `background-image`
    - 背景图片
- `background-repeat`
    - 背景图像水平或垂直平铺
- `background-position`
    - 设置定位
- 简写
```css
body {
    background:#ffffff url('img_tree.png') no-repeat right top;
}
```

#### 2.2 `文本`

- `color`
    - 设置文字颜色
    - 十六进制值 如: `＃FF0000`
    - 一个RGB值 如: `RGB(255,0,0)`
    - 颜色的名称 如: `red`

```css
h1 {
    color: red;
}
```

- `text-align`
    - 设置对齐方式

```css
p {
    text-align: center;
}
```

- `text-decoration`
    - 设置文本装饰

```css
a {
    text-decoration: none;
}
```

#### 2.3 `字体`

- `font-size`
    - 设置文本的字体大小

```css
p {
    font-size:14px;
}
```

- `font-family`
    - 设置文本的字体系列

```css
p {
    font-family:"Times New Roman", Times, serif;
}
```

#### 2.4 `链接`

```css
    a:link {
        color:#000000;  /* 未访问链接*/
    }
    a:visited {
        color:#00FF00;  /* 已访问链接 */
    } 
    a:hover {
        color:#FF00FF;  /* 鼠标移动到链接上 */
    } 
    a:active {
        color:#0000FF;  /* 鼠标点击时 */
    } 
}
```

#### 2.5 `列表`

- `list-style`
    - 设置列表样式

```css
ul {
    list-style: none;
}
```

#### 2.6 `盒子模型`

> 所有的HTML元素可以看作是一个盒子，CSS盒模型本质上是一个盒子，封装周围的HTML元素，它包括：边距，边框，填充，和实际内容。

![盒子模型](http://ws1.sinaimg.cn/large/9c62a0cfgy1g1lur8b9lyj20mq0clgm0.jpg)

- `Margin(外边距)`
    - 清除边框外的区域，外边距是透明的。
- `Border(边框)`
    - 围绕在内边距和内容外的边框。
- `Padding(内边距)` 
    - 清除内容周围的区域，内边距是透明的。
- `Content(内容)`
    - 盒子的内容，显示文本和图像。

#### 2.7 `边框`

> CSS边框属性允许你指定一个元素边框的样式和颜色。

![边框属性](http://ws1.sinaimg.cn/large/9c62a0cfgy1g1luw7j1f6j20yq0bimx8.jpg)

- 属性
    - `border-width`
    - `border-style` (required)
    - `border-color`
- 简写

```css
p {
    border:5px solid red;
}
```
#### 2.8 `margin 外边距`

> CSS margin(外边距)属性定义元素周围的空间。margin 清除周围的（外边框）元素区域。margin 没有背景颜色，是完全透明的。

![margin](http://ws1.sinaimg.cn/large/9c62a0cfgy1g1lv3goxnrj20p30cnwf0.jpg)

- 属性

```css
section {
    margin-top:100px;
    margin-bottom:100px;
    margin-right:50px;
    margin-left:50px;
}
```

- 简写

```css
section {
    margin: 100px 50px;
}
```

#### 2.9 `padding 填充`

> CSS padding 定义元素边框与元素内容之间的空间，即上下左右的内边距。当元素的 padding（填充）内边距被清除时，所释放的区域将会受到元素背景颜色的填充。

![padding](http://ws1.sinaimg.cn/large/9c62a0cfgy1g1lv3goxnrj20p30cnwf0.jpg)

- 属性

```css
section {
    padding-top:25px;
    padding-bottom:25px;
    padding-right:50px;
    padding-left:50px;
}
```

- 简写

```css
section {
    padding:25px 50px;
}
```

#### 2.10 `position 定位`

> position 属性指定了元素的定位类型。

- 属性
    - `static`
        - HTML 元素的默认值，即没有定位，遵循正常的文档流对象。
        - 静态定位的元素不会受到 `top`, `bottom`, `left`, `right`的影响。
    - `relative`
        - 相对定位元素是相对自己本身所在的位置进行定位的。
    - `fixed`
        - 元素的位置相对于浏览器窗口是固定位置。
        - 即使窗口是滚动的它也不会移动。
    - `absolute`
        - 绝对定位的元素的位置相对于最近的已定位父元素，如果元素没有已定位的父元素，那么它的位置相对于`<html>`。
    - `sticky`
        - 基于用户的滚动位置来定位。
- 重叠元素
    - 元素的定位与文档流无关，所以它们可以覆盖页面上的其它元素
    - `z-index`属性指定了一个元素的堆叠顺序（哪个元素应该放在前面，或后面）

```css
img {
    position:absolute;
    left:0px;
    top:0px;
    z-index:-1;
}
```

#### 2.11 `overflow 溢出`

> CSS overflow 属性用于控制内容溢出元素框时显示的方式。

- 属性
    - `visible`
        - 默认值。内容不会被修剪，会呈现在元素框之外。
    - `hidden`
        - 内容会被修剪，并且其余内容是不可见的。
    - `scroll`
        - 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
    - `auto`
        - 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
    - `inherit`
        - 规定应该从父元素继承 overflow 属性的值。

#### 2.12 `float 浮动 `

> CSS 的 Float（浮动），会使元素向左或向右移动，其周围的元素也会重新排列。

**注意：** 一个浮动元素会尽量向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止。

- `eg`.

```css
img {
    float:left;
}
```
- 清除浮动

> 元素浮动之后，周围的元素会重新排列，为了避免这种情况，使用 clear 属性。clear 属性指定元素两侧不能出现浮动元素。

- `eg`.

```css
.text_line {
    clear:both;
}
```

#### 2.13 `组合`

> 	组合选择符说明了两个选择器直接的关系。CSS组合选择符包括各种简单选择符的组合方式。

- 组合方式
    - 后代选择器(以空格分隔)
    - 子元素选择器(以大于号分隔）
    - 相邻兄弟选择器（以加号分隔）
    -普通兄弟选择器（以破折号分隔）

- 后代选择器
    - 后代选择器用于选取某元素的后代元素。

```css
div p {
    background-color: yellow;
}

```
**注意：** 实例选取了所有`<div>`中的`<p>`元素

- 子元素选择器
    - 与后代选择器相比，子元素选择器`（Child selectors）`只能选择作为某元素子元素的元素。

```css
div>p {
    background-color: yellow;
}
```
**注意：** 实例选择了`<div>`元素中所有直接子元素 `<p>`

- 相邻兄弟选择器
    - 相邻兄弟选择器`（Adjacent sibling selector）`可选择紧接在另一元素后的元素，且二者有相同父元素。

```css
div+p {
    background-color: yellow;
}
```
**注意：** 实例选取了所有位于 `<div>` 元素后的第一个 `<p>` 元素

- 后续兄弟选择器
    - 后续兄弟选择器选取所有指定元素之后的相邻兄弟元素。

```css
div~p {
    background-color: yellow;
}
```
**注意：** 实例选取了所有 `<div>` 元素之后的所有相邻兄弟元素 `<p>`
#### 2.14 `伪类`

- 例如`:hover`, `:link`, `:first-child`被称作伪类

- `:hover`
    - 当鼠标悬停时，显示样式

```css
a:hover {
    background-color:#FF704D;
}
```

- `:first-child`
    - 选择父元素的第一个子元素

```css
p:first-child {
    color:blue;
}
```

`fin`
