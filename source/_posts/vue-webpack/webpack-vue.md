---
title: Vue.js 阅读笔记（四）
date: 2020-1-14
category:
    - Vue
tags: 
    - Vue
thumbnail: /images/asuka/asu-17.jpg

---

### Vue.js 阅读笔记（四）

> 系统、框架性的认识 `Vue`。`webpack`、`vue-router`、`vuex` 和工程化。

<!-- more -->

> 高效开发离不开基础工程的搭建，开始之前需要提前安装 `Node.js` 和 `NPM`，如果不熟悉它们，可以先查阅相关资料，完成安装并了解 `npm` 最基本的用法。

#### 前端工程化和 `webpack`

近几年来，前端领域发展迅速，前端的工作早已不再是切几张图那么简单，项目比较大时，可能会多人协同开发。模块化、组件化、`CSS` 预编译等概念也成了经常讨论的话题。

##### `webpack`

通常，前端工程化项目需要解决以下问题：

- `JavaScript`、`CSS` 代码的合并和压缩。

- `CSS` 预处理：`Less`、`Sass`、`Stylus` 的编译。

- 生成雪碧图 (`CSS Sprite`)

- `ES6` 转 `ES5`

- 模块化

`....`

这些问题，我们都可以通过前端模块打包提供一个解决方案，也就是 `webpack`。打包后的代码已经不是你写的代码，其中夹杂了很多 `webpack` 自身的模块处理代码，需要理解 `编译` 的概念。

![webpack](http://images.akashi.org.cn/Fu7LwhdZ5-nS2KXTHHhs36pvk5Zt)

在左边的是业务中写的各种格式的文件，比如 `typescript`、`less`、`jpg`、`vue` 等，这些格式的文件通过特定的加载器(`Loader`)编译以后，最终统一生成为 `.js`、`.css`、`.png` 等静态资源文件。

在 `webpack` 中，一张图片，一个 `css`甚至一个字体，都称为模块(`Module`)，彼此存在依赖关系，`webpack` 就是来处理模块间的依赖关系的，并把它们进行打包。

在 `webpack` 中加载文件，是在 `.js` 文件中导入，如：

```js
import 'src/styles/index.css';
```

`import` 是在 `ES 2015` 中的使用，这里也可以写成：

```js
require('src/styles/index.css')
```

在打包时，`index.css` 会被打包进一个 `.js` 文件中，通过动态创建 `<style>` 的形式来加载，当然，也可以进一步配置，在打包编译时，把所有的 `css` 文件提取出来，生成一个 `css` 的文件。

##### `SPA`

`webpack` 的主要适用场景是单页面应用(`SPA`)，`SPA` 通常是由一个 `html` 文件和一堆按需加载的 `js` 文件组成，它的 `html` 结构非常简单，比如：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>webpack app</title>
    <link rel="stylesheet" href="dist/main.css">
</head>
<body>
    <div id="app"></div>
    <script src="dist/main.js"></script>
</body>
</html>
```

只有一个 `<div>` 节点，所有的代码都集成在了 `main.js` 中，理论上它可以实现知乎、淘宝这样的大型项目。

##### `export` 和 `import`

这两个语法是在编写模块化项目中大量使用的，是 `ES6` 中的语法，需要做一些简单的了解。

`export` 和 `import` 是用来导出和导入模块的，一个模块就是一个 `js` 文件，它拥有独立的作用域，里面定义的变量外部是无法获取的。

比如将一个配置文件作为模块导出：

```js
// config.js
var Config = {
    version: '1.0.0'
};

export {
    Config
};
```

或 

```js
// config.js
export var Config = {
    version: '1.0.0'
};
```

其中，无论是 `变量`，`函数`，`数组`，`常量` 都可以导出。

导出模块后，在需要使用模块的文件使用 `import` 再导入，就可以在这个文件内使用这些模块了。

```js
// main.js
import { Config } from './config.js';

console.log(Config) // { version: '1.0.0' }
```

在以上几个例子中，导入的模块都是在 `export` 文件中设置的，也就是说用户必须预先知道这个名称叫什么，比如 `Config`。而有时候用户不想去了解名称是什么，只是把模块的功能拿来使用，或者想自己自定义名称，这时可以使用 `export default` 来输出默认的模块。

```js
// config.js
export default {
    version: '1.0.0'
};
```

```js
// main.js
import conf from './config.js';

console.log(conf); // { version: '1.0.0' }
```

当然，你也可以规定默认模块的名称：

```js
// config.js
var config = {
    version: '1.0.0'
};

module.exports = config;
```

这里的 `module.exports = config;` 相当于 `export default config;`。

#### `Vue CLI`

> `Vue CLI` 是一个基于 `Vue.js` 进行快速开发的项目脚手架，基于 `webpack` 构建。

##### 安装

```js
npm install -g @vue/cli
```

安装完成之后，就可以在命令行中访问 `vue` 命令，比如可以用来检查版本验证是否安装成功：

```js
vue --version
```

##### 快速原型开发

可以使用 `vue serve` 和 `vue build` 命令对单个 `*.vue` 文件进行快速原型开发，不过这需要先额外安装一个全局的扩展：

```js
npm install -g @vue/cli-service-global
```

注意，这仅仅用于简单的快速测试，实际开发中并不推荐。

##### 使用 `Vue CLI` 手脚架快速搭建一个工程化项目

- 创建一个新项目

```js
vue create demo
```

开始创建，提示选取一个预设，可以使用默认的预设，这个默认的设置非常适合快速创建一个新项目的原型，而手动设置则提供了更多的选项，它们是面向生产的项目更加需要的。

![vue-create](http://images.akashi.org.cn/FpOw9wJicjVZ-dYt9wofC41FSkjC)

![preset](http://images.akashi.org.cn/FqmUv4HUmnqDbn5Bq6i-pLbiHQsn)

等待创建完成之后，就可以根据提示，进入项目，启动服务：

```js
cd demo
npm run serve
```

这样，一个新建的工程化项目就在对应的端口下启动了，可以根据提示在浏览器查看启动的项目。

#### 前端路由与 `vue-router`

##### 前端路由

前端路由，即前端来维护一个路由规则。

实现有两种，一种是利用 `url` 的 `hash`，就是常说的锚点(`#`)，`JavaScript` 通过 `hashChange` 事件来监听 `url` 的改变，`IE7` 以下需要轮询；

另一种就是 `HTML5` 的 `History` 模式。它使 `url` 看起来像普通网站那样，以 `/` 分隔，但页面并没有跳转，不过使用这种模式需要服务端支持，服务端在接收到所有的请求后，都将指向同一个 `html` 不然会出现 `404`。因此，`SPA` 只有一个 `html`，整个网站的所有内容都在一个 `html` 里，通过 `JavaScript` 来处理。

前端路由可以带来页面的持久性、前后端彻底分离等优势，下面结合具体的框架 `vue-router` 进行介绍。

##### `vue-router` 安装

```js
npm install --save vue-router
```

如果在一个模块化工程中使用它，必须要通过 `Vue.use()` 明确地安装路由功能：

```js
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
```

##### 基本使用

每个页面对应一个组件，也就是对应一个 `.vue` 文件。在 `src` 目录下创建 `views` 目录，用于存放所有的页面，然后在 `views` 下创建 `index.vue` 和 `about.vue` 两个文件。

```html
<!-- index.vue -->
<template>
    <div>Index</div>
</template>

<script>
export default {
    name: 'index'
}
</script>

<style lang="stylus" scoped>

</style>
```

```html
<!--  about.vue -->
<template>
    <div>About</div>
</template>

<script>
export default {
    name: 'about'
}
</script>

<style lang="stylus" scoped>

</style>
```

回到 `main.js` 中进行配置，创建一个数组来制定路由匹配列表，每一个路由映射一个组件：

```js
// main.js
import Vue from 'vue'
import App from './App.vue'

import VueRouter from 'vue-router'

Vue.use(VueRouter);

Vue.config.productionTip = false

const Routers = [{
    path: '/index',
    name: 'index',
    component: (resolve) => require(['./views/index.vue'], resolve)
    // component: () => import('./views/index.vue')
  }, {
    path: '/about',
    name: 'about',
    component: (resolve) => require(['./views/about.vue'], resolve)
  }
];

const router = new VueRouter({
  mode: 'history',
  routes: Routers
});

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app')
```

`Routers` 里每一项的 `path` 属性就是指定的当前匹配的路径，`component` 是映射的组件。

`webpack` 会把每一个路由打包成一个 `js` 文件，在请求到该页面时，才会去加载这个页面的 `js`，也就是异步实现的懒加载(按需加载)

这样做的好处是不需要在打开首页的时候就把所有的页面内容全部加载进来，只在访问时才加载。

如果非要一次性加载，可以写为：

```js
{
    path: '/index',
    component: require('./views/index.vue')
}
```

最后，在根实例 `app.vue` 中添加一个路由视图 `<router-view>` 来挂载所有的路由组件：

```html
<!-- app.vue -->
<template>
  <div id="app"></div>
</template>

<script>

export default {
  name: 'app',
}
</script>
```

`<router-view>` 会根据当前路由动态渲染不同的页面组件。网页中一些公共的部分，比如顶部的导航栏、侧边导航栏、底部的版权信息，这些可以直接写在 `app.vue` 里面，与 `<router-view>` 同级，路由切换时，切换的是 `<router-view>` 挂载的组件，其他内容不会发生变化。

`npm run serve` 启动服务，就可以通过 `127.0.0.1:8080/index` 和 `127.0.0.1:8080/about` 访问页面了。

##### 结构梳理

现在新建一个 `router` 目录，用于路由配置。

`router` 下新建 `index.js` 将路由部分从 `main.js` 中提出：

```js
// router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const Routers = [{
    path: '*',
    redirect: '/index'
  }, {
    path: '/index',
    name: 'index',
    component: (resolve) => require(['../views/index.vue'], resolve)
  }, {
    path: '/about',
    name: 'about',
    component: (resolve) => require(['../views/about.vue'], resolve)
  }
];

const router = new VueRouter({
  mode: 'history',
  routes: Routers
});

export default router
```

在路由列表中添加一项，用于访问路径不存在时，重定向到首页：

```js
{
    path: '*',
    redirect: '/index'
}
```

精简后的 `main.js`

```js
// main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router/index'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
```

路由列表的 `path` 也可以带参数，比如个人主页的场景，一部分路由是动态的 `/user/12345`，其中 `id` 是动态的，但是它们都路由到同一个页面，这个页面里面期望获取这个 `id`，然后请求相关数据。

具体路由参数配置：

```js
// main.js
const Routers = [{
    path: '/user/:id',
    component: (resolve) => require(['../views/user.vue'], resolve)
}];
```

在 `views` 下新建 `user.vue` 文件

```html
<!-- user.vue -->
<template>
    <div>User {{ $route.params.id }}</div>
</template>

<script>
export default {
    name: 'user'
}
</script>
```

使用 `this.$route` 可以访问到当前路由的很多信息，开发中会经常用到里面的数据。

##### 跳转

`vue-router` 有两种跳转页面的方法，第一种是使用内置的  `<router-link>` 组件，它会被渲染为一个 `<a>` 标签：

```html
 <!-- index.vue -->
<template>
    <div>
        <div>Index</div>
        <router-link to="/about">about</router-link>
    </div>
</template>

<script>
export default {
    name: 'index'
}
</script>
```

它的用法和一般组件一样，`to` 是一个 `prop`，需要指定跳转的路径，也可以使用 `v-bind` 动态设置。使用 `<router-link>`，在 `HTML5` 的 `History` 模式下会拦截点击，避免浏览器重新加载页面。

`<router-link>` 常用 `prop`:

- `tag`
    - 可以指定渲染成什么标签

```html
<router-link to="/about" tag="li">
```

- `replace`
    - 使用 `replace` 不会留下 `History` 记录，所以不能使用后退键和返回上一个页面

```html
<router-link to="/about" replace>
```

- `active-class`
    - 对应的路由匹配成功后，会自动给当前元素设置一个名为 `router-link-active` 的 `class`，设置 `prop: active-class` 可以修改默认名称

另一种方法是通过 `Javascript` 进行设置，类似于 `window.location.href`，使用 `router` 实例的方法，通过点击事件进行跳转：

```html
<!-- about.vue -->
<template>
    <div>
        <div>About</div>
        <button @click="handleRouter">go to user</button>
    </div>
</template>

<script>
export default {
    name: 'about',
    methods: {
        handleRouter () {
            this.$router.push('/user/123');
        }
    }
}
</script>
```

`$router` 的其他方法：

- `replace`
    - 类似于 `<router-link>` 的 `replace` 功能，它不会向 `history` 添加新记录，而是替换掉当前的 `history` 记录，如：`this.$router.replace('/user/123')`

- `go`
    - 类似于 `window.history.go()`，在 `history` 记录中向前或者后退多少步，参数是整数。

```js
this.$router.go(-1);
this.$router.go(2)
```

##### 高级用法

> 在 `SPA` 项目中修改网页标题。

网页标题是通过 `<title></title>` 来显示的，但是 `SPA` 只有一个固定的 `html`，切换到不同页面时，标题并不会发生改变，那么该如何修改标题呢？

比较理想的一个思路是，在页面发生路由变化时，统一设置。`vue-router` 提供了导航钩子 `beforeEach` 和 `afterEach`，它们会在路由即将改变前和改变后触发，所以设置标题可以在 `beforeEach` 钩子完成。

```js
// router/index.js
const Rourters = [{
    path: '/index',
    name: 'index',
    meta: {
        title: '首页'
    },
    component: (resolve) => require(['../views/index.vue'], resolve)
},{
    path: '/about',
    name: 'about',
    meta: {
        title: '关于'
    },
    component: (resolve) => require(['../views/about.vue'], resolve)
},{
    path: '/user:id',
    name: 'user',
    meta: {
        title: '个人主页'
    },
    component: (resolve) => require(['../views/user.vue'], resolve)
}, {
    path: '*',
    redirect: '/index'
}];

const router = new VueRouter({
  mode: 'history',
  routes: Routers
});

router.beforeEach((to, from, next) => {
    window.document.title = to.meta.title;
    next();
});

export default router
```

导航钩子有 `3` 个参数：

- `to`

    - 即将要进入的目标的路由对象

- `from`

    - 当前导航即将要离开的路由对象

- `next`

    - 调用该方法后，才能进入下一个钩子

路由列表的 `meta` 字段可以自定义一些信息，比如将每个页面的 `title` 写入 `meta` 来统一维护，`beforeEach` 钩子可以ongoing路由对象 `to` 里获取 `meta` 信息，从而改变标题。

#### 状态管理与 `Vuex`

##### 状态管理与使用场景

一个组件可以分为数据(`model`)和视图(`view`)，数据更新时，视图也会自动更新。在视图中又可以绑定一些事件，它们触发 `methods` 里的指定方法，从而可以改变数据、更新视图，这时一个组件基本的运行模式。

但在实际的业务开发中，经常有跨组件共享数据的需求，`Vuex` 就是用来统一管理组件状态的，它定义的一系列规范来使用和操作数据，使组件应用更加高效。

使用 `Vuex` 有一定的门槛和复杂性，它的主要使用场景是大型单页应用，更适合多人协同开发。如果项目不是很复杂，或者希望短期内见效，需要考虑是否真的有必要使用 `Vuex`，一个简单的 [store模式](https://cn.vuejs.org/v2/guide/state-management.html#%E7%AE%80%E5%8D%95%E7%8A%B6%E6%80%81%E7%AE%A1%E7%90%86%E8%B5%B7%E6%AD%A5%E4%BD%BF%E7%94%A8) 就满足需求了。

##### `Vuex` 安装

```js
npm install vuex --save
```

在一个模块化的打包系统中，必须显式地通过 `Vue.use()` 来安装 `Vuex`：

```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
```

##### `Vuex` 基本使用

现在我们从一开始就考虑高效的结构，先新建一个 `store` 目录，在下面新建 `index.js` 做状态管理配置：

```js
// store/index.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
    },
    mutations: {
    },
});
```

然后在 `main.js` 里面引入并声明：

```js
// main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
```

这样，一个基本的 `Vuex` 框架就构建好了，仓库 `store` (指 `store/index.js`) 包含了应用的数据（状态）和操作过程。`Vuex` 里的数据都是响应式的，任何组件使用同一 `store` 的数据时，只要 `store` 的数据发生变化，对应的组件也会立即更新。

数据保存在 `Vuex` 选项的 `state` 字段内，想要更改 `Vuex` 的 `store` 中的状态的唯一方法是提交 `mutation`，通过这两个方法，就可以完成大部分数据状态管理的操作，下面通过一个计数器的例子了解 `Vuex` 的使用。

首先，定义一个数据 `count`，初始值为 `0`，在其他组件通过 `$store.state.count` 读取值：

```js
// store/index.js
export default new Vuex.Store({
    state: {
        count: 0
    },
    mutations: {
    },
})
```

获取数据，这里我们使用一个计算属性接收数据：

```html
 <!-- index.vue -->
<template>
    <div>
        <div>Index</div>
        <router-link to="/about">about</router-link>
        <div>{{ count }}</div>
    </div>
</template>

<script>
export default {
    name: 'index',
    computed: {
        count () {
            return this.$store.state.count;
        }
    }
}
</script>
```

在组件内通过显式的提交 `mutations` 可以改变 `state` 中的数据：

```js
// store/index.js
export default new Vuex.Store({
    state: {
        count: 0
    },
    mutations: {
        increment (state) {
            state.count ++;
        },
        decrease (state) {
            state.count --;
        }
    },
})
```

在组件中，通过 `this.$store.commit` 方法来执行 `mutations`。在 `index.vue` 中添加两个按钮用于加减：

```html
<!-- index.vue -->
<template>
    <div>
        <div>Index</div>
        <router-link to="/about">about</router-link>
        <div>{{ count }}</div>
        <button @click="handleIncrement">+1</button>
        <button @click="handleDecrease">-1</button>
    </div>
</template>

<script>
export default {
    name: 'index',
    computed: {
        count () {
            return this.$store.state.count;
        }
    },
    methods: {
        handleIncrement () {
            this.$store.commit('increment');
        },
        handleDecrease () {
            this.$store.commit('decrease');
        }
    }
}
</script>
```

这看起来像 `JavaScript` 的观察者模式，组件只负责提交一个事件名，`Vuex` 对应的 `mutations` 来完
成对应的业务逻辑。

`mutations` 还可以接受第二个参数，可以是数字、字符串或者对象等类型，比如我们传入一个默认参数，指定增加的值：

```js
// store/index.js
export default new Vuex.Store({
    state: {
        count: 0
    },
    mutations: {
        increment (state, n) {
            n = n || 1;
            state.count += n;
        },
        decrease (state) {
            state.count --;
        }
    },
})
```

```html
<!-- index.vue -->
<template>
    <div>
        <div>Index</div>
        <router-link to="/about">about</router-link>
        <div>{{ count }}</div>
        <button @click="handleIncrement">+1</button>
        <button @click="handleDecrease">-1</button>
        <button @click="handleIncrementMore">+5</button>
    </div>
</template>

<script>
export default {
    name: 'index',
    computed: {
        count () {
            return this.$store.state.count;
        }
    },
    methods: {
        handleIncrement () {
            this.$store.commit('increment');
        },
        handleDecrease () {
            this.$store.commit('decrease');
        },
        handleIncrementMore () {
            this.$store.commit('increment', 5);
        }
    }
}
</script>
```

如果一个参数不够，可以传入一个对象：

```js
// store/index.js
mutations: {
    increment (state, params) {
        state.count += params.count;
    }
}
```

```js
// index.vue
methods: {
    handleIncrement () {
        this.$store.commit({
            type: 'increment',
            count: 10
        });
    }
}
```

##### 高级用法

`Vuex` 还有 `3` 个选项可以使用：`getters`、`actins`、`modules`。

- `getters`

有时候我们需要从 `store` 中的 `state` 中派生出一些状态，例如对列表进行过滤并计数：

```js
// stre/index.js
const store = new Vuex.Store({
    state: {
        list: [1, 3, 5, 6, 9, 13, 17]
    }
});
```

```js
// index.vue
computed: {
  list () {
    return this.$store.state.list.filter(item => item < 10);
  }
}
```

这样写完全没有问题，但是有时候其他组件也需要过滤后的数据，这样就需要把同样的方法在写一遍，为了避免这种重复，就可以使用 `getters` 了。

`getters` 可以看做是 `store` 的计算属性。就像计算属性一样，`getter` 的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算。

```js
// stre/index.js
const store = new Vuex.Store({
    state: {
        list: [1, 3, 5, 6, 9, 13, 17]
    },
    getters: {
        filteredList: state => {
            return state.list.filter(item => item < 10);
        }
    }
});
```

```js
// index.vue
export default {
    computed: {
        list () {
            return this.$store.getters.filteredList;
        }
    }
}
```

- `actions`

`mutations` 里面不应该异步操作数据，所以有了 `actions` 选项，`actions` 与 `mutations` 很像，不同的是 `action` 里面提交的是 `mutation`，并且可以异步操作业务逻辑。

`action` 在组件内通过 `$store.dispatch` 触发。我们用一个 `Promise` 在 `1` 秒钟后提交 `mutations`:

```js
export default new Vuex.Store({
    state: {
        count: 0
    },
    mutations: {
        increment (state, n) {
            n = n || 1;
            state.count += n;
        },
        decrease (state) {
            state.count --;
        }
    },
    actions: {
        asyncIncrement (context) {
            return new Promise(resolve => {
                setTimeout(() => {
                    context.commit('increment');
                    resolve();
                }, 1000)
            });
        }
    }
})
```

```html
<!-- index.vue -->
<template>
    <div>
        <div>Index</div>
        <div>{{ count }}</div>
        <button @click="handleIncrement">+1</button>
        <button @click="handleActionIncrement">+1</button>
    </div>
</template>

<script>
export default {
    name: 'index',
    computed: {
        count () {
            return this.$store.state.count;
        }
    },
    methods: {
        handleIncrement () {
            this.$store.commit('increment');
        },
        handleActionIncrement () {
            this.$store.dispatch('asyncIncrement');
        }
    }
}
</script>
```

`Promise` 是一种异步方案，异步 `action` 同时当然也可以用普通的回调来实现：

```js
// store/index.js
actions: {
    asyncIncrement (context, callback) {
        setTimeout (() => {
            context.commit('increment');
            callback();
        }, 1000);
    }
}
```

`mutations` 和 `actions` 看起来很像，但 `Vuex` 很像是一种与开发者的约定，涉及改变数据的，就使用 `mutations`，存在业务逻辑的，就用 `actions`。

- `modules`

它用来将 `store` 分割到不同的模块。

```js
const moduleA = {
    state: { ... },
    mutations: { ... },
    actions: { ... },
    getters: { ... }
}

const moduleB = {
    state: { ... },
    mutations: { ... },
    actions: { ... }
}

const store = new Vuex.Store({
    modules: {
        a: moduleA,
        b: moduleB
    }
})

store.state.a // moduleA 的状态
store.state.b // moduleB 的状态
```

不同模块下的数据状态管理，添加命名空间 `namespaced`:

```js
// store/index.js
const moduleA = {
    namespaced: true,
    state: {
        count: 1,
    },
    mutations: {
        add (state) {
        state.count += 2;
        }
    },
    actions: {},
    getters: {}
}

const moduleB = {
    namespaced: true,
    state: {
        count: 0,
    },
    mutations: {
        add (state) {
        state.count ++;
        }
    },
    actions: {}
}

const store = new Vuex.Store({
    modules: {
        a: moduleA,
        b: moduleB
    }
})

export default store;
```

使用 `namespaced` 后，提交时在前面加上模块名：

例如：`this.$store.commit('a/add')`

```html
<template>
    <div>
        <div>A: {{ countA }}</div>
        <div>B: {{ countB }}</div>
        <button @click="handleAdda">+2</button>
        <button @click="handleAddb">+1</button>
    </div>
</template>

<script>
export default {
    name: 'index',
    computed: {
        countA () {
            return this.$store.state.a.count;
        },
        countB () {
            return this.$store.state.b.count;
        }
    },
    methods: {
        handleAdda () {
            this.$store.commit('a/add');
        },
        handleAddb () {
            this.$store.commit('b/add');
        }
    }
}
</script>
```
