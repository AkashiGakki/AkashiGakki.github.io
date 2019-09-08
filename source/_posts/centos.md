---
title: CentOS 安装 Python3 环境
date: yyyy-mm-dd
category: 
    - Linux
    - 环境安装
tags:
    - Linux
    - 环境安装
thumbnail: /images/bg-21.jpg

---

#### `CentOS` 安装 `Python3` 环境

> 在云服务器下安装 `Python3` 环境，系统为 `CentOS`。

<!-- more -->

##### 远程连接

- 通过 `ssh` 连接到远程服务器

```shell
ssh -p 22 root@xx.xxx.xxx.xxx
```

连接到远程服务器，`@`后接服务器公网 `IP` 地址，回车后输入连接密码进行远程登录。

##### 创建目录

> `CnetOS` 默认安装了 `Python2`，可以通过 `which python` 找到它的安装位置。所以需要在开始前新建一个目录用于 `Python3` 的安装。

- 创建安装 `Python3` 环境目录

```shell
sudo mkdir /usr/local/python3
```

##### 源文件下载

- 下载源文件

```shell
wget https://www.python.org/ftp/python/3.6.5/Python-3.7.4.tgz
```

- 解压缩包

```shell
tar -xzvf Python-3.7.4.tgz
```

- 进入解压目录

```shell
cd Python-3.7.4
```

##### 编译安装

- 指定在创建的目录安装

```shell
sudo ./configure --prefix=/usr/local/python3
```

- 编译安装

```shell
sudo make && sudo make install
```

至此，安装完成。在 `/usr/local/python3` 就可以看见 `python3` 的文件了。

##### 设置软连接

> 为了区分 `Python2` 和 `Python3`，需要设置一个软连接让系统环境可以找到 `Python3` 并使用它。

- 软连接

`python3`:

```shell
sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```

`pip3`:

```shell
sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

这样，两个版本就可以共存了，我们可以使用 `python` 来调用 `python` 环境，`python3` 来调用 `python3` 环境。

##### 解决 `yum` `Python` 版本矛盾

如果不幸出现了 `yum` 失效的情况，需要更改 `yum` 的配置文件和 `urlgrabber-ext-down` 文件，（使用以上方法安装一般不会出现失效的情况）

1. 修改 `yum` 配置文件，将 `python` 版本指向以前的旧版本

```shell
vim /usr/bin/yum
```

将第一行改成 `#!/usr/bin/python2.7`

2. 修改 `urlgrabber-ext-down` 文件，更改 `python` 版本

```shell
vim /usr/libexec/urlgrabber-ext-down
```

将第一行改成 `#!/usr/bin/python2.7`
