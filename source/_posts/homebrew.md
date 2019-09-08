---
title: Homebrew 日常使用
date: yyyy-mm-dd
category:
    - 杂项
tags:
    - 杂项
    - 包管理工具
    - Homebrew
thumbnail: /images/bg-15.jpg

---

#### `Homebrew`

> `Homebrew` 是一款 `Mac OS` 平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能。简单的一条指令，就可以实现包管理，而不用你关心各种依赖和文件路径的情况，十分方便快捷。

<!-- more -->

包管理工具顾名思义就是程序软件包的安装管理工具， `Linux` 上有 `apt`, `apt-get`, `yum` 等包管理系统，`Mac OS` 也有一个优秀的包管理工具，它就是 `Homebrew`。 当然，`Windows` 也有类似的管理工具，推荐 `Scoop`，你可以在[这里](https://scoop.sh/)学习使用。

那么回到今天的主题，这里是 `Homebrew` 的官网地址：`https://brew.sh/`

##### 安装和使用

在安装 `Homebrew` 之前，需要将 `Xcode Command Line Tools` 安装完成，这样就可以使用基于 `Xcode Command Line Tools` 编译的 `Homebrew`

```ruby
xcode-select --install
```

###### 安装

打开终端，输入以下命令，输入密码，完成安装：

```ruby
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

`Homebrew` 是基于 `ruby` 的，命令都是通过 `ruby` 脚本运行，不过不用担心，`Mac OS` 默认安装了 `ruby` 环境，可以直接使用命令。

确认安装成功：

```shell
brew -v
```

终端打印出安装版本信息，则证明安装成功。

你也可以查询帮助信息：

```shell
brew -h
```

###### 卸载

如果你想进行卸载

终端输入命令，输入密码，等待卸载完成：

```ruby
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
```

##### 基本使用

###### 常用命令

- `brew install [package]`：安装包

- `brew uninstall [package]`：卸载包

- `brew outdated`：列出过时的软件

- `brew upgrade`：更新过时的软件(全部或指定)

- `brew update`：升级 `homebrew` 在服务器端上的包目录

- `brew list`：列出所有安装的包

- `brew clean up`：清理旧版本缓存

- `brew search [package]`: 安装包检索

- `brew info [package]`：安装包信息检索

###### 安装任意包

```shell
brew install [package]
```

`eg`: 使用 `Homebrew` 安装 `node`

```shell
brew install node
```

###### 卸载任意包

如果你想进行卸载：

```shell
brew uninstall [package]
```

`eg`: 使用 `Homebrew` 卸载 `Python`

```shell
brew uninstall python
```

###### 查询可用包

```shell 
brew search [package]
```

当不确定是否存在可用的安装包，可以尝试查询，例如我们查询是否存在 `wget`:

```shell
brew search wget
```

如果可以查询到相关信息，就可以根据查询到的名称进行安装使用。

###### 查询安装列表

查看本机通过 `Homebrew` 安装的包:

```shell
brew list
```

###### 查询任意包信息

```shell
brew list [backage]
```

这里查询 `git` 的相关信息：

```shell
brew info git
```

##### `Homebrew Cask`

> `Homebrew Cask`可以优雅、简单、快速的安装和管理 `OS X` 图形界面程序，比如 `Google Chrome` 和 `Dropbox`。

这里我们尝试安装 `Chrome`。

首先，确认是否存在：

```shell
brew search chrome
```

等待搜索完成，我们可以发现，在 `casks` 一栏有 `google-chrome` 选项，那么接下来就进行安装：

```shell
brew cask install google-chrome
```

更多安装和使用你可以自己去尝试和发现。
