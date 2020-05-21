---
title: MongoDB 之可视化工具推荐 —— adminMongo
date: yyyy-mm-dd
category:
    - 数据库
    - MongoDB 
tags:
    - 数据库
    - MongoDB
    - 可视化工具
thumbnail: /images/bg-19.jpg

---

#### `MongoDB` 之可视化工具推荐 —— `adminMongo`

> 最近学习 `MongoDB` 发现了一款好用的可视化工具 —— `adminMongo`，记录一下基本使用。

<!-- more -->

##### 简介

`adminMongo` 是一个跨平台用户界面(`GUI`)，用于处理所有 `MongoDB` 连接/数据库需求。

`adminMongo` 连接信息(包括用户名/密码)以未加密的方式存储在配置文件中，因此不建议在没有适当安全性考虑的情况下在生产或面向公共的服务器上运行此应用程序。

`github` 地址： `https://github.com/mrvautin/adminMongo`

##### 安装

1. 克隆 `git` 仓库到本地

> 选取合适的文件目录下终端运行：

```shell
git clone https://github.com/mrvautin/adminMongo
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ul87q9tuj20vo08mjuw.jpg)

2. 进入目录

```shell
cd adminMongo
```

3. 安装依赖

```shell
cnpm install
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ul8vzr6xj20vo0dagpw.jpg)

终端提示需要安装包和升级可按具体情况运行：

```shell
npm xxx     # 看具体缺少哪些包，分别进行安装
npm update  # 进行升级
```

4. 启动

```shell
cnpm start
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ul9f9cowj20vo08q40e.jpg)

这时，程序已经启动，并且监听本地的 `1234` 端口，我们可以打开浏览器进行访问。

注意：以上 `cnpm` 为 `npm` 的国内淘宝镜像源，速度比较快，如果没有配置可以使用 `npm` 对 `cnpm` 进行替换即可；或者输入以下命令进行安装使用：

```shell
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

5. 访问启动后的地址 `http://localhost:1234`

`localhost` 即本地 `IP`: `127.0.0.1`

`1234` 表示程序监听的端口号

进入地址之后，需要填写连接名称和地址，连接名称可任意命名，这里填入 `localhost`，地址为：`mongodb://127.0.0.1:12017`

`12017` 为 `MongoDB` 默认监听的端口号

如果提示连接错误，可以尝试以 `mongodb://localhost` 进行连接

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ulq8u3vaj21z40l80vc.jpg)

确认之后点击添加连接。

6. 连接 `MongoDB`

添加之后，跳转到连接界面，点击连接进入 `MongoDB` 数据库：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ulrayqebj21z40pgdja.jpg)

这个时候就可以看见本地所有的 `MongoDB` 数据库了：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ulsi4a2nj21z40z0tfr.jpg)

可以随意的进行查询和编辑了：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5ulsru5m0j21z412446i.jpg)

