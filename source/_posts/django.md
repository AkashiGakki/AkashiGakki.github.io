---
title: Django 项目搭建及分页功能实现
date: yyyy-mm-dd
category:
    - Python
    - Django
tags:
    - Python
    - Django

---

#### `Django` 项目搭建及分页功能实现

> 利用 `Django` 框架实现一个简易 `Web Blog`

<!-- more -->

##### `Django` 安装

- 安装

```shell
pip3 install django
```

确认安装成功：

```shell
django-admin
```

出现提示信息，则安装成功。

或

```shell
python3 -m django --version
```

输出正确版本信息，则证明安装成功。

##### 项目搭建

###### `Django` 项目

- 初始化项目

```shell
django-admin startproject django_introduction
```

- 运行项目

```shell
python3 manage.py runserver
```

可以通过终端提示 `http://127.0.0.1:8000/` 进行访问：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5wpgdsnrqj21z412ajv8.jpg)

- 项目目录

    - `settings.py`
        - 项目配置文件
        - `BASE_DIR` 项目根目录
        - `SECRET_KEY` 安全码，项目自动生成
        - `DEBUG` 调试，`true` 和 `false` 可选
        - `ALLOWED_HOSTS` 配置允许的地址
        - `INSTALLED_APPS` 已安装应用，自己创建的应用需要在这里配置
        - `MIDDLEWARE` 中间件即 `Django` 自带的工具集
        - `ROOT_URLCONF` 指向 `RUL` 的路径
        - `TEMPLATES` 模板配置
        - `WSGI_APPLICATION`
        - `DATABASES` 数据库配置，默认是 `db.sqlite3` 
            - `AUTH_PASSWORD_VALIDATORS` 密码认证
        - `LANGUAGE_CODE` 语言
        - `TIME_ZONE` 时区
        - `STATIC_URL` 静态文件配置地址

    - `urls.py`
        - 项目路由配置文件

    - `manage.py`
        - 项目管理文件
        - `manage.py` 是与项目进行交互的命令行工具集的入口

    - `wsgi.py`
        - `python` 服务器网关接口，项目与服务器通信的接口

    - `__init__.py` 声明模块的文件，默认内容为空

###### `Django` 应用

> `Djanog` 项目与应用是一对多的关系，一个 `Django` 应用可以包含一组配置和若干个 `Django` 应用，`Django` 应用是一个可重用的 `Python` 软件包。


- 创建应用

```shell
python3 manage.py startapp blog
```

添加应用名到 `setting.py` 中的 `INSTALLED_APPS`

```python
'blog.apps.BlogConfig'
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5wp88s4s4j21de0e4ta9.jpg)

参考应用目录 `blog` => `apps.py` => `BlogConfig`

- 应用目录

    - `views.py`
        - 视图处理

    - `models.py`
        - 定义应用模型

    - `admin.py`
        - 定义 `admin` 模块管理对象

    - `apps.py`
        - 声明应用

    - `tests.py`
        - 编写应用测试用例

    - `urls.py`
        - （自行创建）管理应用路由

- 对视图和路由的理解实例

编写视图函数 `views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('hello world!')
```

编写路由配置

1. 配置应用层次路由

在 `blog` 应用下创建 `urls.py` 文件：

```python
from django.urls import path, include
# 引入刚才实现的视图文件
import blog.views

# 如果函数存在，则转发至对应路由位置
urlpatterns = [
    path('hello_world', blog.views.hello_world)
]
```

2. 配置项目层次路由

在项目的 `urls.py` 文件中实现：

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
```

这时，启动项目服务器，

```
python3 manage.py runserver
```

就可以在路由`http://127.0.0.1:8000/blog/hello_world` 访问。

##### 模型(`Model`)

> 在 `Django` 中我们以创建类的形式来创建数据表,对数据库的操作，就是对类和类的对象的操作，即 `ORM`

###### `Model` 定义

在 `blog` 应用的 `models.py` 中定义：

```python
from django.db import models


class Article(models.Model):
    # 文章唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 文章发布日期
    publish_date = models.DateTimeField(auto_now=True)
```

###### `Model` 迁移

> 通过模型的迁移将模型定义保存到数据库

- 创建模型变更的迁移文件

```python 
python3 manage.py makemigrations
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5wqbgwisaj21so03sq3r.jpg)

- 执行迁移文件同步变更到数据库

```python
python3 manage.py migrate
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5wqevlhzyj21sm0kwgqq.jpg)

##### `Django shell`

使用命令可以进入 `Django shell` 环境

> `Python shell` 用于交互式 `Python` 编程， `Django shell`也类似，它继承 `Django` 项目环境。

临时性操作使用 `Djaogo shell` 更加方便，它方便开发、调试、 `Debug`

```python
python3 manage.py shell
```

- 基本使用
    - `python manage.py shell`
    - `from blog.model import Article`
    - `Article.object.all()`

##### `Admin` 模块

> `Django` 的后台管理工具，可以读取定义的模型元数据，提供强大的管理使用页面。

管理页面的一般功能：认证用户、显示管理模型、校验输入等。由于管理页面是基础设施中的重要部分，功能又太过于统一，创建太过繁琐，所以 `Django` 提供了一个强大的 `Admin` 模块。

- 创建创建管理员用户

```shell
pthon3 manage.py createsuperuser
```

`Username`: `akashi`(自定义)
`Email`: (选填)
`Password`: `akashiadmin123`

- 登录页面进行管理

启动服务器(`python3 manage.py runserver`)，可以在`http://127.0.0.1:8000/admin/`登录进行访问。

- 将模型注册到 `admin`

在 `blog/admin.py` 中：

```python
from django.contrib import admin
from blog.models import Article

admin.site.register(Article)
```

- 文章列表显示标题

在 `models.py` 定义一个函数，添加返回值：

```python
def __str__(self):
    return self.title
```

重新启动服务： `python3 manage.py runserver`，便可以返回文章的标题。

##### `Django` 视图和模板

###### `Template`

> 模板系统的表现形式是文本，用于编写页面表现内容，做到了页面表现形式和表现内容分离。

定义了特有的标签占位符：

- 变量

```python
{{变量}}
```

- `for` 循环

```python
{% for x in list %}
{% endfor %}
```

- `if-else` 循环

```python
{% if %}
{% else %}
{% endif %}
```

###### 使用模板系统渲染博客页面

- 实现博客首页

新建页面存放路径：`blog` => `templates` => `blog` => `index.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>My Blog</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"></script>
</head>
<body>
<header class="container page-header">
    <h1>My blog
        <small> —— by akashi</small>
    </h1>
</header>
<div class="container page-body">
    <div class="col-md-9" role="main">
        <div class="body-main">
            {% for article in article_list %}
            <div>
                <h3>{{ article.title }}</h3>
                <p>{{ article.brief_content }}</p>
            </div>
            {% endfor %}
        </div>
    </div>
    <div class="col-md-3" role="complementary">
        <div>
            <h3>最新文章</h3>
            {% for article in article_list %}
            <h5><a href="#">{{ article.title }}</a></h5>
            {% endfor %}
        </div>
    </div>
</div>
</body>
</html>
```

在 `views.py` 中编辑返回方法：

```python
def get_index_page(request):
    all_article = Article.objects.all()
    # 渲染模板数据返回
    return render(request, 'blog/index.html', {
        'article_list': all_article
    })
```

配置路由，在应用路由 `urls.py` 中添加：

```python
path('index', blog.views.get_index_page),
```

之后便可以在 `http://127.0.0.1:8000/blog/index` 进行访问。

- 博客详情页

依照首页的步骤，先规划页面路径：`blog` => `templates` => `blog` => `detail.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{{ current_article.title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"></script>
</head>
<body>
<header class="container page-header">
    <h3>{{ current_article.title }}</h3>
</header>
<div class="container page-body">
    <div class="body-main">
        <p>
            {{ current_article.content }}
        </p>
    </div>
</div>
</body>
</html>
```

方法定义：

```python
def get_detail_page(request):
    current_article = Article.objects.all()[0]
    section_list = current_article.content.split('\n')
    return render(request, 'blog/detail.html', {
        'current_article': current_article,
        'section_list': section_list
    })
```

路由配置：

```python
path('detail', blog.views.get_detail_page)
```

##### 实现文章详情页页面跳转

- 文章跳转

重新规划 `URL`，传入 `article_id` 作为参数：

```python
path('detail/<int:article_id>', blog.views.get_detail_page)
```

同时，在视图层以形参的方式传入：

```python
def get_detail_page(request, article_id):
    current_article = Article.objects.get(article_id=article_id)
    section_list = current_article.content.split('\n')
    return render(request, 'blog/detail.html', {
        'current_article': current_article,
        'section_list': section_list
    })
```

这样，就可以指定 `id` 进行文章跳转。

- 实现超链接跳转

`index.html`:

```html
<div class="body-main">
    {% for article in article_list %}
    <div>
        <h3>
            <a href="/blog/detail/{{ article.article_id }}">{{ article.title }}</a>
        </h3>
        <p>{{ article.brief_content }}</p>
    </div>
    {% endfor %}
</div>
...
<div>
    <h3>最新文章</h3>
    {% for article in article_list %}
    <h5><a href="/blog/detail/{{ article.article_id }}">{{ article.title }}</a></h5>
    {% endfor %}
</div>
```

##### 实现文章上下篇跳转

首先，在 `detail.html` 中添加翻页标签：

```html
<div class="container">
    <nav aria-label="...">
        <ul class="pager">
            <li><a href="blog/detail/{{ previous_article.article_id }}">上一篇：{{ previous_article.title }}</a></li>
            <li><a href="blog/detail/{{ next_article.article_id }}">下一篇：{{ next_article.title }}</a></li>
        </ul>
    </nav>
</div>
```

然后，在 `views.py` 中添加需要的变量，并添加逻辑：

```python
def get_detail_page(request, article_id):

    current_article = None
    previous_article = None
    next_article = None
    all_article = Article.objects.all()
   
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.article_id == article_id:
            current_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]

    section_list = current_article.content.split('\n')
    return render(request, 'blog/detail.html', {
        'current_article': current_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article
    })
```

这样，就实现了上一页，下一页的跳转。

##### 实现分页功能

首页，也是在 `index.html` 添加分页标签：

```html
<div class="container body-footer clo-md-4 col-md-offset-3">
    <nav aria-label="Page navigation">
        <ul class="pagination">
            <li>
                <a href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            <li><a href="#">1</a></li>
            <li><a href="#">2</a></li>
            <li><a href="#">3</a></li>
            <li><a href="#">4</a></li>
            <li><a href="#">5</a></li>
            <li>
                <a href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        </ul>
    </nav>
</div>
```

然后，设计 `URL` 并获取分页的值：

设计 `URL` 如下： `http://127.0.0.1:8000/blog/index?page=9`

获取：

```python
def get_index_page(request):
    all_article = Article.objects.all()
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        # 赋一个默认值
        page = 1
    
    # 渲染模板数据返回
    return render(request, 'blog/index.html', {
        'article_list': all_article
    })
```

- 使用 `Django` 分页组件

导入：

```python
# 引入分页组件
from django.core.paginator import Paginator
```

获取当前页、上一页、下一页并实现逻辑：

```python
def get_index_page(request):
    all_article = Article.objects.all()
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        # 赋一个默认值
        page = 1

    # 实例化分页组件
    # 传入文章列表和分页数量
    paginator = Paginator(all_article, 2)
    # 获取分页数
    page_num = paginator.num_pages
    # 获取当前页
    page_article_list = paginator.page(page)
    # 判断是否有下一页
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    # 判断是否有上一页
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    # 渲染模板数据返回
    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'current_page': page,
        'previous': previous_page,
        'next': next_page
    })
```

同时，修改分页链接：

```html
<div class="container body-footer clo-md-4 col-md-offset-3">
    <nav aria-label="Page navigation">
        <ul class="pagination">
            <li>
                <a href="/blog/index?page={{ previous }}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            {%  for num in page_num %}
            <li><a href="/blog/index?page={{ num }}">{{ num }}</a></li>
            {% endfor %}
            <li>
                <a href="/blog/index?page={{ next }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        </ul>
    </nav>
</div>
```

这样，就完成了分页功能。

##### 实现最近文章列表

通过 `order_by` 查询并切片获取最新文章列表返回：

```python
def get_index_page(request):
    
    all_article = Article.objects.all()
    # - 表示倒序排序
    top3_article_list = Article.objects.order_by('-publish_date')[:3]
    
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        # 赋一个默认值
        page = 1

    # 实例化分页组件
    # 传入文章列表和分页数量
    paginator = Paginator(all_article, 2)
    # 获取分页数
    page_num = paginator.num_pages
    # 获取当前页
    page_article_list = paginator.page(page)
    # 判断是否有下一页
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    # 判断是否有上一页
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    # 渲染模板数据返回
    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'current_page': page,
        'previous': previous_page,
        'next': next_page,
        'top3_article_list': top3_article_list
    })
```

修改前端链接：

```html
<div class="col-md-3" role="complementary">
    <div>
        <h3>最新文章</h3>
        {% for article in top3_article_list %}
            <h5><a href="/blog/detail/{{ article.article_id }}">{{ article.title }}</a></h5>
        {% endfor %}
    </div>
</div>
```

这样，最新文章获取也完成了。

至此，完成了简易博客的全部功能。
