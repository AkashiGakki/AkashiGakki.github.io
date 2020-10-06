---
title: CesiumJS 进阶
date: 2020-10-04
category: 
    - 前端
tags:
    - 前端
    - Cesium
thumbnail: /images/asuka/asu-24.jpg

---

# `CesiumJS` 进阶

> 记录使用 `Cesium` 的实体（`Entity`）`API`绘制空间数据、使用 `Viewer` 为操作 `entities` 提供出来的功能函数、使用 `Primitive` `API` 的几何图形和外观系统、创建使用 `ParticleSystem` 粒子系统等。

<!-- more -->

## 空间数据可视化（`Entity`）

> Cesium 具有丰富的用于空间数据的 API，可以分为两类：面向图形开发人员的低级API（通常称为原始(`Primitive`) `API`）和用于数据驱动的可视化的高级API（称为实体(`Entity`) `API`）。

- `Primitive API`

`原始API` 的主要目标是暴露手头执行任务所需的最小抽象量。它希望我们像图形程序员一样思考，并使用图形术语。它的结构是为给定的可视化类型提供最有性能和灵活性的实现，而不是为了 `API` 的一致性。

`原始API` 功能强大且灵活，但大多数应用程序都提供比 `Primitive API` 的抽象级别更高的服务接口。`Primitive API` 更面向于底层图形开发。

- `Entity API`

`实体API` 的目的是公开一组设计一致的高级对象，这些对象将相关的可视化和信息聚合到一个统一的数据结构中，我们称之为实体。它让我们专注于展示我们的数据，而不是担心可视化的潜在机制。它还提供了易于构建复杂的、时间动态可视化的构造，这种可视化方式与静态数据自然相适应。

虽然 `实体API` 实际上在背后使用了 `Primitive API`，但我们几乎永远不必关注实现细节。通过将各种启发式应用到我们提供的数据，`实体API` 能够提供灵活的、高性能的可视化，同时公开一致的、易于学习和易于使用的接口。

### 管理 `Entities`

> 每一个 `Entity` 对象都被添加到 `EntityCollection` 对象集合中，其中每个实体都有唯一的 `ID`。

- 添加

```js
let entity = new Entity({
    id : 'uniqueId',
    ...
});
this.$viewer.entities.add(entity);
```

所有实体实例都有一个唯一的 `id`，在创建或修改时可用于从集合中检索实体。我们可以为实体指定一个 `ID`，否则将自动生成一个 `ID`。

- 隐藏

```js
entity.show = false;
```

- 获取

> 使用 `getByiId` 检索实体。如果不存在具有提供的 `ID` 的实体，则返回 `undefined`。

```js
let entity = this.$viewer.entities.getById('uniqueId')
```

要获取实体或创建新实体（如果不存在），可以使用 `getOrCreateEntity`。

```js
let entity = this.$viewer.entities.getOrCreateEntity('uniqueId');
```

- 修改

> 可以在获取实体后对其属性进行修改。

```js
let entity = this.$viewer.entities.getById('uniqueId')
entity.label.text= "akashi"; 
```

- 移除

```js
// 先查后删
let entity = viewer.entities.getById('uniqueId');
this.$viewer.entities.remove(entity);

// 直接移除
this.$viewer.entities.removeById('uniqueId');

//移除所有
this.$viewer.entities.removeAll();  
```

### 点、图标和标签（Points, billboards, and labels）

> 可以通过设置 `position`、`point` 和 `label` 来创建图形点或标签。

- 点 && 文字标签

```js
let point = this.$viewer.entities.add({
  name: "point",
  position: Cesium.Cartesian3.fromDegrees(121.506377, 31.245105),
  point: {
    pixelSize: 5,
    color: Cesium.Color.RED,
    outlineColor: Cesium.Color.WHITE,
    outlineWidth: 2,
  },
  label: {
    text: "Shanghai",
    font: "14pt monospace",
    style: Cesium.LabelStyle.FILL_AND_OUTLINE,
    outlineWidth: 2,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
    pixelOffset: new Cesium.Cartesian2(0, -9),
  },
});
this.$viewer.zoomTo(point);

let camera = new Cesium.Camera(this.$viewer.scene);
camera.flyTo({
  destination: Cesium.Cartesian3.fromDegrees(
    121.506377,
    31.245105,
    1000000.0
  ),
});
```

![点](http://images.akashi.org.cn/FkZUo19H2HVXmfrQ_6J5Lz1oa90A)

- 图标

```js
let logo = this.$viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(139.46, 35.42),
  billboard: {
    image: "images/Nogizaka46_Logo.png",
    width: 128,
    height: 128,
  },
});
this.$viewer.trackedEntity = logo;

let camera = new Cesium.Camera(this.$viewer.scene);
camera.flyTo({
  destination: Cesium.Cartesian3.fromDegrees(
    136,
    36,
    1000000
  ),
});
```

![图标](http://images.akashi.org.cn/FsRX4nF9mRyKiY0BPNSl40Ei4qOJ)

### `Picking` 拾取

> 在 `Cesium` 中，想获取不同的对象，需要通过 `pick` 方法来进行拾取。

然而其中又有多种 `pick` 的方法，包括 `scene` 中的 `pick`、`pickPosition` 和 `drillPick`；`camera` 中的 `getPickRay` 和 `pickEllipsoid`；以及 `Globe` 中的 `pick`。

1. 屏幕坐标

> 通过 `movement.position` 获取。

```js
// 屏幕坐标
let handler = new Cesium.ScreenSpaceEventHandler(
  this.$viewer.scene.canvas
);
handler.setInputAction((movement) => {
  console.log(movement.position);
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

2. 世界坐标

> 通过 `viewer.scene.camera.pickEllipsoid(movement.position, ellipsoid)` 获取，可以获取当前点击视线与椭球面相交处的坐标，其中 `ellipsoid` 是当前地球使用的椭球对象。

```js
 // 世界坐标
let handler = new Cesium.ScreenSpaceEventHandler(this.$viewer.scene.canvas);
handler.setInputAction((movement) => {
  let position = this.$viewer.scene.camera.pickEllipsoid(
    movement.position,
    this.$viewer.scene.globe.ellipsoid
  );
  console.log(position);
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

3. 场景坐标

> 通过 `viewer.scene.pickPosition(movement.position)` 获取，根据窗口坐标，从场景的深度缓冲区中拾取相应的位置，返回笛卡尔坐标。

```js
// 场景坐标
let handler = new Cesium.ScreenSpaceEventHandler(this.$viewer.scene.canvas);
handler.setInputAction((movement) => {
  let position = this.$viewer.scene.pickPosition(movement.position);
  console.log(position);
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

4. 地标坐标

> 通过 `viewer.scene.globe.pick(ray, scene)` 获取，可以获取点击处地球表面的世界坐标，不包括模型、倾斜摄影表面。其中 `ray=viewer.camera.getPickRay(movement.position)`。

```js
// 地标坐标
let handler = new Cesium.ScreenSpaceEventHandler(this.$viewer.scene.canvas);
handler.setInputAction((movement) => {
  let ray = this.$viewer.camera.getPickRay(movement.position);
  let position = this.$viewer.scene.globe.pick(ray, this.$viewer.scene);
  console.log(position);
}, Cesium.ScreenSpaceEventType.LEFT_CLICK);
```

### 形状和体积（Shapes and Volumes）

之前介绍过，`Cesium` 加载点线面矢量数据可以通过 `Entity API` 或 `Primitive API` 实现，而无论我们怎样定义实体实例和几何，所有形状和物体都有一组共同的属性来控制它们的外观。

1. `fill`

> 布尔型，用于指定目标形状是否被填充，默认为 `true`

2. `outline`

> 布尔型，用于指定是否绘制形状的边缘， 默认为 `false`

3. `material`

> 如果 `fill` 为 `true`，该属性可以控制填充的材质类型，默认为 `Color.WHITE`

具体形状的外观属性可通过官方 `API` 中的 `Cesium.Entity` 下各形状的 `Type` 属性查看。

[Cesium.Entity API](http://cesium.xin/cesium/cn/Documentation1.62/Entity.html?classFilter=Entity)

![Entity API](http://images.akashi.org.cn/FsJLRGzYgBQOTdEV7mZt8bGqnOBi)

#### 材质

例如我们创建一个蓝色半透明的椭圆实例，默认 `fill` 为 `true`：

```js
let entity = this.$viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(-103.0, 40.0),
  ellipse: {
    semiMinorAxis: 250000.0,
    semiMajorAxis: 400000.0,
    material: Cesium.Color.BLUE.withAlpha(0.5),
  },
});

this.$viewer.zoomTo(entity);
```

![半透明材质](http://images.akashi.org.cn/FvOloMU9w5r4iBKF9i_HOovlLHjB)

然后改变其材质属性，实现各种不同的效果：

```js
// 棋盘材质
entity.ellipse.material = new Cesium.CheckerboardMaterialProperty({
  evenColor: Cesium.Color.WHITE,
  oddColor: Cesium.Color.BLACK,
  repeat: new Cesium.Cartesian2(4, 4),
});
```

![棋盘材质](http://images.akashi.org.cn/FupDZBF4Im7pkivmamfh7fHbIOlU)

```js
// 条纹材质
entity.ellipse.material = new Cesium.StripeMaterialProperty({
  evenColor: Cesium.Color.WHITE,
  oddColor: Cesium.Color.BLACK,
  repeat: 32,
});
```

![条纹材质](http://images.akashi.org.cn/FkqWGGkd5WrgKfLwGGvCE60cjGny)

```js
// 网格材质
entity.ellipse.material = new Cesium.GridMaterialProperty({
  color: Cesium.Color.YELLOW,
  cellAlpha: 0.2,
  lineCount: new Cesium.Cartesian2(8, 8),
  lineThickness: new Cesium.Cartesian2(2.0, 2.0),
});
```

![网络材质](http://images.akashi.org.cn/Fm4NviTfzBD-7c6X9EeO8_pKmxKz)

#### 轮廓

`outline` 没有相应的材料，而是依赖于两个独立的 `outlineColor` 和 `outlineWidth` 属性。

```js
entity.ellipse.fill = false;
entity.ellipse.outline = true;
entity.ellipse.outlineColor = Cesium.Color.YELLOW;
entity.ellipse.outlineWidth = 5.0;

this.$viewer.zoomTo(entity);
```

![轮廓](http://images.akashi.org.cn/Fko4Cy-WuQdrI7KhgXexPIflgt_e)

#### 高度与挤压

> 覆盖在地球上的所有形状，当前是圆、椭圆、多边形和矩形，也可以放置在海拔高度或挤压成一个物体。在这两种情况下，形状或物体仍然符合其下方的地球曲率。

当需要物体距离地面一定高度的时候，可以在相应的图形对象上设置高度属性：

```js
let polygon = this.$viewer.entities.add({
  name: "正方形",
  id: "square",
  polygon: {
    hierarchy: Cesium.Cartesian3.fromDegreesArray([...]),
    material: Cesium.Color.RED.withAlpha(0.5),
    outline: true,
    outlineColor: Cesium.Color.BLACK,
    height: 250000,
  },
});

this.$viewer.zoomTo(polygon);
```

在侧面可以看到物体就有了高度。

![设置高度](http://images.akashi.org.cn/Fo0tcgymZDEO7Xcqj1TLzXwHI8bO)

将形状挤压成物体同样，需要设置 `extrudedHeight` 属性:

```js
let polygon = this.$viewer.entities.add({
  name: "正方形",
  id: "square",
  polygon: {
    hierarchy: Cesium.Cartesian3.fromDegreesArray([...]),
    material: Cesium.Color.RED.withAlpha(0.5),
    outline: true,
    outlineColor: Cesium.Color.BLACK,
    height: 200000,
    extrudedHeight: 250000,
  },
});
```

![平面挤压为物体](http://images.akashi.org.cn/FveQPouieVvc2NvX-6iQn6wohCss)

注意：意外发现当同时使用 `height` 与 `extrudedHeight` 并且值相同时，`extrudedHeight` 不会生效。


### 三维图形（3D models）

> `CesiumJS` 支持通过 `glTF`（运行时`asset format`）创建 `3D` 模型。

```js
let position = Cesium.Cartesian3.fromDegrees(
  -75.62808254394531,
  40.02824946899414
);
let modelMatrix = Cesium.Transforms.eastNorthUpToFixedFrame(position);

let heading = Cesium.Math.toRadians(10.0);
let pitch = Cesium.Math.toRadians(-10.0);
let roll = Cesium.Math.toRadians(0.0);

let headingPitchRoll = new Cesium.HeadingPitchRoll(heading, pitch, roll);
let orientation = new Cesium.Transforms.headingPitchRollQuaternion(
  position,
  headingPitchRoll
);

let carModel = this.$viewer.scene.primitives.add(
  new Cesium.Model.fromGltf({
    //异步的加载模型
    url: "model3D/Truck.glb",
    scale: 3.0, //缩放
    position: position,
    orientation: orientation,
    modelMatrix: modelMatrix, //模型矩阵
  })
);

this.$viewer.scene.camera.setView({
  destination: new Cesium.Cartesian3.fromDegrees(
    -75.62808254394531,
    40.02624946899414,
    50.0
  ),
  orientation: {
    heading,
    pitch,
    roll,
  },
});
```

![3D Model(Primitive)](http://images.akashi.org.cn/Fqp5XCusD4NtgLzIJit1jPQZV0vl)

```js
let position = Cesium.Cartesian3.fromDegrees(-123.0744619, 44.0503706, 0);

let heading = Cesium.Math.toRadians(135);
let pitch = 0;
let roll = 0;
let hpr = new Cesium.HeadingPitchRoll(heading, pitch, roll);
let orientation = Cesium.Transforms.headingPitchRollQuaternion(
  position,
  hpr
);

let entity = this.$viewer.entities.add({
  name: "J15",
  position: position,
  orientation: orientation,
  model: {
    uri: "model3D/J15.glb",
    minimumPixelSize: 128,
    maximumScale: 20000,
  },
});

this.$viewer.trackedEntity = entity;
```

![3D models](http://images.akashi.org.cn/Fi4sUKzbxiqX7mEOMozvPmvXptgn)

默认情况下，模型竖直放置、并且面向东面。可以指定四元组（`Quaternion`）给 `Entity.orientation` 属性，以改变放置的方向。

```js
//位置
let position = Cesium.Cartesian3.fromDegrees(-123.0744619, 44.0503706);

//绕垂直于地心的轴旋转
let heading = Cesium.Math.toRadians(45.0);

//绕纬度线旋转
let pitch = Cesium.Math.toRadians(15.0);

//绕经度线旋转
let roll = Cesium.Math.toRadians(0.0);

let orientation = Cesium.Transforms.headingPitchRollQuaternion(position, heading, pitch, roll);
```

![HeadingPitchRoll](http://images.akashi.org.cn/Fjz0QFcnruF5ldtVBQ-vQQGqjQMt)

`heading`（`yaw`）、`pitch`、`roll` 对应了绕 `Z`（垂直轴）、`Y`（维度方向）、`X`（经度方向）进行旋转，正数表示顺时针旋转（由于相对运动，在浏览器上看起来是地球在逆时针旋转），可以参考下图理解（人面向北面，摇头`heading`、点头`pitch`、歪头`roll`）。

### Entity API

> Entity 实例将多种形式的可视化聚集到单个高级对象中。通过手动创建并将实体添加到 `Viewer.entities` 中。

Name | Type | Description
--- | --- | ---
box | BoxGraphics | 与该实体关联的框。
corridor | CorridorGraphics | 与该实体关联的走廊。
cylinder | CylinderGraphics | 与该实体关联的圆柱体。
ellipse | EllipseGraphics | 与该实体关联的椭圆。
ellipsoid | EllipsoidGraphics | 与该实体关联的椭球。
label | LabelGraphics | 与该实体关联的options.label。
model | ModelGraphics | 与该实体关联的模型。
path | PathGraphics | 与该实体关联的路径。
plane | PlaneGraphics | 与该实体关联的平面。
point | PointGraphics | 与该实体关联的点。
polygon | PolygonGraphics | 与该实体关联的多边形。
polyline | PolylineGraphics | 与该实体关联的折线。
rectangle | RectangleGraphics | 与该实体关联的矩形。
wall | WallGraphics | 与该实体关联的墙。

#### `Box`

```js
// 立方体
let blueBox = this.$viewer.entities.add({
  name: "Blue box",
  //中心的位置
  position: Cesium.Cartesian3.fromDegrees(-114.0, 40.0, 300000.0),
  box: {
    //长宽高
    dimensions: new Cesium.Cartesian3(400000.0, 300000.0, 500000.0),
    material: Cesium.Color.BLUE.withAlpha(0.5),
  },
});

let redBox = this.$viewer.entities.add({
  name: "Red box with black outline",
  position: Cesium.Cartesian3.fromDegrees(-107.0, 40.0, 300000.0),
  box: {
    dimensions: new Cesium.Cartesian3(400000.0, 300000.0, 500000.0),
    material: Cesium.Color.RED,
    outline: true,  //显示轮廓
    outlineColor: Cesium.Color.BLACK,
  },
});

let outlineOnly = this.$viewer.entities.add({
  name: "Yellow box outline",
  position: Cesium.Cartesian3.fromDegrees(-100.0, 40.0, 300000.0),
  box: {
    dimensions: new Cesium.Cartesian3(400000.0, 300000.0, 500000.0),
    fill: false, //不显示填充
    outline: true,
    outlineColor: Cesium.Color.YELLOW,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![box](http://images.akashi.org.cn/Fp1om-38SxhZuc0M7iQzzeWeMvBP)

#### `Ellipse`

```js
// 椭圆
// 浮空的绿色圆形
let greenCircle = this.$viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(-111.0, 40.0, 150000.0),
  name: "Green circle at height",
  ellipse: {
    semiMinorAxis: 300000.0,
    semiMajorAxis: 300000.0,
    height: 200000.0, //浮空
    material: Cesium.Color.GREEN,
  },
});

// 红色椭圆形，位于地表，带轮廓
let redEllipse = this.$viewer.entities.add({
  //不带高度
  position: Cesium.Cartesian3.fromDegrees(-103.0, 40.0),
  name: "Red ellipse on surface with outline",
  ellipse: {
    semiMinorAxis: 250000.0,
    semiMajorAxis: 400000.0,
    material: Cesium.Color.RED.withAlpha(0.5),
    outline: true,
    outlineColor: Cesium.Color.RED,
  },
});

//蓝色椭圆柱，旋转了角度
let blueEllipse = this.$viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(-95.0, 40.0, 100000.0),
  name: "Blue translucent, rotated, and extruded ellipse",
  ellipse: {
    semiMinorAxis: 150000.0,
    semiMajorAxis: 300000.0,
    extrudedHeight: 200000.0, //拉伸
    rotation: Cesium.Math.toRadians(45), //旋转
    material: Cesium.Color.BLUE.withAlpha(0.7),
    outline: true,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![ellipse](http://images.akashi.org.cn/Fv_7mzukP8t8Oq2Nuc2R5yNoBpBm)

#### `Corridor`

> 走廊。

```js
 // Corridor
let redCorridor = this.$viewer.entities.add({
  name: "Red corridor on surface with rounded corners and outline",
  corridor: {
    positions: Cesium.Cartesian3.fromDegreesArray([
      -100.0,
      40.0,
      -105.0,
      40.0,
      -105.0,
      35.0,
    ]),
    width: 200000.0,
    material: Cesium.Color.RED.withAlpha(0.5),
    outline: true,
    outlineColor: Cesium.Color.RED,
  },
});

let greenCorridor = this.$viewer.entities.add({
  name: "Green corridor at height with mitered corners",
  corridor: {
    positions: Cesium.Cartesian3.fromDegreesArray([
      -90.0,
      40.0,
      -95.0,
      40.0,
      -95.0,
      35.0,
    ]),
    height: 100000.0,
    width: 200000.0,
    cornerType: Cesium.CornerType.MITERED,
    material: Cesium.Color.GREEN,
  },
});

let blueCorridor = this.$viewer.entities.add({
  name: "Blue extruded corridor with beveled corners and outline",
  corridor: {
    positions: Cesium.Cartesian3.fromDegreesArray([
      -80.0,
      40.0,
      -85.0,
      40.0,
      -85.0,
      35.0,
    ]),
    height: 200000.0,
    extrudedHeight: 100000.0,
    width: 200000.0,
    cornerType: Cesium.CornerType.BEVELED,
    material: Cesium.Color.BLUE.withAlpha(0.5),
    outline: true,
    outlineColor: Cesium.Color.BLUE,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![corridor](http://images.akashi.org.cn/Fku5Q4eKL8DmJmECTp490UWNel-B)

#### `Cylinder`

```js
//圆柱和圆锥 Cylinder Cones
let greenCylinder = this.$viewer.entities.add({
  name: "Green cylinder with black outline",
  position: Cesium.Cartesian3.fromDegrees(-100.0, 40.0, 200000.0),
  cylinder: {
    //圆柱
    length: 400000.0,
    topRadius: 200000.0,
    bottomRadius: 200000.0,
    material: Cesium.Color.GREEN,
    outline: true,
    outlineColor: Cesium.Color.DARK_GREEN,
  },
});

let redCone = this.$viewer.entities.add({
  name: "Red cone",
  position: Cesium.Cartesian3.fromDegrees(-105.0, 40.0, 200000.0),
  cylinder: {
    //圆锥
    length: 400000.0,
    topRadius: 0.0,
    bottomRadius: 200000.0,
    material: Cesium.Color.RED,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![cylinder](http://images.akashi.org.cn/FtSOiWZUrIRaqzWZWAOyaPHme4Yd)

#### `Polygon`

```js
// 多边形 Polygon
let redPolygon = this.$viewer.entities.add({
  name: "贴着地表的多边形",
  polygon: {
    hierarchy: Cesium.Cartesian3.fromDegreesArray([
      -115.0,
      37.0,
      -115.0,
      32.0,
      -107.0,
      33.0,
      -102.0,
      31.0,
      -102.0,
      35.0,
    ]),
    material: Cesium.Color.RED,
  },
});

let greenPolygon = this.$viewer.entities.add({
  name: "绿色拉伸多边形",
  polygon: {
    hierarchy: Cesium.Cartesian3.fromDegreesArray([
      -108.0,
      42.0,
      -100.0,
      42.0,
      -104.0,
      40.0,
    ]),
    extrudedHeight: 500000.0,
    material: Cesium.Color.GREEN,
  },
});

let orangePolygon = this.$viewer.entities.add({
  name: "每个顶点具有不同拉伸高度的橘色多边形",
  polygon: {
    hierarchy: Cesium.Cartesian3.fromDegreesArrayHeights([
      -108.0,
      25.0,
      100000,
      -100.0,
      25.0,
      100000,
      -100.0,
      30.0,
      100000,
      -108.0,
      30.0,
      300000,
    ]),
    extrudedHeight: 0,
    perPositionHeight: true,
    material: Cesium.Color.ORANGE,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

let bluePolygon = this.$viewer.entities.add({
  name: "具有挖空效果的蓝色多边形",
  polygon: {
    hierarchy: {
      positions: Cesium.Cartesian3.fromDegreesArray([
        -99.0,
        30.0,
        -85.0,
        30.0,
        -85.0,
        40.0,
        -99.0,
        40.0,
      ]),
      holes: [
        {
          positions: Cesium.Cartesian3.fromDegreesArray([
            -97.0,
            31.0,
            -97.0,
            39.0,
            -87.0,
            39.0,
            -87.0,
            31.0,
          ]),
          holes: [
            {
              positions: Cesium.Cartesian3.fromDegreesArray([
                -95.0,
                33.0,
                -89.0,
                33.0,
                -89.0,
                37.0,
                -95.0,
                37.0,
              ]),
              holes: [
                {
                  positions: Cesium.Cartesian3.fromDegreesArray([
                    -93.0,
                    34.0,
                    -91.0,
                    34.0,
                    -91.0,
                    36.0,
                    -93.0,
                    36.0,
                  ]),
                },
              ],
            },
          ],
        },
      ],
    },
    material: Cesium.Color.BLUE,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![polygon](http://images.akashi.org.cn/Fh4fh6BUEKFuiqVsckdzc1mS0ITG)

#### `Polylines`

```js
// Polylines
let redLine = this.$viewer.entities.add({
  name: "Red line on terrain",
  polyline: {
    positions: Cesium.Cartesian3.fromDegreesArray([-75, 35, -125, 35]),
    width: 5,
    material: Cesium.Color.RED,
    clampToGround: true,
  },
});
redLine.show = false;

let greenRhumbLine = this.$viewer.entities.add({
  name: "Green rhumb line",
  polyline: {
    positions: Cesium.Cartesian3.fromDegreesArray([-75, 35, -125, 35]),
    width: 5,
    arcType: Cesium.ArcType.RHUMB,
    material: Cesium.Color.GREEN,
  },
});
greenRhumbLine.show = false;

let glowingLine = this.$viewer.entities.add({
  name: "Glowing blue line on the surface",
  polyline: {
    positions: Cesium.Cartesian3.fromDegreesArray([-75, 37, -125, 37]),
    width: 10,
    material: new Cesium.PolylineGlowMaterialProperty({
      glowPower: 0.2,
      taperPower: 0.5,
      color: Cesium.Color.CORNFLOWERBLUE,
    }),
  },
});
glowingLine.show = false;

let orangeOutlined = this.$viewer.entities.add({
  name:
    "Orange line with black outline at height and following the surface",
  polyline: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -75,
      39,
      250000,
      -125,
      39,
      250000,
    ]),
    width: 5,
    material: new Cesium.PolylineOutlineMaterialProperty({
      color: Cesium.Color.ORANGE,
      outlineWidth: 2,
      outlineColor: Cesium.Color.BLACK,
    }),
  },
});
orangeOutlined.show = false;

let purpleArrow = this.$viewer.entities.add({
  name: "Purple straight arrow at height",
  polyline: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -75,
      43,
      500000,
      -125,
      43,
      500000,
    ]),
    width: 10,
    arcType: Cesium.ArcType.NONE,
    material: new Cesium.PolylineArrowMaterialProperty(
      Cesium.Color.PURPLE
    ),
  },
});
purpleArrow.show = false;

let dashedLine = this.$viewer.entities.add({
  name: "Blue dashed line",
  polyline: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -75,
      45,
      500000,
      -125,
      45,
      500000,
    ]),
    width: 4,
    material: new Cesium.PolylineDashMaterialProperty({
      color: Cesium.Color.CYAN,
    }),
  },
});
dashedLine.show = false;

this.$viewer.zoomTo(this.$viewer.entities);
```

![polyline](http://images.akashi.org.cn/FtMPTHJ2AW7aa8qyYSCmHs4t2lNr)

#### `Polyline Volumes`

```js
// Polyline Volumes
function computeCircle(radius) {
  var positions = [];
  for (var i = 0; i < 360; i++) {
    var radians = Cesium.Math.toRadians(i);
    positions.push(
      new Cesium.Cartesian2(
        radius * Math.cos(radians),
        radius * Math.sin(radians)
      )
    );
  }
  return positions;
}

function computeStar(arms, rOuter, rInner) {
  var angle = Math.PI / arms;
  var length = 2 * arms;
  var positions = new Array(length);
  for (var i = 0; i < length; i++) {
    var r = i % 2 === 0 ? rOuter : rInner;
    positions[i] = new Cesium.Cartesian2(
      Math.cos(i * angle) * r,
      Math.sin(i * angle) * r
    );
  }
  return positions;
}

let redTube = this.$viewer.entities.add({
  name: "Red tube with rounded corners",
  polylineVolume: {
    positions: Cesium.Cartesian3.fromDegreesArray([
      -85.0,
      32.0,
      -85.0,
      36.0,
      -89.0,
      36.0,
    ]),
    shape: computeCircle(60000.0),
    material: Cesium.Color.RED,
  },
});

let greenBox = this.$viewer.entities.add({
  name: "Green box with beveled corners and outline",
  polylineVolume: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -90.0,
      32.0,
      0.0,
      -90.0,
      36.0,
      100000.0,
      -94.0,
      36.0,
      0.0,
    ]),
    shape: [
      new Cesium.Cartesian2(-50000, -50000),
      new Cesium.Cartesian2(50000, -50000),
      new Cesium.Cartesian2(50000, 50000),
      new Cesium.Cartesian2(-50000, 50000),
    ],
    cornerType: Cesium.CornerType.BEVELED,
    material: Cesium.Color.GREEN,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

let blueStar = this.$viewer.entities.add({
  name: "Blue star with mitered corners and outline",
  polylineVolume: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -95.0,
      32.0,
      0.0,
      -95.0,
      36.0,
      100000.0,
      -99.0,
      36.0,
      200000.0,
    ]),
    shape: computeStar(7, 70000, 50000),
    cornerType: Cesium.CornerType.MITERED,
    material: Cesium.Color.BLUE,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![Polyline Volumes](http://images.akashi.org.cn/FpHyXntnj1RkRexHNbFKapzgYxFi)

#### `Rectangle`

```js
// rectangle
//红色矩形
let redRectangle = this.$viewer.entities.add({
  name: "Red translucent rectangle with outline",
  rectangle: {
    coordinates: Cesium.Rectangle.fromDegrees(-110.0, 20.0, -80.0, 25.0),
    material: Cesium.Color.RED.withAlpha(0.5),
    outline: true,
    outlineColor: Cesium.Color.RED,
  },
});

//绿色旋转、拉伸的矩形
let greenRectangle = this.$viewer.entities.add({
  name: "Green translucent, rotated, and extruded rectangle",
  rectangle: {
    coordinates: Cesium.Rectangle.fromDegrees(-100.0, 30.0, -90.0, 40.0),
    material: Cesium.Color.GREEN.withAlpha(0.5),
    rotation: Cesium.Math.toRadians(45),
    extrudedHeight: 300000.0,
    height: 100000.0,
    outline: true,
    outlineColor: Cesium.Color.GREEN,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![rectangle](http://images.akashi.org.cn/FjvCfNNzuasoWcdAYz775CO9-5R6)

#### `Sphere Ellipsoid`

```js
// Sphere Ellipsoid
let blueEllipsoid = this.$viewer.entities.add({
  name: "Blue ellipsoid",
  position: Cesium.Cartesian3.fromDegrees(-114.0, 40.0, 300000.0),
  ellipsoid: {
    //可以指定三个轴的半径
    radii: new Cesium.Cartesian3(200000.0, 200000.0, 300000.0),
    material: Cesium.Color.BLUE,
  },
});

let redSphere = this.$viewer.entities.add({
  name: "Red sphere with black outline",
  position: Cesium.Cartesian3.fromDegrees(-107.0, 40.0, 300000.0),
  ellipsoid: {
    //正球体
    radii: new Cesium.Cartesian3(300000.0, 300000.0, 300000.0),
    material: Cesium.Color.RED,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

let ellipsoidOutlineOnly = this.$viewer.entities.add({
  name: "Yellow ellipsoid outline",
  position: Cesium.Cartesian3.fromDegrees(-100.0, 40.0, 300000.0),
  ellipsoid: {
    radii: new Cesium.Cartesian3(200000.0, 200000.0, 300000.0),
    fill: false,
    outline: true,
    outlineColor: Cesium.Color.YELLOW,
    slicePartitions: 24, //横向切割线
    stackPartitions: 36, //纵向切割线
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![sphere](http://images.akashi.org.cn/FhOvzmTscLb5bg112xAMAR5k_1pI)

#### `Wall`

```js
// wall
//东西方向的横墙
let redWall = this.$viewer.entities.add({
  name: "Red wall at height",
  wall: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -115.0,
      44.0,
      200000.0, //坐标点
      -90.0,
      44.0,
      200000.0,
    ]),
    minimumHeights: [100000.0, 100000.0], //按坐标点的最小高度数组
    material: Cesium.Color.RED,
  },
});

//四边围墙
let greenWall = this.$viewer.entities.add({
  name: "Green wall from surface with outline",
  wall: {
    positions: Cesium.Cartesian3.fromDegreesArrayHeights([
      -107.0,
      43.0,
      100000.0,
      -97.0,
      43.0,
      100000.0,
      -97.0,
      40.0,
      100000.0,
      -107.0,
      40.0,
      100000.0,
      -107.0,
      43.0,
      100000.0,
    ]),
    material: Cesium.Color.GREEN,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

//曲折的墙
let blueWall = this.$viewer.entities.add({
  name: "Blue wall with sawtooth heights and outline",
  wall: {
    //坐标点，不指定高度
    positions: Cesium.Cartesian3.fromDegreesArray([
      -115.0,
      50.0,
      -112.5,
      50.0,
      -110.0,
      50.0,
      -107.5,
      50.0,
      -105.0,
      50.0,
      -102.5,
      50.0,
      -100.0,
      50.0,
      -97.5,
      50.0,
      -95.0,
      50.0,
      -92.5,
      50.0,
      -90.0,
      50.0,
    ]),
    maximumHeights: [
      //上高
      100000,
      200000,
      100000,
      200000,
      100000,
      200000,
      100000,
      200000,
      100000,
      200000,
      100000,
    ],
    minimumHeights: [
      //下高
      0,
      100000,
      0,
      100000,
      0,
      100000,
      0,
      100000,
      0,
      100000,
      0,
    ],
    material: Cesium.Color.BLUE,
    outline: true,
    outlineColor: Cesium.Color.BLACK,
  },
});

this.$viewer.zoomTo(this.$viewer.entities);
```

![wall](http://images.akashi.org.cn/FpaX3ZzEX_zLSF-8mEBllXk3rFW3)

## 几何图形和外观（`Geometry and Appearances`）

我们可以通过 `Primitive` `API`来操控几何图形及其外观，或者绘制各种特殊的形状。需要先得到 `Scene` 对象，然后在其上添加 `Primitive` 对象：

`Primitive` 由两个部分组成：

![Primitive](http://images.akashi.org.cn/FltZn-Or6Xd8d3DTSuMEBO8JEv90)

- 几何形状（`Geometry`）：定义了 `Primitive` 的结构，例如三角形、线条、点等

- 外观（`Appearance`）：定义 `Primitive` 的着色（Sharding），包括GLSL（OpenGL着色语言，OpenGL Shading Language）顶点着色器和片段着色器（ vertex and fragment shaders），以及渲染状态（render state）

### Primitive API

Cesium支持以下几何图形：

几何图形 | 说明
--- | ---
BoxGeometry | 立方体
BoxOutlineGeometry | 仅有轮廓的立方体
CircleGeometry | 圆形或者拉伸的圆形
CircleOutlineGeometry | 只有轮廓的圆形
CorridorGeometry | 走廊：沿着地表的多段线，且具有一定的宽度，可以拉伸到一定的高度
CorridorOutlineGeometry | 只有轮廓的走廊
CylinderGeometry | 圆柱、圆锥或者截断的圆锥
CylinderOutlineGeometry | 只有轮廓的圆柱、圆锥或者截断的圆锥
EllipseGeometry | 椭圆或者拉伸的椭圆
EllipseOutlineGeometry | 只有轮廓的椭圆或者拉伸的椭圆
EllipsoidGeometry | 椭球体
EllipsoidOutlineGeometry | 只有轮廓的椭球体
RectangleGeometry | 矩形或者拉伸的矩形
RectangleOutlineGeometry | 只有轮廓的矩形或者拉伸的矩形
PolygonGeometry | 多边形，可以具有空洞或者拉伸一定的高度
PolygonOutlineGeometry | 只有轮廓的多边形
PolylineGeometry | 多段线，可以具有一定的宽度
SimplePolylineGeometry | 简单的多段线
PolylineVolumeGeometry | 多段线柱体
PolylineVolumeOutlineGeometry | 只有轮廓的多段线柱体
SphereGeometry | 球体
SphereOutlineGeometry | 只有轮廓的球体
WallGeometry | 墙
WallOutlineGeometry | 只有轮廓的墙

```js
// 盒子 box
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: Cesium.BoxGeometry.fromDimensions({
        vertexFormat: Cesium.PerInstanceColorAppearance.VERTEX_FORMAT,
        dimensions: new Cesium.Cartesian3(400000.0, 300000.0, 500000.0),
      }),
      modelMatrix: Cesium.Matrix4.multiplyByTranslation(
        Cesium.Transforms.eastNorthUpToFixedFrame(
          Cesium.Cartesian3.fromDegrees(-105.0, 45.0)
        ),
        new Cesium.Cartesian3(0.0, 0.0, 250000),
        new Cesium.Matrix4()
      ),
      id: "boxid",
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.RED.withAlpha(0.5)
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance({
      closed: true,
    }),
  })
);

// 圆 circle
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.CircleGeometry({
        center: Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
        radius: 200000.0,
        // height: 300000,
        // extrudedHeight: 0
      }),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.PINK
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 走廊 corridor
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.CorridorGeometry({
        positions: Cesium.Cartesian3.fromDegreesArray([
          -90.0,
          40.0,
          -70.0,
          35.0,
          -70.0,
          30.0,
        ]),
        width: 60000,
      }),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.RED.withAlpha(0.5)
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 共面多边几何 Coplanar
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.CoplanarPolygonGeometry({
        polygonHierarchy: new Cesium.PolygonHierarchy(
          Cesium.Cartesian3.fromDegreesArrayHeights([
            -110.0,
            65.0,
            100000,
            -100.0,
            65.0,
            100000,
            -100.0,
            70.0,
            100000,
            -110.0,
            70.0,
            300000,
          ])
        ),
      }),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.GREEN
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 圆柱 Cylinder
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.CylinderGeometry({
        length: 400000,
        topRadius: 200000,
        bottomRadius: 200000,
      }),
      modelMatrix: Cesium.Matrix4.multiplyByTranslation(
        Cesium.Transforms.eastNorthUpToFixedFrame(
          Cesium.Cartesian3.fromDegrees(-100, 60)
        ),
        new Cesium.Cartesian3(0.0, 0.0, 100000.0),
        new Cesium.Matrix4()
      ),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.GREEN
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 椭圆 ellipse
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.EllipseGeometry({
        center: Cesium.Cartesian3.fromDegrees(-100.0, 20.0),
        semiMinorAxis: 200000.0,
        semiMajorAxis: 300000.0,
        // 回转
        rotation: Cesium.Math.PI_OVER_FOUR,
        vertexFormat: Cesium.VertexFormat.POSITION_AND_ST,
        height: 300000,
        extrudedHeight: 0,
      }),
    }),
    appearance: new Cesium.EllipsoidSurfaceAppearance({
      material: Cesium.Material.fromType("Checkerboard"),
    }),
  })
);

// 椭球 ellipsoid
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.EllipsoidGeometry({
        radii: new Cesium.Cartesian3(500000.0, 500000.0, 1000000.0),
        vertexFormat: Cesium.VertexFormat.POSITION_AND_NORMAL,
      }),
      modelMatrix: Cesium.Matrix4.multiplyByTranslation(
        Cesium.Transforms.eastNorthUpToFixedFrame(
          Cesium.Cartesian3.fromDegrees(-95, 35)
        ),
        new Cesium.Cartesian3(0.0, 0.0, 500000.0),
        new Cesium.Matrix4()
      ),
      id: "ellipsoid",
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.AQUA
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 多边形 polygon 三角形
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.PolygonGeometry({
        polygonHierarchy: {
          positions: Cesium.Cartesian3.fromDegreesArray([
            -80.0,
            45.0,
            -80.0,
            40.0,
            -85.0,
            40.0,
          ]),
        },
        height: 300000,
        vertexFormat: Cesium.PerInstanceColorAppearance.VERTEX_FORMAT,
      }),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.PURPLE.withAlpha(0.5)
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);


// 矩形 rectangle
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.RectangleGeometry({
        rectangle: Cesium.Rectangle.fromDegrees(
          -140.0,
          30.0,
          -110.0,
          40.0
        ),
        vertexFormat: Cesium.PerInstanceColorAppearance.VERTEX_FORMAT,
      }),
      id: "rectangle",
      attributes: {
        color: new Cesium.ColorGeometryInstanceAttribute(
          0.0,
          1.0,
          1.0,
          0.5
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 球体 Sphere(can't shown)
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.SphereGeometry({
        radius: 10000.0,
        // vertexFormat : Cesium.VertexFormat.POSITION_ONLY
      }),
      modelMatrix: Cesium.Matrix4.multiplyByTranslation(
        Cesium.Transforms.eastNorthUpToFixedFrame(
          Cesium.Cartesian3.fromDegrees(-140, 40)
        ),
        new Cesium.Cartesian3(0.0, 0.0, 100000.0),
        new Cesium.Matrix4()
      ),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.YELLOW.withAlpha(0.5)
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 墙体 Wall
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.WallGeometry({
        positions: Cesium.Cartesian3.fromDegreesArrayHeights([
          -115.0,
          45.0,
          300000.0,
          -115.0,
          50.0,
          300000.0,
          -120.0,
          50.0,
          300000.0,
          -120.0,
          45.0,
          300000.0,
          -115.0,
          45.0,
          300000.0,
        ]),
      }),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.BLUE.withAlpha(0.5)
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);

// 多边形实现箭头
this.$viewer.scene.primitives.add(
  new Cesium.Primitive({
    geometryInstances: new Cesium.GeometryInstance({
      geometry: new Cesium.PolygonGeometry({
        polygonHierarchy: new Cesium.PolygonHierarchy(
          Cesium.Cartesian3.fromDegreesArray([
            -105,
            55,
            -110,
            60,
            -115,
            55,
            -113,
            55,
            -113,
            50,
            -107,
            50,
            -107,
            55,
          ])
        ),
        height: 300000.0,
        // perPositionHeight: true,
        extrudedHeight: 10,
      }),
      attributes: {
        color: Cesium.ColorGeometryInstanceAttribute.fromColor(
          Cesium.Color.RED.withAlpha(0.5)
        ),
      },
    }),
    appearance: new Cesium.PerInstanceColorAppearance(),
  })
);
```

### `Appearance`

> `primitive` 的属性除了 `Geometry`，还有另一个关键属性就是 `Appearance`。它定义了 `primitive` `的纹理，即单个像素的颜色。primitive` 可以有多个几何实例，但只能有一个外观。

外观定义了绘制 `Primitive` 时在GPU上执行的完整 `GLSL` 顶点和面片着色器。外观还定义了完整的渲染状态，它控制绘制 `primitvie` 时 `GPU` 的状态。

我们可以直接定义渲染状态，也可以使用更高级的属性，如“闭合(`closed`)”和“半透明(`translucent`)”，外观将转换为渲染状态。

```js
let appearance  = new Cesium.PerInstanceColorAppearance({
  translucent : false,
  closed : true
});
```

## 粒子系统(`Introduction to Particle Systems`)

> 粒子系统是一种图形技术，可以模拟复杂的物理效果。粒子系统是小图像的集合，当它们一起观看时，会形成一个更复杂的“模糊”物体，如火、烟、天气或烟花等效果。

通过使用诸如初始位置、速度和生命周期等属性指定单个粒子的行为，可以控制这些复杂的效果。

### `Particle system basics`

> 基础粒子效果

```js
let model = this.$viewer.entities.getById("Truck");
let particleSystem = this.$viewer.scene.primitives.add(
  new Cesium.ParticleSystem({
    image: "images/smoke.png",
    imageSize: new Cesium.Cartesian2(20, 20),
    startScale: 1.0,
    endScale: 4.0,
    particleLife: 1.0,
    speed: 5.0,
    emitter: new Cesium.CircleEmitter(0.5),
    emissionRate: 5.0,
    modelMatrix: model.computeModelMatrix(
      Cesium.JulianDate.now(),
      new Cesium.Matrix4()
    ),
    lifetime: 16.0,
  })
);
```

`ParticleSystem` 一个参数化的对象，用于控制单个粒子对象 `Particle` 随时间的外观和行为。粒子由粒子发射器产生，有一个位置和类型，存活一段时间，然后消亡。

其中一些属性是动态的，如 `startScale` 和 `endScale`、`startColor`和`endColor`。

对于具有最大和最小输入的每个变量，粒子上该变量的实际值将随机分配到最大和最小输入之间，并在粒子的整个生命周期内静态保持该值。允许像这样更改的属性包括`imageSize`、`speed`、`life`和`particleLife`。

### `Emitters` 发射器

> 当粒子诞生时，其初始位置和速度矢量由 `ParticleEmitter` 控制。发射器将每秒生成一些粒子，由 `emissionRate` 参数指定，根据发射器类型用随机速度初始化。

#### `BoxEmitter` 盒形发射器

> `BoxEmitter` 在一个盒子内随机取样的位置初始化粒子，并将它们从六个盒子表面中的一个引导出来。它接收 `Cartesian3` 参数，该参数指定框的宽度、高度和深度尺寸。

```js
let particleSystem = scene.primitives.add(new Cesium.ParticleSystem({
  image: "images/smoke.png",
  color: Cesium.Color.MAGENTA,
  emissionRate: 5.0,
  emitter: new Cesium.BoxEmitter(new Cesium.Cartesian3(5.0, 5.0, 5.0)),
  imageSize : new Cesium.Cartesian2(25.0, 25.0),
  modelMatrix : entity.computeModelMatrix(viewer.clock.startTime, new Cesium.Matrix4()),
  lifetime : 16.0
}));
```

#### `CircleEmitter` 圆形发射器

> `CircleEmitter` 在发射器上轴线方向上的圆形内的随机采样位置初始化粒子。它接收一个指定圆半径的浮点参数。

```js
let particleSystem = scene.primitives.add(new Cesium.ParticleSystem({
  image : '../../SampleData/smoke.png',
  color: Cesium.Color.MAGENTA,
  emissionRate: 5.0,
  emitter: new Cesium.CircleEmitter(5.0),
  imageSize : new Cesium.Cartesian2(25.0, 25.0),
  modelMatrix : entity.computeModelMatrix(viewer.clock.startTime, new Cesium.Matrix4()),
  lifetime : 16.0
}));
```

#### `ConeEmitter` 锥形发射器

> `ConeEmitter` 在圆锥体的顶端初始化粒子，并以随机的角度引导它们离开圆锥体。它使用一个指定圆锥体角度的浮点参数。圆锥体沿发射器的上轴定向。

```js
let particleSystem = scene.primitives.add(new Cesium.ParticleSystem({
  image : '../../SampleData/smoke.png',
  color: Cesium.Color.MAGENTA,
  emissionRate: 5.0,
  emitter: new Cesium.ConeEmitter(Cesium.Math.toRadians(30.0)),
  imageSize : new Cesium.Cartesian2(25.0, 25.0),
  modelMatrix : entity.computeModelMatrix(viewer.clock.startTime, new Cesium.Matrix4()),
  lifetime : 16.0
}));
```

#### `SphereEmitter` 球形发射器

> `SphereEmitter` 在球体内随机取样的位置初始化粒子，并将它们从球体中心向外引导。它使用一个指定球体半径的浮点参数。

```js
let particleSystem = scene.primitives.add(new Cesium.ParticleSystem({
  image : '../../SampleData/smoke.png',
  color: Cesium.Color.MAGENTA,
  emissionRate: 5.0,
  emitter: new Cesium.SphereEmitter(5.0),
  imageSize : new Cesium.Cartesian2(25.0, 25.0),
  modelMatrix : entity.computeModelMatrix(viewer.clock.startTime, new Cesium.Matrix4()),
  lifetime : 16.0
}));
```

### 配置粒子系统

#### 粒子发射率

> `emissionRate` 控制每秒发射多少粒子，可以改变系统中粒子的密度。

指定一组 `burst` 在一定时间发射粒子，可以增加粒子系统的多样性或爆炸性。

```js
bursts : [
  new Cesium.ParticleBurst({time : 5.0, minimum : 300, maximum : 500}),
  new Cesium.ParticleBurst({time : 10.0, minimum : 50, maximum : 100}),
  new Cesium.ParticleBurst({time : 15.0, minimum : 200, maximum : 300})
]
```

在给定的时间，粒子会在最大和最小之间进行发射。

#### 粒子生命周期和系统生命周期

默认情况下，粒子系统将永远运行。要使粒子系统以设定的持续时间运行，可以使用 `lifetime` 以秒为单位指定持续时间，并将 `loop` 设置为 `false`。

```js
lifetime : 16.0,
loop: false
```

要随机化每个粒子的输出，可以使用变量 `minimumParticleLife` 和 `maximumArticleLife`。

```js
minimumParticleLife: 5.0,
maximumParticleLife: 10.0
```

#### 样式化粒子

- 颜色

粒子的样式是使用 `image` 和 `color` 指定的纹理，这些纹理可以在粒子的生命周期中更改以创建动态效果。 下面的代码使烟雾粒子从绿色过渡到白色。

```js
startColor : Cesium.Color.LIGHTSEAGREEN.withAlpha(0.7),
endColor : Cesium.Color.WHITE.withAlpha(0.0),
```

- 大小

粒子的大小由 `imageSize` 控制。要随机化大小，可以使用`minimumImageSize.x`和`maximumImageSize.x`控制宽度（以像素为单位），并使用`minimumImageSize.y`和`maximumImageSize.y`控制高度（以像素为单位）。

```js
minimumImageSize : new Cesium.Cartesian2(30.0, 30.0),
maximumImageSize : new Cesium.Cartesian2(60.0, 60.0)
```

粒子的大小可以通过 `startScale` 和 `endscale` 属性在其生命周期中进行调整，以使粒子随时间增长或收缩。

```js
startScale: 1.0,
endScale: 4.0
```

- 速度

速度由 `speed` 或 `minimumSpeed` 和 `maximumSpeed` 控制。

```js
minimumSpeed: 5.0,
maximumSpeed: 10.0
```

#### `UpdateCallback` 更新回调

通过应用更新函数，可以进一步自定义粒子系统。对于重力、风或颜色更改等效果，它可以动态更新每个粒子。

一个让粒子对重力作出反应的例子：

```js
let gravityVector = new Cesium.Cartesian3();
let gravity = -(9.8 * 9.8);
function applyGravity(p, dt) {
  let position = p.position;

  Cesium.Cartesian3.normalize(position, gravityVector);
  Cesium.Cartesian3.multiplyByScalar(gravityVector, gravity * dt, gravityVector);

  p.velocity = Cesium.Cartesian3.add(p.velocity, gravityVector, p.velocity);
}
```

该函数计算重力矢量，并使用重力加速度来改变粒子的速度。 将重力设置为粒子系统的 `updateFunction`：

```js
updateCallback : applyGravity
```

#### `Positioning` 定位

使用两个Matrix4变换矩阵定位粒子系统：

- `modelMatrix`

将粒子系统从模型转换为世界坐标。

- `emitterModelMatrix`

在粒子系统的局部坐标系中变换粒子系统发射器。

```js
let model = this.$viewer.entities.getById("Truck");
let particleSystem = this.$viewer.scene.primitives.add(
  new Cesium.ParticleSystem({
    image: "images/smoke.png",

    startColor: Cesium.Color.LIGHTSEAGREEN.withAlpha(0.7),
    endColor: Cesium.Color.WHITE.withAlpha(0.0),

    startScale: 1.0,
    endScale: 4.0,

    particleLife: 1.0,

    minimumSpeed: 1.0,
    maximumSpeed: 4.0,

    imageSize: new Cesium.Cartesian2(25, 25),
    emissionRate: 5.0,
    lifetime: 16.0,

    emitter: new Cesium.CircleEmitter(0.5),

    modelMatrix: model.computeModelMatrix(
      Cesium.JulianDate.now(),
      new Cesium.Matrix4()
    ),
    emitterModelMatrix: new Cesium.Matrix4.fromTranslationQuaternionRotationScale(
      new Cesium.Cartesian3(-4.0, 0.0, 2.0),
      new Cesium.Quaternion(0, 0, 0, 1),
      new Cesium.Cartesian3(7.0, 6.0, 5.0),
      new Cesium.Matrix4()
    ),
    bursts: [
      new Cesium.ParticleBurst({
        time: 5.0,
        minimum: 10,
        maximum: 100,
      }),
      new Cesium.ParticleBurst({
        time: 10.0,
        minimum: 50,
        maximum: 100,
      }),
      new Cesium.ParticleBurst({
        time: 15.0,
        minimum: 200,
        maximum: 300,
      }),
    ],
  })
);
```

## 高级粒子系统效应(`Advanced Particle System Effects`)

> 一些动态更新粒子的行为，需要在 `updateParticle` 函数中定义粒子的移动行为和其他动态元素。

以雪粒子更新函数为例：

```js
let snowUpdate = function (particle, dt) {
  dt;
  Cesium.Cartesian3.normalize(particle.position, snowGravityVector);
  Cesium.Cartesian3.multiplyByScalar(
    snowGravityVector,
    Cesium.Math.randomBetween(-30.0, -300.0),
    snowGravityVector
  );
  particle.velocity = Cesium.Cartesian3.add(
    particle.velocity,
    snowGravityVector,
    particle.velocity
  );

  let distance = Cesium.Cartesian3.distance(
    vm.$viewer.scene.camera.position,
    particle.position
  );
  if (distance > snowRadius) {
    particle.endColor.alpha = 0.0;
  } else {
    particle.endColor.alpha =
      snowSystem.endColor.alpha / (distance / snowRadius + 0.1);
  }
};
```

更新函数用于定义粒子的移动、排列和可视化。修改粒子的color颜色、imageSize图像大小和particleLife粒子生命周期。我们甚至可以基于到相机距离定义粒子、导入模型或到地球本身的距离等。

- 额外的天气效应

使用雾和大气效果来增强可视化效果，并匹配我们试图复制的天气类型。

hueshift沿着颜色光谱改变颜色，saturationShift改变了视觉实际需要的颜色与黑白的对比程度，brightnessShift改变了颜色的生动程度。

雾密度改变了地球上覆盖物与雾的颜色之间的不透明程度。雾的minimumBrightness用来使雾变暗。

```js
// snow
scene.skyAtmosphere.hueShift = -0.8;
scene.skyAtmosphere.saturationShift = -0.7;
scene.skyAtmosphere.brightnessShift = -0.33;

scene.fog.density = 0.001;
scene.fog.minimumBrightness = 0.8;
```

### `Snow`

```js
// 雪景
snow() {
  let vm = this;
  this.$viewer.terrainProvider = Cesium.createWorldTerrain();
  this.$viewer.scene.globe.depthTestAgainstTerrain = true;
  this.$viewer.scene.camera.setView({
    destination: new Cesium.Cartesian3(
      277096.634865404,
      5647834.481964232,
      2985563.7039122293
    ),
    orientation: {
      heading: 4.731089976107251,
      pitch: -0.32003481981370063,
    },
  });

  let snowGravityVector = new Cesium.Cartesian3();
  let snowUpdate = function (particle, dt) {
    dt;
    Cesium.Cartesian3.normalize(particle.position, snowGravityVector);
    Cesium.Cartesian3.multiplyByScalar(
      snowGravityVector,
      Cesium.Math.randomBetween(-30.0, -300.0),
      snowGravityVector
    );
    particle.velocity = Cesium.Cartesian3.add(
      particle.velocity,
      snowGravityVector,
      particle.velocity
    );

    let distance = Cesium.Cartesian3.distance(
      vm.$viewer.scene.camera.position,
      particle.position
    );
    if (distance > snowRadius) {
      particle.endColor.alpha = 0.0;
    } else {
      particle.endColor.alpha =
        snowSystem.endColor.alpha / (distance / snowRadius + 0.1);
    }
  };

  // 雾与大气效果
  this.$viewer.scene.skyAtmosphere.hueShift = -0.8;
  this.$viewer.scene.skyAtmosphere.saturationShift = -0.7;
  this.$viewer.scene.skyAtmosphere.brightnessShift = -0.33;

  this.$viewer.scene.fog.density = 0.001;
  this.$viewer.scene.fog.minimumBrightness = 0.8;

  let snowParticleSize = this.$viewer.scene.drawingBufferWidth / 100.0;
  let snowRadius = 100000.0;

  let snowSystem = new Cesium.ParticleSystem({
    modelMatrix: new Cesium.Matrix4.fromTranslation(
      this.$viewer.scene.camera.position
    ),
    minimumSpeed: -1.0,
    maximumSpeed: 0.0,
    lifetime: 15.0,
    emitter: new Cesium.SphereEmitter(snowRadius),
    startScale: 0.5,
    endScale: 1.0,
    image: "images/snow.png",
    emissionRate: 700.0,
    startColor: Cesium.Color.WHITE.withAlpha(0.0),
    endColor: Cesium.Color.WHITE.withAlpha(1.0),
    minimumImageSize: new Cesium.Cartesian2(
      snowParticleSize,
      snowParticleSize
    ),
    maximumImageSize: new Cesium.Cartesian2(
      snowParticleSize,
      snowParticleSize
    ),
    updateCallback: snowUpdate,
  });
  this.$viewer.scene.primitives.add(snowSystem);
},
```
<iframe height=500 width=100% src="http://images.akashi.org.cn/cesium-vue%20-%20Google%20Chrome%202020-09-27%2017-13-48.mp4" frameborder=0 allowfullscreen></iframe>

### `Rain`

```js
// 雨景
rain() {
  let vm = this;
  this.$viewer.terrainProvider = Cesium.createWorldTerrain();
  this.$viewer.scene.globe.depthTestAgainstTerrain = true;
  this.$viewer.scene.camera.setView({
    destination: new Cesium.Cartesian3(
      277096.634865404,
      5647834.481964232,
      2985563.7039122293
    ),
    orientation: {
      heading: 4.731089976107251,
      pitch: -0.32003481981370063,
    },
  });

  // rain
  this.$viewer.scene.skyAtmosphere.hueShift = -0.97;
  this.$viewer.scene.skyAtmosphere.saturationShift = 0.25;
  this.$viewer.scene.skyAtmosphere.brightnessShift = -0.4;

  this.$viewer.scene.fog.density = 0.00025;
  this.$viewer.scene.fog.minimumBrightness = 0.01;

  let rainParticleSize = this.$viewer.scene.drawingBufferWidth / 100.0;
  let rainRadius = 100000.0;

  let rainGravityScratch = new Cesium.Cartesian3();
  let rainUpdate = function (particle, dt) {
    dt;
    rainGravityScratch = Cesium.Cartesian3.normalize(
      particle.position,
      rainGravityScratch
    );
    rainGravityScratch = Cesium.Cartesian3.multiplyByScalar(
      rainGravityScratch,
      -1050.0,
      rainGravityScratch
    );

    particle.position = Cesium.Cartesian3.add(
      particle.position,
      rainGravityScratch,
      particle.position
    );

    let distance = Cesium.Cartesian3.distance(
      vm.$viewer.scene.camera.position,
      particle.position
    );
    if (distance > rainRadius) {
      particle.endColor.alpha = 0.0;
    } else {
      particle.endColor.alpha =
        rainSystem.endColor.alpha / (distance / rainRadius + 0.1);
    }
  };

  let rainSystem = new Cesium.ParticleSystem({
    modelMatrix: new Cesium.Matrix4.fromTranslation(
      this.$viewer.scene.camera.position
    ),
    speed: -1.0,
    lifetime: 15.0,
    emitter: new Cesium.SphereEmitter(rainRadius),
    startScale: 1.0,
    endScale: 0.0,
    image: "images/rain.png",
    emissionRate: 900.0,
    startColor: new Cesium.Color(0.27, 0.4, 0.6, 0.0),
    endColor: new Cesium.Color(0.27, 0.4, 0.6, 0.98),
    imageSize: new Cesium.Cartesian2(
      rainParticleSize,
      rainParticleSize * 2
    ),
    updateCallback: rainUpdate,
  });
  this.$viewer.scene.primitives.add(rainSystem);
},
```
<iframe height=500 width=100% src="http://images.akashi.org.cn/cesium-vue%20-%20Google%20Chrome%202020-09-27%2017-16-49.mp4" frameborder=0 allowfullscreen></iframe>
