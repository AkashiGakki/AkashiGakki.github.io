---
title: Ubuntu 下 MySQL 的安装
date: yyyy-mm-dd
category: 
    - Linux
    - 环境安装
tags:
    - Linux
    - 环境安装
thumbnail: /images/bg-41.jpg

---

### `Ubuntu` 下 `MySQL` 的安装

> 记录服务器下 `MySQL` 的安装过程。

<!-- more -->

```shell
apt install mysql-client-core-5.7
apt install mysql-client-5.7
apt install mysql-server-5.7
```

停止、启动和重启 `mysql` 服务

```shell
service mysql stop
service mysql start
service mysql restart
```

查看默认登录的用户名和密码

```shell
sudo cat /etc/mysql/debian.cnf
```

使用默认用户登录

```shell
mysql -u debian-sys-maint -p
```

查看当前所有存在的用户

```shell
select user from mysql.user;
```

修改密码

```shell
update mysql.user set authentication_string=PASSWORD("这里输入你的密码") where User='root';
```

更新所有操作权限

```shell
update mysql.user set plugin="mysql_native_password";
flush privileges;
```

退出并重新使用你设置的密码登录

```shell
exit
mysql -uroot -p
```
