---
title: Django Web 身份验证系统搭建（下）
date: yyyy-mm-dd
category:
    - Python
    - Django
tags:
    - Python
    - Django
    - 项目部署

---

#### `Django Web` 身份验证系统搭建（下）

> 接上一篇实现用户功能，完善数据库模型。

<!-- more -->

接上一节，这次我们需要创建一个新的应用程序，其中包含与处理用户账户相关的所有功能。还需要对模型稍加修改，让每个主题都归属于特定用户。

##### 创建用户账户

###### 创建

首先，使用 `startapp` 来创建一个名为 `users` 的应用程序：

```shell
python3 manage.py startapp users
```

###### 添加到 `settings.py` 中

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5z753prgfj21eu0faabo.jpg)

这样，`Django` 将把应用程序 `users` 包含到项目中。

###### 创建应用程序 `users` 的 `URL`

首先，在项目层路由中(根目录的`urls.py`)设计 `users` 的 `URL`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('learning_logs.urls')),
    path('users/', include('users.urls'))
]
```

然后，新建应用层(`users`)的 `urls.py`，同样，在之后的页面路由中负责转发应用程序 `users` 的函数方法到视图层。

##### 登录页面

###### 设计应用层的 `URL`

```python
from django.urls import path, include
# from django.contrib.auth.views import auth_login
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html')),
]
```

注意，和之前不同的是，这一次我们没有设计视图层，而是将请求发送给 `Django` 的默认视图函数 `LoginView`，函数参数指明登录模板的位置。

###### 模板

在应用 `users` 下的路径建立模板： `users` => `templates` => `users` => `login.html`

`login.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}

    <form action="/users/login" method="post">
        {% csrf_token %}
        {{ form.as_p }}

        <button name="submit">login</button>
        <input type="hidden" name="next" value="/note/index">
    </form>
</body>
</html>
```

###### 链接到登录页面

更改首页 `index.html`，链接到 `login.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a> -
        {% if user.is_authenticated %}
            Hello, {{ user.username }}.
        {% else %}
            <a href="/users/login">login</a>
        {% endif %}
    </div>
    <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
</body>
</html>
```

这时，可以使用管理员用户进行登录尝试，访问`http://127.0.0.1:8000/users/login/` 进入登录页面。

##### 注销

现在需要提供一个让用户注销的途径，我们不用创建用于注销的页面，而是让用户单击一个链接完成注销并返回到主页。

为此，需要为链接定义一个 `URL` 模式，编写一个视图函数，并在首页 `index.html` 添加一个注销链接。

###### 注销 `URL`

```python
from django.urls import path, include
from django.contrib.auth.views import LoginView
import users.views

urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html')),
    path('logout', users.views.logout_view)
]
```

###### 视图函数 `logout_view`

`views.py`:

```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect('/note/index')
```

###### 链接到注销视图

在主页添加链接：

`index.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a> -
        {% if user.is_authenticated %}
            Hello, {{ user.username }}.
        {% else %}
            <a href="/users/login">login</a>
        {% endif %}
        <a href="/users/logout">logout</a>
    </div>
    <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
</body>
</html>
```

##### 注册页面

> 接下来就是创建一个让新用户可以注册的页面，我们使用 `Django` 提供的表单 `UserCreationForm`。

###### `URL` 模式

```python
from django.urls import path, include
from django.contrib.auth.views import LoginView
import users.views

urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html')),
    path('logout', users.views.logout_view),
    path('register', users.views.register)
]
```

###### 视图函数 `register()`

`views.py`:

```python
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(
                username=new_user.username, password=request.POST['password1']
            )
            login(request, authenticate_user)
            return HttpResponseRedirect('/note/index')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
```

###### 注册模板

模板路径：`users` => `templates` => `users` => `register.html`

`register.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a> -
        {% if user.is_authenticated %}
            Hello, {{ user.username }}.
            <a href="/users/logout">logout</a>
        {% else %}
            <a href="/users/register">register</a>
            <a href="/users/login">login</a>
        {% endif %}
    </div>

    <form action="/users/register" method="post">
        {% csrf_token %}
        {{ form.as_p }}

        <button name="submit">register</button>
        <input type="hidden" name="next" value="/note/index">
    </form>
</body>
</html>
```

###### 链接到注册页面

`index.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a> -
        {% if user.is_authenticated %}
            Hello, {{ user.username }}.
            <a href="/users/logout">logout</a>
        {% else %}
            <a href="/users/register">register</a>
            <a href="/users/login">login</a>
        {% endif %}
    </div>
    <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
</body>
</html>
```

##### 让用户拥有自己的数据

> 用户应该能够输入其专有的数据，因此我们将创建一个系统，确定各项数据所属的用户，再限制对页面的访问，让用户只能使用自己的数据。

我们需要修改模型 `Topic`，让每个主题都归属于特定用户。这也将影响条目，因为每个条目都属于特定的主题。

首先，限制对一些页面的访问。

###### 使用 `@login_required` 限制访问

> `Django` 提供了装饰器 `@login_required`，可以实现对于某些页面，只允许已经登录的用户访问它们。

1. 限制对 `topics` 页面的访问

只允许已登录的用户请求 `topics` 页面：

`learning_logs/views.py`:

```python
--snip--
from django.contrib.auth.decorators import login_required
--snip--

def get_index_page(request):
    return render(request, 'learning_logs/index.html')


@login_required()
def get_topics_page(request):
    topics_list = Topic.objects.all()
    return render(request, 'learning_logs/topics.html', {
        'topics': topics_list
    })
--snip--
```

`login_required()` 的代码检查用户是否已登录，仅当用户已登录时， `Django` 才会运行 `get_topics_page()` 的代码；如果用户未登录，就重定向到登录页面。

为实现这种重定向，我们需要修改 `setting.py`，让 `Django` 知道哪里去找登录页面：

在 `setting.py` 末尾添加:

```python
LOGIN_URL = '/users/login/'
```

2. 全面限制对项目的访问

除主页(`get_index_page()`、注册页面(`register()`)和注销页面(`logout_view()`)，限制其他所有视图函数的页面访问。

###### 将数据关联到用户

现在，需要将数据关联到提交它们的用户。我们只需将最高层的数据关联到用户，这样更低层的数据会自动关联到用户。

下面来修改模型 `Topic`，在其中添加一个关联到用户的外键。这样以后，必须对数据库进行迁移，最后，对必要的视图进行修改，使其只显示与当前登录用户相关联的数据。

1. 修改模型 `toopic`

只涉及两行：

```python
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
```

导入模型 `User`，建立外键关系。

2. 确定当前有哪些用户

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5zeg3a6u3j21jm0g2tb9.jpg)

3. 迁移数据库

知道用户 `ID` 之后，就可以迁移数据库了。

```shell
python3 manage.py makemigrations learning_logs
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5zejsvhenj21oc0f641k.jpg)

这里我们将既有的所有主题关联到了管理用户 `akashi`上（通过 `ID`），接下来使用这个值来迁移数据库：

```shell
python3 manage.py migrate
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5zenw30s0j21jy06mmyl.jpg)

###### 只允许用户访问自己的主题

当前，无论以哪一个用户身份登录，都可以看到所有的主题。现在，我们来改变这种情况，只向用户显示属于自己的主题。

在 `views.py` 中，对函数 `get_topics_page()` 做如下修改：

```python
@login_required()
def get_topics_page(request):
    """显示主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'topics': topics
    }
    return render(request, 'learning_logs/topics.html', context)
```

###### 保护用户的主题

现在，我们还没有对显示单个主题的页面访问进行限制，可以通过 `URL` 对不是当前用户的主题进行查看。

为修复这种问题，我们在视图函数 `get_entry_page()` 获取请求的条目前进行检查：

```python
from django.http import HttpResponseRedirect, Http404

@login_required()
def get_entry_page(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'learning_logs/topic.html', context)
```

###### 保护页面 `edit_entry`

使用同样的方法，禁止用户通过 `URL` 来访问其他用户的条目：

```python
@login_required()
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # post提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(('/note/topics/' + str(topic.id)))

    context = {
        'entry': entry,
        'topic': topic,
        'form': form
    }
    return render(request, 'learning_logs/edit_entry.html', context)
```

###### 将新主题关联到当前用户

当前，用于添加新主题的页面存在问题，因为它没有将新主题关联到特定的用户。

以下修复问题：

```python
@login_required()
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # form.save()
            return HttpResponseRedirect('/note/topics')

    context = {
        'form': form
    }
    return render(request, 'learning_logs/new_topic.html', context)
```

##### 设置项目样式

###### 第三方应用程序 `django-bootstrap3`

我们使用 `django-bootstrap3` 来将 `Bootstrap` 继承到项目中。这个应用程序下载必要的 `Bootstrap` 文件，将它们存放到项目的合适位置，让我们可以在项目的模板中使用样式设置指令。

为安装 `django-bootstrap3`，在活动的虚拟环境中执行如下命令：

```shell
pip3 install django-bootstrap3
```

接下来，需要在 `settings.py` 中的 `INSTALLED_APPS` 中添加如下代码，在项目中包含应用程序 `django-bootstrap3`：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'bootstrap3',

    'learning_logs',
    'users'
]

# django-bootstrap3的设置
BOOTSTRAP3 = {
    'include_jquery': True
}
```

###### 主页样式 `index`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60in6rpk3j21z412adk5.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container">

        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar"
            ></button>
            <a href="/note/index" class="navbar-brand">Learning Log</a>
        </div>

        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/note/topics">Topics</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                    <li><a href="#">Hello, {{ user.username }}</a></li>
                    <li><a href="/users/logout">log out</a></li>
                {% else %}
                    <li><a href="/users/register">register</a></li>
                    <li><a href="/users/login">log in</a></li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
<div class="container">
    <div class="page-header">
        <div class="jumbotron">
            <h1>Track Your Learning.</h1>
            <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
        </div>
    </div>
</div>
<div class="container">
    <h3>
        <a href="/users/register">Register an account</a>
        to make your own Learning Log, and list the topics you're learning about.
    </h3>
    <h3>Whenever you learn something new about a topic, make an entry summarizing what you're learned.</h3>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 话题页样式 `topics`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60ip4mi40j21z4124goe.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topics</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container">

        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar"
            ></button>
            <a href="/note/index" class="navbar-brand">Learning Log</a>
        </div>

        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/note/topics">Topics</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                    <li><a href="#">Hello, {{ user.username }}</a></li>
                    <li><a href="/users/logout">log out</a></li>
                {% else %}
                    <li><a href="/users/register">register</a></li>
                    <li><a href="/users/login">log in</a></li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
<div class="container">
    <div class="page-header">
        <h1>Topics</h1>
    </div>
</div>
<div class="container">
    <ul>
        {% for topic in topics %}
            <li>
                <h3><a href="/note/topics/{{ topic.id }}">{{ topic }}</a></h3>
            </li>
        {% empty %}
            <li>No topics have been added yet.</li>
        {% endfor %}
    </ul>

    <h3><a href="/note/new_topic">Add new topic</a></h3>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 条目页样式 `topic`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60irkdu9ej21z41240w2.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topic</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container">

        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar"
            ></button>
            <a href="/note/index" class="navbar-brand">Learning Log</a>
        </div>

        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/note/topics">Topics</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                    <li><a href="#">Hello, {{ user.username }}</a></li>
                    <li><a href="/users/logout">log out</a></li>
                {% else %}
                    <li><a href="/users/register">register</a></li>
                    <li><a href="/users/login">log in</a></li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
<div class="container">
    <div class="page-header">
        <h2>Topic: {{ topic }}</h2>
        <small>Entries:</small>
    </div>
</div>
<div class="container">
    <p><a href="/note/new_entry/{{ topic.id }}">Add new entry</a></p>

    {% for entry in entries %}
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3>
                    {{ entry.date_added | date:'M d, Y H:i' }}
                    <small><a href="/note/edit_entry/{{ entry.id }}">Edit entry</a></small>
                </h3>
            </div>
            <div class="panel-body">
                {{ entry.text | linebreaks }}
            </div>
        </div>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 新建话题 `new_topic`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60itscxffj21z40dcdgp.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>New_Topic</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container">

        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar"
            ></button>
            <a href="/note/index" class="navbar-brand">Learning Log</a>
        </div>

        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/note/topics">Topics</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                    <li><a href="#">Hello, {{ user.username }}</a></li>
                    <li><a href="/users/logout">log out</a></li>
                {% else %}
                    <li><a href="/users/register">register</a></li>
                    <li><a href="/users/login">log in</a></li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
<div class="container">
    <div class="page-herder">
        <h2>Add a new topic:</h2>
    </div>
</div>
<div class="container">
    <form action="/note/new_topic" method="post" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}

        {% buttons %}
            <button name="submit" class="btn btn-primary">add topic</button>
        {% endbuttons %}
    </form>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 新建条目 `new_entry`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60ivczx0cj21z40mkab9.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>New_Entry</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container">

        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar"
            ></button>
            <a href="/note/index" class="navbar-brand">Learning Log</a>
        </div>

        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/note/topics">Topics</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                    <li><a href="#">Hello, {{ user.username }}</a></li>
                    <li><a href="/users/logout">log out</a></li>
                {% else %}
                    <li><a href="/users/register">register</a></li>
                    <li><a href="/users/login">log in</a></li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
<div class="container">
    <div class="page-herder">
        <h2>Add a new entry:</h2>
    </div>
</div>
<div class="container">
    <form action="/note/new_entry/{{ topic.id }}" method="post" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}

        {% buttons %}
            <button name="submit" class="btn btn-primary">add entry</button>
        {% endbuttons %}
    </form>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 编辑条目 `edit_entry`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60iwpj6afj21z40n6jsr.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Edit_Entry</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container">

        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar"
            ></button>
            <a href="/note/index" class="navbar-brand">Learning Log</a>
        </div>

        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/note/topics">Topics</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                    <li><a href="#">Hello, {{ user.username }}</a></li>
                    <li><a href="/users/logout">log out</a></li>
                {% else %}
                    <li><a href="/users/register">register</a></li>
                    <li><a href="/users/login">log in</a></li>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
<div class="container">
    <div class="page-herder">
        <h2>Edit entry:</h2>
    </div>
</div>
<div class="container">
    <form action="/note/edit_entry/{{ entry.id }}" method="post" class="form">
        {% csrf_token %}
        {% bootstrap_form form %}

        {% buttons %}
            <button name="submit" class="btn btn-primary">save changes</button>
        {% endbuttons %}
    </form>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 注册 `register`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60iy7hmnwj21z412478b.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<div class="container">
    <div class="page-header">
        <h2>Register an account.</h2>
    </div>
</div>
<div class="container">
    <form action="/users/register" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}

        {% buttons %}
            <button name="submit" class="btn btn-primary">register</button>
        {% endbuttons %}

        <input type="hidden" name="next" value="/note/index">
    </form>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```

###### 登录 `login`

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g60izgdwazj21z40gywfl.jpg)

```html
{% load bootstrap3 %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
    <style>
        body {
            font-family: "plantc", "Source Han Serif", serif;
            font-weight: bolder;
            text-decoration: none;
        }
        footer {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>
<body>
<div class="container">
    <div class="page-header">
        <h2>Log in to your account.</h2>
    </div>
</div>
<div class="container">
    <form action="/users/login" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}

        {% buttons %}
            <button name="submit" class="btn btn-primary">log in</button>
        {% endbuttons %}

        <input type="hidden" name="next" value="/note/index">
    </form>
</div>
<footer class="footer">
    <h4>Copyright &copy; 2019 Akashi_Sai. All Rights Reserved.</h4>
</footer>
</body>
</html>
```
