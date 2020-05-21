---
title: Vue.js 阅读笔记（三）
date: 2019-12-16
category:
    - Vue
tags: 
    - Vue
thumbnail: /images/asuka/asu-16.jpg

---

### Vue.js 阅读笔记（三）

> 系统、框架性的认识 `Vue`，组件详解。

<!-- more -->

#### 组件与复用

- 为什么使用组件？

> 在实际业务中，我们可能需要重复使用到相同的组件，业务需求也会发生频繁的变动，这时，组件的复用就体现出优势了。

- 组件用法

在我们创建 `Vue` 的实例时，需要将实例注册并挂载到挂载点：

```js
var app = Vue({
    el: '#app',
})
```

组件与之类似，需要注册后才可以使用。

注册有全局注册和局部注册两种方式，全局注册后，任何 `Vue` 的实例都可以使用。

全局注册：

```js
Vue.component('my-component', {
    //...
})
```

`my-component` 是注册组件的自定义名称，推荐用小写加减号分割的形式命名。

子父实例中使用这个组件，必须要在实例创建前注册，之后就可以使用 `<my-component></my-component>` 的形式来使用组件了。

```html
<div id="app">
    <my-component></my-component>
</div>
<script>
    Vue.component('my-component', {
        template: '<div>这里是子组件内容</div>'
    });

    var app = new Vue({
        el: '#app',
    })
</script>
```

渲染后结果：

```html
<div id="app">
    <div>这里是子组件内容</div>
</div>
```

局部组件：

在 `Vue` 的实例中，使用 `components` 选项可以局部注册组件，注册后的组件只有在该实例作用域下有效，组件下也可以嵌套组件。

```html
<div id="app">
    <my-component></my-component>
</div>
<script>
    var Child = {
        template: '<div>这里是子组件内容</div>'
    }

    var app = new Vue({
        el: '#app',
        components: {
            'my-component': Child
        }
    })
</script>
```

`Vue` 组件的模板在某些情况下会受到 `HTML` 的限制，如 `<table>` 内规定只允许是 `<tr>`、`<td>`、`<th>` 这些表格元素，所以在 `<table>` 内直接使用组件是无效的。这种情况下，可以使用特殊的 `is` 属性来挂载组件。

```html
<div id="app">
    <table>
        <tbody is="my-component"></tbody>
    </table>
</div>
<script>
    Vue.component('my-component', {
        template: '<div>这里是子组件的内容</div>'
    })
    var app = new Vue({
        el: '#app',
    })
</script>
```

`<tbody>` 在渲染时，会被替换为组件内容。常见的限制元素还有 `<ul>`、`<ol>`、`<select>`。

除了 `template` 之外，组件中还可以像 `Vue` 实例那样使用其他选项，如 `data`、`computed`、`methods` 等。

但是，使用 `data` 时，和实例稍微有点区别， `data` 必须是函数，然后将数据 `return` 出去。

```js
Vue.component('my-component', {
    template: '<div>{{ message }}</div>',
    data: function() {
        return {
            message: '这里是子组件的内容'
        }
    }
});

var app = new Vue({
    el: '#app',
});
```

可以简写为：

```js
Vue.component('my-component', {
    template: '<div>{{ message }}</div>',
    data () {
        return {
            message: '这里是子组件的内容'
        }
    }
});
```

`JavaScript` 对象时引用关系，所以如果 `return` 出的对象引用了外部的一个对象，那么这个对象就是共享的，任何一方修改都会同步。

```html
<div id="app">
    <my-component></my-component>
    <my-component></my-component>
    <my-component></my-component>
</div>
<script>
    var data = {
        counter: 0
    };

    Vue.component('my-component', {
        template: '<button @click="counter++">{{ counter }}</button>',
        data () {
            return data;
        }
    });

    var app = new Vue({
        el: '#app',
    });
</script>
```

组件使用了 `3` 次，但是点击任意一个按钮所有数字都会加 `1`，那是因为组件的 `data` 引用的是外部的对象，这不是我们期望的结果，所以给组件返回一个新的 `data` 对象来独立。

```html
<div id="app">
    <my-component></my-component>
    <my-component></my-component>
    <my-component></my-component>
</div>
<script>
    Vue.component('my-component', {
        template: '<button @click="counter++">{{ counter }}</button>',
        data () {
            return {
                counter: 0
            };
        }
    });

    var app = new Vue({
        el: '#app',
    });
</script>
```

这样 `3` 个按钮就不互相影响了，完全达到了复用的目的。

#### 使用 `props` 传递数据

> 组件不仅仅是要把模板的内容进行复用，更重要的是组件间要进行通信。

通常父组件的模板中包含子组件，父组件要正向的向子组件传递数据或参数，子组件接收到后根据参数的不同来渲染不同的内容或执行操作。

这个正向传递数据的过程就是通过 `props` 来实现的。

```html
<div id="app">
    <my-component message="来自父组件的数据"></my-component>
</div>
<script>
    Vue.component('my-component', {
        props: ['message'],
        template: '<div>{{ message }}</div>'
    });

    var app = new Vue({
        el: '#app',
    });
</script>
```

渲染结果：

```html
<div id="app">
    <div>来自父组件的数据</div>
</div>
```

`props` 中声明的数据与组件 `data` 函数 `reture` 的数据的主要区别就是 `props` 的数据来自父级，而 `data` 中的是组件自己的数据，作用域是组件本身。

这两种数据都可以在模板 `template` 及计算属性 `computed` 和 方法 `methods` 中使用。

由于 `HTML` 特性不区分大小写，当使用 `DOM` 模板时，驼峰命名的 `props` 名称要转为短横分隔命名：

```html
<div id="app">
    <my-component warning-text="提示信息"></my-component>
</div>
<script>
    Vue.component('my-component', {
        props: ['warningText'],
        template: '<div>{{ warningText }}</div>'
    });

    var app = new Vue({
        el: '#app',
    });
</script>
```

有时候，需要传递来自父组件的动态数据，使用 `v-bind` 来动态绑定 `props` 的值：

```html
<div id="app">
    <input type="text" v-model="msg">
    <my-component :message="msg"></my-component>
</div>
<script>
    Vue.component('my-component', {
        props: ['message'],
        template: '<div>{{ message }}</div>'
    });

    var app = new Vue({
        el: '#app',
        data: {
            msg: ''
        }
    });
</script>
```

父组件传值给子组件，子组件获取值后可以进行使用。

- 单向数据流

通过 `props` 传递的数据是单向的，也就是说父组件数据变化时会传递给子组件，但是反过来不行。

在业务中，经常会遇到两种情况需要改变 `props` 的情况，一种是父组件传递初始值进来，子组件将它作为初始值保存起来，在自己的作用域下可以随意的改变和修改：

```html
<div id="app">
    <my-component :init-count='count'></my-component>
</div>
<script>
    Vue.component('my-component', {
        props: ['initCount'],
        template: '<div>{{ compCount }}</div>',
        data () {
            return {
                compCount: this.initCount
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            count: 1
        }
    });
</script>
```

另一种是 `props` 作为需要被转变的原始值传入，使用计算属性进行修改后使用：

```html
<div id="app">
        <my-component :width='width'></my-component>
    </div>
    <script>
        Vue.component('my-component', {
            props: ['width'],
            template: '<div :style="style">子组件内容</div>',
            computed: {
                style: function() {
                    return {
                        width: this.width + 'px'
                    }
                }
            },
        });

        var app = new Vue({
            el: '#app',
            data: {
                width: 100
            }
        });
    </script>
```

计算属性里面的函数还可以进一步使用简写方式：

```js
computed: {
    style () {
        return {
            width: this.width + 'px'
        }
    }
},
```

最终渲染结果：

```html
<div id="app">
    <div style="width: 100px;">子组件内容</div>
</div>
```

- 数据验证

上面所介绍的 `props` 选项的值都是一个数组，当然，除了数组之外，还可以是对象，当 `props` 需要验证时，就需要对象的写法：

一般当自己的组件需要提供给别人使用时，推荐都进行数据验证，比如某个数据必须是数字，如果传入字符串，就会在控制台弹出警告。

```js
Vue.component('my-component', {
    props: {
        // 必须是数字类型
        propA: Number,

        // 必须是字符串或者数字类型
        propB: [String, Number],

        // 布尔值，如果没有定义，默认为 true
        propC: {
            type: Boolean,
            default: true
        },

        // 数字，而且必传
        propD: {
            type: Number,
            required: true
        },

        // 如果是数组或对象，默认值必须是一个函数来返回
        propE: {
            type: Array,
            default: function() {
                return [];
            }
        },

        // 自定义一个验证器
        propF: {
            validator: function() {
                return value > 20;
            }
        }
    }
});
```

验证的 `type` 类型可以是：

- `String`

- `Number`

- `Boolean`

- `Object`

- `Array`

- `Function`

`type` 也是一个自定义构造器，使用 `instanceof` 检测。

#### 组件通信

> 从父组件向子组件通信，通过 `props` 传递数据就可以了，但是 `Vue` 的通信场景不止一种，组件关系可以分为父子组件通信、兄弟组件通信、跨级组件通信。

- 自定义事件

当子组件需要像父组件传递数据，就需要使用到自定义事件。类似有 `JS` 设计模式中的观察者模式，子组件用 `$emit()` 来触发事件，父组件用 `$on()` 来监听子组件的事件。

父组件也可以直接在子组件的自定义标签上使用 `v-on` 来监听子组件触发的自定义事件。

```html
<div id="app">
    <p>总数：{{ total }}</p>
    <my-component
        @increase="handleGetTotal"
        @reduce="handleGetTotal"></my-component>
</div>
<script>
    Vue.component('my-component', {
        template: '\
        <div>\
            <button @click="handleIncrease">+1</button>\
            <button @click="handleReduce">-1</button>\
        </div>',
        
        data() {
            return {
                counter: 0
            }
        },
        methods: {
            handleIncrease() {
                this.counter++;
                this.$emit('increase', this.counter);
            },
            handleReduce() {
                this.counter--;
                this.$emit('reduce', this.counter);
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            total: 0
        },
        methods: {
            handleGetTotal(total) {
                this.total = total;
            }
        }
    });
</script>
```

- 使用 `v-model`

其实也是通过事件的方式实现，但语法糖可以一定量上简化代码。

```html
<div id="app">
    <p>总数：{{ total }}</p>
    <my-component v-model="total"></my-component>
</div>
<script>
    Vue.component('my-component', {
        template: '<button @click="handleClick">+1</button>',
        data() {
            return {
                counter: 0
            }
        },
        methods: {
            handleClick() {
                this.counter++;
                this.$emit('input', this.counter);
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            total: 0
        },
    });
</script>
```

当然，也可以完全还原第一个例子：

```html
<div id="app">
    <p>总数：{{ total }}</p>
    <my-component v-model="total"></my-component>
</div>
<script>
    Vue.component('my-component', {
        template: '\
        <div>\
            <button @click="handleIncrease">+1</button>\
            <button @click="handleReduce">-1</button>\
        </div>',
        data() {
            return {
                counter: 0
            }
        },
        methods: {
            handleIncrease() {
                this.counter++;
                this.$emit('input', this.counter);
            },
            handleReduce() {
                this.counter--;
                this.$emit('input', this.counter);
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            total: 0
        },
    });
</script>
```

`v-model` 还可以用来创建自定义的表单输入组件，进行数据的双向绑定：

```html
<div id="app">
    <p>总数：{{ total }}</p>
    <my-component v-model="total"></my-component>
    <button @click='handleIncrease'>+1</button>
    <button @click="handleReduce">-1</button>
</div>
<script>
    Vue.component('my-component', {
        props: ['value'],
        template: '<input :value="value" @input="updateValue">',
        data() {
            return {
                counter: 0
            }
        },
        methods: {
            updateValue() {
                this.$emit('input', event.target.value);
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            total: 0
        },
        methods: {
            handleIncrease() {
                this.total++;
            },
            handleReduce() {
                this.total--;
            }
        }
    });
</script>
```

控件接收一个 `value` 属性，在有新的 `value` 时触发 `input` 事件。

- 非父子间通信

兄弟组件和跨多级组件之间的通信，在 `Vue.js 2.x` 中，推荐使用一个空的 `Vue` 实例作为中央事件总线(`bus`)，也就是一个中介。

```html
<div id="app">
    {{ message }}
    <component-a></component-a>
</div>
<script>
    var bus = new Vue();

    Vue.component('component-a', {
        template: '<button @click="handleEvent">传递事件</button>',
        methods: {
            handleEvent() {
                bus.$emit('on-message', '来自组件 component-a 的内容');
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        },
        mounted () {
            var _this = this;
            // 在实例初始化时，监听来自 bus 的事件
            bus.$on('on-message', function(msg) {
                _this.message = msg;
            })
        }
    });
</script>
```

除了中央事件总线 `bus` 外，还有两种方法可以实现组件间的通信：父链和子组件索引。

- 父链

> 在子组件中，使用 `this.$parent` 可以直接访问该组件的父实例或组件，父组件也可以通过 `this.$children` 访问它的所有的子组件，而且可以递归向上或向下无限访问，直到根实例或最内层的组件。

```html
<div id="app">
    {{ message }}
    <component-a></component-a>
</div>
<script>
    Vue.component('component-a', {
        template: '<button @click="handleEvent">通过父链之间修改数据</button>',
        methods: {
            handleEvent() {
                this.$parent.message = '来自子组件 component-a 的内容';
            }
        }
    });

    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        }
    })
</script>
```

尽管 `Vue` 允许这样操作，但在业务中，子组件应该尽可能的避免依赖父组件的数据，更不应该去主动修改它的数据。

因为这样使得父子附件紧耦合，只看父组件，很难理解父组件的状态，因为它可能被任意组件修改，理想情况下，只有组件自己能修改它的状态。父子组件最好还是通过 `props` 和 `$emit` 来通信。

- 子组件索引

> 当子组件较多时，通过 `this.$children` 来一一遍历找出需要的一个组件实例是比较困难的，尤其是组件动态渲染时，它们的序列是不固定的。 `Vue` 提供了子组件索引的方法，用特殊的属性 `ref` 来为子组件指定一个索引名称。

```html
<div id="app">
    <button @click="handleRef">通过 ref 获取子组件实例</button>
    <component-a ref="comA"></component-a>
</div>
<script>
    Vue.component('component-a', {
        template: '<div>子组件</div>',
        data() {
            return {
                message: '子组件内容'
            }
        }
    });

    var app = new Vue({
        el: '#app',
        methods: {
            handleRef() {
                var msg = this.$refs.comA.message;
                alert(msg);
            }
        }
    })
</script>
```

在父组件模板中，子组件标签上使用 `ref` 指定一个名称，并在子组件内通过 `this.$refs` 来访问指定名称的子组件。

`$refs` 只在组件渲染完成后才填充，并且并非是响应式的，它仅仅是作为一个直接访问子组件的应急方案，应当避免在模板或计算属性中使用 `$refs`。

##### 使用 `slot` 分发内容

- 什么是 `slot`

当需要让组件组合使用，混合父组件与子组件的内容时，就会用到 `slot`，这个过程叫做内容分发，

在一个 `Vue` 实例中，使用 `props` 传递数据，`enents` 触发事件和 `slot` 内容分发，这就构成了 `Vue` 组件的 `3` 个 `API` 来源，再复杂的组件也是由这 `3` 部分组成的。

- 作用域

在介绍 `slot` 之前，需要理解编译的作用域，比如父组件中有如下模板：

```html
<child-component>
    {{ message }}
</child-component>
```

这里的 `message` 就是一个 `slot`，但是他绑定的是父组件的数据，而不是组件 `child-component` 的数据。

父组件模板的内容是在父组件作用域内编译的，子组件模板的内容是在子组件作用域内编译的。

一个绑定数据作用域在父组件的例子：

```html
<div id="app">
    <child-component v-show="showChild"></child-component>
</div>
<script>
    Vue.component('child-component', {
        template: '<div>子组件</div>',
    });

    var app = new Vue({
        el: '#app',
        data: {
            showChild: true
        }
    })
</script>
```

一个绑定数据作用域在子组件的例子：

```html
<div id="app">
    <child-component></child-component>
</div>
<script>
    Vue.component('child-component', {
        template: '<div v-show="showChild">子组件</div>',
        data() {
            return {
                showChild: true
            }
        }
    });

    var app = new Vue({
        el: '#app',
    })
</script>
```

了解了两者作用域的区别，我们就可以知道，`slot` 分发的内容，作用域是在父组件上的。

- `slot` 用法

单个 `slot`:

在子组件内使用特殊的 `<slot>` 元素可以为这个组件开启一个 `slot` (插槽)，在父组件模板中，插入在子组件标签内的所有内容将代替子组件的 `<slot>` 标签及它的内容。

```html
<div id="app">
    <child-component>
        <p>分发内容</p>
        <p>分发更多内容</p>
    </child-component>
</div>
<script>
    Vue.component('child-component', {
        template: '\
        <div>\
            <slot>\
                <p>如果父组件没有插入内容，默认出现。</p>\
            </slot>\
        </div>'
    });

    var app = new Vue({
        el: '#app'
    })
</script>
```

具名 `slot`:

给 `<slot>` 元素指定一个 `name` 之后可以分发多个内容，具名 `slot` 可以与单个 `slot` 共存。

```html
<div id="app">
    <child-component>
        <h2 slot="header">标题</h2>
        <p>正文内容</p>
        <p>更多正文内容</p>
        <div slot="footer">底部信息</div>
    </child-component>
</div>
<script>
    Vue.component('child-component', {
        template: '\
        <div class="container">\
            <div class="header">\
                <slot name="header"></slot>\
            </div>\
            <div class="main">\
                <slot></slot>\
            </div>\
            <div class="footer">\
                <slot name="footer"><slot>\
            </div>\
        </div>'
    });

    var app = new Vue({
        el: '#app'
    })
</script>
```

渲染后：

```html
<div id="app">
    <div class="container">
        <div class="header">
            <h2>标题</h2>
        </div>
        <div class="main"> 
            <p>正文内容</p> 
            <p>更多正文内容</p> 
        </div> 
        <div class="footer">
            <div>底部信息</div>
        </div>
    </div>
</div>
```

- 作用域插槽

作用域插槽是一种特殊的 `slot`，使用一个可以复用的模板代替已渲染元素。

```html
<div id="app">
    <child-component>
        <template scope="props">
            <p>来组父组件的内容</p>
            <p>{{ props.msg }}</p>
        </template>
    </child-component>
</div>
<script>
    Vue.component('child-component', {
        template: '\
        <div class="container">\
            <slot msg="来组子组件的内容"></slot>\
        </div>'
    });

    var app = new Vue({
        el: '#app'
    })
</script>
```

观察例子可发现，父组件在 `template` 标签中属性 `scope` 定义了一个临时变量 `props` 来访问子组件插槽的数据 `msg`。

作用域插槽是使用场景主要是既可以复用子组件的 `slot`，又可以使 `slot` 的内容不一致。

- 访问 `slot`

使用方法 `$slots` 访问分发内容。

```html
<div id="app">
    <child-component>
        <h2 slot="header">标题</h2>
        <p>正文内容</p>
        <p>更多正文内容</p>
        <div slot="footer">底部信息</div>
    </child-component>
</div>
<script>
    Vue.component('child-component', {
        template: '\
        <div class="container">\
            <div class="header">\
                <slot name="header"></slot>\
            </div>\
            <div class="main">\
                <slot></slot>\
            </div>\
            <div class="footer">\
                <slot name="footer"><slot>\
            </div>\
        </div>',
        mounted() {
            var header = this.$slots.header;
            var main = this.$slots.default;
            var footer = this.$slots.footer;
            console.log(header)
            console.log(footer[0].elm.innerHTML)
        }
    });

    var app = new Vue({
        el: '#app'
    })
</script>
```

通过 `$slots` 可以访问某个具名的 `slot`，`this.$slots.default` 包括了所有没有包含在具名 `slot` 的节点。

`$slots` 在业务中几乎用不到，在 `render` 函数创建组件时会比较有用，但是还是用于独立组件的开发中。
