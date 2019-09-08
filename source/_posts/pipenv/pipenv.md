---
title: Python 包管理工具 pipenv 构建虚拟环境
date: yyyy-mm-dd
category:
    - 杂项
tags:
    - 杂项
    - 虚拟环境
thumbnail: /images/bg-28.jpg

---

#### `Python` 包管理工具 `pipenv` 构建虚拟环境

> 又一 `Python` 虚拟环境和包管理工具，`requests` 的作者 `Kenneth Reitz` 的作品，相当于 `virtualenv` 和 `pip` 的合体，解决 `requirements.txt` 的不确定构建问题。

<!-- more -->

##### 为什么使用 `pipenv`

1. `requirements.txt` 依赖管理存在局限。

当我们通过 `pip install -r requirements.txt` 安装依赖模块时，会默认安装最新的版本，但如果你的库有存在不兼容旧版本的接口时，代码在新的环境下就不能运行了。这就是不确定构建。

2. 依赖关系的复杂性

当我们的项目使用了包 `A`，它依赖于包 `B` 的 `2.x` 系列，这时候 `requirements.txt` 会长这样：

```pipfile
A==1.0
B==2.5.1
```

当我们需要使用包 `C`，而它依赖于 `B` 的 `3.0` 的 `API`，在这种情况下 `pip install C` 就会变成：

```pipfile
A==1.0
B==3.0.0
C==1.0
```

这时候 `A` 很可能就没办法使用。而通过 `Pipfile.lock` 的确定构建就可以解决这个问题。

自己的使用感受是，相对于 `virtualenv`， 启动和使用更加方便。

因为 `virtualenv` 的项目和虚拟环境是分开管理的，在使用 `virtualenv` 一段时间以后，就可能分不清哪个项目对应哪个虚拟环境，而使用 `pipenv` 就不用关心这个问题，直接在项目下 `pipenv shell` 就搞定了。

但为保证包的完整性，加入到 `Pipfile` 的操作就比较耗时间。

##### 安装 `pipenv`

```shell
pip3 install pipenv
```

##### 创建虚拟环境

```shell
mkdir project
cd project
pipenv install
```

初始化好虚拟环境后，会在项目目录下生成 `2个` 文件 `Pipfile` 和 `Pipfile.lock`。为 `pipenv` 包的配置文件，代替原来的 `requirement.txt`。

项目提交时，可将 `Pipfile` 文件和 `Pipfile.lock` 文件一并提交，待其他开发克隆下载，根据此 `Pipfile` 运行命令 `pipenv install --dev` 生成自己的虚拟环境。

`Pipfile.lock` 文件是通过 `hash` 算法将包的名称和版本，及依赖关系生成哈希值，可以保证包的完整性。

##### 激活虚拟环境

```shell
pipenv shell
```

`pipenv` 很智能，如果你进入了一个项目文件没有安装虚拟环境，直接启动虚拟环境，那么它会新建一个虚拟环境。

也就是说，创建过程是可以直接省略的。

##### 退出虚拟环境

```shell
exit
```

##### 安装/卸载包

安装相关模块并加入到 `Pipfile`

```shell
pipenv install xxx
pipenv uninstall xxx
```

##### 查看安装包依赖关系

```shell
pipenv graph
```

##### 查看虚拟环境安装目录

```shell
pipenv --venv
```

##### 显示目录信息

```shell
pipenv --where
```

##### 生成 `lockfile`

```shell
pipenv lock
```

##### 运行 `Python` 文件

```shell
pipenv run python xxx.py
```

##### 删除虚拟环境

```shell
pipenv --rm
```
