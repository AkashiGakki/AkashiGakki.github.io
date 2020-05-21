---
title: 云服务器 ftp 的搭建和使用
date: 2019-8-17
category:
    - Linux
    - ftp
tags:
    - Linux
    - ftp
    - 远程连接
thumbnail: /images/bg-22.jpg

---

#### 云服务器 `ftp` 的搭建和使用

> 记录一下 `CentOS` 远程服务器上 `ftp` 的搭建和使用，实现上传和下载。

<!-- more -->

##### 工作原理

`FTP` 采用客户端/服务端的工作模式（`C/S结构`），通过 `TCP` 协议建立客户端和服务器之间的连接，但与其他大多数应用协议不同，FTP协议在客户端和服务端之间建立了两条通信链路，分别是控制链路和数据链路。

其中，控制链路负责 `FTP` 会话过程中 `FTP` 命令的发送和接收，数据链路则负责数据的传输。 `FTP` 会话包含了两个通道，控制通道和数据通道。

`FTP` 的工作有两种方式，一种是主动模式，一种是被动模式，以 `FTPServer` 为参照物，主动模式，服务器主动连接客户端传输，被动模式，等待客户端的的连接 。（无论是主动模式还是被动模式，首先的控制通道都是先建立起来的，只是在数据传输模式上的区别）。

##### 环境准备

`vsftpd` 是 `linux` 下的一款小巧轻快，安全易用的 `FTP` 服务器软件，首先我们需要安装它。

```shell
yum install -y vsftpd
```

安装完成后进入文件查看：

```shell
cd etc/vsftpd
```

相关配置文件：

- 主配置文件

`/etc/vsftpd/vsftpd.conf`

- 黑名单

`/etc/vsftpd/ftpusers`

里面的用户不允许访问 `FTP` 服务器

- 白名单

`/etc/vsftpd/user_list`

允许访问 `FTP` 服务器的用户列表

##### 启动服务器

- 设置开机自启动

```shell
systemctl enable vsftpd.service
```

- 启动 `ftp` 服务

```shell
systemctl start vsftpd.service
```

- 查看 `ftp` 服务端口

```shell
netstat -antup | grep ftp
```

开通服务器对应的 `ftp` 端口(`21`)，便可以使用 `ftp` 登录。

登录：

```shell
# 连接到ftp服务器
ftp 公网IP
# 切换到pub目录
cd pub/
# 上传文件
put etc/xxx/
# 下载文件
get xxx
```

##### 配置

- 更改权限

更改 `/var/ftp/pub` 目录的权限，为 `ftp` 用户添加写权限，并重新加载配置文件

```shell
#更改/var/ftp/pub目录的权限
chmod o+w /var/ftp/pub/  
#重启ftp服务
systemctl restart vsftpd.service
```

- 配置本地用户登录

本地用户登录就是指使用 `Linux` 操作系统中的用户账号和密码登录 `ftp` 服务器，`vsftp` 安装后默只支持匿名 `ftp` 登录，用户如果试图使用 `Linux` 操作系统中的账号登录服务器，将会被 `vsftpd` 拒绝

```shell
# 创建用户akashi
useradd akashi
# 修改用户akashi的密码
passwd akashi
```

回车后根据提示输入新密码完成创建。

修改 `/etc/vsftpd/vsftpd.conf`:

```shell
anonymous enable=NO
local_enable=YES
```

这样，就可以通过本地用户进行登录了。

##### 一些参数说明

- 用户登陆控制

参数 |	说明
--- | ---
`anonymous_enable=YES` |	接受匿名用户
`no_anon_password=YES` |	匿名用户 `login` 时不询问口令
`anon_root=(none)` |	匿名用户主目录
`local_enable=YES` |	接受本地用户
`local_root=(none)` |	本地用户主目录

- 用户权限控制

参数 |	说明
--- | ---
`write_enable=YES` |	可以上传(全局控制)
`local_umask=022` |	本地用户上传文件的 `umask`
`file_open_mode=0666` |	上传文件的权限配合 `umask` 使用
`anon_upload_enable=NO` |	匿名用户可以上传
`anon_mkdir_write_enable=NO` |	匿名用户可以建目录
`anon_other_write_enable=NO` |	匿名用户修改删除
`chown_username=lightwiter` |	匿名上传文件所属用户名
