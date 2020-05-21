---
title: Highcharts 数据可视化
date: 2019-7-26
thumbnail: /images/bg-9.jpg
category: 
    - 前端
    - JavaScript
    - Charts
tags: 
    - 前端
    - JavaScript
    - charts

---

#### Highcharts
---

> `Highcharts` 是一个用纯`JavaScript`编写的一个图表库， 能够很简单便捷的在`web`网站或是`web`应用程序添加有交互性的图表

<!-- more -->

##### 获取`Highcharts`

- `CDN`获取
    - `https://code.highcharts.com.cn/index.html`
- 官网获取资源包
    - `https://www.highcharts.com.cn/download`
- `npm`、`bower`等第三方包管理工具下载
    - `npm`:
        - `https://www.highcharts.com.cn/docs/install-from-npm`
    - `bower`:
        - `https://www.highcharts.com.cn/docs/install-from-bower`

##### 引入`Highcharts`

```html
<script src="http://cdn.highcharts.com.cn/highcharts/highcharts.js"></script>
```

##### 创建一个简单的图表

- 引入`CDN`的`JS`文件
- 初始化函数 `Highcharts.chart` 来创建图表
    - 该函数接受两个参数，第一个参数是 `DOM` 容器的 `Id`，第二个参数是`图表配置`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Highcharts_Demo</title>
</head>
<body>
    <!-- 图表容器 DOM -->
    <div id="container" style="width: 600px;height:400px;"></div>
    <!-- 引入 highcharts.js -->
    <script src="http://cdn.highcharts.com.cn/highcharts/highcharts.js"></script>
    <script>
        // 图表配置
        var options = {
            chart: {
                type: 'bar'                          //指定图表的类型，默认是折线图（line）
            },
            title: {
                text: 'Highcharts_Demo'                 // 标题
            },
            xAxis: {
                categories: ['苹果', '香蕉', '橙子']   // x 轴分类
            },
            yAxis: {
                title: {
                    text: '吃水果个数'                // y 轴标题
                }
            },
            series: [{                              // 数据列
                name: 'Akashi',                        // 数据列名
                data: [1, 0, 4]                     // 数据
            }, {
                name: 'Asuka',
                data: [5, 7, 3]
            }],
            credits:{
                enabled:false                       // 去除右下角水印
            }
        };
        // 图表初始化函数
        var chart = Highcharts.chart('container', options);
    </script>
</body>
</html>
```

##### 去除水印

> 去除右下角水印链接，只需要在`highcharts.js`中修改

```js
credits:{
    enabled:false
}；
```

![效果](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ddzbrb0cj215e0memxp.jpg)
