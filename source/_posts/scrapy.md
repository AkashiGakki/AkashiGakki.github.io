---
title: Scrapy 实现豆瓣图片爬取
date: yyyy-mm-dd
category:
    - Python
    - Scrapy
tags:
    - Python
    - Scrapy
    - Spider
    - 爬虫

---

#### `Scrapy` 实现豆瓣图片爬取

> 使用 `Scrapy` 框架爬取豆瓣网站小姐姐图片资源（逃ﾚ(ﾟ∀ﾟ;)ﾍ=3=3=3）。

<!-- more -->

##### 准备工作

- `Scrapy` 框架安装

```shell
pip3 install scrapy
```

终端输入 `scrapy` 验证安装成功。

- `MongoDB` 安装

```shell
brew install mongodb
```

终端输入 `mongo` 验证安装成功。

- `PyMongo` 安装

```shell
pip3 install pymongo
```

验证安装：

```python
python3
import pymongo
pymongo.version
```

##### 创建项目

首先，确定我们爬取的目标，我们以 豆瓣上 `gakki` 的所有图片为例，从 `https://movie.douban.com/celebrity/1018562/photos/` 页面开始，爬取所有相关图片页的图片。然后开始创建项目：

创建一个 `Scrapy` 项目，项目初始文件可以直接用 `scrpay` 命令生成，命令如下：

```shell
scrapy startproject gakkiDouban
```

##### 创建 `Spider`

`Spider` 是自己定义的类， `Scrapy` 用它来从网页里抓取内容，并解析抓取的结果。

`Spider` 继承 `Scrapy` 提供的 `Spider` 类 `scrapy.Spider`，还要定义 `Spider` 的名称和起始请求，以及怎样处理爬取后的结果的方法。

使用命令行创建一个 `Spider`，命令如下：

```shell
cd gakkiDouban
scrapy genspider images movie.douban.com/celebrity/1018562/photos/\?start\=0
```

进入刚才创建的文件夹，然后执行 `genspider` 命令。第一个参数是 `Spider` 的名称，第二个参数是网站的域名。这里为 `?` 和 `=` 添加了转义字符。

##### 创建 `Item`

`Item` 是保存爬取数据的容器，它的使用方法和字典类似。不过，相比字典，`Item` 多了额外的保护机制，可以避免拼写错误或者定义字段错误。

创建 `Item` 需要继承 `scrapy.Item` 类，并且定义类型为 `scrapy.Field` 的字段。观察目标网站，我们需要获取的内容有 `url`、`page`。

定义 `Item`，修改 `item.py` 如下：

```python
import scrapy

class GakkidoubanItem(scrapy.Item):
    url = scrapy.Field()
    page = scrapy.Field()
```

这里定义了两个字段，接下来爬取时我们会使用到这个 `Item`。

##### 解析 `Response`

在创建 `Spider` 步骤时，我们看到有一个 `parse` 方法，它的参数 `resposne` 是 `start_urls` 里面的链接爬取后的结果。所以在 `parse()` 方法中，我们可以直接对 `response` 变量包含的内容进行解析，比如浏览器请求结果的网页源代码，或者进一步分析源代码的内容，或者找出结果中的链接而得到下一个请求。

这里我们先需要获得定义的字段内容 `url` 和 `page`：

```python
def parse(self, response):

    root = response.css('.article')
    
    page = root.css('.thispage::text').extract_first()
    urls = root.css('.cover')
    for uri in urls:
        url = uri.css('img::attr("src")').extract()[0]
```

这里的 `extract_first()` 方法来获取第一个元素， `extract()` 方法获取整个列表。

##### 使用 `Item`

`Item` 可以理解为一个字典，不过在声明的时候需要实例化，然后依次用刚才解析的结果赋值给 `Item`的每一个字段，最后将 `Item` 返回。

```python
from gakkiDouban.items import GakkidoubanItem


def parse(self, response):

    root = response.css('.article')
    item = GakkidoubanItem()
    item['page'] = root.css('.thispage::text').extract_first()
    urls = root.css('.cover')
    for uri in urls:
        item['url'] = uri.css('img::attr("src")').extract()[0]
        yield item
```

##### 后续 `Request`

获取了页面内容抓取之后，我们还需要从当前页中找到信息生成下一个请求，这样循环往复迭代，实现整站的爬取。

```python
def parse(self, response):

    root = response.css('.article')
    item = GakkidoubanItem()
    item['page'] = root.css('.thispage::text').extract_first()
    urls = root.css('.cover')
    for uri in urls:
        item['url'] = uri.css('img::attr("src")').extract()[0]
        yield item

    next_url = response.css('.paginator .next a::attr("href")').extract_first()
    url = response.urljoin(next_url)
    yield scrapy.Request(url=url, callback=self.parse)
```

这里我们获取了下一页的链接，然后调用 `urljoin()` 方法实现了下一个请求，这个方法在 `URL` 是相对地址时构造一个绝对地址，而如果是绝对地址又保持原样返回。

最后利用回调函数(`callback`)再次进入 `pares()`，就进入了下一页的爬取和解析。

##### 运行

在 `settings.py` 中设置 `user-agent`，伪装成浏览器：

```shell
USER_AGENT ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
```

这里因为域的问题修改一下 `spider` 文件，使其允许域名为豆瓣主目录，避免提取下一页时地址被过滤：

```python
class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/celebrity/1018562/photos/]
```

终端进入项目爬虫目录运行：

```shell
scrapy crawl images
```

`images` 是我们上面自定义的 `Spider` 名称。

##### 保存到文件

现在运行完 `Scpary` 后，我们只能在控制台看到输出结果，如果要将结果保存下来改怎么做呢？

如需保存成 `Json` 文件，可以执行如下命令：

```shell
scrapy crawl images -o images.json
```

这样，运行完成之后，项目内多了一个 `images.json` 文件，包含了刚才抓取的所有内容。

如果需要以每个 `Item` 输入一行 `Json` ，输出后缀为 `jl`，为 `jsonline` 的缩写：

```shell
scrapy crawl images -o images.jl
```

或者

```shell
scrapy crawl images -o images.jsonlines
```

除了以上格式，还可以自定义其他输出，如 `csv`, `xml`, `pickle`, `marshal` 和 `ftp` 远程输出：

```shell
scrapy crawl images -o images.csv
scrapy crawl images -o images.xml
scrapy crawl images -o images.pickle
scrapy crawl images -o images.marshal
scrapy crawl images -o ftp://user:pass@ftp.example.com/path/to/images.csv
```

其中，`ftp` 输出需正确配置用户名、密码、地址、书城路径。

##### 使用 `Item Pipeline`

如果需要实现更复杂的操作，如将结果保存到数据库，筛选 `item` 等需要定义 `Item Pipeline` 来实现。

`Item Pipeline` 为项目管道，当 `Item` 生成后，它会自动被送到 `Item Pipeline` 进行处理，我们常用 `Item Pipeline` 来实现下面操作：

- 清理 `HTML` 数据
- 验证爬取数据，检查爬取字段
- 查重并丢弃重复内容
- 将爬取结果保存到数据库

要实现 `Item Pipeline` ，只需定义一个类并实现 `process_item()` 方法即可。启用 `Item Pipeline` 后，`Item Pipeline` 会自动调用这个方法。`process_item()` 方法必须返回包含数据的字典或 `Item` 对象，或者抛出 `DropItem` 异常。

实现如下：

```python
import pymongo


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[self.mongo_db].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
```

定义好 `MongoPipeline` 之后，还需要在 `settings.py` 中使用它，需要定义 `MongoDB` 连接常量。

```shell
ITEM_PIPELINES = {
    'gakkiDouban.pipelines.MongoPipeline': 300,
}

MONGO_URL = 'localhost'
MONGO_DB = 'gakki_images'
```

在重新执行爬取，命令如下：

```shell
scrapy crawl images
```

爬取完成之后， `MongoDB` 中就创建了一个 `gakki_images` 数据库和 `gakki_images` 集合。

##### 一些自定义

仔细分析豆瓣的 `URL` 我们会发现，以 `https://img3.doubanio.com/view/photo/r/public/p747045173.jpg` 为例，网站是通过字符串下标的第 `37` 位控制加载图片的大小的，豆瓣服务器的图片存储分为 `m`, `l`, `r` 等不同的格式，而 `r` 对应的就是 `row`，是存储的最高清的图片格式。

我们在所有图片页进行爬取，抓到的是 `m` 缩略图格式，现在需要将 `URL` 进行修改，获取原生的图片。

定义一个新的图片处理管道：

```python
class SplitPipeline(object):
    def process_item(self, item, spider):
        url_split = list(item['url'])
        url_split[37] = 'r'
        item['url'] = ''.join(url_split)
        return item
```

同样，在 `settings.py` 中定义使用：

```shell
ITEM_PIPELINES = {
    'gakkiDouban.pipelines.SplitPipeline': 300,
    'gakkiDouban.pipelines.MongoPipeline': 400,
}
```

再次执行爬取，就可以得到 `row` 豆瓣最高清格式的图片。
