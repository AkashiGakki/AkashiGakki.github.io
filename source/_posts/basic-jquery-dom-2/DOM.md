---
title: JQuery DOM 操作（下）
date: 2019-7-26
category: 
    - 前端
    - JavaScript
tags:
    - 前端
    - JavaScript
thumbnail: /images/bg-8.jpg

---

#### `JQuery` `DOM` 操作（下）

##### 捕获

> `jQuery` 拥有可操作 `HTML` 元素和属性的强大方法。

<!--more-->

###### 获取内容

- `text()`

> 设置或返回所选元素的文本内容

- `html()`

> 设置或返回所选元素的内容（包括 HTML 标记）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>get value</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <div id="text">
        <p>这里是文本内容</p>
    </div>
    <button id="btn-1">text</button>
    <button id="btn-2">html</button>
<script>
    $(function() {
        $("#btn-1").click(function() {
            text = $("#text").text();
            console.log(text);
        });

        $("#btn-2").click(function() {
            html = $("#text").html();
            console.log(html);
        })
    });
</script>
</body>
</html>
```

- `val()`

> 设置或返回表单字段的值

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>get val</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <input type="text" value="akashi">
    <button id="btn">val</button>
<script>
    $(function() {
        $("#btn").click(function() {
            value = $("input").val();
            console.log(value);
        });
    });
</script>
</body>
</html>
```

###### 获取属性

- `attr()`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>get attr</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <a href="https://akashi_sai.gitee.io/">点击访问</a>
    <button id="btn">attribute</button>
<script>
    $(function() {
        $("#btn").click(function() {
            attribute = $("a").attr("href");
            console.log(attribute);
        });
    });
</script>
</body>
</html>
```

##### 设置

> 通过之前的四个方法，设置内容和属性。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>set value</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <p id="text-1">这里是一个段落</p>
    <p id="text-2">这里是另外一个段落</p>
    <input type="text" value="akashi">
    <div>
        <button id="btn-1">set text</button>
        <button id="btn-2">set html</button>
        <button id="btn-3">set val</button>
    </div>
<script>
    $(function() {
        $("#btn-1").click(function() {
            $("#text-1").text("set text");
        });

        $("#btn-2").click(function() {
            $("#text-2").html("set <b>html</b>");
        })

        $("#btn-3").click(function() {
            $("input").val("asuka");
        })
    });
</script>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>set attr</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <a href="https://akashi_sai.gitee.io/">访问博客</a>
    <button>set attr</button>
<script>
    $(function() {
        $("button").click(function() {
            $("a").attr({
                "href": "https://akashigakki.github.io/",
                "title": "GitHub Blog"
            });
            title = $("a").attr("title");
            $("a").html(title);
        });
    });
</script>
</body>
</html>
```

##### 添加元素

###### 添加新的`HTML`元素

- `append()`

> `jQuery` `append()` 方法在被选元素的结尾插入内容（仍在该元素的内部）。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>append</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <button>append</button>
    <div>
        <ul>
            <li>Item_1</li>
            <li>Item_2</li>
            <li>Item_3</li>
        </ul>
    </div>
<script>
    $(function() {
        $("button").click(function() {
            $("ul").append("<li>追加列表项</li>");
        });
    });
</script>
</body>
</html>
```

- `prepend()`

> `jQuery` `prepend()` 方法在被选元素的开头插入内容。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>prepend</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <button>prepend</button>
    <div>
        <ul>
            <li>Item_1</li>
            <li>Item_2</li>
            <li>Item_3</li>
        </ul>
    </div>
<script>
    $(function() {
        $("button").click(function() {
            $("ul").prepend("<li>追加列表项</li>");
        });
    });
</script>
</body>
</html>
```

- `after()`

> `jQuery` `after()` 方法在被选元素之后插入内容。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>after</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <button>after</button>
    <div>
        <ul>
            <li>Item_1</li>
            <li>Item_2</li>
            <li>Item_3</li>
        </ul>
    </div>
<script>
    $(function() {
        $("button").click(function() {
            $("ul").after("<li>追加列表项</li>");
        });
    });
</script>
</body>
</html>
```

- `before()`

> `jQuery` `before()` 方法在被选元素之前插入内容。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>before</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
</head>
<body>
    <button>before</button>
    <div>
        <ul>
            <li>Item_1</li>
            <li>Item_2</li>
            <li>Item_3</li>
        </ul>
    </div>
<script>
    $(function() {
        $("button").click(function() {
            $("ul").before("<li>追加列表项</li>");
        });
    });
</script>
</body>
</html>
```

注意：`append()`和`prepend()`方法添加新元素是在选中元素的内部，而`after()`和`before()`方法添加新元素是在选中元素的外部（元素之后或元素之前）。

##### 删除元素

###### 删除元素/内容

- `remove()`

> 删除被选元素（及其子元素）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>remove</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #container {
            background-color: yellow;
            text-align: center;
            margin: 5px;
            padding: 5px;
        }
    </style>
</head>
<body>
    <button>点击删除元素</button>
    <div id="container">
        <p>这里是元素内容</p>
        <p>这里是元素内容</p>
    </div>
<script>
    $(function() {
        $("button").click(function() {
            $("#container").remove();
        });
    });
</script>
</body>
</html>
```

- `empty()`

> 从被选元素中删除子元素

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>empty</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        #container {
            background-color: yellow;
            text-align: center;
            margin: 5px;
            padding: 5px;
        }
    </style>
</head>
<body>
    <button>点击清空元素</button>
    <div id="container">
        <p>这里是元素内容</p>
        <p>这里是元素内容</p>
    </div>
<script>
    $(function() {
        $("button").click(function() {
            $("#container").empty();
        });
    });
</script>
</body>
</html>
```

###### 过滤被删除的元素

```js
$("p").remove(".part");
```

删除了`class`名为`part`的段落（`p`），如果存在`class`名不是`part`的段落，则不会被删除。

##### `CSS`类

- `addClass()`

> 向被选元素添加一个或多个类

```js
$("button").click(function(){
  $("h1, h2, p").addClass("yellow");
  $("div").addClass("important");
});
```

也可以同时添加多个类：

```js
$("button").click(function(){
  $("body div:first").addClass("important blue");
});
```

- `removeClass()`

> 从被选元素删除一个或多个类

```js
$("button").click(function(){
  $("h1, h2, p").removeClass("yellow");
});
```

- `toggleClass()`

> 对被选元素进行添加/删除类的切换操作

```js
$("button").click(function(){
  $("h1,h2,p").toggleClass("yellow");
});
```

- `css()`

> 设置或返回样式属性

##### `css()`方法

语法：

```js
css("propertyname", "value");
```

```js
$("p").css("background-color","yellow");
```

也可以同时设置多个：

```js
$("p").css({"background-color":"yellow", "font-size":"200%"});
```

##### 尺寸

> `jQuery` 提供多个处理尺寸的重要方法：

- `width()`

> `width()` 方法设置或返回元素的宽度（不包括内边距、边框或外边距）。

- `height()`

> `height()` 方法设置或返回元素的高度（不包括内边距、边框或外边距）。

- `innerWidth()`

> `innerWidth()` 方法返回元素的宽度（包括内边距）。

- `innerHeight()`

> `innerHeight()` 方法返回元素的高度（包括内边距）。

- `outerWidth()`

> `outerWidth()` 方法返回元素的宽度（包括内边距和边框）。

- `outerHeight()`

> `outerHeight()` 方法返回元素的高度（包括内边距和边框）。


![size](http://ww1.sinaimg.cn/large/9c62a0cfly1g5b2jy58lcj20ro0kagnw.jpg)

##### 遍历

> `jQuery` 遍历，意为移动，用于根据其相对于其他元素的关系来查找（或选取）`HTML`元素。

通过`jQuery`遍历，可以从当前元素开始，在家族树中向上移动（祖先），向下移动（子孙），水平移动（同胞），这种移动被称为对`DOM`树进行遍历：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>parent</title>
    <style>
        * {
            border: 1px solid pink;
            list-style: none;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div>div
        <ul>ul
            <li>li
                <span>span</span>
            </li>
            <li>li
                <b>b</b>
            </li>
        </ul>
    </div>
</body>
</html>
```

![DOM](http://ww1.sinaimg.cn/large/9c62a0cfly1g5c6dfw4r5j21520jgq3e.jpg)

##### `jQuery` 祖先

> 通过 `jQuery`，可以向上遍历 `DOM` 树，以查找元素的祖先。

- `parent()` 方法

> `parent()` 方法返回被选元素的直接父元素。该方法只会向上一级对 `DOM` 树进行遍历

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>parent</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div * {
            border: 1px solid pink;
            list-style: none;
            margin: 15px;
            padding: 5px;
            display: block;
        }
    </style>
</head>
<body>
    <div>div（祖父元素）
        <ul>ul（父元素）
            <li>li（当前选中元素）
                <span>span（子孙元素）</span>
            </li>
        </ul>
    </div>
<script>
    $(function() {
        $("li").parent().css({
            "border": "2px solid yellow"
        });
    });
</script>
</body>
</html>
```

- `parents()`方法

> `parents()` 方法返回被选元素的所有祖先元素，一直到文档根元素。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>parents</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div * {
            border: 1px solid pink;
            list-style: none;
            margin: 15px;
            padding: 5px;
            display: block;
        }
    </style>
</head>
<body>
    <div>div（祖父元素）
        <ul>ul（父元素）
            <li>li（当前选中元素）
                <span>span（子孙元素）</span>
            </li>
        </ul>
    </div>
<script>
    $(function() {
        $("li").parents().css({
            "border": "2px solid yellow"
        });
    });
</script>
</body>
</html>
```

- `parentsUntil()`方法

> `parentsUntil()` 方法返回介于两个给定元素之间的所有祖先元素。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>parentsUntil</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div * {
            border: 1px solid pink;
            list-style: none;
            margin: 15px;
            padding: 5px;
            display: block;
        }
    </style>
</head>
<body>
    <div>div（祖父元素）
        <ul>ul（父元素）
            <li>li（当前选中元素）
                <span>span（子孙元素）</span>
            </li>
        </ul>
    </div>
<script>
    $(function() {
        $("li").parentsUntil("body").css({
            "border": "2px solid yellow"
        });
    });
</script>
</body>
</html>
```

##### `jQuery` 子孙

- `children()` 方法

> `children()` 方法返回被选元素的所有直接子元素。该方法只会向下一级对 `DOM` 树进行遍历。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>children</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div * {
            border: 1px solid pink;
            list-style: none;
            margin: 15px;
            padding: 5px;
            display: block;
        }
    </style>
</head>
<body>
    <div>div（祖父元素）
        <ul>ul（父元素）
            <li>li（当前选中元素）
                <span>span（子孙元素）
                    <b></b>
                </span>
            </li>
        </ul>
    </div>
<script>
    $(function() {
        $("li").children().css({
            "border": "2px solid yellow"
        });
    });
</script>
</body>
</html>
```

- `find()` 方法

> `find()` 方法返回被选元素的后代元素，一直到最后一个。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>children</title>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <style>
        div * {
            border: 1px solid pink;
            list-style: none;
            margin: 15px;
            padding: 5px;
            display: block;
        }
    </style>
</head>
<body>
    <div>div（祖父元素）
        <ul>ul（父元素）
            <li>li（当前选中元素）
                <span>span（子孙元素）
                    <b></b>
                </span>
            </li>
        </ul>
    </div>
<script>
    $(function() {
        $("li").find("*").css({
            "border": "2px solid yellow"
        });
    });
</script>
</body>
</html>
```

当然，也可以对返回的标签进行过滤，来返回固定的标签。

```js
$(function() {
    $("li").find("span").css({
        "border": "2px solid yellow"
    });
});
```

##### `jQuery` 同胞

- `siblings()` 方法

> `siblings()` 方法返回被选元素的所有同胞元素。

```js
$(function() {
  $("h2").siblings();
});
```

同时，也可以传入参数来过滤同胞元素进行搜索。

```js
$(function(){
  $("h2").siblings("span");
});
```

方法 | 用途
--- | ---
`next()` | 返回被选元素的下一个同胞元素。该方法只返回一个元素
`nextAll()` | 返回被选元素的所有跟随的同胞元素
`nextUntil()` | 返回介于两个给定参数之间的所有跟随的同胞元素
`prev()` | 返回被选元素的前一个同胞元素。该方法只返回一个元素
`prevAll()` | 返回被选元素的所有之前的同胞元素
`prevUntil()` | 返回介于两个给定参数之间的所有之前的同胞元素
 
##### `jQuery` 过滤

> 遍历-过滤，缩小搜索元素的范围。

- `first()` 方法

> `first()` 方法返回被选元素的首个元素。

```js
$(function() {
    $("p").first();
});
```

- `last()` 方法

> `last()` 方法返回被选元素的最后一个元素。

```js
$(function() {
    $("p").last();
});
```

- `eq()` 方法

> `eq()` 方法返回被选元素中带有指定索引号的元素。

索引号从 0 开始，因此首个元素的索引号是 `0` 而不是 `1` 。
下面的例子选取第二个 `<p>` 元素（索引号 1）：

```js
$(function() {
    $("p").eq(1);
});
```

- `filter()` 方法

> `filter()` 方法允许规定一个标准。不匹配这个标准的元素会被从集合中删除，匹配的元素会被返回。

下面的例子返回带有类名 "`title`" 的所有 `<p>` 元素：

```js
$(function() {
    $("p").filter(".title");
});
```

- `not()` 方法

> `not()` 方法返回不匹配标准的所有元素。

提示：`not()` 方法与 `filter()` 相反。

```js
$(function() {
    $("p").not(".title");
});
```

##### `jQuery` `AJAX`

> `AJAX` 是与服务器交换数据的技术，它在不重载全部页面的情况下，实现了对部分网页的更新。

`AJAX` = 异步 `JavaScript` 和 `XML`（`Asynchronous JavaScript and XML`）。

简短地说，在不重载整个网页的情况下，`AJAX` 通过后台加载数据，并在网页上进行显示。

`jQuery` 提供多个与 `AJAX` 有关的方法。

通过 `jQuery` `AJAX` 方法，可以使用 `HTTP Get` 和 `HTTP Post` 从远程服务器上请求`文本`、`HTML`、`XML` 或 `JSON` ，同时可以把这些外部数据直接载入网页的被选元素中。

##### `jQuery` `load()` 方法

> `load()` 方法从服务器加载数据，并把返回的数据放入被选元素中。

语法:

```js
$(selector).load(URL, data, callback);
```

`URL` 为必须参数，指定加载文件的路径。

`data` 为可选参数，规定与请求一同发送的查询字符串键/值对集合。

`callback` 回调函数，规定方法完成后执行的函数名称。

##### `jQuery` `get()` / `post()`

两种在客户端和服务器端进行请求-响应的常用方法：

`DET` 和 `POST`

`Get` 从指定的资源请求数据

`Post` 向指定的资源提交要处理的数据

- `$.get()` 方法

> `$.get()` 方法通过 `HTTP GET` 请求从服务器上请求数据。

语法：

```js
$.get(URL, callback);
```

- `$.post()` 方法

> `$.post()` 方法通过 `HTTP POST` 请求向服务器提交数据。

语法:

```js
$.post(URL, data, callback);
```

实例：

```js
$.ajax({
    type: 'get',
    async: false,
    cache: false,
    dataType: 'json',
    url: 'xxx.xxx.com',
    success: function (res) {
        // 获取成功后的处理函数
    }
});
```

##### `jQuery` `JSONP`

> `Jsonp`(`JSON with Padding`) 是 `json` 的一种"使用模式"，可以让网页从别的域名（网站）那获取资料，即跨域读取数据。

要理解跨域，先要了解一下“同源策略”。所谓同源是指，域名，协议，端口相同。所谓“同源策略“，简单的说就是基于安全考虑，当前域不能访问其他域的东西。

同源策略，它是由 `Netscape` 提出的一个著名的安全策略，现在所有支持 `JavaScript` 的浏览器都会使用这个策略。

[参考实现](https://blog.csdn.net/hansexploration/article/details/80314948)
