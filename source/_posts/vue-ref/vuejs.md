---
title: Vue.js 阅读笔记（一）
date: 2019-12-11
category:
    - Vue
tags: 
    - Vue
thumbnail: /images/asuka/asu-14.jpg

---

### Vue.js 阅读笔记（一）

> 系统、框架性的认识 `Vue`。数据绑定、计算属性、过滤器 (data、methods、computed、filter...)。

<!-- more -->

#### `Vue.js` 是什么？

> 简单来说，是一个数据双向绑定的渐进式前端框架。

##### `MVVM` 模式

要了解 `Vue` 就需要了解 `MVVM` 模式，它是由经典的 `MVC` 架构衍生来的。当 `View` (视图层) 变化时，会自动更新到 `ViewModel` (视图模型) ，反之亦然。 `View` 和 `ViewModel` 之间通过双向绑定建立联系。

#### 实例与数据绑定

> 首先，通过例子简单认识 `Vue` 的特别之处。

##### 实例

- 数据双向绑定：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Vue.js</title>
    <script src="https://cdn.bootcss.com/vue/2.6.10/vue.common.dev.js"></script>
</head>
<body>
    <div id="app">
        <input type="text" v-model="name" placeholder="your name">
        <h1>Hello, {{ name }} !</h1>
    </div>
    <script>
        var app = new Vue({
            el: '#app',
            data: {
                name: ''
            }
        })
    </script>
</body>
</html>
```

- 点击事件：

```html
<div id="app">
    <button  v-if="showBtn" v-on:click="handleClick">Click me</button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            showBtn: true
        },
        methods: {
            handleClick: function() {
                console.log('clicked!');
            }
        }
    })
</script>
```

- `for`:

```html
<div id="app">
    <ul>
        <li v-for="book in books">{{ book.name }}</li>
    </ul>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            books: [{
                name: 'vue.js'
            }, {
                name: 'javascript'
            }, {
                name: 'react'
            }]
        }
    })
</script>
```

##### 生命周期

比较常用的生命周期钩子：

`created`: 实例创建完成后调用，需要初始化处理一些数据时会比较有用。

`mounted`: `el` 挂载到实例上后调用，一般我们的第一个业务处理逻辑会在这里开始。

`beforeDestroy`: 实例销毁之前调用。

##### 插值与表达式

使用双大括号 `{{ xx }}` 实现最基本的文本插值，它会自动将我们双向绑定的数据实时显示出来。

```html
<div id="app">
    {{ date }}
    <span v-html="link"></span>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            date: new Date(),
            link: '<a href="#">This is a link.</a>'
        },
        mounted: function() {
            // 声明一个变量指向Vue的实例this，保证作用域一致
            var _this = this;
            this.timer = setInterval(function() {
                _this.date = new Date();
            }, 1000);
        },
        beforeDestroy: function() {
            if (this.timer) {
                clearInterval(this.timer)
            }
        }
    })
</script>
```

插值表达式中的简单运算、三元运算

```html
<div id="app">
    {{ number / 3 }}
    {{ isOK ? '确定' : '取消' }}
    {{ text.split(',').reverse().join(',') }}
    <span v-html="link"></span>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            number: 100,
            isOK: false,
            text: '123,456'
        }
    })
</script>
```

##### 过滤器

在插值尾部添加管道符 `|` 对数据进行过滤

通过给实例添加 `filters` 来设置

```html
<div id="app">
    {{ date | formDate }}
</div>
<script>
    var padDate = function(value) {
        return value < 10 ? '0' + value : value;
    }

    var app = new Vue({
        el: '#app',
        data: {
            date: new Date()
        },
        filters: {
            formDate: function(value) {
                // value为需要过滤的数据
                var date = new Date(value);
                var year = date.getFullYear(value);
                var month = padDate(date.getMonth(value) + 1);
                var day = padDate(date.getDate());
                var hours = padDate(date.getHours(value));
                var minutes = padDate(date.getMinutes(value));
                var seconds = padDate(date.getSeconds(value));

                return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;
            }
        },
        mounted: function() {
            var _this = this;
            this.timer = setInterval(function() {
                _this.date = new Date();
            }, 1000);
        },
        beforeDestroy: function() {
            if (this.timer) {
                clearInterval(this.timer)
            }
        }
    })
</script>
```

#### 指令与事件

> 指令是在 `Vue` 中最常用的一个功能，带有前缀 `v-`，如 `v-if`、`v-html`等。

指令的主要职责就是当其表达式的值改变时，相应的将某些行为应用到 `DOM` 上。

数据驱动 `DOM` 是 `Vue.js` 的核心理念，所以不到万不得已时不要主动操作 `DOM`，只需要维护好数据，`DOM` 的事 `Vue` 会帮你优雅的处理。

##### `v-if`

对元素进行判断

```html
<div id="app">
    <p v-if="show">显示这段文本</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            show: true,
        }
    })
</script>
```

##### `v-band`

绑定元素数据，用于动态更新 `HTML` 元素上的属性。

```html
<div id="app">
    <a v-bind:href="url">链接</a>
    <img v-bind:src="imgUrl" alt="img">
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            url: 'https://www.github.com',
            imgUrl: 'https://xxx.xx.xx/img.png'
        }
    })
</script>
```

##### `v-on`

绑定事件监听器。

```html
<div id="app">
    <p v-if="show">显示这段文本</p>
    <button v-on:click="handleClose">点击隐藏</button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            show: true,
        },
        methods: {
            handleClose: function() {
                this.show = false;
            }
        }
    })
</script>
```

##### 语法糖

语法糖是指在不影响功能的情况下，添加某种方法实现同样的效果，从而方便程序的开发。

在 `Vue.js` 中，`v-bind` 和 `v-on` 都提供了语法糖，可以缩写为 `:` 和 `@`：

```html
<div id="app">
    <a :href="url">链接</a>
    <img :src="imgUrl" alt="img">
    <button @click="handleClose">点击隐藏</button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            url: 'https://www.github.com',
            imgUrl: 'https://xxx.xx.xx/img.png'
        },
        methods: {
            handleClose: function() {
                this.show = false;
            }
        }
    })
</script>
```

语法糖可以简化代码的书写。

#### 计算属性

> 模板内的表达式常用于简单的运算，当其过长或逻辑复杂时，会难以维护。计算属性就是用于解决该问题的。

```html
<div id="app">
    {{ reversedTest }}
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            text: '123,456',
        },
        computed: {
            reversedTest: function() {
                return this.text.split(',').reverse().join(',');
            }
        }
    })
</script>
```

##### 计算属性的用法

```html
<div id="app">
    总价：{{ prices }}
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            package1: [{
                name: 'iPhone8',
                price: 7199,
                count: 2,
            }, {
                name: 'iPad',
                price: 2888,
                count: 1
            }],
            package2: [{
                name: 'apple',
                price: 3,
                count: 5,
            }, {
                name: 'banana',
                price: 2,
                count: 10,
            }],
        },
        computed: {
            prices: function() {
                var prices = 0;
                for (let i = 0; i < this.package1.length; i++) {
                    prices += this.package1[i].price * this.package1[i].count;
                }
                for (let i = 0; i < this.package2.length; i++) {
                    prices += this.package2[i].price * this.package2[i].count;
                }
                return prices;
            }
        }
    })
</script>
```

例子中，商品数量或价格变化时，计算属性 `prices` 就会自动更新，视图中的价格也会自动变化。

每一个计算属性都包含了一个 `getter` 和一个 `setter`，上面例子是计算属性的默认用法，只是利用了 `getter` 来读取。

在需要时，也可以提供一个 `setter` 函数，当手动修改计算属性的值就像修改一个普通数据那样时，就会触发 `setter` 函数，执行一些自定义的操作。

```html
<div id="app">
    {{ fullName }}
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            firstName: 'sai',
            lastName: 'akashi',
        },
        computed: {
            fullName: {
                get: function() {
                    return this.firstName + ' ' + this.lastName;
                },
                set: function(newValue) {
                    var names = newValue.split(' ');
                    this.firstName = names[0];
                    this.lastName = names[names.length-1];
                }
            }
        }
    })
</script>
```

绝大多数情况下，我们只会用默认的 `getter` 方法来读取一个计算属性，在业务中很少用到 `setter`，所以在声明一个计算属性时，可以直接使用默认的写法，不必将 `getter` 和 `setter` 都声明。

计算属性还有两个很实用的技巧容易被忽略，一是计算属性可以依赖其他计算属性，二是计算属性不仅可以依赖当前的 `Vue` 实例的数据，还可以依赖其他实例的数据。

```js
var app2 = new Vue({
    el: '#app2',
    computed: {
        reversedTest: function() {
            return app1.text.split(',').reverse.join(',');
        }
    }
})
```

这里的 `app2` 的计算属性是依赖 `app1` 的数据 `text`。

这样的用法在组件和组件化里会时常用到，尤其是在多人协同开发时。

##### 计算属性缓存

有一个问题，你可能会发现调用 `methods` 里的方法也可以和计算属性达到同样的目的

```html
<div id="app">
    {{ reversedTest() }}
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            text: '123,456',
        },
        methods: {
            reversedTest: function() {
                return this.text.split(',').reverse().join(',');
            }
        },
    })
</script>
```

既然可以使用 `methods` 代替，甚至还可以接受参数，使用起来更灵活，那么为什么还需要计算属性呢？原因就是计算属性是基于它的依赖缓存的。

一个计算属性所依赖的数据发生变化时，它才会重新取值，所以 `text` 只要不改变，计算属性也就不会更新。

但是 `methods` 不同，只要重新渲染，它就会被调用，因此函数也会被执行。

使用计算属性还是 `methods` 取决于你是否需要缓存，当遍历大数组和做大量计算时，应当使用计算属性。

#### `v-bind` `class` 与 `style` 的绑定

> `DOM` 元素经常会动态的绑定一些 `class` 类名或 `style` 样式，在 `vue` 中同样可以通过 `v-bind` 实现多种绑定的方法。

`v-bind`:

```html
<img v-bind:src="imgUrl">
```

可以简写为：

```html
<img :scr="imgUrl">
```

##### 绑定 `class` 的几种方式

- 对象语法

> 给 `v-band:class` 设置一个对象，可以动态的切换 `class`。

```html
<div id="app">
    <div class="static" :class="{ 'active': isActive }"></div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            isActive: true,
        }
    })
</script>
```

渲染结果：

```html
<div class="static active"></div>
```

当 `:class` 的表达式过长或逻辑复杂时，还可以绑定一个计算属性，这是一种很友好和常见的用法，一般当条件多于两个时，都可以使用 `data` 或 `computed`。

```html
<div id="app">
    <div :class="classes"></div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            isActive: true,
            error: null,
        },
        computed: {
            classes: function() {
                return {
                    active: this.isActive && !this.error,
                    'text-fail': this.error && this.error.type === 'fail',
                    'text': !this.error
                }
            }
        }
    })
</script>
```

最终渲染结果：

```html
<div class="active text"></div>
```

- 数组语法

> 给 `:class` 绑定一个数组，应用一个 `class` 列表。

```html
<div id="app">
    <div :class="[activeCls, errorCls]"></div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            activeCls: 'active',
            errorCls: 'error'
        }
    })
</script>
```

也可以在数组中使用对象语法：

```html
<div id="app">
    <div :class="[{ 'active': isActive }, errorCls]"></div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            isActive: true,
            errorCls: 'error'
        }
    })
</script>
```

以上两个实例的最终渲染结果都为：

```html
<div class="active error"></div>
```

当然，也可以和对象语法一样，使用 `data`, `computed`, `metohds` 三种方法。

```html
<div id="app">
    <button :class="classes"></button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            size: 'large',
            disabled: true
        },
        computed: {
            classes: function() {
                return [
                    'btn',
                    {
                        ['btn-' + this.size]: this.size !== '',
                        ['btn-disabled']: this.disabled
                    }
                ];
            }
        }
    })
</script>
```

最终渲染结果：

```html
<button class="btn btn-large btn-disabled"></button>
```

使用计算属性给元素动态设置类名，在业务中经常用到，尤其在写复用的组件时，所以在开发过程中，如果表达式较长或逻辑复杂，应该尽量的优先使用计算属性。

- 组件上的使用

如果直接在自定义组件上使用 `class` 或 `:class`，样式规则会直接应用到个组件的根元素上：

```js
Vue.component('my-component', {
    template: '<p class="article">some text</p>'
});
```

```html
<div id="app">
    <my-component :class="{ 'active': isActive }"></my-component>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            isActive: true,
        }
    })
</script>
```

##### 绑定内联样式

> 使用 `:style` 可以给元素绑定内联样式，方法与 `:class` 类似，有对象语法和数组语法，看起来像直接在元素上写 `CSS`。

```html
<div id="app">
    <div :style="styles">context</div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            styles: {
                color: 'red',
                fontSize: 14 + 'px'
            }
        },
    })
</script>
```

最终渲染结果：

```html
<div style="color: red; font-size: 14px;">context</div>
```

在实际业务中，`:style` 的数组语法并不常用，一般写在 `data` 和 `computed` 中，较为常用的应当是计算属性：

```html
<div id="app">
    <div :style="styles">context</div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        computed: {
            styles: function() {
                return {
                    color: 'yellow',
                    fontSize: 18 + 'px'
                }
            }
        }
    })
</script>
```

另外，使用 `:style` 时，`Vue.js` 会自动给特殊的 `CSS` 属性名称增加前缀，如 `transform`。
