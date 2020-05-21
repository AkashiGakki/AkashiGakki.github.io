---
title: Google Cloud 搭建 SSR 服务器
date: 2019-8-28
category:
    - Linux
    - SSR
tags:
    - Linux
    - 云服务
    - SSR
    - Google Cloud
thumbnail: /images/bg-25.jpg

---

#### `Google Cloud` 搭建 `SSR` 服务器

> 使用 `Google Cloud` 搭建属于自己的 `SSR` 服务器，实现愉快的科学上网。

<!-- more -->

##### 创建 `VM` 实例

- 创建

首先，进入 `Google Cloud` 控制台，创建 `VM` 实例。

![VM实例](http://images.akashi.org.cn/Fv5IdWRtAC-VYCOuiEXM7oFbD22j)

`计算` => `Computer Engine` => `VM 实例`

![创建](http://images.akashi.org.cn/FvoG2kuHjY-qBYkk_3hVjlEemena)

- 配置

选取配置：

![配置](http://images.akashi.org.cn/FklsyL57OQM581TkKZVJi30dMjmm)

实际尝试后，台湾的速度是最快的。选择最小的内存，只是用于 `SSR` 服务端安装是足够的，预计每月 `$5`，一年就是 `$60`。

防火墙需要勾选允许 `http` 和 `https`

![防火墙](http://images.akashi.org.cn/Fkf6GdnkX2vay8szF6aJ8VWNKx7E)

点击创建，这样，服务器就创建成功了。

##### 安装 `BBR`

- 远程登录

`BBR` 是 `Google` 发布的拥塞控制算法，可以有效缓解服务器连接速度慢等问题，下面我们通过脚本进行安装。

点击实例的 `ssh`，在浏览器进行远程登录：

![ssh](http://images.akashi.org.cn/Fo3dd7hJtuMNda7AWG6KxAvLUpgX)

![远程登录](http://images.akashi.org.cn/Fna8I_fiNCnCc_GqY2BniYfdv774)

- 获取 `root` 权限

连接到服务器后，获取 `root` 用户权限：

```shell
sudo -i
```

安装一些基本的工具：

```shell
sudo yum install git
sudo yum install wget
sudo yum update
```

- 安装 `BBR` 加速

```shell
wget -N –no-check-certificate https://raw.githubusercontent.com/FunctionClub/YankeeBBR/master/bbr.sh && bash bbr.sh install
```

完成后重启服务器，并且重新连接，获取 `root` 用户权限后，开启 `BBR` 服务：

```shell
bash bbr.sh start
```

##### 安装 `SSR`

接下来，就是 `SSR` 服务端的安装。

- `ssr` 脚本安装

```shell
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssrmu.sh && chmod +x ssrmu.sh && bash ssrmu.sh
```

按照要求配置 `ip`，用户，端口，密码、加密方式，协议等等。

![ssr配置](http://images.akashi.org.cn/FlQCayRBArmNJom7ZvOqQHFyEh3B)

然后，记住你的配置，之后需要在本地的客户端输入配置实现科学上网。

- 设置外部 `IP` 为静态

![静态IP](http://images.akashi.org.cn/FvmUToxLRUyPskVVXP_a1jk4fRIq)

- 添加防火墙规则

![防火墙](http://images.akashi.org.cn/FnhP2ZcMsYZCglsZi5sY3u7axcFT)

注意：设置的端口需要与刚才 `ssr` 设置的端口一致。

以我的为例，我设置的是 `8989` 端口，端口原则上可以自由设置，但尽量设置大于 `1000` 的端口，而且不要和一些自己开发常用的端口冲突。

![入站](http://images.akashi.org.cn/Fmw_DxcDSm_T4CtPvXvn0Wys1wIg)

![出站](http://images.akashi.org.cn/Flsf5qUWc9-fOubbyxFixCfSa1wr)

至此，服务端的配置已经全部完成，接下来就可以在 `Mac`、`PC`、`IOS`、`安卓` 等设备上安装 `shadowsocks` 客户端，填写你的配置，实现科学上网了。
