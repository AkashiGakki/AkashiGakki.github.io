---
title: JQuery DOM 操作（上）
date: 2019-7-23
category:
    - 前端
    - JavaScript
tags:
    - 前端
    - JavaScript
thumbnail: /images/bg-5.jpg

---

#### JQuery DOM 操作（上）

##### 什么是`JQuery`

> `jQuery`是一个轻量级的`JavaScript`库，它极大地简化了`JavaScript`编程。

<!--more-->

`jQuery`包含以下功能：

- `HTML`元素选取
- `HTML`元素操作
- `CSS`操作
- `HTML`事件函数
- `JavaScript`特效和动画
- `HTML` `DOM`遍历和修改
- `AJAX`
- `Utilities`

##### 使用

- 官网下载导入

    - `https://jquery.com/download/`

- `CDN` 载入`jQuery`

    - `https://www.bootcdn.cn/jquery/`
    
##### 语法

> `jQuery` 语法是通过选取 `HTML` 元素，并对选取的元素执行某些操作。

基础语法：

```js
$(selector).action()
```

通过美元符号(`$`)定义`jQuery`。

- 文档就绪事件

> 为了防止文档在完全加载（就绪）之前运行 `jQuery` 代码，即在 `DOM` 加载完成后才可以对 `DOM` 进行操作。如果在文档没有完全加载之前就运行函数，操作可能失败。

```js
$(document).ready(function(){
    // 函数体
});
```

简洁写法：

```js
$(function() {
    // 函数体
});
```

##### 选择器

> `jQuery`选择器可以快速选择`HTML`元素进行操作。

- 元素选择器

    - 基于元素名选取元素

```js
$(document).ready(function(){
    $("button").click(function(){
        $("p").hide();
    });
});
```

- `id`(`#`)选择器

    - 基于`id`选取元素
    
```js
$(document).ready(function(){
    $("button").click(function(){
        $("#test").hide();
    });
});
```

- `class`(`.`)选择器

    - 基于`class`选取元素
    
```js
$(document).ready(function(){
    $("button").click(function(){
        $(".test").hide();
    });
});
```

##### 事件

> 事件，即页面对访问者的响应。

常见`DOM`事件

鼠标事件 | 键盘事件 | 表单事件 | 文档/窗口事件
--- | --- | --- | ---
click  |  keypress  |  submit  |  load
dblclick  |  keydown  |  change  |  resize
mouseenter  |  keyup  |  focus  |  scroll
mouseleave   |    |  blur  |  unload
hover|

- 事件方法

点击事件`click()`

```js
$("p").click(function(){
    $(this).hide();
});
```

双击事件`dblclick()`

```js
$("p").dblclick(function(){
    $(this).hide();
});
```

鼠标进入`mouseenter()`

鼠标离开`mouseleave()`

按下鼠标`mousedown()`

松开鼠标`mouseup()`

光标悬停`hover()`

元素获得焦点`focus()`

元素失去焦点`blur()`

> 使用方式大体相同，具体实现效果根据需求使用。

#### `jQuery`效果

##### 显示/隐藏

> 通过 `jQuery`，可以使用 `hide()` 和 `show()` 方法来隐藏和显示 `HTML` 元素。

```js
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Show and Hide</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <p>这里是显示/隐藏的文字。</p>
    <button id="show">显示</button>
    <button id="hide">隐藏</button>
<script>
    $(function() {
        // 隐藏
        $("#hide").click(function() {
            $("p").hide();
        });
        // 显示
        $("#show").click(function() {
            $("p").show();
        });
    });
</script>
</body>
</html>
```

语法：

```js
$(selector).hide(speed,callback);

$(selector).show(speed,callback);
```

可选的 `speed` 参数规定隐藏/显示的速度，可以取以下值：`"slow"`、`"fast"` 或毫秒。

可选的 `callback` 参数是隐藏或显示完成后所执行的函数名称。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Show && Hide</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <p>这里是显示/隐藏的文字。</p>
    <button>Hide</button>
<script>
    $(function() {
        $("button").click(function() {
            $("p").hide(1000, alertHandle);
        });

        function alertHandle() {
            alert("文字被隐藏！");
        }
    });
</script>
</body>
</html>
```

> 通过 `jQuery`，还可以使用 `toggle()` 方法来切换 `hide()` 和 `show()` 方法。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Show && Hide</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <p>这里是显示/隐藏的文字。</p>
    <button>Show/Hide</button>
<script>
    $(function() {
        $("button").click(function() {
            $("p").toggle(1000);
        });
    });
</script>
</body>
</html>
```

##### 淡入淡出

- `fadeIn()`

> `jQuery` `fadeIn()` 用于淡入已隐藏的元素。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Fade</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div {
            width: 100px;
            height: 100px;
            display: none;
            margin: 30px;
        }

        #red {
            background-color: red;
        }

        #orange {
            background-color: orange;
        }

        #yellow {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <button>Control</button>
    <div id="red"></div>
    <div id="orange"></div>
    <div id="yellow"></div>
<script>
    $(function() {
        $("button").click(function() {
            $("#red").fadeIn();
            $("#orange").fadeIn("slow");
            $("#yellow").fadeIn(1200);
        });
    });
</script>
</body>
</html>
```

语法:

```js
$(selector).fadeIn(speed,callback);
```

- `fadeOut()`

> `jQuery` `fadeOut()` 方法用于淡出可见元素。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Fade</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div {
            width: 100px;
            height: 100px;
            margin: 30px;
        }

        #red {
            background-color: red;
        }

        #orange {
            background-color: orange;
        }

        #yellow {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <button>Control</button>
    <div id="red"></div>
    <div id="orange"></div>
    <div id="yellow"></div>
<script>
    $(function() {
        $("button").click(function() {
            $("#red").fadeOut();
            $("#orange").fadeOut("slow");
            $("#yellow").fadeOut(1200);
        });
    });
</script>
</body>
</html>
```

语法:

```js
$(selector).fadeOut(speed,callback);
```

- `fadeToggle()`

> `jQuery` `fadeToggle()` 方法可以在 `fadeIn()` 与 `fadeOut()` 方法之间进行切换。

如果元素已淡出，则 `fadeToggle()` 会向元素添加淡入效果。

如果元素已淡入，则 `fadeToggle()` 会向元素添加淡出效果。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Fade</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div {
            width: 100px;
            height: 100px;
            margin: 30px;
        }

        #red {
            background-color: red;
        }

        #orange {
            background-color: orange;
        }

        #yellow {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <button>Control</button>
    <div id="red"></div>
    <div id="orange"></div>
    <div id="yellow"></div>
<script>
    $(function() {
        $("button").click(function() {
            $("#red").fadeToggle();
            $("#orange").fadeToggle("slow");
            $("#yellow").fadeToggle(1200);
        });
    });
</script>
</body>
</html>
```

语法:

```js
$(selector).fadeToggle(speed,callback);
```

- `fadeTo()`

> `jQuery` `fadeTo()` 方法允许渐变为给定的不透明度（值介于 `0` 与 `1` 之间）。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Fade</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div {
            width: 100px;
            height: 100px;
            margin: 30px;
        }

        #red {
            background-color: red;
        }

        #orange {
            background-color: orange;
        }

        #yellow {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <button>Control</button>
    <div id="red"></div>
    <div id="orange"></div>
    <div id="yellow"></div>
<script>
    $(function() {
        $("button").click(function() {
            $("#red").fadeTo("slow", 0.15);
            $("#orange").fadeTo("slow", 0.4);
            $("#yellow").fadeTo("slow", 0.6);
        });
    });
</script>
</body>
</html>
```

语法:

```js
$(selector).fadeTo(speed,opacity,callback);
```

##### 滑动

- `slideDown()`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Slid Down</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #flip, #panel {
            padding: 5px;
            text-align: center;
            background-color: aquamarine;
        }

        #panel {
            padding: 30px;
            display: none;
        }
    </style>
</head>
<body>
    <div id="flip">点击下拉</div>
    <div id="panel">这里是隐藏的内容</div>
<script>
    $(function() {
        $("#flip").click(function() {
            $("#panel").slideDown("slow");
        });
    });
</script>
</body>
</html>
```

语法:

```js
$(selector).slideDown(speed,callback);
```

- `slideUp()`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Slid Down</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #flip, #panel {
            padding: 5px;
            text-align: center;
            background-color: aquamarine;
        }

        #panel {
            padding: 30px;
        }
    </style>
</head>
<body>
    <div id="flip">点击上滑</div>
    <div id="panel">这里是隐藏的内容</div>
<script>
    $(function() {
        $("#flip").click(function() {
            $("#panel").slideUp("slow");
        });
    });
</script>
</body>
</html>
```

语法:

```js
$(selector).slideUp(speed,callback);
```

- `slideToggle()`

> `jQuery` `slideToggle()` 方法可以在 `slideDown()` 与 `slideUp()` 方法之间进行切换。

如果元素向下滑动，则 slideToggle() 可向上滑动它们。

如果元素向上滑动，则 slideToggle() 可向下滑动它们。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Slid Down</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #flip, #panel {
            padding: 5px;
            text-align: center;
            background-color: aquamarine;
        }

        #panel {
            padding: 30px;
        }
    </style>
</head>
<body>
    <div id="flip">点击下拉/上滑</div>
    <div id="panel">这里是隐藏的内容</div>
<script>
    $(function() {
        $("#flip").click(function() {
            $("#panel").slideToggle("slow");
        });
    });
</script>
</body>
</html>
```

语法：

```js
$(selector).slideToggle(speed,callback);
```

##### 动画

- `animate()`

> `jQuery` `animate()` 方法用于创建自定义动画。默认情况下，所有的 `HTML` 元素有一个静态的位置，且是不可移动的。 如果需要改变为，我们需要将元素的 `position` 属性设置为 `relative`, `fixed`, 或 `absolute`!

```js
$("button").click(function(){
    $("div").animate({left:'250px'});
});
```

- 操作多个属性

```js
$("button").click(function(){
    $("div").animate({
        left:'250px',
        opacity:'0.5',
        height:'150px',
        width:'150px'
    });
});
```

- 使用相对值

```js
$("button").click(function(){
    $("div").animate({
        left:'250px',
        height:'+=150px',
        width:'+=150px'
    });
});
```

- 使用队列功能

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Animate</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #container {
            width: 100px;
            height: 100px;
            background-color: yellow;
            margin: 30px;
            position: relative;
        }
    </style>
</head>
<body>
    <button>开始动画</button>
    <div id="container"></div>
<script>
    $(function() {
        $("button").click(function() {
            var dom = $("#container");
            dom.animate({
                height: '300px',
                opacity: '0.4',
            }, "slow");
            dom.animate({
                width: '300px',
                opacity: '0.7',
            }, "slow");
            dom.animate({
                height: '100px',
                opacity: '0.4',
            }, "slow");
            dom.animate({
                width: '100px',
                opacity: '0.7',
            }, "slow");
        });
    });
</script>
</body>
</html>
```

语法：

```js
$(selector).animate({params},speed,callback);
```

##### 停止动画

- `stop()`

> `jQuery` `stop()` 方法用于停止动画或效果，在它们完成之前。`stop()` 方法适用于所有 `jQuery` 效果函数，包括滑动、淡入淡出和自定义动画。

语法:

```js
$(selector).stop(stopAll,goToEnd);
```

可选的 `stopAll` 参数规定是否应该清除动画队列。默认是 `false`，即仅停止活动的动画，允许任何排入队列的动画向后执行。

可选的 `goToEnd` 参数规定是否立即完成当前动画。默认是 `false`。

因此，默认地，`stop()` 会清除在被选元素上指定的当前动画。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Slid Down</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #flip, #panel {
            padding: 5px;
            text-align: center;
            background-color: aquamarine;
        }

        #panel {
            padding: 30px;
            display: none;
        }
    </style>
</head>
<body>
    <button>点击停止</button>
    <div id="flip">点击下拉</div>
    <div id="panel">这里是隐藏的内容</div>
<script>
    $(function() {
        $("#flip").click(function() {
            $("#panel").slideDown(3000);
        });
        $("button").click(function() {
            $("#panel").stop();
        });
    });
</script>
</body>
</html>
```

##### `Callback`

> `Callback` 函数在当前效果（动画） 100% 完成之后执行。回调函数在以上效果中作为可选参数，如果选择传入，则会在效果完成后触发函数。

##### 链

> `jQuery`允许把动作/方法链接在一起。这种链式操作是`JS`的一种特性。

```js
$("#p1").css("color","red").slideUp(2000).slideDown(2000);
```
