---
title: 深入理解 Vue.js（一）
date: 2020-09-26
category: 
    - Vue
tags:
    - Vue
thumbnail: /images/asuka/asu-23.jpg

---

# 深入理解 `Vue.js`（一）

> 重读文档，同时也是对自己的积累的又一次推倒重建。

<!-- more -->

## 什么是 `Vue.js`

> `Vue` 是一个渐进式前端框架，其核心概念是数据的双向绑定、组件化、单向数据流、可复用等。既然是重新阅读官方文档，那我们从一个工程化项目开始。

### `Vue` 工程化项目

```terminal
npm install -g @vue/cli
vue -V
vue create vue-demo
cd vue-demo
npm run serve
```

这时，我们得到了一个这样的文件结构：

![tree](http://images.akashi.org.cn/FsjFES612aObJu33MW5FV1OcoLCJ)

首先我们来关注 `src/main.js`：

```js
import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
```

可见，这里引入了 `vue` 与 `App.vue` 文件，同时 `new` 了一个 `Vue` 实例并做了节点渲染。

现在我们先封装一个组件 `ComponentItem` 并抛出。在 `component` 文件夹下新建 `ComponentItem.vue` 文件:

```html
<template>
  <div>这是一个Vue子组件</div>
</template>

<script>
export default {
  name: "ComponentItem",
};
</script>

<style scoped></style>
```

一个 `vue` 文件由模板 `template`、脚本 `script` 和样式 `style`三部分构成。

进入 `App.vue` 在 `script` 中导入(`import`) `components` 中被抛出的组件 `ComponentItem` 并在 `components` 中声明使用，最终在 `template` 中渲染到浏览器显示。

```html
<template>
  <div id="app">
    <ComponentItem />
  </div>
</template>

<script>
import ComponentItem from './components/ComponentItem'

export default {
  name: 'App',
  components: {
    ComponentItem
  }
}
</script>

<style>
#app {
  ...
}
</style>
```

注：这里删除掉自动生成的 `HelloWorld.vue` 文件以及引入的相关多余内容。

这时我们可以在浏览器看到子组件便被渲染到了页面上。

### 数据与方法

> 熟悉了基本的组件创建，我们先回顾一下 `Vue` 的数据与方法。

`Vue` 的初始数据声明在 `data` 中。当一个实例被创建时，它将 `data` 对象(组件中为`data`函数)中的所有属性(`property`)加入到 `Vue` 的响应式系统中，通过属性值的变化，自动绑定到视图，称为数据的双向绑定。

注意：在组件中，`data` 是一个函数而不是对象，这样每个实例便可以维护一份被返回对象的独立的拷贝。

比如在我们新建的 `ComponentItem` 组件中，我们这样使用 `data`:

```js
export default {
  name: "ComponentItem",
  data() {
    return {}
  }
};
```

注意：只有当实例被创建时就已经存在于 `data` 中的属性(`property`)才是 `响应式` 的。所以如果我们在后续会需要一些属性，但是一开始它为空或不存在，那么需要在 `data` 中设置一些初始值。

`Vue` 以自身的 `diff` 算法遍历计算 `Virtual DOM`，找到最小差异 `DOM` 更新，避免了真实的 `DOM` 渲染引起的整个 `DOM` 树的重排重绘，减小浏览器消耗。

`Vue` 自定义实例属性带有 `$` 前缀，与用户定义的 `property` 进行区分，如：

```js
var data = {
    a: 1
}

var vm = new Vue({
  el: '#app',
  data: data
})

vm.$data === data // => true
vm.$el === document.getElementById('app') // => true

// $watch 是一个实例方法
vm.$watch('a', function (newValue, oldValue) {
  // 这个回调将在 `vm.a` 改变后调用
})
```

更多 `API` 查找参照 [官网文档](https://cn.vuejs.org/v2/api/#%E5%AE%9E%E4%BE%8B-property)

常用的如：`vm.$data`、`vm.$el`、`vm.$props`、`vm.$options`、`vm.$refs`、`vm.$watch`、`vm.$set`、`vm.$on`、`vm.$emit`、`vm.$attrs` 等。

### 钩子函数与生命周期

每个 `Vue` 实例在被创建时都要经过一系列的初始化过程，如设置数据监听、编译模板、挂载实例到 `DOM`、数据变化更新 `DOM` 等。在整个过程中，会运行一些生命周期钩子的函数，允许用户在不同阶段添加自己的代码进行处理。

如：

```js
created() {},
mounted() {},
updated() {},
destroyed() {}
```

![生命周期](http://images.akashi.org.cn/Fl6bx36VFinnwpDPz25fF_XcpTcl)

注意：不要在选项 `property` 或回调上使用箭头函数，因为箭头函数并没有 `this`，`this` 会作为变量一直向上级词法作用域查找，直至找到为止，会导致出现属性未定义、方法不存在的错误。

## 模板语法

> 在 `Vue.js` 的使用上，框架提供了基于 `HTML` 的 `模板语法` 和 `渲染函数(render) & JSX`。

`模板语法` 允许开发者声明式地将 `DOM` 绑定至底层 `Vue` 实例的数据。然后 `Vue` 将模板编译成虚拟 `DOM` 渲染函数。结合响应系统，`Vue` 能够智能地计算出最少需要重新渲染多少组件，并把 `DOM` 操作次数减到最少。

如果熟悉虚拟 `DOM` 并偏爱原生的 `JavaScript`，可使用 `渲染函数(render)+JSX语法`。

这里介绍模板语法的使用方法。

### 插值

#### 文本插值

数据绑定最常见的形式就是使用双大括号进行文本插值：

```html
<template>
  <div class="container">
    <span>Message: {{ msg }}</span>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      msg: "This is a message"
    }
  }
};
</script>
```

#### 原始 HTML

双大括号会将数据解释为普通文本，而非 `HTML` 代码。使用 `v-html` 可以输出 `HTML`:

```html
<template>
  <div class="container">
    <span>Message: {{ msg }}</span>
    <div v-html="html"></div>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      msg: "This is a message",
      html: "<span style='color:red'>This should bu red</span>"
    }
  }
};
</script>
```

注意：动态渲染的任意 `HTML` 可能会非常危险，因为它很容易导致 `XSS` 攻击。只对可信内容使用 `HTML` 插值，绝不要对用户提供的内容使用插值。

#### `Attribute`

使用 `v-bind` 指令动态绑定到 `HTML attribute` 上：

```html
<template>
  <div class="container">
    <div v-bind:id="id"></div>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      id: 0
    }
  }
};
</script>
```

#### 使用 `JavaScript` 表达式

同时，所有的数据绑定 `Vue.js` 还提供了完全的 `JavaScript` 表达式支持:

```html
<template>
  <div class="container">
    <div v-bind:id="'list-' + id"></div>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      id: 0
    }
  }
};
</script>
```

### 指令

> 指令(`Directives`) 是带有 `v-` 前缀的特殊 `attribute`。

#### 参数

一些指令能够接收一个“参数”，在指令名称之后以冒号表示。如，`v-bind` 指令可以用于响应式地绑定更新 `HTML attribute`、`v-on` 指令可以用于绑定事件监听器：

```html
<template>
  <div class="container">
    <a v-bind:href="url">URL</a>
    <button v-on:click="handleClick">Click</button>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      url: "https://akashi_sai.gitee.io"
    }
  },
  methods: {
    handleClick() {
      console.log("clicked!")
    }
  }
};
</script>
```

这里 `v-bind` 指令将该元素的 `href` `attribute` 与表达式 `url` 的值绑定，`v-on` 指令将该元素的 `click` 事件与 `handleClick` 方法进行绑定。

#### 动态参数

可以用方括号括起来的 `JavaScript` 表达式作为一个指令的参数，将上面的例子修改一下就可写为：

```html
<template>
  <div class="container">
    <a v-bind:[href]="url">URL</a>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      href: 'href',
      url: "https://akashi_sai.gitee.io"
    }
  }
};
</script>
```

虽然效果上好像没有什么不同，但好处是这个参数可以是动态计算出来的，方便后续修改和提供了更多操作的可能。

- 对动态参数的值的约束

1. 动态参数预期会求出一个 `字符串`，异常情况下值为 `null`。这个特殊的 `null` 值可以被显性地用于移除绑定。任何其它非字符串类型的值都将会触发一个警告。

2. 语法上的约束，如空格和引号放在 `HTML attribute` 名里是无效的。

#### 修饰符

修饰符(`modifier`)是以半角句号 `.` 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。例如，`.prevent` 修饰符告诉 `v-on` 指令对于触发的事件调用 `event.preventDefault()`：

```html
<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>
```

修饰符可以分类为事件修饰符、按键修饰符、系统修饰符和自定义修饰符。

### 简写

简写是 `Vue` 提供的一种可选的合法字符，用于会频繁使用的两个特定的 `attribute`，`v-bind` 和 `v-on`。

#### `v-bind` 缩写

```html
<!-- 完整语法 -->
<a v-bind:href="url">...</a>

<!-- 缩写 -->
<a :href="url">...</a>

<!-- 动态参数的缩写 (2.6.0+) -->
<a :[key]="url"> ... </a>
```

#### `v-on` 缩写

```html
<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>

<!-- 缩写 -->
<a @click="doSomething">...</a>

<!-- 动态参数的缩写 (2.6.0+) -->
<a @[event]="doSomething"> ... </a>
```

## 计算属性和侦听器

### 计算属性(`Computed`)

> 用于解耦模板内的复杂逻辑，达到方便维护和简洁清晰的效果。

```html
<template>
  <div class="container">
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      message: "This is a message!",
    };
  },
  computed: {
    msg() {
      return this.message
        .split("")
        .reverse()
        .join("");
    },
  }
};
</script>

<style scoped></style>
```

#### 计算属性缓存(`computed`) `vs` 方法(`methods`)

我们发现调用方法也可以实现同样的效果，区别在于 `计算属性` 是基于它们的响应式依赖进行缓存的，只在相关响应式依赖发生改变时它们才会重新求值。

而方法每当重新渲染时，都会再次执行函数。如果不希望一个值每次渲染都重新计算，那么使用方法在性能上是比较浪费的。

#### 计算属性 `vs` 监听属性

侦听属性是一个更通用的方式来观察和响应 `vue` 实例上的数据变动。但 `Vue` 官方建议，不要滥用 `watch`，通常更好的做法是使用计算属性。

#### 计算属性的 `setter`

计算属性默认只有 `getter`，不过在需要时也可以提供一个 `setter`：

```js
computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      let names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
```

### 侦听器(`Watch`)

虽然计算属性在大多数情况下更合适，但有时也需要一个 `自定义的侦听器`。这就是为什么 `Vue` 通过 `watch` 选项提供了一个更通用的方法，来响应数据的变化。当需要在数据变化时执行 `异步` 或 `开销较大` 的操作时，这个方式是最有用的。

```html
<template>
  <div class="container">
    <p>FullName: {{ fullName }}</p>
    <p>FirstName: <input type="text" v-model="firstName" /></p>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      firstName: "Akashi",
      lastName: "Sai",
      fullName: ""
    };
  },
  watch: {
    firstName(newName, oldName) {
      this.fullName = newName + ' ' + this.lastName;
    }
  }
};
</script>
```

#### `handler` 和 `immediate`

以上是变化之后，`wath` 才执行，需要在最初时候 `watch` 就执行用到 ·、`handler` 和 `immediate` 属性。

```js
watch: {
  firstName: {
    handler(newName, oldName) {
      this.fullName = newName + " " + this.lastName;
    },
    immediate: true
  },
}
```

#### 深度监听 `deep`

```html
<template>
  <div class="container">
    <p>{{ obj.a }}</p>
    <p>obj.a <input type="text" v-model="obj.a" /></p>
  </div>
</template>

<script>
export default {
  name: "ComponentItem",
  data() {
    return {
      obj: {
        a: "123"
      }
    };
  },
  watch: {
    obj: {
      handler(val) {
        console.log('obj.a', val);
      },
      deep: true
    },
  }
};
</script>
```

同时，官网也给出了监听不同层级的对应方法，效果与上述相同：

```js
watch: {
  'obj.a': {
    handler(val) {
      console.log('obj.a', val);
    }
  }
}
```

监听同时也可以通过方法的形式写在 `methods` 中：

```js
watch: {
  "obj.a": "watchMethods" // 方法名
},
methods: {
  watchMethods(val) {
    console.log('val', val);
  }
},
```

## `Class` 与 `Style` 绑定

> 操作元素的 `class` 列表和内联样式是数据绑定的一个常见需求。一般操作是通过 `v-bind` 绑定后处理。

而将 `v-bind` 用于 `class` 和 `style` 时，`Vue.js` 做了专门的增强。表达式结果的类型除了字符串之外，还可以是对象或数组。

### 绑定 `HTML Class`

#### 对象语法

```html
<div :class="{ active: isActive }"></div>
```

```js
data() {
  return {
    isActive: true
  };
}
```

渲染后：

```js
<div class="active"></div>
```

同时，也可以绑定在一个返回的计算属性中：

```html
<div :class="classObject"></div>
```

```js
data() {
  return {
    isActive: true
  }
}
computed: {
  classObject() {
    return {
      active: this.isActive
    }
  }
}
```

以上效果是相同的。

#### 数组语法

```html
<div :class="classObject"></div>
```

```js
data() {
  return {
    classObject: ['active', 'text']
  };
}
```

渲染后：

```js
<div class="active text"></div>
```

### 绑定内联样式

#### 对象语法

```html
<div :style="styles">Akashi</div>
```

```js
data() {
  return {
    styles: {
      color: 'red',
      fontSize: '13px'
    }
  };
}
```

同样的，对象语法常常结合返回对象的计算属性使用。

#### 数组语法

```html
<div :style="[baseStyles, overridingStyles]">Akashi</div>
```

```js
data() {
  return {
    baseStyles: {
      color: 'red'
    },
    overridingStyles: {
      fontSize: '13px'
    },
    // 亲测这样声明并不会生效，数组必须直接声明在内联样式中
    // styles: [this.baseStyles, this.overridingStyles]
  };
}
```

## 条件渲染

> `v-if` 指令用于条件性地渲染一块内容。当返回的值为真的时候被渲染。

### `v-if`

```html
<div class="container">
  <div v-if="type === 'a'">A</div>
  <div v-else-if="type === 'b'">B</div>
  <div v-else>Not A/B</div>
</div>
```

```js
data() {
  return {
    type: 'c'
  };
}
```

渲染结果：

```html
<div class="container">
  <div>Not A/B</div>
</div>
```

#### 用 `key` 管理可复用元素

默认 `Vue` 元素是复用的，这样可以高效的渲染元素，例如：

```html
<template v-if="loginType === 'username'">
  <label>Username</label>
  <input placeholder="Enter your username">
</template>
<template v-else>
  <label>Email</label>
  <input placeholder="Enter your email address">
</template>
```

上面的代码中切换 `loginType` 将不会清除用户已经输入的内容。因为两个模板使用了相同的元素，`<input>` 不会被替换掉——仅仅是替换了它的 `placeholder`。

当需求是不需要复用，使用完全独立的两个元素时，可以添加具有唯一值的 `key` 属性。

```html
<template v-if="loginType === 'username'">
  <label>Username</label>
  <input placeholder="Enter your username" key="username-input">
</template>
<template v-else>
  <label>Email</label>
  <input placeholder="Enter your email address" key="email-input">
</template>
```

### `v-show`

> 与 `v-if` 相似，根据条件展示元素。

```html
<div v-show="true">Show</div>
```

不同的是带有 `v-show` 的元素始终会被渲染并保留在 `DOM` 中。`v-show` 只是简单地切换元素的 `CSS` `property` `display`。

### `v-if` vs `v-show`

`v-if` 会动态的渲染和重建节点元素，是属于真正的条件渲染，同时它也是惰性的，只有条件为真时才会渲染。

`v-show` 无论条件真假都会渲染，只是动态对 `CSS` 进行切换进而实现显隐。

一般来说，`v-if` 有更高的切换开销，而 `v-show` 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 `v-show` 较好；如果在运行时条件很少改变，则使用 `v-if` 较好。

同时，不推荐同时使用 `v-if` 和 `v-for`。当 `v-if` 与 `v-for` 一起使用时，`v-for` 具有比 `v-if` 更高的优先级，即在每次重新渲染的时候都会遍历整个列表，即使 `v-if` 为 `false`。

## 列表渲染

> `v-for` 指令基于一个数组来渲染一个列表。

### `v-for`


```html
<div class="container">
  <ul>
    <li v-for="(item, index) in items" :key="item">
      {{ index }} - {{ item }}
    </li>
  </ul>
</div>
```

```js
data() {
  return {
    items: ["akashi", "asuka", "agkki"]
  }
}
```

注意参数顺序，第一个参数为值，第二个参数为当前项的索引（可省略）。

为了 `Vue` 能跟踪每个节点的身份，从而重用和重新排序现有元素，需要为每项提供一个唯一的 `key` 属性。

#### 使用对象

同时 `v-for` 也支持使用对象进行迭代：

```html
<div class="container">
  <ul>
    <li v-for="(value, key, index) of items" :key="index">
      {{ index }} - {{ key }} - {{ value }}
    </li>
  </ul>
</div>
```

```js
data() {
  return {
    items: {
      name: "akashi",
      age: 23
    }
  }
}
```

注意：这时，参数顺序变为了键值、键名、索引。

同时，也可以用 `of` 替代 `in` 作为分隔符，它更接近 `JavaScript` 迭代器的语法。

而我们在实际中的开发中，更多的是使用数组对象的情况：

```html
<div class="container">
  <ul>
    <li v-for="(item, index) in items" :key="item.name">
      {{ index }} - {{ item.name }} - {{ item.age }}
    </li>
  </ul>
</div>
```

```js
data() {
  return {
    items: [
      {
        name: "akashi",
        age: 23,
      },
      {
        name: "asuka",
        age: 22,
      },
      {
        name: "gakki",
        age: 31,
      },
    ]
  }
}
```

#### 数组更新检测

`Vue` 将 `JS` 的数组方法进行了侦听，数组方法的触发也会动态的更新到视图。

其中包括：

- 变更方法

  - `push()`
  - `pop()`
  - `shift()`
  - `unshift()`
  - `splice()`
  - `sort()`
  - `reverse()`
  - `join()`

注：此类方法对原数组进行了修改。

- 替换数组

  - `filter()`
  - `concat()`
  - `slice()`
  - `map()`

注：此类方法会返回一个新的数组，而不会改变原始数组。

## 事件处理

### 监听事件及处理方法

可以用 `v-on` 指令监听 `DOM` 事件（简写为 `@`），并在触发时运行一些 `JavaScript` 代码。

```html
<div class="container">
  <button @click="handleClick">click</button>
  <p>Counter: {{ counter }}</p>
</div>
```

```js
data() {
  return {
    counter: 0,
  };
},
methods: {
  handleClick() {
    this.counter += 1;
  },
},
```

访问原始的 `DOM` 事件。可以使用特殊变量 `$event`，将其传入方法：

```html
<button @click="handleClick($event)">click</button>
```

```js
handleClick(e) {
  console.log('$event', e);
}
```

注：如果函数不需要多余参数值，默认定义的参数同样可以获取 `DOM` 事件。

```html
<button @click="handleClick">click</button>
```

```js
handleClick(e) {
  console.log('$event', e);
}
```

### 事件修饰符

> 在事件处理程序中调用 `event.preventDefault()` 或 `event.stopPropagation()` 是非常常见的需求。尽管我们可以在方法中轻松实现这点，但更好的方式是：方法只有纯粹的数据逻辑，而不是去处理 `DOM` 事件细节。

为此，`Vue.js` 为 `v-on` 提供了事件修饰符：

- `.stop`
- `.prevent`
- `.capture`
- `.self`
- `.once`
- `.passive`

```html
<!-- 阻止单击事件继续传播 -->
<a v-on:click.stop="doThis"></a>

<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>

<!-- 修饰符可以串联 -->
<a v-on:click.stop.prevent="doThat"></a>

<!-- 只有修饰符 -->
<form v-on:submit.prevent></form>

<!-- 添加事件监听器时使用事件捕获模式 -->
<!-- 即内部元素触发的事件先在此处理，然后才交由内部元素进行处理 -->
<div v-on:click.capture="doThis">...</div>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<div v-on:click.self="doThat">...</div>

<!-- 点击事件将只会触发一次 -->
<a v-on:click.once="doThis"></a>

<!-- 滚动事件的默认行为 (即滚动行为) 将会立即触发 -->
<!-- 而不会等待 `onScroll` 完成  -->
<!-- 这其中包含 `event.preventDefault()` 的情况 -->
<div v-on:scroll.passive="onScroll">...</div>
```

### 按键修饰符

```html
<div class="container">
  <input @keyup.enter="onEnter">
</div>
```

```js
onEnter(e) {
  console.log(e.target.value);
}
```

为了在必要的情况下支持旧浏览器，`Vue` 提供了绝大多数常用的按键码的别名：

- `.enter`
- `.tab`
- `.delete` (捕获“删除”和“退格”键)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`

还可以通过全局 `config.keyCodes` 对象自定义按键修饰符别名：

```js
// 可以使用 `v-on:keyup.f1`
Vue.config.keyCodes.f1 = 112
```

### 系统修饰符

可以用如下修饰符来实现仅在按下相应按键时才触发鼠标或键盘事件的监听器。

- `.ctrl`
- `.alt`
- `.shift`
- `.meta`

注：在 `Mac` 系统键盘上，`meta` 对应 `command` 键 (`⌘`)。在 `Windows` 系统键盘 `meta` 对应 `Windows` 徽标键 (`⊞`)。在 `Sun` 操作系统键盘上，`meta` 对应实心宝石键 (`◆`)。

```html
<!-- Alt + C -->
<input v-on:keyup.alt.67="clear">
```

#### `.exact` 修饰符

`.exact` 修饰符允许你控制由精确的系统修饰符组合触发的事件。

```html
<!-- 即使 Alt 或 Shift 被一同按下时也会触发 -->
<button v-on:click.ctrl="onClick">A</button>

<!-- 有且只有 Ctrl 被按下的时候才触发 -->
<button v-on:click.ctrl.exact="onCtrlClick">A</button>

<!-- 没有任何系统修饰符被按下的时候才触发 -->
<button v-on:click.exact="onClick">A</button>
```

#### 鼠标按钮修饰符

- `.left`
- `.right`
- `.middle`

这些修饰符会限制处理函数仅响应特定的鼠标按钮。

## 表单输入绑定

> 使用 `v-model` 指令在表单 `<input>`、`<textarea>` 及 `<select>` 元素上创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。

v-model 在内部为不同的输入元素使用不同的 property 并抛出不同的事件：

- text 和 textarea 元素使用 value property 和 input 事件；
- checkbox 和 radio 使用 checked property 和 change 事件；
- select 字段将 value 作为 prop 并将 change 作为事件

### 基础用法

#### 文本

```html
<div class="container">
  <input v-model="message" />
  <p>{{ message }}</p>
</div>
```

```js
data() {
  return {
    message: "",
  };
},
```

#### 多行文本

```html
<div class="container">
  <textarea v-model="message" placeholder="edit..." />
  <p>{{ message }}</p>
</div>
```

```js
data() {
  return {
    message: "",
  };
}
```

#### 复选框

```html
<div class="container">
  <input type="checkbox" v-model="checked" />
  <label for="checkbox">{{ checked }}</label>
</div>
```

```js
data() {
  return {
    checked: false,
  };
},
```

多个复选框：

```html
<div class="container">
  <div>
    <label for="akashi">Akashi</label>
    <input
      type="checkbox"
      id="akashi"
      value="akashi"
      v-model="checkedNames"
    />
  </div>
  <div>
    <label for="asuka">Asuka</label>
    <input
      type="checkbox"
      id="asuka"
      value="asuka"
      v-model="checkedNames"
    />
  </div>
  <div>
    <label for="gakki">Gakki</label>
    <input
      type="checkbox"
      id="gakki"
      value="gakki"
      v-model="checkedNames"
    />
    <div>CheckedNames: {{ checkedNames }}</div>
  </div>
</div>
```

```js
data() {
  return {
    checkedNames: [],
  };
}
```

#### 单选框

```html
<div class="container">
  <div>
    <label for="akashi">Akashi</label>
    <input type="radio" id="akashi" value="akashi" v-model="picked" />
  </div>
  <div>
    <label for="asuka">Asuka</label>
    <input type="radio" id="asuka" value="asuka" v-model="picked" />
  </div>
  <div>
    <label for="gakki">Gakki</label>
    <input type="radio" id="gakki" value="gakki" v-model="picked" />
    <div>Picked: {{ picked }}</div>
  </div>
</div>
```

```js
data() {
  return {
    picked: "",
  };
}
```

#### 选择框

```html
<div class="container">
  <select v-model="selected" style="width:60px">
    <option value="akashi">Akashi</option>
    <option value="asuka">Asuka</option>
    <option value="gakki">Gakki</option>
  </select>
  <div>Selected: {{ selected }}</div>
</div>
```

```js
data() {
  return {
    selected: "",
  };
}
```

### 绑定值

即单选框、复选框、选择框的 `value` 的绑定。各组件 `v-model` 绑定状态下会修改 `vlue` 的值。

### 修饰符

- `.lazy`

在默认情况下，`v-model` 在每次 `input` 事件触发后将输入框的值与数据进行同步。通过添加 `lazy` 修饰符，从而转为在 `change` 事件 `之后` 进行同步。

- `.number`

如果想自动将用户的输入值转为数值类型，可以给 `v-model` 添加 `number` 修饰符。

- `.trim`

如果要自动过滤用户输入的首尾空白字符，可以给 `v-model` 添加 `trim` 修饰符。

## 组件基础

基本使用：

> `ButtonCounter.vue`

```html
<template>
  <div>
    <button @click="onClick">clicked {{ count }} times</button>
  </div>
</template>

<script>
export default {
  name: "ButtonCounter",
  data() {
    return {
      count: 0,
    };
  },
  methods: {
    onClick() {
      this.count++;
    },
  },
};
</script>
```

> `App.vue`

```html
<template>
  <div id="app">
    <ButtonCounter />
  </div>
</template>

<script>
import ButtonCounter from "./components/ButtonCounter"

export default {
  name: "App",
  components: {
    ButtonCounter
  },
};
</script>
```

### 复用

> 组件可以被多次复用，但每个组件都会维护一个独立的 `data`。

一个组件的 `data` 选项必须是一个函数，因此每个实例可以维护一份被返回对象的独立的拷贝。

> `App.vue`

```html
<template>
  <div id="app">
    <ButtonCounter />
    <ButtonCounter />
    <ButtonCounter />
  </div>
</template>

<script>
import ButtonCounter from "./components/ButtonCounter"

export default {
  name: "App",
  components: {
    ButtonCounter
  },
};
</script>
```

### `Prop` 向子组件传递数据

> `Prop` 允许我们在组件上注册一些自定义属性，子组件 `prop` 属性通过接收父组件传递过来的值实现数据传递。

```html
<template>
  <div id="app">
    <BlogPost :title="title" />
  </div>
</template>

<script>
import BlogPost from "./components/BolgPost";

export default {
  name: "App",
  components: {
    BlogPost,
  },
  data() {
    return {
      title: "Blog",
    };
  },
};
</script>
```

> `BlogPost.vue`

```html
<template>
  <div>{{ title }}</div>
</template>

<script>
export default {
  name: "BlogPost",
  props: ["title"],
};
</script>
```

### 单个根元素

> 值得注意的是，每个组件必须只有一个 `根元素`。在开发时，可以使用一个父元素统一将模板内容包裹。`prop` 太多也需要对数据进行重构，以保证内容的清晰和易维护。

一个好的例子：

> `BlogPost.vue`

```html
<template>
  <div class="blog-container">
    <h3>{{ params.title }}</h3>
    <div>{{ params.author }}</div>
  </div>
</template>

<script>
export default {
  name: "BlogPost",
  props: {
    params: {
      type: Object,
      required: true,
      default: () => ({}),
    },
  },
};
</script>
```

> `App.vue`

```html
<template>
  <div id="app">
    <BlogPost :params="paramsData" />
  </div>
</template>

<script>
import BlogPost from "./components/BolgPost";

export default {
  name: "App",
  components: {
    BlogPost,
  },
  data() {
    return {
      paramsData: {
        title: "Blog",
        author: "Akashi",
      },
    };
  },
};
</script>
```

### 监听子组件事件

> 在开发中，不仅仅需要自上而下从父组件向子组件传递数据，同时也会有子组件向父组件进行沟通的需求。

为保证单向数据流，自然是不允许子组件直接修改父组件的数据，造成数据的维护困难。这里就要引出自定义事件对子组件进行监听：

父级组件可以像处理 `native` `DOM` 事件一样通过 `v-on` 监听子组件实例的任意事件：

> `App.vue`

```html
<template>
  <div id="app">
    <BlogPost :params="paramsData" @enlarge-text="enlargeText" />
  </div>
</template>

<script>
import BlogPost from "./components/BolgPost";

export default {
  name: "App",
  components: {
    BlogPost,
  },
  data() {
    return {
      paramsData: {
        title: "Blog",
        author: "Akashi",
        style: {
          fontSize: 1,
        },
      },
    };
  },
  methods: {
    enlargeText() {
      this.paramsData.style.fontSize += 0.1;
    },
  },
};
</script>
```

同时子组件可以通过调用内建的 `$emit` 方法并传入事件名称来触发一个事件：

> `BlogPost.vue`

```html
<template>
  <div :style="styles">
    <h3>{{ params.title }}</h3>
    <div>{{ params.author }}</div>
    <button @click="onClick">Enlarge text</button>
  </div>
</template>

<script>
export default {
  name: "BlogPost",
  props: {
    params: {
      type: Object,
      required: true,
      default: () => ({}),
    },
  },
  computed: {
    styles() {
      return {
        fontSize: this.params.style.fontSize + "em",
      };
    },
  },
  methods: {
    onClick() {
      this.$emit("enlarge-text");
    },
  },
};
</script>
```

#### 使用事件抛出一个值

有时候需要向上传递一个特殊的值，这时可以使用 `$emit` 的第二个参数来提供这个值：

> `BlogPost.vue`

```html
<template>
  <div :style="styles">
    <h3>{{ params.title }}</h3>
    <div>{{ params.author }}</div>
    <button @click="onClick">Enlarge text</button>
  </div>
</template>

<script>
export default {
  name: "BlogPost",
  props: {
    params: {
      type: Object,
      required: true,
      default: () => ({}),
    },
  },
  computed: {
    styles() {
      return {
        fontSize: this.params.style.fontSize + "em",
      };
    },
  },
  data() {
    return {
      count: 0.1
    }
  },
  methods: {
    onClick() {
      this.$emit("enlarge-text", this.count++);
    },
  },
};
</script>
```

这时，父组件在监听这个事件的时候，可以通过 `$event` 访问到被抛出的这个值：

> `App.vue`

```html
<template>
  <div id="app">
    <BlogPost :params="paramsData" @enlarge-text="enlargeText" />
  </div>
</template>

<script>
import BlogPost from "./components/BolgPost";

export default {
  name: "App",
  components: {
    BlogPost,
  },
  data() {
    return {
      paramsData: {
        title: "Blog",
        author: "Akashi",
        style: {
          fontSize: 1,
        },
      },
    };
  },
  methods: {
    enlargeText(e) {
      this.paramsData.style.fontSize += e;
    },
  },
};
</script>
```

#### 在组件上使用 `v-model`

> 自定义事件也可以用于创建支持 v-model 的自定义输入组件。

```html
<template>
  <div id="app">
    <input type="text" v-model="text">
    <p>{{ text }}</p>
  </div>
</template>

<script>

export default {
  name: "App",
  data() {
    return {
      text: "",
    };
  },
};
</script>
```

等价于：

```html
<template>
  <div id="app">
    <input 
      type="text"
      :value="text"
      @input="onInput"
    >
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      text: "",
    };
  },
  methods: {
    onInput(e) {
      this.text = e.target.value;
    },
  },
};
</script>
```

为了让组件正常工作，这个组件内的 `<input>` 必须：

- 将其 `value` `attribute` 绑定到一个名叫 `value` 的 `prop` 上
- 在其 `input` 事件被触发时，将新的值通过自定义的 `input` 事件抛出

```html
<template>
  <div>
    <input
      type="text"
      :value="value"
      @input="onInput($event)"
    />
  </div>
</template>

<script>
export default {
  name: "CustomInput",
  props: {
    value: {
      default: ""
    }
  },
  data() {
    return {};
  },
  methods: {
    onInput(e) {
      this.$emit("input", e.target.value);
    },
  },
};
</script>
```

这样就可以在组件上使用 `v-model`。

```html
<template>
  <div id="app">
    <CustomInput v-model="text" />
    <p>{{ text }}</p>
  </div>
</template>

<script>
import CustomInput from "./components/CustomInput"

export default {
  name: "App",
  components: {
    CustomInput,
  },
  data() {
    return {
      text: "",
    };
  },
};
</script>
```

### 通过插槽分发内容

有时父组件需要动态的向一个子组件传递内容。

这时可以使用 `slot` 插槽在子组件中进行占位：

> `ContextBox.vue`

```html
<template>
  <div>
    <strong>Error!</strong>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "ContextBox",
};
</script>
```

然后在父组件中可以直接将节点内容传递过去：

> `App.vue`

```html
<template>
  <div id="app">
    <ContextBox>Something bad happened.</ContextBox>
  </div>
</template>

<script>
import ContextBox from "./components/ContextBox";

export default {
  name: "App",
  components: {
    ContextBox,
  },
};
</script>
```

实际上插槽还有具名插槽和作用域插槽等，这里暂时先只介绍一般插槽的使用。

### 动态组件

在一个需求中，需要在不同的组件之间动态的进行切换，这时可以通过 `Vue` 的 `<component>` 元素加一个特殊的 `is` `attribute` 来实现：

```html
<template>
  <div id="app">
    <button 
      v-for="tab in tabs" 
      :key="tab.name" 
      @click="onClick(tab.component)"
    >{{ tab.name }}</button>

    <component :is="currentTab" />
  </div>
</template>

<script>
import Home from "./components/Home";
import About from "./components/About";

export default {
  name: "App",
  components: {
    Home,
    About,
  },
  data() {
    return {
      tabs: [
        {
          name: "Home",
          component: Home,
        },
        {
          name: "About",
          component: About,
        },
      ],
      currentTab: "Home",
    };
  },
  methods: {
    onClick(tab) {
      this.currentTab = tab;
    },
  },
};
</script>
```

`is` 属性指明了被绑定的组件，这个 `attribute` 可以用于常规 `HTML` 元素，但这些元素也将被视为组件，这意味着所有的 `attribute` 都会作为 `DOM` `attribute` 被绑定。

以上就是 `Vue` 官方文档中使用 `vue` 的基础介绍梳理。在重看整理的同时也加入了一些笔者常用内容的记录、对官方的例子进行了具体实现。
