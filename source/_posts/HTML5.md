---
title: H5 笔记整理
date: yyyy-mm-dd
category: 
    - 前端
    - HTML
tags:
    - 前端
    - H5
thumbnail: /images/bg-11.jpg

---

#### `H5` 笔记整理

---

> 整理复习 `H5` 的基础内容。

<!-- more -->

##### 将 `HTML5` 元素定义为块元素

> `HTML5` 定义了 `8` 个新的 `HTML` 语义（`semantic`） 元素。所有这些元素都是 `块级` 元素。

通过设置 `CSS` 的 `display` 属性值为 `block`，让旧版本的浏览器正确显示这些元素：

```css
header, section, footer, aside, nav, main, article, figure {
    display: block; 
}
```

##### 为 `HTML` 添加新元素

通过设置块级元素，还可以自定义 `HTML` 新元素：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Custom</title>
    <script>
        document.createElement("ele");
    </script>
    <style>
        ele {
            display: block;
            background-color: yellow;
            padding: 50px;
            font-family: 'plantc'
        }
    </style>
</head>
<body>
    <ele>自定义元素</ele>
</body>
</html>
```

##### `HTML5` 新元素

- `<canvas>` 新元素

标签 | 描述
--- | ---
`<canvas>` | 标签定义图形，比如图表和其他图像。该标签基于 `JavaScript` 的绘图 `API`

- 新多媒体元素

标签 | 描述
--- | ---
`<audio>`   | 定义音频内容
`<video>`	| 定义视频（`video` 或者 `movie`）
`<source>`	| 定义多媒体资源 `<video>` 和 `<audio>`
`<embed>`	| 定义嵌入的内容，比如插件。
`<track>`	| 为诸如 `<video>` 和 `<audio>` 元素之类的媒介规定外部文本轨道。

- 新表单元素

标签 | 描述
--- | ---
`<datalist>`	| 定义选项列表。请与 `input` 元素配合使用该元素，来定义 `input` 可能的值。
`<keygen>`	| 规定用于表单的密钥对生成器字段。
`<output>`	| 定义不同类型的输出，比如脚本的输出。

- 新的语义和结构元素

> `HTML5` 提供了新的元素来创建更好的页面结构：

标签 | 元素
--- | ---
`<article>` |	定义页面独立的内容区域。
`<aside>` |	定义页面的侧边栏内容。
`<bdi>` |	允许您设置一段文本，使其脱离其父元素的文本方向设置。
`<command>` |	定义命令按钮，比如单选按钮、复选框或按钮
`<details>` |	用于描述文档或文档某个部分的细节
`<dialog>` |	定义对话框，比如提示框
`<summary>` |	标签包含 `details` 元素的标题
`<figure>` |	规定独立的流内容（图像、图表、照片、代码等等）。
`<figcaption>` |	定义 `<figure>` 元素的标题
`<footer>` |	定义 `section` 或 `document` 的页脚。
`<header>` |	定义了文档的头部区域
`<mark>` |	定义带有记号的文本。
`<meter>` |	定义度量衡。仅用于已知最大和最小值的度量。
`<nav>` |	定义导航链接的部分。
`<progress>` |	定义任何类型的任务的进度。
`<ruby>` |	定义 `ruby` 注释（中文注音或字符）。
`<rt>` |	定义字符（中文注音或字符）的解释或发音。
`<rp>` |	在 `ruby` 注释中使用，定义不支持 `ruby` 元素的浏览器所显示的内容。
`<section>` |	定义文档中的节（`section`、区段）。
`<time>` |	定义日期或时间。
`<wbr>` |	规定在文本中的何处适合添加换行符。

需要记住经常使用的标签：`<article>`, `<aside>`, `<footer>`, `<header>`, `<nav>`, `<section>`。

##### `HTML5` `Canvas`

> `<canvas>` 标签定义图形，是一个图形容器，用于图形的绘制，通过脚本 (通常是`JavaScript`)来完成。

###### 创建一个画布（`Canvas`）

注意: 默认情况下 `<canvas>` 元素没有边框和内容。

```html
<canvas id="canvas" style="border: 1px solid black"></canvas>
```

###### 使用 `JavaScript` 来绘制图像

`canvas` 元素本身是没有绘图能力的。所有的绘制工作必须在 `JavaScript` 内部完成：

```js
    // 找到canvas元素
    var c = document.getElementById("canvas");
    // 创建context对象
    var ctx = c.getContext("2d");
    // 设置颜色和填充方式
    ctx.fillStyle = "red";
    ctx.fillRect(0, 0, 150, 150);
```

`getContext("2d")` 对象是内建的 `HTML5` 对象，拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法。

设置`fillStyle`属性可以是`CSS`颜色，渐变，或图案。`fillStyle` 默认设置是`#000000`（黑色）。

`fillRect(x,y,width,height)` 方法定义了矩形当前的填充方式。

###### `Canvas` 坐标

`canvas` 是一个二维网格。

`canvas 的左上角坐标为 `(0,0)`

> `fillRect(0, 0, 150, 150)` 意为从`(0,0)`左上角开始，填充一个`150*150`的矩形。画布默认为`300*150`，如果超出了画布大小，最大以画布为界，溢出部分隐藏。

![canvas](http://ww1.sinaimg.cn/large/9c62a0cfly1g5fm0p16gfj215m07oglf.jpg)

###### `Canvas` 路径

使用`canvas`画线：

- `moveTo(x,y)` 定义线条开始坐标

- `lineTo(x,y)` 定义线条结束坐标

```js
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    // 定义开始坐标(0,0)，结束坐标(200,100)，然后使用stroke() 方法绘制线条
    ctx.moveTo(0, 0);
    ctx.lineTo(200, 100);
    ctx.stroke();
```

在`canvas`中绘制圆形：

```js
arc(x, y, r, start, stop)
```

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Circle</title>
    <style>
        #circle {
            background-color: orange;
        }
    </style>
</head>
<body>
    <canvas id="circle" width="200px" height="200px"></canvas>
<script>
    // 创建context对象
    var ctx = document.getElementById("circle").getContext("2d");

    // 开始一条路径，或重置当前的路径
    ctx.beginPath();

    // 设置线条宽度
    ctx.lineWidth = "2";
    // 设置线条颜色
    ctx.strokeStyle = "pink";

    // 绘制圆 arc(x, y, r, start, stop)
    ctx.arc(100, 100, 90, 0, 2*Math.PI);
    ctx.stroke();
</script>
</body>
</html>
```

###### `Canvas` 文本

使用 `canvas` 绘制文本，重要的属性和方法如下：

- `font` 定义字体

- `fillText(text, x, y)` 在 `canvas` 上绘制实心的文本

- `strokeText(text, x, y)` 在 `canvas` 上绘制空心的文本

实心的文本：

```js
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    ctx.font = "30px Arial";
    ctx.fillText("Akashi", 10, 50);
```

空心的文本：

```js
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    ctx.font = "30px Arial";
    ctx.strokeText("Akashi", 10, 50);
```

###### `Canvas` 渐变

- `createLinearGradient(x, y, x1, y1)`  创建线条渐变

- `createRadialGradient(x, y, r, x1 , y1, r1)`  创建一个径向/圆渐变

> 在使用渐变对象时，必须使用两种或两种以上的停止颜色，`addColorStop()` 方法指定颜色停止，参数使用坐标来描述，可以是 `0` 至 `1` 。

线性渐变：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Gradient</title>
    <style>
        #canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="canvas"></canvas>
<script>
    var ctx = document.getElementById("canvas").getContext("2d");

    // 创建
    var grd = ctx.createLinearGradient(0, 0, 200, 200);
    grd.addColorStop(0, "red");
    grd.addColorStop(1, "white");

    // 填充
    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, 300, 150)
</script>
</body>
</html>
```

径向\圆渐变：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Gradient</title>
    <style>
        #gradient {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="gradient"></canvas>
<script>
    var ctx = document.getElementById("gradient").getContext("2d");

    var grd = ctx.createRadialGradient(150, 75, 0, 150, 75, 100);

    grd.addColorStop(0, "red");
    grd.addColorStop(1, "white");

    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, 300, 150);
</script>
</body>
</html>
```
##### `HTML5` 内联 `SVG`

> `HTML5` 支持内联 `SVG`。

###### 什么是 `SVG`？

`SVG` 指可伸缩矢量图形 (`Scalable Vector Graphics`)
`SVG` 用于定义用于网络的基于矢量的图形
`SVG` 使用 `XML` 格式定义图形
`SVG` 图像在放大或改变尺寸的情况下其图形质量不会有损失
`SVG` 是万维网联盟的标准

###### `SVG` 优势

与其他图像格式相比（比如 `JPEG` 和 `GIF`），使用 `SVG` 的优势在于：

`SVG` 图像可通过文本编辑器来创建和修改
`SVG` 图像可被搜索、索引、脚本化或压缩
`SVG` 是可伸缩的
`SVG` 图像可在任何的分辨率下被高质量地打印
`SVG` 可在图像质量不下降的情况下被放大

###### `Canvas` 与 `SVG` 的比较

`Canvas` | `SVG`
---| ---
依赖分辨率 | 不依赖分辨率
不支持事件处理器 | 支持事件处理器
弱的文本渲染能力 | 最适合带有大型渲染区域的应用程序（比如谷歌地图）
能够以 .png 或 .jpg 格式保存结果图像 | 复杂度高会减慢渲染速度（任何过度使用 DOM 的应用都不快）
最适合图像密集型的游戏，其中的许多对象会被频繁重绘 | 不适合游戏应用

##### `HTML5` 拖放（`Drag` 和 `Drop`）

###### 设置元素可拖放

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Drag_Drop</title>
    <style>
        img {
            width: 100px;
            height: auto;
            border: 1px solid black;
            margin: 10px;
        }

        #container {
            border: 1px solid black;
            width: 120px;
            min-height: 170px;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div id="container" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
    <img id="asuka" src="./asuka.jpg" alt="asuka" draggable="true" ondragstart="drag(event)">
<script>
    function allowDrop(event) {
        event.preventDefault();
    }

    function drag(event) {
        event.dataTransfer.setData("Text", event.target.id);
    }

    function drop(event) {
        event.preventDefault();
        var data = event.dataTransfer.getData("Text");
        event.target.appendChild(document.getElementById(data));
    }
</script>
</body>
</html>
```

首先，要设置元素是可以被拖放的，把 `draggable` 属性设置为 `true` ：

```html
<img draggable="true">
```

###### 定义元素被拖动时事件

- `ondragstart`

- `setData()`

`ondragstart` 属性调用了一个函数，`drag(event)`，它规定了被拖动的数据。

`dataTransfer.setData()` 方法设置被拖数据的数据类型和值：

```js
function drag(ev) {
    ev.dataTransfer.setData("Text", ev.target.id);
}
```

##### 设置元素拖放后事件

`ondragover` 事件规定在何处放置被拖动的数据。

默认地，无法将数据/元素放置到其他元素中。如果需要设置允许放置，我们必须阻止对元素的默认处理方式。

这要通过调用 `ondragover` 事件的 `event.preventDefault()` 方法：

```js
ev.preventDefault()
```

##### 进行放置

当放置被拖数据时，会发生 `drop` 事件

```js
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(data));
}
```

注释：

- 调用 `preventDefault()` 来避免浏览器对数据的默认处理（`drop` 事件的默认行为是以链接形式打开）
- 通过 `dataTransfer.getData("Text")` 方法获得被拖的数据。该方法将返回在 `setData()` 方法中设置为相同类型的任何数据。
- 被拖数据是被拖元素的 `id ("asuka")`
- 把被拖元素追加到放置元素（目标元素）中

##### `HTML5` `Video`(视频)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Video</title>
</head>
<body>
    <video id="video" width="500px" controls>
        <source src="./gakki.mp4" type="video/mp4">
    </video>
    <div>
        <button onclick="playControl()">播放/暂停</button>
    </div>
</body>
<script>
    var video = document.getElementById("video");
    function playControl() {
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
    }
</script>
</html>
```

###### 可选属性

属性 | 值 | 描述
--- | --- | ---
`autoplay` |	`autoplay` |	如果出现该属性，则视频在就绪后马上播放。
`controls` |	`controls` |	如果出现该属性，则向用户显示控件，比如播放按钮。
`height` |	`pixels` |	设置视频播放器的高度。
`loop` |	`loop` |	如果出现该属性，则当媒介文件完成播放后再次开始播放。
`muted` |	`muted` |	如果出现该属性，视频的音频输出为静音。
`poster` |	`URL` |	规定视频正在下载时显示的图像，直到用户点击播放按钮。
`preload` |	`auto` `metadata` `none` |	如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "`autoplay`"，则忽略该属性。
`src` |	`URL` | 	要播放的视频的 `URL`。
`width` |	`pixels` |	设置视频播放器的宽度。

##### `HTML5` `Audio` (音频)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Audio</title>
</head>
<body>
    <audio id="audio" controls>
        <source src="./aimer.mp3">
    </audio>
    <div>
        <button onclick="playControl()">播放/暂停</button>
    </div>
<script>
    var audio = document.getElementById("audio");
    // 设置自动播放
    audio.play();
    
    function playControl() {
        if (audio.paused) {
            audio.play();
        } else {
            audio.pause();
        }
    }
</script>
</body>
</html>
```

###### 可选属性

属性 | 值 | 描述
--- | --- | ---
`autoplay` | 	`autoplay` |	如果出现该属性，则音频在就绪后马上播放。
`controls` |	`controls` |	如果出现该属性，则向用户显示音频控件（比如播放/暂停按钮）。
`loop` |	`loop` |	如果出现该属性，则每当音频结束时重新开始播放。
`muted` |   `muted`	 |  如果出现该属性，则音频输出为静音。
`preload` | 	`auto` `metadata` `none`	|    规定当网页加载时，音频是否默认被加载以及如何被加载。
`src` |	`URL` |	规定音频文件的 `URL`。

##### `HTML5` 语义元素

> 语义元素可以清楚地描述标签的意义，方便开发者的开发和浏览器的识别。

###### `<section>`

> `<section>` 标签定义文档中的节（`section`、区段）。比如章节、页眉、页脚或文档中的其他部分。

###### `<article>`

> `<article>` 标签定义独立的内容。

###### `<nav>`

> `<nav>` 标签定义导航链接的部分。

###### `<aside>`

> `<aside>` 标签定义页面主区域内容之外的内容（比如侧边栏）。

###### `<header>`

> `<header>`元素描述了文档的头部区域，主要用于定义内容的介绍展示区域。

###### `<footer>`

> `<footer>` 元素描述了文档的底部区域。

###### `<figure>` 和 `<figcaption>`

> `<figure>` 标签规定独立的流内容（图像、图表、照片、代码等等）。

`<figure>` 元素的内容应该与主内容相关，但如果被删除，则不应对文档流产生影响。

 > `<figcaption>` 标签定义 `<figure>` 元素的标题.

`<figcaption>` 元素应该被置于 "`figure`" 元素的第一个或最后一个子元素的位置。
