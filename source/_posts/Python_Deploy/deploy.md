---
title: Python 应用 uWSGI + Nginx 部署
date: yyyy-mm-dd
category: 
    - Python, Nginx
tags:
    - Python
    - Nginx
thumbnail: /images/bg-42.jpg

---

#### `Python` 应用 `uWSGI` + `Nginx` 部署

> `uWSGI` + `Nginx` 项目部署。

<!-- more -->

##### 新建一个 `Django` 应用部署

- 使用 `py` 文件启动 `uWSGI`

```python
def application(env, start_response):
    start_response('200 ok', [('Content-type', 'text/html')])
    return [b'Hello uWSGI.']
```

启动:

```shell
uwsgi --http-socket :8000 --plugin python3 --wsgi-file uwsgi_test.py
```

可能需要安装

```shell
sudo apt install uwsgi-plugin-common
sudo apt install uwsgi-plugin-python3
```

视情况也可能是 `apt install uwsgi-plugin-python`，看自己使用的 `Python` 版本和软连接情况。

这样，在对应的 `IP` 下的 `8000` 端口可以访问到文件。

- 新建 `Django` 项目

```python
django-admin startproject django_deployment
```

- 通过修改配置允许外部访问

`setting.py`:

```shell
ALLOWED_HOSTS = ["*"]
```

- 启动

```python
python3 manage.py runserver 0.0.0.0:8000
```

##### 打通 `Django` 与 `uWSGI` 的链路

先停止应用

- 启动 `uwsgi` 打通关系

在项目根目录启动

```python
uwsgi --http-socket :8000 --plugin python3 --module django_deployment.wsgi
```

- 将命令行配置改为文件配置

新建 `django-uwsgi.ini`:

```shell
touch django-uwsgi.ini
vim django-uwsgi.ini
```

```python
# 配置域
[uwsgi]

# 工作目录
chdir = /source/python/deployment/django_deployment

# 模块
module = django_deployment.wsgi

# 请求端口
http-socket = :8000

# master
master = True

# 进程
processes = 4

# 线程
threads = 1

# 是否退出是清理相关内容
vacuum = true
```

- 启动 

```python
uwsgi --ini django-uwsgi-ini
```

- 后台启动

后台运行程序并打印日志

```python
# 配置域
[uwsgi]

# 工作目录
chdir = /source/python/deployment/django_deployment

# 模块
module = django_deployment.wsgi

# 请求端口
http-socket = :8000

# master
master = True

# 进程
processes = 4

# 线程
threads = 1

# 是否退出是清理相关内容
vacuum = true

# backend run uwsgi
daemonize = %(chdir)/log/uwsgi-8000.log
log-maxsize = 1024*1024*1024
pidfile = %(chdir)/pid/uwsgi-8000.pid
```

创建文件夹 `log` 和 `pid`

启动

```python
uwsgi --ini django-uwsgi.ini
```

停止 

```python
uwsgi --stop pid/uwsgi-8000.pid
```

#### `Django` `Nginx` + `uWSGI` 部署

##### `uWSGI` 启动 `Django` 服务器

- 启动并查看 `pid`

```python
uwsgi --ini django-uwsgi-ini
```

```shell
cat pid/uwsgi-8000.pid
```

```shell
ps -aux | grep xxx
```

##### 修改 `Nginx` 配置文件，完成反向代理

复制备份配置文件 `nginx.conf` 为 `nginx.conf.back`

修改 `nginx.conf`

在 `63` 行处：

```python
upstream uwsgi {
    server 122.51.1.19:8000;
}

server {
    listen 80;
    server_name 122.51.1.19;
    charset utf-8;
    location / {
        proxy_pass http://uwsgi;
    }
}
 ```

 - 启动

 ```shell
 nginx
 ```

 查看启动进程情况

 ```shell
 ps -aux | grep nginx
 ```

 - 添加 `log` 配置文件

 ```python
upstream uwsgi {
    server 122.51.1.19:8000;
}

server {
        listen 80;
        server_name 122.51.1.19;
        charset utf-8;
        access_log /var/log/nginx/nginx.log;
        location / {
            proxy_pass http://uwsgi;
        }
}
```

重启

```shell
nginx -s reload
```

查看日志：

```shell
cd /var/log/ngxin/
ls
tail -f nginx.log
```

##### 收集静态文件，完成静态文件寻址配置

- 收集静态文件

```python
vim django_deployment/settings.py
```

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

```python
python manage.py collectstatic
```

- 配置静态文件路由

```python
upstream uwsgi {
        server 122.51.1.19:8000;
}

server {
    listen 80;
    server_name 122.51.1.19;
    charset utf-8;
    access_log /var/log/nginx/nginx.log;
    location / {
        proxy_pass http://uwsgi;
    }

    location /static {
        allas /source/python/deployment/django_deployment/static;
    }
}
```

重新加载

```shell
nginx -s reload
```

#### `HTTPS` 加密部署

使用 `443` 端口，协议加密传输报文。

- 申请 `SSL` 证书

在 `Nginx` 中新建文件夹 `ssl`，存放 `crt` 和 `key`

远程拷贝到服务器

```shell
scp 2_topic.akashi.org.cn.crt root@122.51.1.19::/etc/nginx/ssl/
scp 3_topic.akashi.org.cn.key root@122.51.1.19:/etc/nginx/ssl
```

- 配置 `Nginx` 支持 `HTTPS`

`nginx.conf`:

```python
listen 443 ssl;
ssl_certificate /etc/nginx/ssl/domain.com.crt;
ssl_certificate_key /etc/nginx/ssl/domain.com.key;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
```

- 定义 `80` 端口的返回

```python
server {
    listen 80;
    server_name topic.akashi.org.cn;
    rewrite ^(.*)$ https://$host$1 permanent;
}
```

或者

```python
server {
    listen 80;
    server_name topic.akashi.org.cn;
    return 301 https://topic.akashi.org.cn;$request_rui;
}
```

- 重启生效

```shell
nginx -s reload
```

### 部署高可用服务

添加配置的启动端口，开启多个服务，并且转发到 `nginx` 上，还可以通过权重分配达到负载均衡

```python
upstream uwsgi {
        server 127.0.0.1:8000 weight=3;
        server 127.0.0.1:8001 weight=1;
}
```

- 注意事项

1. 不要使用 `root` 权限启动 `uwsgi` 服务

2. 关闭 `uwsgi` 外网访问

```python
http-scoket = 127.0.0.1:8000
```

```python
http-scoket = 127.0.0.1:8001
```
