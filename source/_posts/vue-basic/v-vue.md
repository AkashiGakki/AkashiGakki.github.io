---
title: Vue.js 阅读笔记（二）
date: 2019-12-12
category:
    - Vue
tags: 
    - Vue
thumbnail: /images/asuka/asu-15.jpg

---

### Vue.js 阅读笔记（二）

> 系统、框架性的认识 `Vue`。`v-bind`、`v-on`、`v-if`、`v-for`、`v-model`。

<!-- more -->

#### 内置指令

##### 基本指令

- `v-cloak`

> `v-cloak` 不需要表达式，它会在实例结束编译时从绑定的 `HTML` 元素上移除，经常和 `CSS` 中的 `display: none;` 配合使用。

```html
<div id="app" v-cloak>
    {{ message }}
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: 'some messages'
        }
    })
</script>
```

```css
[v-cloak] {
    display: none;
}
```

当网速较慢，`vue.js` 文件还没有加载完时，页面上就会显示 `{{ message }}` 的字样，直到 `Vue` 创建实例、编译模板时， `DOM` 才会被替换，所以这个过程中，屏幕是会有闪动的，使用 `v-cloak` 配合 `CSS`，就是解决初始化慢导致页面抖动的最佳实践。

一般情况下，在使用了 `webpack` 和 `vue-route` 时，项目的 `HTML` 只有一个空的 `div` 元素，剩余的内容都是由路由去挂载不同组件完成的，所以也就不需要 `v-cloak` 了。

- `v-once`

> 也是一个不需要表达式的指令，作用是定义它的组件或元素只被渲染一次，包括元素或组件的所有节点。首次渲染之后，不再随数据的变化重新渲染，将被视为静态内容。

```html
<div id="app" v-once>
    {{ message }}
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: 'some messages'
        }
    })
</script>
```

`v-once` 在业务中很少使用，当需要进一步优化性能时，才可能会使用到。

##### 条件渲染指令

- `v-if`、`v-else-if`、`v-else`

> 与 `JavaScript` 的条件语句 `if`、`else`、`else if` 类似，`Vue.js` 的条件指令可以根据表达式的值在 `DOM` 中渲染或销毁元素/组件。

```html
<div id="app">
    <div v-if="status === 1">当 status 为 1 时，显示</div>
    <div v-else-if="status === 2">当 status 为 2 时，显示</div>
    <div v-else>否则，显示该行</div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            status: 1,
        }
    })
</script>
```

`Vue` 在渲染元素时，会尽可能的复用已有的元素而非重新渲染：

```html
<div id="app">
    <template v-if="type === 'name'">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" placeholder="Here input your name">
    </template>
    <template v-if="type === 'email'">
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" placeholder="Here input your email">
    </template>
    <button @click="handleToggleClick">Change Type</button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            type: 'name',
        },
        methods: {
            handleToggleClick: function() {
                this.type = this.type === 'name' ? 'email' : 'name';      
            }
        }
    })
</script>
```

这里键入内容，点击切换后，虽然 `DOM` 改变了，但是输入框的内容并没有改变，只是替换了 `placeholder` 的内容，`<input>` 元素被复用了。

如果你不希望这样，可以使用 `key` 属性，它可以决定是否要复用元素，`key` 值必须要是唯一的。

```html
<div id="app">
    <template v-if="type === 'name'">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" key="name-input" placeholder="Here input your name">
    </template>
    <template v-if="type === 'email'">
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" key="email-input" placeholder="Here input your email">
    </template>
    <button @click="handleToggleClick">Change Type</button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            type: 'name',
        },
        methods: {
            handleToggleClick: function() {
                this.type = this.type === 'name' ? 'email' : 'name';      
            }
        }
    })
</script>
```

- `v-show`

> `v-show` 与 `v-if` 基本一致，只不过 `v-show` 是改变元素的 `CSS` 属性 `display`，当表达式的值为 `false` 时，元素会隐藏。

```html
<div id="app">
    <div v-show="status === 1">当 status 为 1 时，显示</div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            status: 2,
        }
    })
</script>
```

```html
<div id="app">
    <div v-show="isShow">显示/隐藏</div>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            isShow: false
        }
    })
</script>
```

注意：`v-show` 不能在 `<template>` 上使用。

- `v-if` 和 `v-show` 的选择

`v-if` 是条件渲染，会根据表达式适当的销毁或重建元素及绑定事件或子组件。若表达式一开始为 `false`，则一开始元素\组件并不会被渲染，只有当条件第一次变为 `true` 时才开始编译。

`v-show` 只是简单的 `CSS` 属性切换，无论条件是否为 `true`，都会被编译。

相比之下，`v-if` 更适合条件不经常改变的场景，因为它切换的开销相对较大，而 `v-show` 适合用于频繁切换的条件。

##### 列表渲染指令

- `v-for`

> 当需要将一个数组遍历或枚举一个对象循环显示时，就需要用到列表渲染指令`v-for`。

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
            books: [
                { name: 'book_1' },
                { name: 'book_2' },
                { name: 'book_3' }
            ]
        }
    })
</script>
```

除了用 `in` 做分隔符，也可以使用 `of` 作为分隔符：

```html
<li v-for="book of books">{{ book.name }}</li>
```

还支持一个可选参数作为当前索引：

```html
<li v-for="(book, index) in books">{{ index }} - {{ book.name }}</li>
```

可选参数放在后面

除了数组外，对象的属性也是可以遍历的。

```html
<div id="app">
    <ul>
        <li v-for="(value, key, index) in user">{{ index }} - {{ key }} - {{ value }}</li>
    </ul>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            user: {
                name: 'Akashi',
                gender: 'male',
                age: 22
            }
        }
    })
</script>
```

遍历对象属性时，有两个可选参数，分别是键名和索引，参数传入顺序为 `(value, key, index)`。

- 数组更新

> `Vue` 的核心是数据与视图的双向绑定，当我们修改数组时，`Vue` 会检测到数据的变化，所以渲染的视图也会立即更新。

数组方法：

- `push()`
    - 向数组的末尾添加一个或多个元素，并返回新的长度。

- `pop()`
    - 用于删除并返回数组的最后一个元素。

- `shift()`
    - 用于把数组的第一个元素从其中删除，并返回第一个元素的值。

- `unshift()`
    - 向数组的开头添加一个或更多元素，并返回新的长度。

- `splice()`
    - 从数组中添加/删除项目，然后返回被删除的项目。

- `sort()`
    - 对数组的元素进行排序。

- `reverse()`
    - 用于颠倒数组中元素的顺序。

还有一些方法不会改变原数组：

- `filter()`
    - 创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。

- `concat()`
    - 用于连接两个或多个数组。

- `slice()`
    - 从已有的数组中返回选定的元素(切片)。

```html
<div id="app">
    <ul>
        <li v-for="(user, index) in users">{{ index }} - {{ user.name }}</li>
    </ul>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            users: [
                {
                    name: 'Akashi',
                    gender: 'male',
                    age: 22
                }, {
                    name: 'Asuka',
                    gender: 'female',
                    age: 21
                }
            ]
        }
    });
    app.users = app.users.filter(function (item) {
        if (item.age > 21) {
            return item;
        }
    });
</script>
```

这样，第二项 `Asuka` 就会被过滤。

`Vue` 在检测到数据变化时，并不是直接渲染整个列表，而是最大化的复用了 `DOM` 元素，替换的数组中，含有相同的元素的项不会被重新渲染，因此可以大胆的用新数组来替换旧数组，不用担心性能问题。

- 过滤与排序

> 当不想改变原数组，想通过一个数组副本来做过滤或者排序显示时，可以使用计算属性来返回过滤或排序后的数组。

```html
<div id="app">
    <ul>
        <li v-for="(user, index) in filterUser">{{ index }} - {{ user.name }}</li>
    </ul>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            users: [
                {
                    name: 'Akashi',
                    gender: 'male',
                    age: 22
                }, {
                    name: 'Asuka',
                    gender: 'female',
                    age: 21
                }
            ]
        },
        computed: {
            filterUser: function() {
                return this.users.filter(function (user) {
                    if (user.gender === 'female')
                        return user;
                });
            }
        }
    });
</script>
```

##### 方法与事件

> `Vue` 中事件处理引入了 `v-on`。

一个计时器的例子：

```html
<div id="app">
    <div>点击次数 {{ counter }}</div>
    <button @click="handleAdd()">+1</button>
    <button @click="handleAdd(10)">+10</button>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            counter: 0,
        },
        methods: {
            handleAdd: function(count) {
                count = count || 1;
                this.counter += count;
            }
        }
    })
</script>
```

在 `methods` 中我们定义了需要的方法供 `@click` 调用，需要注意的是，调用的方法名后可以不跟括号 `()`。此时，如果该方法有参数，默认就会将原生事件对象 `event` 传入。

在大部分业务场景中，如果方法不需要传入参数，为了简便可以不写括号。

`Vue` 还提供了一个特殊的变量 `$event`，用于访问原生 `DOM` 事件：

```html
<div id="app">
    <a href="https://akashigakki.github.io" @click="handleClick('禁止打开', $event)">打开链接</a>
</div>
<script>
    var app = new Vue({
        el: '#app',
        methods: {
            handleClick: function(message, event) {
                event.preventDefault();
                window.alert(message);
            }
        }
    })
</script>
```

- 修饰符

在上一例中使用的 `event.preventDefault()` 也可以用 `Vue` 事件的修饰符来实现。

- `.stop`

- `.prevent`

- `.capture`

- `.self`

- `.once`

具体用法：

```html
<!-- 阻止单击事件冒泡 -->
<a @click.stop="handle"></a>
```

```html
<!-- 提交事件不再重载页面 -->
<form @submit.prevent="handle"></form>
```

修饰符也可以串联：

```html
<a @click.stop.prevent="handle"></a>
```

只有修饰符：

```html
<form @sublit.prevent></form>
```

```html
<!-- 添加事件侦听器时使用事件捕获模式 -->
<div @click.capture="handle">...</div>
```

```html
<!-- 只当事件在该元素本身(而不是子元素)触发时触发回调 -->
<div @click.self="handle">...</div>
```

```html
<!-- 只触发一次，组件同样适用 -->
<div @click.once="handle">...</div>
```

键盘监听事件：

```html
<input @keyup.13="submit">
```

除了具体的某个 `keyCode` 外， `Vue` 还提供了一些快捷键名称：

- `.enter`

- `.tab`

- `delete` (捕获 删除 和 退格键)

- `esc`

- `space`

- `up`

- `down`

- `left`

- `right`

按键可以组合使用，或配合鼠标使用：

- `.ctrl`

- `alt`

- `shift`

- `meta` ( `Mac` 上是 `Command` 键， `Windows` 上是窗口键 )

```html
<!-- shift + s -->
<input @keyup.shift.83="handleSave">
```

##### v-model

> 表单类控件承载了一个网页的录入与交互，`Vue` 中使用 `v-model` 完成表单的数据双向绑定。

- 基本用法

```html
<div id="app">
    <input type="text" v-model="message" placeholder="输入...">
    <p>输入的内容是：{{ message }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        }
    })
</script>
```

对于文本域(`textarea`)也是同样的用法。

可以用 `@input` 代替 `v-model`，事实上，`v-model` 也是一个特殊的语法糖，只不过它会在不同的表单上智能处理。

```html
<div id="app">
    <input type="text" @input="handleInput" placeholder="输入...">
    <p>输入的内容是：{{ message }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: '',
        },
        methods: {
            handleInput: function(e) {
                this.message = e.target.value;
            }
        }
    })
</script>
```

单选按钮：

> 单选按钮在单独使用时，不需要 `v-model`，直接使用 `v-bind` 绑定一个布尔类型的值，为真时为选中。

```html
<div id="app">
    <input type="radio" :checked="picked" @click="handleClick" name="radio" id="radio">
    <label for="radio">单选按钮</label>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            picked: true
        },
        methods: {
            handleClick: function () {
                this.picked = !this.picked;
            }
        }
    })
</script>
```

配合 `v-model` 和 `value` 组合实现互斥效果：

```html
<div id="app">
    <input type="radio" v-model="picked" name="html" id="html" value="html">
    <label for="html">HTML</label>

    <input type="radio" v-model="picked" name="js" id="js" value="js">
    <label for="js">JS</label>

    <input type="radio" v-model="picked" name="css" id="css" value="css">
    <label for="css">CSS</label>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            picked: 'js'
        }
    })
</script>
```

复选框：

> 复选框单独使用时，使用 `v-model` 绑定一个布尔值。

```html
<div id="app">
    <input type="checkbox" v-model="checked" name="checked" id="checked">
    <label for="checked">选择状态： {{ checked }}</label>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            checked: true
        }
    })
</script>
```

多个复选框(以数组绑定值)：

```html
<div id="app">
    <input type="checkbox" v-model="checked" name="html" id="html" value="html">
    <label for="html">HTML</label>

    <input type="checkbox" v-model="checked" name="js" id="js" value="js">
    <label for="js">JS</label>

    <input type="checkbox" v-model="checked" name="css" id="css" value="css">
    <label for="css">CSS</label>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            checked: ['html', 'css']
        }
    })
</script>
```

选择列表：

> 下拉选择器，也分为单选和多选两种方式。

```html
<div id="app">
    <select name="selected" v-model="selected" id="selected">
        <option value="html">HTML</option>
        <option value="js">JS</option>
        <option value="css">CSS</option>
    </select>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            selected: 'js',
        }
    })
</script>
```

在业务中，`<option>` 经常用 `v-for` 动态输出，`value` 和 `text` 也是用 `v-bind` 来动态输出：

```html
<div id="app">
    <select name="selected" v-model="selected" id="selected">
        <option
            v-for="option in options"
            :value="option.value">{{ option.text }}</option>
    </select>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            selected: 'js',
            options: [{
                text: 'HTML',
                value: 'html'
            }, {
                text: 'JavaScript',
                value: 'js'
            }, {
                text: 'CSS',
                value: 'css'
            }]
        }
    })
</script>
```

虽然用选择列表 `<select>` 控件可以简单的完成下拉选择的需求，但是在实际业务中反而不常用，

因为它的样式依赖平台和浏览器，无法统一，也不太美观，功能也受限，比如不支持搜索，

所以常见的解决方案是使用 `<div>` 模拟一个类似的控件。

- 绑定值

> 在业务中，往往需要绑定一个动态数据，这时可以使用 `v-band` 来实现。

单选按钮：

```html
<div id="app">
    <input type="radio" name="radio" v-model="picked" :value="value">
    <label for="radio">单选按钮</label>
    <p>{{ picked }}</p>
    <p>{{ value }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            picked: false,
            value: 123,
        },
    })
</script>
```

在选中时，`app.picked === app.value`，值都是 `123`。

复选框：

```html
<div id="app">
    <input 
        type="checkbox" 
        name="checked" 
        id="checked"
        v-model="toggle"
        :true-value="value1"
        :false-value="value2">
    <label for="checked">复选框</label>
    <p>{{ toggle }}</p>
    <p>{{ value1 }}</p>
    <p>{{ value2 }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            toggle: false,
            value1: 'a',
            value2: 'b',
        },
    })
</script>
```

勾选时，`app.toggle === app.value1`；未勾选时，`app.toggle === app.value2`。

选择列表：

```html
<div id="app">
    <select name="selected" id="selected">
        <option 
            :value="number">123</option>
    </select>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            selected: '',
            number: 456
        },
    })
</script>
```

当选中时，`app.selected` 是一个 `Object`，`app.selected.number === 456`

- 修饰符

> 与事件的修饰符类似，`v-model` 也有修饰符，用于控制数据同步的时机。

`.lazy`:

在输入框中，`v-model` 默认是在 `input` 事件中同步输入框的数据，使用修饰符 `.lazy` 会转变为在 `change` 事件中同步。

```html
<div id="app">
    <input type="text" v-model.lazy="message">
    <p>{{ message }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        },
    })
</script>
```

这时，`message` 并不是实时改变的，而是在失去焦点或按回车时才更新。

`.number`:

使用修饰符 `.number` 可以将输入转换为 `Number` 类型，否则虽然输入的是数字，但它的类型其实是 `String`，在数字输入框中会比较有用。

```html
<div id="app">
    <input type="text" v-model.number="message">
    <p>{{ typeof message }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: 123
        },
    })
</script>
```

`.trim`:

修饰符 `.trim` 可以自动过滤输入的首尾空格。

```html
<div id="app">
    <input type="text" v-model.trim="message">
    <p>{{ message }}</p>
</div>
<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        },
    })
</script>
```
