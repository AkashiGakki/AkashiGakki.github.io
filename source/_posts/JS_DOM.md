---
title: JavaScript DOM
date: yyyy-mm-dd
category:
    - 前端
    - JavaScript
tags:
    - 前端
    - JavaScript
    
---

#### `JavaScript` `DOM` 操作

##### `HTML` `DOM`（文档对象模型）

> 当网页被加载时，浏览器会创建页面的文档对象模型（`Document Object Model`）。

- `HTML` `DOM`树

<!--more-->

![DOM](http://ww1.sinaimg.cn/large/9c62a0cfly1g56f6qie3zj216e0ou0ui.jpg)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>My Title</title>
</head>
<body>
    <a href="#">My Link</a>
    <h1>My Header</h1>
</body>
</html>
```

- 通过可编程的对象模型，`JavaScript`可以创建动态的`HTML`。

    - 改变页面中`HTML`的元素
    - 改变页面中`HTML`的属性
    - 改变页面中`CSS`的样式
    - 对页面中的事件做出反应

##### 查找`HTML`元素

- 通过`id`查找

```js
var x = document.getElementById("intro");
```

- 通过标签名查找

```js
var x = document.getElementById("main");
var y = x.getElementsByTagName("p");
```
- 通过类名查找

```js
var x = document.getElementsByClassName("intro");
```

##### 改变`HTML`

- 改变`HTML`输出流

```js
document.write(Date());
```

- 改变`HTML`内容

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1 id="header">Title</h1>
<script>
    var element = document.getElementById('header').innerHTML = 'new title';
</script>
</body>
</html>
```

- 改变`HTML`属性

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <img id="images" src="images/akashi.jpg" alt="images">
<script>
    document.getElementById('images').src = "images/asuka.jpg";
</script>
</body>
</html>
```

##### 改变`CSS`

- 改变`HTML`样式

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Demo</title>
    <style>
        #block {
            width: 200px;
            height: 200px;
            background-color: aqua;
        }
    </style>
</head>
<body>
    <div id="block"></div>
    <p id="p1">Hello!</p>
<script>
    document.getElementById("block").style.backgroundColor = "red";

    document.getElementById("p1").style.color = "red";
    document.getElementById("p1").style.fontFamily = "plantc";
    document.getElementById("p1").style.fontSize = "larger";
</script>
</body>
</html>
```

> 注意：`CSS`属性使用中划线(`-`)分隔，在`JS`中，需要换成`驼峰式`写法。

- 使用事件

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Demo</title>
    <style>
        #block {
            width: 200px;
            height: 200px;
            background-color: aqua;
        }
    </style>
</head>
<body>
    <div id="block" onclick="change()"></div>
<script>
    function change() {
        document.getElementById("block").style.backgroundColor = "yellow";
    }
</script>
</body>
</html>
```

##### `DOM` 事件

- 对事件做出反应

> 在事件发生时执行`JavaScript`，可以完成一系列功能。

`eg`:
    当用户点击鼠标时；
    当网页已加载时；
    当图像已加载时；
    当鼠标移动到元素上时；
    当输入字段被改变时；
    当提交`HTML`表单时；
    当用户触发按键时；
    
- `onload` 和 `onunload` 事件

    - `onload` 和 `onunload` 事件会在用户进入或离开页面时被触发
    - `onload` 事件可用于检测访问者的浏览器类型和浏览器版本，并基于这些信息来加载网页的正确版本
    - `onload` 和 `onunload` 事件可用于处理 `cookie`

- `onchange` 事件

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>onChange</title>
</head>
<body>
<input type="text" id="demo" onchange="change()">
<script>
    function change() {
        var value = document.getElementById("demo").value;
        console.log(value);
        alert(value);
    }
</script>
</body>
</html>
```

注意：点击回车或者离开输入框后事件触发。

另一种写法：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>onChange</title>
</head>
<body>
<input type="text" id="demo" onchange="change(this.value)">
<script>
    function change(obj) {
        console.log(obj);
        alert(obj);
    }
</script>
</body>
</html>
```

> 实现了同样的效果，但第二种写法在一开始就通过`this`获取了输入框的值以实参的方式传入方法。

- `onmouseover` 和 `onmouseout` 事件

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>onmouseover && onmouseout</title>
    <style>
        #block {
        width: 200px;
        height: 200px;
        color: aliceblue;
        background-color: orange;
        text-align: center;
        line-height: 200px;
        font-size: larger;
        }
    </style>
</head>
<body>
    <div id="block" onmouseover="overHandle(this)" onmouseout="outHandle(this)">Try</div>
<script>
    function overHandle(obj) {
        obj.innerHTML = "Over";
    }
    function outHandle(obj) {
        obj.innerHTML = "Out";
    }
</script>
</body>
</html>
```

- `onmousedown`、`onmouseup` 以及 `onclick` 事件

    - 当点击鼠标按钮时，会触发 `onmousedown` 事件
    - 当释放鼠标按钮时，会触发 `onmouseup` 事件
    - 当完成鼠标点击时，会触发 `onclick` 事件
    
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>onChange</title>
    <style>
        #block {
            width: 200px;
            height: 200px;
            background-color: aqua;
        }
    </style>
</head>
<body>
    <div id="block" onclick="clickHandle(this)"></div>
<script>
    function clickHandle(obj) {
        obj.style.backgroundColor = "yellow";
    }
</script>
</body>
</html>
```

##### `DOM` 事件监听

- `addEventListener()` 方法

    - `addEventListener()` 方法用于向指定元素添加事件句柄
    - `addEventListener()` 方法添加的事件句柄不会覆盖已存在的事件句柄
    - 可以向一个元素添加多个事件句柄
    - 可以向同个元素添加多个同类型的事件句柄，如：两个 `"click"` 事件
    
语法：

```js
element.addEventListener(event, function, useCapture);
```

第一个参数是事件的类型 (如 "click" 或 "mousedown";
第二个参数是事件触发后调用的函数(只是函数名，不加括号；加括号是直接调用);
第三个参数是个布尔值用于描述事件是冒泡还是捕获。该参数是可选的。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>eventListener</title>
</head>
<body>
    <button id="btn">Click!</button>
    <p id="demo"></p>
<script>
    document.getElementById("btn").addEventListener("click", displayDate);

    function displayDate() {
        document.getElementById("demo").innerHTML = Date();
    }
</script>
</body>
</html>
```

- 传递参数

> 当传递参数值时，使用`"匿名函数"`调用带参数的函数

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>eventListener</title>
</head>
<body>
    <button id="btn">Click!</button>
<script>
    document.getElementById("btn").addEventListener("click", function() {
        clickHandle(this);
    });

    function clickHandle(obj) {
        console.log(obj);
        obj.innerHTML = Date();
    }
</script>
</body>
</html>
```

- 事件冒泡或事件捕获

> 事件传递有两种方式：冒泡与捕获。

事件传递定义了元素事件触发的顺序。 如果将 `<p>` 元素插入到 `<div>` 元素中，用户点击 `<p>` 元素, 哪个元素的 `"click"` 事件先被触发呢？

在 `冒泡` 中，`内部元素`的事件会`先`被触发，然后再触发外部元素，即： `<p>` 元素的点击事件先触发，然后会触发 `<div>` 元素的点击事件。

在 `捕获` 中，`外部元素`的事件会先被触发，然后才会触发内部元素的事件，即： `<div>` 元素的点击事件先触发 ，然后再触发 `<p>` 元素的点击事件。

`addEventListener()` 方法可以指定 `"useCapture"` 参数来设置传递类型
默认值为 `false`, 即`冒泡传递`，当值为 `true` 时, 事件使用`捕获传递`。

- `removeEventListener()` 方法

```js
element.removeEventListener("click", clickHandle);
```

#####  `DOM` 元素

- 创建新的 `HTML` 元素 (节点)

    - `appendChild()`
    - 添加到元素尾部
    
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="demo">
        <p id="p1">这里是第一个段落</p>
        <p id="p2">这里是第二个段落</p>
    </div>
<script>
    var para = document.createElement("p");
    var node = document.createTextNode("这里是插入的段落");

    para.appendChild(node);

    var element = document.getElementById("demo").appendChild(para);
</script>
</body>
</html>
```
    
- 创建新的 `HTML` 元素 (节点)

    - `insertBefore()`
    - 添加到开始位置

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="demo">
        <p id="p1">这里是第一个段落</p>
        <p id="p2">这里是第二个段落</p>
    </div>
<script>
    var para = document.createElement("p");
    var node = document.createTextNode("这里是插入的段落");

    para.appendChild(node);

    var element = document.getElementById("demo");
    var child = document.getElementById("p2");

    element.insertBefore(para, child);

</script>
</body>
</html>
```
    
- 移除已存在的元素

    - `removeChild()`
    
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="demo">
        <p id="p1">这里是第一个段落</p>
        <p id="p2">这里是第二个段落</p>
    </div>
<script>
    var para = document.createElement("p");
    var node = document.createTextNode("这里是插入的段落");

    para.appendChild(node);

    var element = document.getElementById("demo");
    var child = document.getElementById("p2");

    element.insertBefore(para, child);

    var removeChild = document.getElementById("p1");
    element.removeChild(removeChild);
</script>
</body>
</html>
```

已知要查找的子元素，然后查找其父元素，再删除这个子元素（删除节点必须知道父节点）:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="demo">
        <p id="p1">这里是第一个段落</p>
        <p id="p2">这里是第二个段落</p>
    </div>
<script>
    // 在p中插入内容
    var para = document.createElement("p");
    var node = document.createTextNode("这里是插入的段落");
    para.appendChild(node);
    
    // 将新的段落插入到两个段落之间
    var element = document.getElementById("demo");
    var child = document.getElementById("p2");
    element.insertBefore(para, child);

    // 删除第一个段落
    var reChild = document.getElementById("p1");
    // 利用子节点查找父节点，再通过父节点删除子节点
    reChild.parentNode.removeChild(reChild);
</script>
</body>
</html>
```
    
- 替换 `HTML` 元素

    - `replaceChild()`
    
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="demo">
        <p id="p1">这里是第一个段落</p>
        <p id="p2">这里是第二个段落</p>
    </div>
<script>
    var para = document.createElement("p");
    var node = document.createTextNode("这里是插入的段落");
    para.appendChild(node);

    var element = document.getElementById("demo");
    var child = document.getElementById("p2");

    var reChild = document.getElementById("p1");
    reChild.parentNode.removeChild(reChild);

    // 替换
    element.replaceChild(para, child);
</script>
</body>
</html>
```
