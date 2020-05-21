---
title: SSH 远程登录 Google Cloud 应用实例
date: 2019-8-29
category:
    - Linux
    - SSH
tags:
    - Linux
    - SSH
thumbnail: /images/bg-26.jpg

---

#### `ssh` 远程登录 `Google Cloud` 应用实例

> 配置 `ssh` 实现远程登录访问 `Google` 服务器。

<!-- more -->

首先，创建实例后，切换到 `root`:

```shell
sudo -i
```

或者

```shell
sudo su
```

##### 查看当前用户

查看当前用户：

```shell
who
```

为当前用户设置新密码：

```shell
sudo passwd xxx
```

注意：`xxx` 是你的用户名，也可以设置 `root` 用户的密码： `sudo passwd root`

也可以在 `root` 用户权限下新增加一个用户并设置密码

```shell
adduser akashi
passwd akashi
```

##### 编辑 `ssh` 配置文件

```shell
vim /etc/ssh/sshd_config
```

修改以下内容为 `yes`:

```shell
PermitRootLogin yes
PasswordAuthentication yes
```

重启生效

```shell
sudo service sshd reload
```

##### 使用 `ssh` 密码登录

```shell
ssh 用户名@公网IP
```

如：

```shell
ssh akashi@35.201.201.156
```

输入上面设置的密码实现登录。

##### 本地生成公钥和私钥

接下来介绍第二种方法，通过密钥实现登录。

在本地终端使用 ssh-keygen 命令生成新的密钥：

```shell
ssh-keygen -t rsa -f ~/.ssh/[KEY_FILENAME] -C [USERNAME]
```

注意：`[KEY_FILENAME]` 是要用于 `SSH` 密钥文件的名称，`[USERNAME]` 是连接到该实例的用户的用户名。

如：

```shell
cd .ssh
ssh-keygen -t rsa -f cloudkey -C akashi
```

注意：生成密钥时的 `passphrase` 是给 `private key` 设置一个密码，避免私钥被人盗用的风险。

##### 获取密钥

```shell
公钥文件：~/.ssh/[KEY_FILENAME].pub
私钥文件：~/.ssh/[KEY_FILENAME]
```

为下一步准备，获取公钥：

```shell
cat [KEY_FILENAME].pub
```

复制获取到的整串字符。

##### 修改 `SSH` 公钥元数据

拿着获取的公钥，访问 `Google Cloud`，进入谷歌云平台页面 -> 计算引擎 -> 元数据 -> SSH 密钥，粘贴保存：

![元数据](http://images.akashi.org.cn/FljhalIw4XFbIq642iCzH1jr3kz0)

![粘贴](http://images.akashi.org.cn/FoxFEbJNY-H_FAX1BWA1wtaOxyDy)

修改完成之后，`Google` 就会把上面这段 `public key` 写入到 `~/.ssh/authorized_keys` 中

接下来就可以通过密钥登录了。

##### 本地通过私钥登录

赋予私钥文件仅本人可读权限

```shell
chmod 400 <下载的与云服务器关联的私钥的绝对路径>
```

```shell
ssh -i ~/.ssh/[KEY_FILENAME] [USERNAME]@[IP]
```

如：

```shell
ssh -i ~/.ssh/cloudkey -p 22 akashi@35.201.201.156
```

至此，两种远程登录的方法介绍完毕。
