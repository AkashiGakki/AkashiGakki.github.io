---
title: Django Web 身份验证系统搭建（上）
date: 2019-8-14
category:
    - Python
    - Django
tags:
    - Python
    - Django
    - 项目部署

---

#### `Django Web` 身份验证系统搭建上）

> 使用 `Django` 搭建一个用户注册和身份验证系统，最终实现多用户注册使用的便签系统。

<!-- more -->

##### 建立虚拟环境

首先，为新项目建立一个目录，命名为 `learning_log`，进入目录并开始虚拟环境的搭建。

###### 建立虚拟环境

```python
mkvirtualenv -p python3 ll_env
```

###### 激活虚拟环境

```python
workon ll_env
```

###### 安装 `Django`

这里使用豆瓣源：

```shell
pip3 install django -i https://pypi.douban.com/simple
```

###### 在 `Django` 中创建项目

```shell
django-admin startproject learning_log .
```

使用命令新建一个 `Django` 项目，名为 `learning_log`，末尾的句点(`.`)让新项目使用合适的目录结构，这样开发完成之后可轻松地将应用程序部署到服务器上。

> 千万不要忘了句点，否则部署应用程序时会出现一些配置问题。

###### 创建数据库

```shell
python3 manage.py migrate
```

###### 启动项目

```shell
python3 manage.py runserver
```

##### 创建应用程序

保持项目启动的终端运行，重新打开一个终端，进入原项目目录，激活虚拟环境，创建应用程序：

首先，进入自己的项目目录再激活虚拟环境

```shell
workon ll_env
python3 manage.py startapp learning_logs
```

###### 定义模型

使用 `pycharm` 打开项目，在应用中打开 `models.py` 定义模型：

```python
from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
```

###### 激活模型

在 `settings.py` 中添加程序：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5y2z60o4sj21f00eo401.jpg)

- 修改数据库

修改数据库在 `Django` 中也称为迁移数据库，使用以下命令完成：

```shell
python3 manage.py makemigrations learning_logs
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5y32r2irwj21p403m0th.jpg)

- 执行迁移文件同步变更到数据库

```shell
python3 manage.py migrate
```

##### `Admin` 模块管理

###### 创建超级用户

```shell
python3 manage.py createsuperuser
```

`Username`: `akashi`
`Password`: `akashiadmin123`

这里只是一个示例，可以自定义。

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5y38z1oo5j21jq05m0tn.jpg)

###### 注册模型

在应用程序下的 `admin.py` 进行注册：

```python
from learning_logs.models import Topic

admin.site.register(Topic)
```

打开管理页(`http://127.0.0.1:8000/admin/`)，尝试添加一些主题： `Chess`、`RockClimbin`

###### 定义模型 `Entry`

这时，我们希望可以在学习笔记中添加定义条目的笔记记录，每个条目都与特定的主题相关联，这种关系被称为多对一关系，即多个条目可以关联到同一个主题。

我们再添加模型 `Entry`:

```python
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return self.text[:50] + "..."
```

这里我们在 `Entry` 类中嵌套了 `Meta` 类， `Meta` 存储用于管理模型的额外信息，我们让它能够设置一个特殊属性，让 `Django` 在需要时使用 `Entries` 来表示多个条目。如果没有这个类， `Django` 将使用 `Entrys` 来表示多个条目。

###### 迁移模型 `Entry`

```shell
python3 manage.py makemigrations learning_logs
python3 manage.py migrate
```

###### 注册模型

```python
from django.contrib import admin
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

同样，完成后添加一些记录在数据库中。

##### 创建网页

使用 `Django` 创建网页一般分为三个阶段： `定义URL`、`编写视图`和`编写模板`。

###### 映射 `URL`

首先，确定页面的存放路径：`learning_logs` => `templates` => `learning_logs` => `index.html`

根据路径，将项目层的 `urls.py` 路由到应用层：

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('note/', include('learning_logs.urls'))
]
```

在应用层新建 `urls.py`，然后路由到对应的方法：

```python
from django.urls import path, include

import learning_logs.views


urlpatterns = [
    path('index', learning_logs.views.get_index_page)
]
```

###### 编写视图

`views.py`:

```python
from django.shortcuts import render


def get_index_page(request):
    return render(request, 'learning_logs/index.html')
```

###### 编写模板

`index.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
    <p>Learning Log</p>
    <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
</body>
</html>
```

这样，通过`http://127.0.0.1:8000/note/index`便可以访问。

##### 创建其他网页

同样，确定页面存放路径：`learning_logs` => `templates` => `learning_logs` => `topics.html`

###### 映射 `URL`

项目层路由使用同一个，无需添加。

下面设计应用层路由：

```python
from django.urls import path, include
import learning_logs.views

urlpatterns = [
    path('index', learning_logs.views.get_index_page),
    path('topics', learning_logs.views.get_topics_page)
]
```

###### 实现视图层

`views.py`:

```python
def get_topics_page(request):
    topics_list = Topic.objects.all()
    return render(request, 'learning_logs/topics.html', {
        'topics': topics_list
    })
```

###### 实现模板

`topic.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topics</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a>
    </div>
    <div>
        <p>Topics</p>
        <ul>
            {% for topic in topics %}
                <li>{{ topic }}</li>
            {% empty %}
                <li>No topics have been added yet.</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

###### 实现特定主题的页面

- 路由

`learning_logs` => `templates` => `learning_logs` => `topic.html`

```python
from django.urls import path, include
import learning_logs.views

urlpatterns = [
    path('index', learning_logs.views.get_index_page),
    path('topics', learning_logs.views.get_topics_page),
    path('topics/<int:topic_id>', learning_logs.views.get_entry_page)
]
```

- 视图方法

```python
ef get_entry_page(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'learning_logs/topic.html', context)
```

- 模板

`topics.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topics</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a>
    </div>
    <div>
        <p>Topics</p>
        <ul>
            {% for topic in topics %}
                <li><a href="/note/topics/{{ topic.id }}">{{ topic }}</a></li>
            {% empty %}
                <li>No topics have been added yet.</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

`topic.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topics</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a>
    </div>
    <div>
        <p>Topic: {{ topic }}</p>
    </div>
    <div>
        <p>Entries:</p>
        <ul>
            {% for entry in entries %}
                <li>
                    <p>{{ entry.date_added }}</p>
                    <p>{{ entry.text }}</p>
                </li>
            {% empty %}
                <li>There are no entries for this topic yet.</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

##### 用户添加新主题

###### 导入表单模块

```python
from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {
            'text': ''
        }
```

###### `URL` 设计

```python
from django.urls import path, include
import learning_logs.views

urlpatterns = [
    path('index', learning_logs.views.get_index_page),
    path('topics', learning_logs.views.get_topics_page),
    path('topics/<int:topic_id>', learning_logs.views.get_entry_page),
    path('new_topic', learning_logs.views.new_topic)
]
```

###### 视图函数

```python
from django.http import HttpResponseRedirect

from .forms import TopicForm


def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/note/topics')

    context = {
        'form': form
    }
    return render(request, 'learning_logs/new_topic.html', context)
```

###### 模板

`new_topic.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topics</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a>
    </div>
    <div>
        <p>Add a new topic:</p>
    </div>
    <form action="/note/new_topic" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">add topic</button>
    </form>
</body>
</html>
```

在 `topics.html` 添加链接:

```html
<div>
    <a href="/note/new_topic">Add a new topic</a>
</div>
```

##### 用户添加新条目

###### 添加新条目表单

```python
from .models import Topic, Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 80
            })
        }
```

###### `URL` 设计

```python
from django.urls import path, include
import learning_logs.views

urlpatterns = [
    path('index', learning_logs.views.get_index_page),
    path('topics', learning_logs.views.get_topics_page),
    path('topics/<int:topic_id>', learning_logs.views.get_entry_page),
    path('new_topic', learning_logs.views.new_topic),
    path('new_entry/<int:topic_id>', learning_logs.views.new_entry)
]
```

###### 视图函数

```python
from .forms import TopicForm, EntryForm

def new_entry(request, topic_id):
    """在特定的主题下添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(('/note/topics/' + str(topic_id)))
    context = {
        'topic': topic,
        'form': form
    }
    return render(request, 'learning_logs/new_entry.html', context)
```

###### 模板

`new_entry`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topics</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a>
    </div>
    <div>
        <p>Add a new entry:</p>
    </div>
    <form action="/note/new_entry/{{ topic.id }}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">add entry</button>
    </form>
</body>
</html>
```

`topic.html`:

添加链接：

```html
...
 <div>
    <a href="/note/new_entry/{{ topic.id }}">Add a new entry</a>
</div>
```

##### 编辑条目

###### `URL` 设计

```python
from django.urls import path, include
import learning_logs.views

urlpatterns = [
    path('index', learning_logs.views.get_index_page),
    path('topics', learning_logs.views.get_topics_page),
    path('topics/<int:topic_id>', learning_logs.views.get_entry_page),
    path('new_topic', learning_logs.views.new_topic),
    path('new_entry/<int:topic_id>', learning_logs.views.new_entry),
    path('edit_entry/<int:entry_id>', learning_logs.views.edit_entry)
]
```

###### 视图函数

```python
from learning_logs.models import Topic, Entry

def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

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

###### 模板

`edit_entry.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Edit_Entry</title>
</head>
<body>
    <div>
        <a href="/note/topics/{{ topic.id }}">Topic - {{ topic }}</a>
    </div>
    <div>
        <p>Edit entry:</p>
    </div>
    <form action="/note/edit_entry/{{ entry.id }}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">save changes</button>
    </form>
</body>
</html>
```

`topic.html`:

链接到页面 `edit_entry`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Topic</title>
</head>
<body>
    <div>
        <a href="/note/index">Learning Log</a> -
        <a href="/note/topics">Topics</a>
    </div>
    <div>
        <p>Topic: {{ topic }}</p>
    </div>
    <div>
        <p>Entries:</p>
        <ul>
            {% for entry in entries %}
                <li>
                    <p>{{ entry.date_added }}</p>
                    <p>{{ entry.text }}</p>
                    <p>
                        <a href="/note/edit_entry/{{ entry.id }}">Edit entry</a>
                    </p>
                </li>
            {% empty %}
                <li>There are no entries for this topic yet.</li>
            {% endfor %}
        </ul>
    </div>
    <div>
        <a href="/note/new_entry/{{ topic.id }}">Add a new entry</a>
    </div>
</body>
</html>
```

至此，项目已经具备了需要的大部分功能。
