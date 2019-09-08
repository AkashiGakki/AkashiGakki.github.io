---
title: Matplotlib 数据可视化
date: yyyy-mm-dd
category:
    - Python
    - 工具
tags:
    - Python
    - 工具
thumbnail: /images/bg-29.jpg

---

#### `matplotlib` 数据可视化

> 使用 `Python` 的数学绘图库工具 `matplotlib` 生成图表。

<!-- more -->

##### 安装 `matplotlib`

```python
pip3 install matplotlib
```

##### 绘制简单的折线图

```python
from matplotlib import pyplot


squates = [1, 4, 9, 16, 25]
pyplot.plot(squates)
pyplot.show()
```

![pyplot](http://images.akashi.org.cn/FisBWQcbLkZSqA9JNhsjP9gd932i)

- 修改标签文字和线条粗细

```python
from matplotlib import pyplot


squates = [1, 4, 9, 16, 25]
pyplot.plot(squates, linewidth=3)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', labelsize=13)

pyplot.show()
```

![pyplot-2](http://images.akashi.org.cn/FsZWlxb-OrPD3ypakWDyno_W3Sef)

- 校正图形

我们发现向 `plot()` 提供一系列数字时，它假设第一个数据点对应的 `x` 轴的值为 `0`，但是我们的第一个值为 `1`，我们需要同时提供输入值和输出值。

```python
from matplotlib import pyplot


squates = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
pyplot.plot(input_values, squates, linewidth=3)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', labelsize=13)

pyplot.show()
```

![pyplot-3](http://images.akashi.org.cn/FtGOe9qkN4jknnpLnPIEUf-9Ym20)

- 使用 `scatter()` 绘制散点图并设置其样式

```python
from matplotlib import pyplot


pyplot.scatter(2, 4, s=30)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', which='major', labelsize=13)

pyplot.show()
```

- 绘制一系列点

```python
from matplotlib import pyplot


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
pyplot.scatter(x_values, y_values, s=30)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', which='major', labelsize=13)

pyplot.show()
```

![scatter](http://images.akashi.org.cn/Fjuyzu9QkCJlzF5CWeU6jMzSJPuU)

- 自动计算数据

```python
from matplotlib import pyplot


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
pyplot.scatter(x_values, y_values)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', which='major', labelsize=13)

# 设置每个坐标轴的取值范围
pyplot.axis([0, 1100, 0, 1100000])

pyplot.show()
```

![自动计算](http://images.akashi.org.cn/FgMkMeqMp_DHf56fKHVfasdQc7Ry)

- 删除数据点轮廓

```python
pyplot.scatter(x_values, y_values, edgecolors='none', s=7)
```

- 自定义颜色

向 `scatter()` 传递参数 `c` 设置颜色的名称。

```python
pyplot.scatter(x_values, y_values, c='red', edgecolors='none', s=7)
```

`RGBA`:

```python
pyplot.scatter(x_values, y_values, c=(0.8, 0.2, 0.2, 0.4), edgecolors='none', s=7)
```

- 使用颜色映射

示例通过 `y` 的值设置颜色：

```python
from matplotlib import pyplot


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, edgecolors='none', s=7)

# 设置标题，并给坐标轴加上标签
pyplot.title('Square Numbers', fontsize=17)
pyplot.xlabel('Value', fontsize=10)
pyplot.ylabel('Square of Value',fontsize=10)

# 设置刻度标记的大小
pyplot.tick_params(axis='both', which='major', labelsize=13)

# 设置每个坐标轴的取值范围
pyplot.axis([0, 1100, 0, 1100000])

pyplot.show()
```

![color](http://images.akashi.org.cn/FnRQMzlsYi43OsFqr5fzvk8uNtMu)

- 自动保存图表

要让程序自动将图表保存到文件中，可以将 `pyplot.show()` 替换为 `pyplot.savefig()`

```python
pyplot.savefig('squares_plot.png', bbox_inches='tight')
```

##### 随机漫步

随机漫步每次行走都完全是随机的，没有明确的方向，结果是由一系列随机决策决定的。

- 创建 `RandomWalk()` 类

为模拟随机漫步，我们将创建一个 `RandomWalk` 类，它随机的选择前进方向。这个类需要三个属性，其中一个是存储随机漫步次数的变量，另外两个是列表，分别存储随机漫步经过的每个点的 `x` 和 `y` 坐标。

```python
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 从(0, 0)开始
        self.x_values = [0]
        self.y_values = [0]
```

- 选择方向

```python
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 从(0, 0)开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 漫步直到指定长度
        while len(self.x_values) < self.num_points:
            # 决定前进的方向及距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的 x 和 y 的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

`rw_visual`

```python
from matplotlib import pyplot
from random_walk import RandomWalk


rw = RandomWalk()
rw.fill_walk()
pyplot.scatter(rw.x_values, rw.y_values, s=7)
pyplot.show()
```

![rw_visual](http://images.akashi.org.cn/Fi_KhhRBi6-z_d0tdsZOoolmis9O)

- 模拟多次

```python
from matplotlib import pyplot
from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()
    pyplot.scatter(rw.x_values, rw.y_values, s=7)
    pyplot.show()

    keep_running = input("Make anther walk? (y/n): ")
    if keep_running == 'n':
        break
```

- 给点着色

```python
# from matplotlib import pyplot
import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=7)

    plt.show()

    keep_running = input("Make anther walk? (y/n): ")
    if keep_running == 'n':
        break
```

![着色](http://images.akashi.org.cn/FiEOQFzpY-tZz8H3_J5QJ7w5SyNj)

- 重新绘制起点和终点

```python
plt.scatter(0, 0, c='green', edgecolors='none', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)
```

![起点、终点](http://images.akashi.org.cn/Fgor0V_avlfCElQuXdk-1VIcC2GZ)

- 隐藏坐标轴

```python
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
```

![隐藏](http://images.akashi.org.cn/Fuv4aCn_Qyn34annNLyJx8KHtXST)

- 增加点数

`rw = RandomWalk(50000)`

```python
# from matplotlib import pyplot
import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=7)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make anther walk? (y/n): ")
    if keep_running == 'n':
        break
```

![增加点数](http://images.akashi.org.cn/Fh4ksyIdv4xcBo7tjGkX4G2UGRVg)

- 调整尺寸

`plt.figure(figsize=(10, 6))`

```python
# from matplotlib import pyplot
import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=7)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make anther walk? (y/n): ")
    if keep_running == 'n':
        break
```

![调整尺寸](http://images.akashi.org.cn/FiY1r3KLTEnbPiLjhxs3qhEetPxK)
