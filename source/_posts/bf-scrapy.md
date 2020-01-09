---
title: Scrapy 实战：广度优先策略抓取
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

#### `Scrapy` 实战：广度优先策略抓取

> 通过广度优先策略抓取 `VCB-Studio` 站点文章信息。

<!-- more -->

##### 新建项目

首先，选取本次爬取的站点： `https://vcb-s.com/`，通过观察分析，站点文章采用分页的形式，我们可以先遍历每一页抓取到所有的文章 `URL` 列表，之后再进入具体文章抓取需要的信息。以上就是广度优先策略抓取。

- `CrawlSpider` 

本次我们以通用爬虫为例， `ScrawlSpider` 是 `Scrapy` 提供的一个通用 `Spider`，在 `Spider` 里，我们可以指定一些爬取规则来实现页面的爬取，这些爬取规则由一个专门的数据结构 `Rule` 表示。 `Rule` 里面包含提取和跟进页面的配置，`Spider` 会根据 `Rule` 来确定当前页面中的那些链接需要继续爬取、那些页面的爬取结果需要用哪个方法解析等。

首先，创建一个 `CrawlSpider`，我们需要定制一个模板，可以通过以下命令查看：

```shell
scrapy genspider -l
```

之前默认使用 `basic`，现在我们使用 `crawl` 进行创建：

```shell
scrapy genspider -t crawl source vcb-s.com
```

简单修改生成后的模板：

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SourceSpider(CrawlSpider):
    name = 'source'
    allowed_domains = ['vcb-s.com']
    start_urls = ['https://vcb-s.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        return item
```

##### 定义 `Rule`

在 `Rule` 里面定义规则，爬取当前分页下面的文章链接和后一页的连接，返回到回调函数之后，就可以获取所有分页下的文章链接了：

```python
rules = (
        Rule(LinkExtractor(allow='archives\/.*', restrict_css='#article-list .title-article a'), callback='parse_item'),
        Rule(LinkExtractor(restrict_css='.pagination li:last-child a'))
    )
```

使用正则表达式传递给 `allow` 做参数进行提取。

运行项目之前我们先设置 `settings.py`，不读取 `robots.txt` 和添加 `user-agent` 伪装为浏览器：

```python
ROBOTSTXT_OBEY = False

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
```

接下来运行项目，就发现下一页和详情页都被抓取到了：

```shell
scrapy crawl source
```

`Rule` 规则定义十分强大，我们仅用了两行就实现了所有文章链接的提取和下一页的提取。

##### 定义容器

在 `items.py` 中定义我们要提取的字段：

```python
import scrapy


class VcbstudioItem(scrapy.Item):
    collection = 'source_list'
    title = scrapy.Field()
    date = scrapy.Field()
    image = scrapy.Field()
    content = scrapy.Field()
    source_url = scrapy.Field()
```

这里我们定义了一个 `collection`，因为之后需要使用 `MongoDB` 进行存储，在这里先定义一个集合。

##### 测试用例

在提取页面信息的时候，我们不清楚自己定义的规则是否提取到准确的信息时，我们可以通过以下两种方式进行调试：

- `Scrapy shell`

在终端输入命令：

```shell
scrapy shell https://vcb-s.com
```

这里的 `URL` 就是我们需要测试的 `URL`，通过这样来模拟 `Scrapy` 的请求过程，就可以测试 `response` 调用的 `xpath()` 和 `css()` 的数据提取了

例如：

```shell
response.css('.title-article h1 a::text').getall()

response.css('.label i.fa.fa-calendar::text').get()
```

查看数据是否被规则正确提取。

- 断点调试

在项目起始目录新建一个测试用例，通过打断点的形式进行测试，查看规则是否正确提取。

新建 `test.py`:

```python
# 引入命令行执行函数模块
from scrapy.cmdline import execute
import sys
import os

# 调试测试

# 获取项目文件位置
# 思路：获取当前位置文件的父文件目录
path = os.path.dirname(os.path.abspath(__file__))
# 设置项目的运行起始位置
run_path = sys.path.append(path)
# 执行spider命令进入调试的断点
execute(['scrapy', 'crawl', 'source'])
```

执行命令中的列表参数就是我们启动项目输入的命令， `debug` 运行 `test.py` 就可以在自己设置的断点处查看当前数据的提取情况。

##### 解析页面

结合使用调试测试，就可以通过 `xpath()` 和 `css()` 提取数据，这里我们换一个方式，让提取信息更规整，使用 `ItemLoader` 实现配置化提取：

```python
from vcbstudio.items import VcbstudioItem
from scrapy.loader import ItemLoader


def parse_item(self, response):

    loader = ItemLoader(item=VcbstudioItem(), response=response)
    loader.add_css('title', '.title-article h1 a::text')
    loader.add_css('date', '.label i.fa.fa-calendar::text')
    loader.add_css('image', '.thumbnail img::attr("src")')
    loader.add_css('content', '.centent-article p::text')
    loader.add_css('source_url', '.dw-box.dw-box-download p a::attr("href")')
    yield loader.load_item()
```

运行项目，至此，我们已经实现了站点文章信息的全部提取。

##### 存储文件

在管道中定义存储方法：

```python
import pymongo
from vcbstudio.items import VcbstudioItem


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

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, VcbstudioItem):
            self.db[item.collection].save(dict(item))
        return item
```

同时添加 `MongoDB` 配置参数到 `settings.py`:

```python
MONGO_URL = 'localhost'
MONGO_DB = 'vcb-studio'
```

启用 `Item Pipeline`:

```python
ITEM_PIPELINES = {
   'vcbstudio.pipelines.MongoPipeline': 300,
}
```


##### 图片下载

`Scrapy` 还提供了专门处理下载的 `Pipeline`，包括文件下载和图片下载，同时支持异步和多线程，十分高效。

首先，定义文件存储路径：

```python
IMAGES_STORE = './images'
```

定义`ImagePipeline`:

内置的 `ImagesPipeline` 会默认读取 `Item` 的 `image_urls` 字段，并认为该字段是一个列表形式，它会遍历 `Item` 的 `image_urls` 字段，然后取出每个 `URL` 进行下载。

但是现在生成 `Item` 的图片链接的字段并不是 `image_urls` 字段， 所以为了实现下载，需要重新定义下载的部分逻辑。我们自定义一个 `ImagePipeline` ，继承内置的 `ImagesPipeline` ， 重写几个方法。

```python
class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Image Downloaded Failed.')
        return item

    def get_media_requests(self, item, info):
        for url in item['image']:
            yield Request(url)
```

设置启用：

```python
ITEM_PIPELINES = {
    'vcbstudio.pipelines.MongoPipeline': 300,
    'vcbstudio.pipelines.ImagePipeline': 301,
}
```

再次启动爬虫，就可以实现边抓取边下载图片了。

```shell
scrapy crawl source
```
