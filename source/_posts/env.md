---
title: Virtualenv 虚拟环境搭建
date: yyyy-mm-dd
category:
    - 杂项
tags:
    - 杂项
    - 虚拟环境
    - env
thumbnail: /images/bg-18.jpg

---

#### `Virturalenv` 虚拟环境搭建

> 在 `Python` 的开发中，我们可能会遇到这这样一种情况，当前的项目依赖是某一个 `python3` 的版本，而另一个项目却是依赖一个 `python2` 的版本(同一种情况也可能发生在 `Diango` 中)，这种情况下，在本地同时开发和维护两个版本就会造成版本冲突，`virturalenv` 就可以解决以上问题。

<!-- more -->

`VirtualEnv` 可以搭建虚拟且独立的 `python` 运行环境, 使得单个项目的运行环境与其它项目独立起来。同时也可以用于在一台机器上创建多个独立的  `python` 运行环境， `VirtualEnvWrapper` 为前者提供了一些便利的命令行上的封装。


##### 安装

```shell
pip3 install virtualenv
```

查看安装版本来确认安装：

```shell
virtualenv --version
```

###### 使用豆瓣源

> 有时使用官方源安装第三方库会出现下载过慢或者超时的情况，这时候可以尝试使用国内的源进行安装。

- 临时使用

```shell
pip3 install pythonModuleName -i https://pypi.douban.com/simple
```

- 永久使用

需要找到 `python` 的安装路径，然后找到 `Lib/site-packages\pip\commands` 下的 `search.py` 文件，发现里面有如下两行代码:

```python
from pip.models import PyPI
default=PyPI.pypi_url,
```

可以看出来 `PyPI.pypi_url` 是从 `moudels` 模块里导入的，所以要找到 `moudels` 模板，该模块位于上一级目录，打开 `moudels` 里面的 `index.py` 文件:

```python
PyPI = Index('https://pypi.python.org/')
```

修改 `https://pypi.python.org/` 为 `https://pypi.douban.com/simple`

##### 新建 `virtualenv` 环境

###### 新建虚拟环境

```shell
virtualenv env-test
```

这样，我们就创建了一个名为 `env-test` 的虚拟环境。

当然，也可以指定安装依赖的 `python` 版本，使用参数 `-p` 进行指定：

```
virtualenv -p python3 py-test
```

###### 激活

进入虚拟环境，进入 `bin` 目录，使用 `source activate` 激活虚拟环境，当然也可以一步到位：

```shell
source env-test/bin/activate
```

这样，就激活了当前的虚拟环境，做到了与其他 `Python` 项目的环境进行隔离，可以自行安装需要的依赖进行开发了。

`Windows` 用户进入 `Script` 目录，运行 `activite.bat` 进行激活。

###### 退出虚拟环境

只需运行

```shell
deactivate
```

同样， `Windows` 用户需要执行脚本退出，运行 `deactivate.bat` 退出环境。

##### 安装 `virtualenvwrapper`

> `Virtaulenvwrapper` 是 `virtualenv` 的扩展包管理工具，可以更方便地新增，删除，复制，切换虚拟环境。

###### 安装

```shell
pip3 install virtualenvwrapper
```

安装完成后，需要对 `virtualenvwrapper` 进行配置:

```shell
export WORKON_HOME=~/Envs                       // 虚拟环境存储路径
source /usr/local/bin/virtualenvwrapper.sh      // 执行命令封装包
```

> 由于每次都需要执行这两部操作，我们可以将其写入终端的配置文件中。例如，如果使用 `bash`，则添加到 `~/.bashrc` 中；如果使用 `zsh`，则添加到 `~/.zshrc` 中。这样每次启动终端的时候都会自动运行，执行之后 `virtualenvwrapper` 就可以用啦。

写入配置之后执行生效，

```shell
source ~/.zshrc
```

这里要看自己本机的配置情况，我使用的是 `zsh`，所以执行 `source ~/.zshrc`。

###### 使用

现在，可以使用 `virtualenvwrapper`  新建一个虚拟环境：

```shell
mkvirtualenv env-pytest
```

激活环境

```shell
workon env-pytest
```

`workon` 不带参数可以列出本机所有的虚拟环境:

```shell
workon
```

所有的命令可使用：`virtualenvwrapper --help` 进行查看，这里列出几个常用的：

- 创建基本环境：`mkvirtualenv [环境名]`

- 删除环境：`rmvirtualenv [环境名]`

- 激活/切换环境：`workon [环境名]`

- 退出环境：`deactivate`

- 列出所有环境：`workon` 或者 `lsvirtualenv -b`

- 查询子虚拟环境列表：`lsvirtualenv -b`

- 查看当前环境已经安装的 `Python` 安装包：`lssitepackages`
