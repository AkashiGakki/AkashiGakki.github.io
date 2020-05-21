---
title: Highmaps 地图数据可视化
date: yyyy-mm-dd
thumbnail: /images/bg-10.jpg
category: 
    - 前端
    - JavaScript
    - Charts
tags: 
    - 前端
    - JavaScript
    - charts

---

#### `Highmaps`
---

> `Highmaps` 是继承自 `Highcharts` 的专门用于地图的图表插件。`Highmaps` 除了根据值展示地理区域色块外，还支持线段（可以表示公路，河流等）、点（城市，兴趣点等）等其他地理元素。

<!-- more -->

##### 加载`js`文件

```js
<script src="https://img.hcharts.cn/highmaps/highmaps.js"></script>
```

如果需要和`Highcharts` 一起使用，则是引入 `map.js` 即可

```js
<script src="https://img.hcharts.cn/highcharts/highcharts.js"></script>
<script src="https://img.hcharts.cn/highmaps/modules/map.js"></script>
```

##### 加载地图数据文件

> 以下以加载中国地图为例：

###### 通过加载 `js` 文件加载地图数据

直接以 `script` 标签的形式加载文件，对应的取地图数据的方法是：

```js
<script src="https://data.jianshukeji.com/geochina/china.js"></script>
<script>
    var mapdata = Highcharts.maps['cn/china'];
</script>
```

其中 `Highcharts.maps['cn/china']` 可以通过查看文件获得。

###### 通过加载 `json` 文件加载地图数据

由于跨域问题，所以加载 `json` 时需要用到 `jsonp`，这里直接用我们提供的接口即可

```js
$.getJSON('https://data.jianshukeji.com/jsonp?filename=geochina/china.json&callback=?', function(data) {
    var mapdata = data;
});
```

地图数据集查询：`https://img.hcharts.cn/mapdata/`

##### 初始化地图

```js
// 初始化地图
var map = Highcharts.mapChart('container', {
    series: [{
        mapData: mapdata,
    }]
});    
```

##### 加载数据并与地图关联

加载地图数据并初始化图表后，可以将业务数据配置在 `series.data` 中，格式如下：

```js
series: [{
    mapData: mapdata,
    data: [{
        name: '北京',
        value: 2000,
        rank: 1
    },{
        name: '上海',
        value: 1500,
        rank: 2
    }]
}]
```

需要注意的是，设置完数据后，我们还需要指定数据与地图数据的关联属性，即 `joinBy`，例如：

```js
series: [{
    mapData: mapdata,
    data: [{
        name: '北京',
        value: 2000,
        rank: 1
    }, {
        name: '上海',
        value: 1500,
        rank: 2
    }],
    joinBy: 'name'
}]
```

这样，一个简单的中国地图图表数据就创建好了。

##### `js` 加载地图数据实例展示

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>China_Map</title>
    <!-- 引入 js 依赖 -->
    <script src="https://img.hcharts.cn/highcharts/highcharts.js"></script>
    <script src="https://img.hcharts.cn/highmaps/modules/map.js"></script>
</head>
<body>
    <div id="container"></div>
<!-- 通过 js 加载地图数据 -->
<script src="https://data.jianshukeji.com/geochina/china.js"></script>
<script>
    var mapdata = Highcharts.maps['cn/china'];
    // 初始化地图
    var map = Highcharts.mapChart('container', {
        // 添加标题
        title: {
            text: "China_Map"
        },
        // 图表配置
        series: [{
            mapData: mapdata,
            data: [{
                name: '北京',
                value: 2000,
                rank: 1
            }, {
                name: '上海',
                value: 1500,
                rank: 2
            }],
            joinBy: 'name'
        }],
        // 去除水印
        credits: {
            enabled: false
        }
    });    
</script>
</body>
</html>
```

![js_map](http://ww1.sinaimg.cn/large/9c62a0cfly1g5efug2pndj216y0lwq5d.jpg)

##### `json` 加载地图数据实例展示

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>China_Map</title>
    <!-- 引入 js 依赖 -->
    <script src="https://img.hcharts.cn/highcharts/highcharts.js"></script>
    <script src="https://img.hcharts.cn/highmaps/modules/map.js"></script>
</head>
<body>
    <div id="main"></div>
<!-- 通过 js 加载地图数据 -->
<script src="https://data.jianshukeji.com/geochina/china.js"></script>
<!-- 加载 jQuery 依赖 -->
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
<script>
    $.getJSON('https://data.jianshukeji.com/jsonp?filename=geochina/china.json&callback=?', function(mapdata) {
        var map = Highcharts.mapChart('main', {
            title: {
                text: 'China_Map'
            },
            series: [{
                mapData: mapdata,
                name: 'value',
                data: [{
                    city: '北京',
                    value: 2000,
                    rank: 1
                },{
                    city: '上海',
                    value: 1500,
                    rank: 2
                },{
                    city: '四川',
                    value: '1300',
                    rank: 3
                },{
                    city: '重庆',
                    value: '1300',
                    rank: 3
                },{
                    city: '广东',
                    value: 1200,
                    rank: 4
                }],
                joinBy: ['name', 'city']
            }],
            credits: {
                enabled: false
            }
        });
    });
</script>
</body>
</html>
```

![json_map](http://ww1.sinaimg.cn/large/9c62a0cfly1g5efuy1pi3j216u0momzn.jpg)

#### 尝试创建一个世界地图

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Map_World</title>
    <script src="https://img.hcharts.cn/highcharts/highcharts.js"></script>
    <script src="https://img.hcharts.cn/highmaps/modules/map.js"></script>
</head>
<body>
    <div id="container"></div>
<!-- 地图数据集参考：https://img.hcharts.cn/mapdata/ -->
<script src="https://img.hcharts.cn/mapdata/custom/world-eckert3-highres.js"></script>
<script>
    var mapdata = Highcharts.maps['custom/world-eckert3-highres'];
    var map = Highcharts.mapChart('container', {
        title: {
            text: 'World_Map'
        },
        series: [{
            mapData: mapdata,
            name: 'Country',
            data: [{
                name: 'China',
                value: 1230
            },{
                name: 'United States of America',
                value: 1235
            },{
                name: 'Australia',
                value: 1245
            },{
                name: 'Russia',
                value: 1256
            }],
            joinBy: 'name'
        }],
        credits:{
            enabled:false
        },
        mapNavigation: {
            enabled: true, // 开启地图导航器，默认是 false
            enableButtons: true, // 是否启用缩放按钮
        }
    });
</script>
</body>
</html>
```
![world_map](http://ww1.sinaimg.cn/large/9c62a0cfly1g5eg2yosjgj21uo0m6afj.jpg)

