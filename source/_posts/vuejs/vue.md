---
title: Vuejs 整理笔记
date: 2019-8-13
category: 
    - Vue
tags:
    - Vue
    - 前端框架
thumbnail: /images/bg-20.jpg

---

#### `Vue.js` 整理笔记

> `Vue.js` 是一套用于构建用户界面的轻量级的MVVM渐进式前端框架，通过简单的 `API` 提供高效的数据绑定和灵活的组件系统。

<!-- more -->

##### 基础语法

###### 创建第一个 `Vue` 实例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Vue.js</title>
    <!-- 在head中引入Vue.js的支持 -->
    <script src="./vue.js"></script>
    <!-- 也可以引用CDN库 -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/vue@2.5.22/dist/vue.js"></script> -->

</head>
<body>
    //双括号绑定数据
    <div id="root">{{msg}}</div>

    <script>
        // 创建一个Vue实例并作数据绑定
        new Vue({
            el: '#root',
            data: {
                msg: 'Hello Vue!'
            }
        })
        // 原生JS写法
        // var dom = document.getElementById("root");
        // dom.innerHTML = "HELLO!";
    </script>
</body>
</html>
```
`el`：是 `element` 的缩写，指要操作或绑定的元素

`data`：写需要操作改变的内容。

> 注意：学 `javascript` 时，很多时候都是操作 `DOM` 的模式，而 `vue` 则更多是操作数据的双向绑定。

###### 挂载点、模板与实例

- 挂载点：

需要操作的元素。例如：`<div id="app"></div>` 并在实例中通过 `el: '#app'` 进行数据的双向绑定。

> Vue只会去处理挂载点下的内容。

- 模板：

挂载点内部的内容我们把它叫做模板内容。也可以将模板在实例中编写，不过渲染时要加上 `H5` 标签例如：

```html
<div id="root"></div>

<script>
    new Vue({
        el: '#root',
        template: '<h1>{{msg}}<h1>',
        data: {
            msg: 'Hello Vue!'
        }
    })
</script>
```

- `Vue` 实例：

自动根据 `el`，`template`，`data` 数据生成最终的效果。最后放在挂载点之中。

###### `Vue` 实例中的数据、事件和方法

- 插值法:

- 插值表达式
    - 双大括号`{{msg}}`

- 指令
    - `v-text` 和 `v-html`
    - 监听事件指令 `v-on`
    - 属性绑定指令 `v-bind`
    - 表单输入绑定指令 `v-model`
    - 计算属性
    - 条件渲染：`v-if` 和 `v-show`

- `v-text`:

```html
<div id="root">
        <div v-text="content"></div>
    </div>

    <script>
        var app = new Vue({
            el: '#root',
            data: {
                msg: 'Hello Vue!',
                content: '<h2>HEOOL!!!</h2>'
            }
        })
    </script>
```

> 输出：`<h2>HEOOL!!!</h2>`
    
- `v-html`:

```html
<div id="root2">
        <div v-html="content"></div>
    </div>

    <script>
        var app2 = new Vue({
            el: '#root2',
            data: {
                content: '<h2>Hello!!!</h2>'
            }
        })
    </script>
```


![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5xvqjt0oaj217005wt8s.jpg)


- `v-on`:监听事件

```html
<div id="app">
        <!-- v-on:click绑定点击事件 -->
        <div v-on:click='handleClick'>{{content}}</div>
    </div>

    <script>
        var app = new Vue({
            el: '#app',
            data: {
                content: 'Hello',
            },
            // 执行方法
            methods: {
                handleClick: function() {
                    // 通过操作实例里面的数据，Vue会自动更新。不需要操作DOM
                    this.content = 'Vue!'
                }
            }
        })
    </script>
```

> `v-on`:可以简写为`@`，即`v-on:click`等价于`@click`

###### `Vue` 中的属性绑定和双向数据绑定

- `v-bind`：属性绑定

```html
<div id="app2">
        <div v-bind:title='title'>HELLO WORLD!</div>
    </div>

    <script>
        var app2 = new Vue({
            el: '#app2',
            data: {
                title: 'This is hello world'
            }
        })
    </script>
```

> `v-bind`:可以简写为：，即`v-bind:title `等价于`:title`

- `v-model`：双向数据绑定

```html
<div id="app3">
        <input type="text" v-model='content'>
        <div v-text='content'></div>
    </div>

    <script>
        var app3 = new Vue({
            el: '#app3',
            data: {
                content: 'This is content'
            }
        })
    </script>
```

> 当 `input` 框中的数据改变，`div` 中 `content` 的内容也会相应的发生改变。

###### `Vue` 中的计算属性和侦听器

- 计算属性：

```html
<div id="app4">
        姓：<input type="text" v-model='firstName'>
        名：<input type="text" v-model='lastName'>
        <div>{{fullName}}</div>
    </div>

    <script>
        var app4 = new Vue({
            el: '#app4',
            data: {
                firstName: '',
                lastName: ''
            },
            computed: {
                fullName: function() {
                    return this.firstName + ' ' + this.lastName
                }
            }
        })
    </script>
```

- `侦听器`：

```html
<div id="app4">
        姓：<input type="text" v-model='firstName'>
        名：<input type="text" v-model='lastName'>
        <div>{{fullName}}</div>
        <div>{{count}}</div>
    </div>

    <script>
        var app4 = new Vue({
            el: '#app4',
            data: {
                firstName: '',
                lastName: '',
                count: 0
            },
            // 计算属性
            computed: {
                fullName: function() {
                    return this.firstName + ' ' + this.lastName
                }
            },
            // 侦听器
            watch: {
                firstName: function() {
                    this.count++
                },
                lastName: function() {
                    this.count++
                }
            }
        })
    </script>
```

###### `v-if`、`v-show` 和 `v-for` 指令

- `v-if`：控制 `DOM` 存在与否

```html
<div id="app5">
        <div v-if='show'>Hello</div>
        <button @click='handleClick'>Toggle</button>
    </div>

    <script>
        var app5 = new Vue({
            el: '#app5',
            data: {
                show: true
            },
            methods: {
                handleClick: function() {
                    this.show = !this.show;
                }
            }
        })
    </script>
```

- `v-show`：控制 `DOM` 的显示与否

```html
<div id="app5">
        <div v-show='show'>Hello</div>
        <button @click='handleClick'>Toggle</button>
    </div>

    <script>
        var app5 = new Vue({
            el: '#app5',
            data: {
                show: true
            },
            methods: {
                handleClick: function() {
                    this.show = !this.show;
                }
            }
        })
    </script>
```

> 区别：`v-if` 是直接将 `div` 在 `DOM` 中移除；而 `v-show` 是通过 `display：none` 来达到隐藏，`DOM` 结构依然存在。

- `v-for`：循环显示

```html
<div id="app5">
        <div v-show='show'>Hello</div>
        <button @click='handleClick'>Toggle</button>
        <ul>
            <!-- 方法一 -->
            <!-- <li v-for='item in list' v-text='item'></li> -->
            <!-- 方法二 -->
            <li v-for='(item, index) of list' :key='index'>{{item}}</li>
        </ul>
    </div>

    <script>
        var app5 = new Vue({
            el: '#app5',
            data: {
                show: true,
                list: [
                    1, 2, 3
                ]
            },
            methods: {
                handleClick: function() {
                    this.show = !this.show;
                }
            }
        })
    </script>
```

##### `Vue` 中的组件

> 使用 `Vue` 中的组件开发一个 `TodoList`

###### `todolist` 功能开发

`Add`:

```html
<!-- TodoList -->
<div id="app6">
    <input v-model='inputValue'>
    <button @click='handleSubmit'>提交</button>
    <ul>
        <li v-for='item in list'>{{item}}</li>
    </ul>
</div>

<script>
    new Vue({
        el: '#app6',
        data: {
            inputValue: 'TODO',
            list: []
        },
        methods: {
            handleSubmit: function() {
                this.list.push(this.inputValue);
                this.inputValue = ''
            }
        }
    })
</script>
```

###### `TodoList` 中组件的拆分

- 全局组件：

```html
    ...
        <ul>
            <todo-item></todo-item>
        </ul>
    ...
<script>
        // 创建全局组件
        Vue.components('todo-item', {
            template: '<li>item</li>'
        })
</script>
```

- 局部组件：

```html
<script>
    // 创建全局组件
    // Vue.components('todo-item', {
    //     template: '<li>item</li>'
    // })

    // 局部组件
    var TodoItem = {
        template: '<li>item</li>'
    }

    new Vue({
        el: '#app6',
        // 声明（注册）局部组件
        components: {
            'todo-item' : TodoItem
        },
        data: {
            inputValue: 'TODO',
            list: []
        },
        methods: {
            handleSubmit: function() {
                this.list.push(this.inputValue);
                this.inputValue = ''
            }
        }
    })
</script>
```

- 父组件向子组件传参

```html
<!-- TodoList -->
<div id="app6">
    <input v-model='inputValue'>
    <button @click='handleSubmit'>提交</button>
    <ul>
        <todo-item
            v-for='(item, index) of list'
            :key='index'
            :content='item' 
        ></todo-item>
        <!-- 以属性形式传参:content -->
    </ul>
</div>

<script>
    // 创建全局组件
    Vue.component('todo-item', {
        // 子组件接收父组件传进来的参数
        props: ['content'],
        template: '<li>{{content}}</li>'
    })
    
    new Vue({
        el: '#app6',
        data: {
            inputValue: 'TODO',
            list: []
        },
        methods: {
            handleSubmit: function() {
                this.list.push(this.inputValue);
                this.inputValue = ''
            }
        }
    })
</script>
```

###### 实现TosoList的删除功能

- 子组件向父组件通信

```html
<!-- TodoList -->
<div id="app6">
    <input v-model='inputValue'>
    <button @click='handleSubmit'>提交</button>
    <ul>
        <todo-item
            v-for='(item, index) of list'
            :key='index'
            :content='item' 
            :index='index'
            @delete='handleDlete'
        ></todo-item>
        <!-- 以属性形式传参:content -->
        <!-- 父组件监听子组件delete事件，并执行handleDlete方法 -->
    </ul>
</div>

<script>
    // 创建全局组件
    Vue.component('todo-item', {
        // 子组件接收父组件传进来的参数
        props: ['content', 'index'],
        template: '<li @click="handleClick">{{content}}</li>',
        methods: {
            handleClick: function() {
                // 发布订阅模式，子组件发布事件，父组件订阅方法
                this.$emit('delete', this.index);    // 调用$emit方法，触发一个delete自定义事件传入index值
            }
        }
    })

    new Vue({
        el: '#app6',
        data: {
            inputValue: 'TODO',
            list: []
        },
        methods: {
            handleSubmit: function() {
                this.list.push(this.inputValue);
                this.inputValue = ''
            },

            handleDlete: function(index) {
                // 实现删除功能
                this.list.splice(index, 1);
            }
        }
    })
</script>
```

##### `Vue-cli`（脚手架工具）的使用

###### 脚手架的使用

> 在考虑到在大型项目中的可维护性，真实的 `Vue` 项目开发过程中，我们会借助 `Webpack` 的打包工具，帮助构建大型项目的开发目录。`Vue` 提供了一个官方的 `CLI`，为单页面应用 (`SPA`) 快速搭建繁杂的脚手架。

- 安装 `node` 和 `npm` 环境

官网`https://nodejs.org/en/download/`下载安装 `node`，`npm` 会附带安装

终端`node -v`,`npm -v`查看是否成功，打印出版本号则为安装成功。

- 安装使用淘宝 `npm` 镜像，加快访问速度

官网`http://npm.taobao.org/`

终端命令行输入`npm install -g cnpm --registry=https://registry.npm.taobao.org`

之后的 `npm` 命令可以用 `cnpm` 进行替换，速度上会快一点

- 在终端进行全局安装 `Vue-cli`

```shell
npm install -g vue-cli
```

- 创建一个基于Webpack模板的新项目

```shell
vue init webpack my-project
```

涉及项目名、项目描述、作者默认可随意，项目构建选 `Runtime + Compiler`、是否安装 `vue-router`视情况而定、代码检查工具`ESLint`、单元测试工具暂时可以选`NO`、然后选择 `npm` 安装

- 进入项目，安装依赖

```shell
cd my-project
cnpm install 
cnpm run dev
```

###### 组件化开发 `TodoList`

- `main.js`：

```js
import Vue from 'vue'
import TodoList from './TodoList'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { TodoList },
  template: '<TodoList/>'
})
```

- `TodoList.vue`：

```html
<template>
  <div id="app">
    <h1 class="title">Todo Something</h1>
    <input v-model="inputValue" @keyup.enter="handleSubmit">
    <button @click="handleSubmit">提交</button>
    <ul>
      <todo-item 
        v-for="(item, index) of list"
        :key="index"
        :content="item"
        :index="index"
        @delete="handleDelete"
        ></todo-item>
    </ul>
  </div>
</template>

<script>
import TodoItem from './components/TodoItem'

export default {
  name: 'App',
  components: {
    'todo-item': TodoItem
  },
  data () {
    return {
      inputValue: '',
      list: []
    }
  },
  methods: {
    handleSubmit: function() {
      if (this.inputValue) {
        this.list.push(this.inputValue);
        this.inputValue = ''
      }
    },
    handleDelete: function(index) {
      this.list.splice(index, 1);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.title {
  color: #42b983;
}

button {
  background: #42b983;
}
</style>
```

`components.TodoItem.vue`:

```html
<template>
  <div class="todoitem">
    <li @click="handleDelete">{{content}}</li>
  </div>
</template>

<script>
export default {
  props: ['content', 'index'],
  methods: {
    handleDelete: function () {
      this.$emit('delete', this.index)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
```

至此，已经将原项目改为组件化的形式。
