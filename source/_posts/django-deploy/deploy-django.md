---
title: Django 项目 Linux 远程部署记录
date: 2020-05-31
category: 
    - Python
tags:
    - Python
    - Nginx
thumbnail: /images/asuka/asu-21.jpg

---

# Django 项目 Linux 远程部署记录

> `Django` 项目部署。该项目名称为 `shop-search`，配置端口号为 `9000`，以下为配置过程记录。

<!-- more -->

## 远程拷贝项目文件

```shell
scp -r ~/Source/Project/Python/shop-search  root@122.51.xx.xx:/source/python/deployment/
```

## 远程账号登录

```shell
ssh akashi@122.51.xx.xx
```

注意：项目最终部署时最好不要使用 `root` 用户部署。`root` 权限过高，直接部署项目存在安全隐患。

注意：`IP` 地址已隐去部分：`xx.xx`，参考时填写自己对应地址，以下相应隐去内容不再做提示。

## 远程虚拟环境启动

在对应项目下启动虚拟环境：

```shell
pipenv shell
pipenv install
```

## 同步、迁移数据表

项目数据库之前已经在远程创建完成，这里不再介绍，可使用 `mysqldump` 对数据进行快速导入导出操作。

基本数据库操作命令：

```shell
# 登录
mysql -uroot -pxxx

# 显示数据库列表
show databases;

# 选择并打开库
use xxx;

# 显示表
show tables;

# 建库
create database 库名;

# 建表：
use 库名；
create table 表名 (字段设定列表)；

# 删库和删表:
drop database 库名;
drop table 表名；
```

一些参考：

- [mysqldump](https://blog.csdn.net/shellching/article/details/8129687)
- [mongodb迁移mysql](https://www.cnblogs.com/xingyunfashi/p/8796107.html)
- [Django连接mysql](https://www.jianshu.com/p/40a8dd30a891)

使用 `Django` 命令同步和迁移数据库。

在迁移过程中如果出现报错 `django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.` 是因为 `2.x`以后 `Django` 版本兼容性导致。

原因参考[文档](https://yuntianti.com/posts/fix-django3-mysqlclient-import-error/).

目前比较好的解决方案就是做一个版本欺骗，简单高效。在 `apps` 下对应作用目录中的 `__init__.py` 中添加：

```py
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()
```

同时安装对应依赖：

```shell
pipenv install pymysql
```

进行同步迁移数据表：

```py
python manage.py makemigrations
python manage.py migrate
```

## `uwsgi` 项目启动

使用 `uwsgi` 对项目进行启动：

```shell
uwsgi --http-socket :9000 --plugin python --module shop-search.wsgi
```

若无报错，结束启动状态。配置后台启动文件。

### `ini` 文件配置

在项目根目录下新建配置文件 `shop-search-uwsgi.ini` 进行配置：

```shell
touch shop-search-uwsgi.ini
sudo vim shop-search-uwsgi.ini
```

配置如下：

```shell
# 配置域
[uwsgi]

# 工作目录
chdir = /source/python/deployment/shop-search

# 模块
module = shop-search.wsgi

# 请求端口
http-socket = :9000

# master
master = True

# 进程
processes = 4

# 线程
threads = 1

# 是否退出是清理相关内容
vacuum = true
```

### 配置 log 和 pid

新建日志文件和 `pid` 存储位置：

```shell
mkdir log && mkdir pid
```

在 `shop-search-uwsgi.ini` 中添加对应配置，用于后台启动和停止。

```shell
# backend run uwsgi
daemonize = %(chdir)/log/uwsgi-9000.log
log-maxsize = 1024*1024*1024
pidfile = %(chdir)/pid/uwsgi-9000.pid
```

### 启动

```shell
sudo uwsgi --ini shop-search.ini
```

启动后可对后台运行进程进行查看：

```shell
ps -aux | grep shop-search
```

注意：本项目依赖虚拟环境，需在虚拟环境中启动才能启动成功，注意查看虚拟环境是否开启，如果是使用远程主机本地环境，则可以忽略。

启动完成后退出虚拟环境：

```shell
exit
```

## 配置 Nginx

启动 `nginx`

```shell
sudo nginx
```

在对应 `nginx` 安装目录下修改配置文件 `nginx.conf`

以下是我的路径参考：

```shell
cd /etc/nginx
sudo vim nginx.conf
```

在 `http` 下添加配置：

注意：在 `60` 多行左右，可以在 `vim` 下输入 `:set nu` 显示行数。

```shell
# Shop-Search Site Config
upstream shop-search {
        server 122.51.xx.xx:9000;
}

server {
        listen 80;
        server_name search.akashi.xx;
        charset utf-8;
        access_log /var/log/nginx/nginx.log;
        location / {
            proxy_pass http://shop-search;
        }

        location /static {
            alias /source/python/deployment/shop-search/static;
        }
}
```

配置完成，重启 `nginx`：

```shell
sudo nginx -s reload
```

更多 `nginx` 配置，如加密部署、部署高可用服务等可参考我的另一篇文章：[Python 应用 uWSGI + Nginx 部署](https://akashigakki.github.io/2019/10/30/Python_Deploy/deploy/#more).

至此，项目远程部署完成。
