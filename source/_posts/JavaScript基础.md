---
title: JavaScript基础
date: yyyy-mm-dd
category: 
    - 前端
    - JavaScript
tags: 
    - 前端
    - 入门教程
    - JavaScript
thumbnail: /images/bg-4.jpg

---

#### JavaScript基础

##### 一、什么是JavaScript？

- 1.1 `JS`
    - `JavaScript`是一种脚本语言
    - `JavaScript`是一种轻量级的编程语言
    - `JavaScript`可插入HTML编程
    - `JavaScript`代码可由浏览器执行

<!-- more -->

- 1.2 `JavaScript`直接写入`HTML`输出流
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML输出流</title>
</head>
<body>
<script>
    document.write('<h1>这是一个标题</h1>');
    document.write('<p>这是一个段落</p>');    
</script>
</body>
</html>
```
注意：如果在文档已加载后使用（比如在函数中），会覆盖整个文档。
- 1.3 `JavaScript`对事件的反应
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>弹出事件</title>
</head>
<body>
    <button type="button" onclick="alert('欢迎！')">点我！</button>
    <button onclick="eventHandle()">再点我！</button>
<script>
    function eventHandle() {
        alert("欢迎！")
    }
</script>
</body>
</html>
```
注意：两个`Button`的弹出效果是一样的，写法上第二个调用了函数，是常见写法。
- 1.4 `JavaScript`改变`HTML`的内容
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>改变HTML内容</title>
</head>
<body>
    <p id="demo">这里是文档内容</p>
    <button onclick="change()">点击修改</button>
<script>
    function change() {
        x = document.getElementById('demo');     // 找到元素
        x.innerHTML = '这里是修改后的内容';     // 修改内容
} 
</script>
</body>
</html>
```
- 1.5 `JavaScript`改变`HTML`的图像

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>判断替换src</title>
</head>
<body>
    <img src="/images/pic_bulboff.gif" id="image" onclick="changeImage()" width="100" height="180" alt="images">
<script>
    function changeImage() {

        document.getElementById('image');

        if (element.src.match('bulbon')) {
            element.src="/images/pic_bulboff.gif";
        } else {
            element.src="/images/pic_bulbon.gif";
        }
    }
</script>
</body>
</html>
```

- 1.6 `JavaScript`改变`HTML`的样式
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>改变HTML样式</title>
</head>
<body>
    <p id="demo">这里是元素样式</p>
    <button onclick="change()">点击修改</button>
<script>
    function change() {
        x = document.getElementById('demo');     
        x.style.color = '#ff0000';
    } 
</script>
</body>
</html>
```
- 1.7 `ECMAScript` 版本

年份 | 名称 | 描述
--- | --- | ---
2009 | ECMAScript 5 | 添加 "strict mode"，严格模式，添加 JSON 支持
2011 | ECMAScript 5.1 | 版本变更
2015 | ECMAScript 6 | 添加类和模块
2016 | ECMAScript 7 | 增加指数运算符 (**)，增加 Array.prototype.includes

##### 二、用法及输出

> 如需在`HTML`页面中插入`JavaScript`，需使用`<script>`标签。脚本可被放置在` HTML` 页面的` <body>` 和` <head>` 部分中。

###### 2.1 导入`JS`的三种方式

- `<body>`中的`JS`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<script>
    // 在这里编辑你的JS代码
</script>  
</body>
</html>
```

- `<head>`中的`JS`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>Document</title>
    <script>
        // 在这里编辑你的JS代码
    </script>
</head>
<body>

</body>
</html>
```

- 外部的`JS`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<!-- 从外部导入js文件 -->
<script src="main.js"></script> 
</body>
</html>
```

###### 2.2 `JavaScript`输出

- 使用`window.alert()`弹出警告框
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>输出</title>
</head>
<body>
<script>
    window.alert('Hello!');
</script>
</body>
</html>
```
注意：`window`是`JS`的全局变量，可以省略不写。(例如`alert('Hello!')`)
- 使用`document.write()`方法将内容写到`HTML`文档中
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>输出</title>
</head>
<body>
<script>
    document.write('Hello!');
</script>
</body>
</html>
```
- 使用`innerHTML`写入到`HTML`元素
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>输出</title>
</head>
<body>
    <p id="demo"></p>
<script>
    document.getElementById('demo').innerHTML = Date(); // 输出当前时间
</script>
</body>
</html>
```
- 使用`console.log()`写入到浏览器控制台输出
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>输出</title>
</head>
<body>
<script>
    console.log('Hello!');
</script>
</body>
</html>
```
注意：从浏览器打开`html`文件，按`F12`打开开发者模式，在`console`控制台查看。

###### 2.3 数据类型及变量

- 数据类型
    - 值类型（基本类型）
        - 字符串`String`
        ```js
        var name = 'Akashi';
        ```
        - 数字`Number`
        ```js
        var age = '21';
        ```
        - 布尔型`Boolean`
        ```js
        var active = true;
        ```
        - 对空`Null`
        ```js
        var person = null;
        ```
        - 未定义`Undefined`
        - `Symbol`
    - 引用数据类型
        - 对象`Object`
        ```js
        var person = {
            name = 'Akashi',
            age = 21,
        }
        ```
        - 数组`Array`
        ```js
        var cars = ['audi', 'toyota', 'bmw'];
        ```
        `or`
        ```js
        var cars = new Array('audi', 'toyota', 'bmw');
        ```
        `or`
        ```js
        var cars2 = new Array();
        cars2[0] = 'audi';
        cars2[1] = 'toyota';
        cars2[2] = 'bmw';
        ```
        - 函数`Function`
        ```js
        function name(params) {
        
        }
        ```

注意：`Undefined`和`Null`：`Undefined` 这个值表示变量不含有值。可以通过将变量的值设置为 `null` 来清空变量。
        
注意：`Symbol` 是 `ES6` 引入了一种新的原始数据类型，表示独一无二的值。

- 创建变量
    - 使用`var`关键词声明变量
```js
<script>
    var length = 16;        // Number 通过数字字面量赋值 
    var points = x * 10;        // Number 通过表达式字面量赋值
    var lastName = "Sai";       // String 通过字符串字面量赋值
    var cars = ["Audi", "Toyota", "BMW"];       // Array  通过数组字面量赋值
    var person = {firstName:"Akashi", lastName:"Sai"};      // Object 通过对象字面量赋值
</script>
```

- 声明变量类型
    - 动态类型
        -  `JavaScript`拥有动态类型。这意味着相同的变量可用作不同的类型
    - 使用关键词`new`声明变量类型
```js
<script>
    var name = new String;
    var num = new Number;
    var flag = new Boolean;
    var list = new Array();
    var person = new Object;
</script>
```

- 函数
```html
<script>
    function functionName(params) {
        // 函数体
    }
</script>
```
- 字母大小写
    - `JavaScript`对大小写敏感

- 注释
    - 单行注释
        - 单行注释以 `//` 开头
    - 多行注释
        - 多行注释以 `/* `开始，以 `*/ `结尾
        
###### 2.4 作用域

> 在 `JavaScript` 中, 作用域为可访问变量，对象，函数的集合。

- 局部变量

    - 变量在函数内声明，变量为局部作用域
    - 局部变量：只能在函数内部访问
    
```js
// 函数外不能调用name变量
function getName() {
    name = 'akashi';
    // 函数内可调用name变量
}
```

- 全局变量

    - 变量在函数外定义，即为全局变量
    - 全局变量有 全局作用域: 网页中所有脚本和函数均可使用
    
```js
var name = 'akashi';

// 函数外可调用name变量

function getName() {
    // 函数内可调用name变量
}
```

- 生命周期

    - JavaScript 变量生命周期在它声明时初始化
    - 局部变量在函数执行完毕后销毁
    - 全局变量在页面关闭后销毁

- 函数参数

    - 函数参数只在函数内起作用，是局部变量

- `HTML`中的全局变量

    - 在 `HTML` 中, 全局变量是 `window` 对象: 所有数据变量都属于 `window` 对象

```js
getName();
// 可以调用window.name
console.log(window.name);

function getName() {
    name = 'akashi';
}
```

###### 2.5 事件

>` HTML` 事件可以是浏览器行为，也可以是用户行为。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>事件</title>
</head>
<body>
    <div id="demo"></div>
    <button onclick="clickHandle()">现在的时间是？</button>
<script>
    function clickHandle() {
        document.getElementById('demo').innerHTML = Date();
    }
</script>
</body>
</html>
```

- 常见的`HTML`事件表

事件  | 描述
--- | ---
`onchange` | `HTML`元素改变
`onclick` | 用户点击`HTML`元素
`onmouseover` | 用户在一个`HTML`元素上移动鼠标
`onmouseout` | 用户从一个`HTML`元素上移开鼠标
`onkeydown` | 用户按下键盘按键
`onload` | 浏览器已完成页面的加载

> 更多参考：`https://blog.csdn.net/qwer_df_b/article/details/77509859`

###### 2.6 字符串

> `JavaScript`字符串可以存储一系列字符，用于存储和处理文本。

- 获取字符串长度

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>String</title>
</head>
<body>

<script>
    var str = 'qwertyuiopasdfghjklzxcvbnm';
    console.log(str.length);
</script>
</body>
</html>
```

- 特殊字符

    - 使用转义字符（`\`），反斜杠是一个转义字符。 转义字符将特殊字符转换为字符串字符
    
代码  |  输出
-- | --
\'  |  单引号
\"  |  双引号
\\  |  反斜杠
\n  |  换行
\r  |  回车
\t  |  tab(制表符)
\b  |  退格符
\f  |  换页符

- 字符串方法

方法 | 描述
--- | --
`charAt()` | 返回指定索引位置的字符
`indexOf()` | 返回字符串中检索指定字符第一次出现的位置
`lastIndexOf()` | 返回字符串中检索指定字符最后一次出现的位置
`match()` | 找到一个或多个正则表达式的匹配
`replace()` | 替换与正则表达式匹配的子串
`search()` | 检索与正则表达式相匹配的值
`slice()` | 提取字符串的片断，并在新的字符串中返回被提取的部分
`split()` | 把字符串分割为子字符串数组
`substr()` | 从起始索引号提取字符串中指定数目的字符
`substring()` | 提取字符串中两个指定的索引号之间的字符
`toString()` | 返回字符串对象值

###### 2.7 运算符

- 算数运算符

运算符  |  描述
-- | --
`+`  |  加法
`-`   | 减法    
`*`   | 乘法    
`/`   | 除法    
`%`  |  取模（余数） 
`++`  |  自增    
`--`  |  自减

- 赋值运算符

运算符  |  例子  |  等同于  |  运算结果
-- | -- | -- | --
`=`  |  x=y  |    |   x=5   
`+=`  |  x+=y  |  x=x+y  |  x=15   
`-=`  |  x-=y  |  x=x-y  |  x=5   
`*=`  |  x*=y  |  x=x*y  |  x=50   
`/=`  |  x/=y  |  x=x/y  |  x=2    
`%=`  |  x%=y  |  x=x%y  |  x=0

- 字符串拼接
    - `+`

```js
    var firstname = 'akashi';
    var lastname = 'sai';
    var fullname = firstname + lastname;
    console.log(fullname);
```

###### 2.8 比较运算符和逻辑运算符

- 比较运算符

运算符  |  描述
-- | --
`==`  |  等于   
`===`  |  绝对等于 
`!=`   |  不等于    
`!==`   |  不绝对等于（值和类型有一个不相等，或两个都不相等） 
`>`   |  大于 
`<`   |  小于       
`>=`  |   大于或等于   
`<=`   |  小于或等于

- 逻辑运算符

运算符  |  描述  |  例子
-- | -- | --
`&&`  |  `and` |   (x < 10 && y > 1) 为 true
`II`  |  `or`  |  (x==5 II y==5) 为 false
`!`  |  `not`  |  !(x==y) 为 true

注意：列表中的`II`为双竖线`||`。

- 条件运算符

```js
variablename=(condition)?value1:value2 
```

`eg`:
```js
voteable=(age<18)?"年龄太小":"年龄已达到";
```

###### 2.9 条件语句

```js
if (condition1) {
    // do something
}
else if (condition2) {
    // do something
}
else {
    // do something
}
```

###### 2.10 `switch`语句

```js
switch(n) {
    case 1:
        // 执行代码块 1
        break;
    case 2:
        // 执行代码块 2
        break;
    default:
        // 与 case 1 和 case 2 不同时执行的代码
}
```

###### 2.11 `for`循环

```js
for (语句 1; 语句 2; 语句 3) {
    // 被执行的代码块
}
```

- `for/in`
    - `JavaScript` `for/in` 语句循环遍历对象的属性
    
```js
    var x;

    var person = {name: "akashi", age: 21, sex: "male"};
    var text = '';
    
    for (x in list) {
        text += list[x];
    }
    console.log(text);
```

###### 2.12 `while`循环

```js
while (条件) {
    // 需要执行的代码
}
```

```js
do {
    // 需要执行的代码
} while (条件);
```

###### 2.13 `break`和`continue`语句

- `break`

    - `break` 语句可用于跳出循环
    - `break` 语句跳出循环后，会继续执行该循环之后的代码

- `continuee`

    - `continue` 语句中断循环中的迭代
    - 如果出现了指定的条件，然后继续循环中的下一个迭代

