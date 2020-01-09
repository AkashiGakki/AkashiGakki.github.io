---
title: Mac 终端美化方案
date: yyyy-mm-dd
category:
    - 杂项
tags:
    - 杂项
    - 终端
    - 美化
thumbnail: /images/bg-17.jpg

---

#### `Mac` 终端美化方案

> 配合 `iTerm2` + `zsh` + `oh-my-zsh` 打造一个 `Mac` 终端美化计划。

<!-- more -->

以下是最终效果：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ti28b3k0j21z40qqn5h.jpg)


##### 使用 `iTerm2`

- 安装

```shell
brew cask install iterm2
```

下载完成之后，打开软件，进入设置(`Preferences`) => `Porfile` => 可以选择颜色(`colors`)、字体(`text`)等。

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5skvbwjbbj21fk0p044a.jpg)

这样就可以使用 `iTerm2` 代替 `Mac` 默认终端(`terminal`)。除了强大的功能，所谓颜值就是第一生产力。

##### 使用 `zsh`

`shell` 的类型有很多种，`Mac` 和 `Linux` 默认使用的是 `bash`。虽然 `bash` 也足够使用，但远没有 `zsh` 强大，界面也不够酷炫，并不是最好的选择。

而 `zsh` 功能极其强大，但是配置复杂，直到出现了开源项目 `oh my zsh`，只需简单的配置，就可以使用。

`Mac` 下默认安装了 `zsh`，但不是最新版

查看当前使用的 `shell`:

```shell
echo $SHELL
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5sfocuy6fj20xc01mt8q.jpg)

查看安装的 `shell`:

```shell
cat /etc/shells
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5sfp31ffvj20xc08ot9e.jpg)

查看 `zsh` 的版本：

```shell
zsh --version
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5sfq0111jj20xc01kdfy.jpg)

更新 `zsh`:

```
brew install zsh
```

添加到 `path`：

```
echo 'export PATH="/usr/local/opt/ncurses/bin:$PATH"' >> ~/.bash_profile
```

切换为 `zsh`

```shell
chsh -s /bin/zsh
```

重启终端，即可使用 `zsh`。

##### 安装 `oh my zsh`

以下提供三种方式，任选其一：

- 使用 `git`

```shell
git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
```

- 使用 `curl`

```shell
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

- 使用 `wget`

```shell
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5sg0kn6xlj218k0lgmzt.jpg)

> 安装完成以后，默认 `Shell` 的 `~/.bashrc` 文件默认不再加载了，替代的是 `~/.zlogin` 和 `~/.zshrc`。所以如果在 `~/.bashrc` 里配置了某些设置，需要把她们复制到 `~/.zshrc` 中。

或者执行：

```shell
echo 'source ~/.bashrc' >> ~/.zshrc
echo 'source ~/.bash_profile' >> ~/.zshrc
```

- 备份配置文件（可省略）

```shell
cp ~/.zshrc ~/.zshrc.orig
```

###### 主题配置

`oh my zsh` 提供了数十种主题，相关文件在 `~/.oh-my-zsh/themes` 目录下，你可以自己选择，也可以自己编写主题。

参考主题列表：`https://github.com/robbyrussell/oh-my-zsh/wiki/themes`

在 `.zshrc` 里找到 `ZSH_THEME`，就可以设置主题了，默认主题是：`ZSH_THEME="robbyrussell"`

`ZSH_THEME="random"`，主题设置为随机，这样我们每打开一个窗口，都会随机在默认主题中选择一个。

这里推荐两款常用的颜值比较高的主题： `agnoster` 和 `ys`

- 字体安装

```shell
git clone https://github.com/supermarin/powerline-fonts.git
```

将该仓库克隆到本地，然后进入工程目录的 `Monaco` 目录，双击后缀名为 `.otf` 的字体文件即可完成该字体的安装。安装该字体的原因主要是为了和 `Oh-My-Zsh` 的 `agnoster`、`powerlevel9k` 主题相兼容，如果不安装该字体，那么后面安装 `powerlevel9kn` 主题后会出现乱码。


`agnoster` 最终效果：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5thwq6f8zj21z40nmq8k.jpg)

###### 插件设置

`oh my zsh` 项目提供了完善的插件体系，相关的文件在 `~/.oh-my-zsh/plugins` 目录下，默认提供了100多种，大家可以根据自己的实际学习和工作环境采用，想了解每个插件的功能，只要打开相关目录下的 `zsh` 文件看一下就知道了。插件也是在 `.zshrc` 里配置，找到 `plugins` 关键字，你就可以加载自己的插件了，系统默认加载 `git`，你可以在后面追加内容，如下：

```shell
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

- 安装 `zsh-autosuggestions`

```shell
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

添加至 `plugins`

- 安装 `zsh-syntax-highlighting`

```shell
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

添加至 `plugins`

- 安装 `incr.zsh`

```shell
wget http://mimosa-pudica.net/src/incr-0.2.zsh
```

将此插件放到 `oh-my-zsh` 目录的插件库下：

在 `~/.zshrc` 文件末尾加上插件

```shell
echo 'source ~/.oh-my-zsh/plugins/incr/incr*.zsh' >> ~/.zshrc
```

更新配置：

```shell
source ~/.zshrc   
```

###### 主题安装

- 克隆该仓库到 `oh-my-zsh` 用户自定义主题目录

```shell
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

修改 ~/.zshrc 配置文件，配置该主题

```shell
ZSH_THEME="powerlevel9k/powerlevel9k"
```

生效配置

```shell
source ~/.zshrc
```

以上，配置完成。还有更多配置、效果随缘更新。
