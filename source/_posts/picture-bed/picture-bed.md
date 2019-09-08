---
title: 自建图床方案
date: yyyy-mm-dd
category:
    - 杂项
tags:
    - 杂项
    - 图床
thumbnail: /images/bg-27.jpg

---

#### 自建图床方案

> 原使用的新浪微博图床不再支持外链，虽然还有补救的方法，但最安全的还是自建图床，本篇在图床的使用上提供了一些选择。

<!-- more -->

##### 维持原有方案

对于 `Markdown` 的重度依赖者来说，图床简直就是刚需，对图床的选择一般考量的无非就是方便、安全且免费，但这个需求原本就是矛盾的，想要数据安全就没有免费的说法。

免费图床方案一般有：[新浪微博图床](https://chrome.google.com/webstore/detail/%E6%96%B0%E6%B5%AA%E5%BE%AE%E5%8D%9A%E5%9B%BE%E5%BA%8A/fdfdnfpdplfbbnemmmoklbfjbhecpnhf?utm_source=chrome-ntp-icon)、[微博图床](https://chrome.google.com/webstore/detail/%E5%BE%AE%E5%8D%9A%E5%9B%BE%E5%BA%8A/pinjkilghdfhnkibhcangnpmcpdpmehk?utm_source=chrome-ntp-icon)、[SMMS图床](https://chrome.google.com/webstore/detail/smms%E5%9B%BE%E5%BA%8A%E6%8F%92%E4%BB%B6/fbamdjnnaaiidpgcfanfcboaanfmjfjk?utm_source=chrome-ntp-icon)

当然除了插件使用也可以直接在网站上使用：[SM·MS](https://sm.ms/)、[Imgur](https://imgur.com/)

微博图床配合 `Chrome` 插件使用完全符合方便的理念，但从微博限制外链开始，很多站点的图片就无法显示了，解决办法也有很多，但都存在缺陷，而且最重要的是,不是自己的图床终究没有办法掌控，万一哪一天微博将你图片删了也完全没有办法，所以使用免费图床，图片备份还是很重要的。

1. 从 `https` 回到 `http`

这个是折腾最少的方法，改了协议以后，原微博图床上的图片就可以正常显示了，但缺点也很明显，在都转为加密协议的潮流之下，使用回 `http` 会有诸多限制，类似于微信公众号等平台是不再支持不加密的图片显示的，同时也存在安全风险。


2. 设置 `no-referrer`

在文章页面源码加上

```html
<meta name="referrer" content="no-referrer" />
```

这种做法也存在缺陷，这样的话站点就识别不了你，对 `SEO` 优化很不友好。

##### 自建付费图床

直接购买一个对象存储服务自建图床是最安全的做法，推荐的有阿里云的 `OSS` 对象存储、腾讯云的 `COS` 对象存储、七牛云和又拍云等。实测阿里云 `OSS` 一年 `40GB` 只需 `9` 元，还是很划算的。

![阿里云OSS](http://images.akashi.org.cn/FrStDjhOtt9WyrLvheFqUQDrFf3G)

##### 七牛云搭建免费图床

那有没有既免费又安全的图床呢，当然也是有的。

七牛云的对象存储服务在实名认证之后可以免费领取 `10GB` 的云存储空间和每个月 `10GB` 的 `CDN` 加速流量，对于个人写作完全是足够了，我们可以用它来搭建一个自用的图床。

首先，注册并完成认证：[七牛云](https://www.qiniu.com/)

进入对象存储，新建存储空间，设置空间名称和选择区域

![七牛云](http://images.akashi.org.cn/Fgxt56AgROtKS4fY9cYtgeBQDa5F)

配置完成后，其实就可以在 `内容管理` 上传和查看图片了。但开始之前我们需要先绑定一个域名，七牛云提供的域名仅供测试使用，时间到了以后会自动回收。所以配置一个自己的域名可以一直使用。

![配置](http://images.akashi.org.cn/Fm8m1dIuIsfaIqfdjisH3dia5rW5)

完成基本配置之后是配置域名的 `CNAME`

详情可参考官方文档：[配置CNAME](https://developer.qiniu.com/fusion/kb/1322/how-to-configure-cname-domain-name)

这里以阿里云的为例，添加 `CNAME` 记录：

![CNAME](http://images.akashi.org.cn/FvkI1szGLEeFoKo5ZiyFOQcZehiH)

配置成功以后就可以配合插件或应用使用了。

![成功](http://images.akashi.org.cn/FpaXX6qlqleV_JTd51pUyFYYZFZa)

可以使用插件[七牛云图床](https://chrome.google.com/webstore/detail/%E4%B8%83%E7%89%9B%E4%BA%91%E5%9B%BE%E5%BA%8A/fmpbbmjlniogoldpglopponaibclkjdg/reviews)自动上传七牛云和获取 `Markdown` 格式图片

![七牛云图床](http://images.akashi.org.cn/FgyxskILg3stJQbF5UESq7as0OGE)

也可以使用[PicGo](https://github.com/Molunerfinn/PicGo)配置来实现七牛云上传：

![picgo](http://images.akashi.org.cn/FuXgMjDGpH7HJFaUGoXpAjMMKGuq)

在配置前我们需要获取七牛云的密钥：

![密钥](http://images.akashi.org.cn/FhR8nzolFxtvhqcX_LEV7gWFjaH0)

在应用中填入详细配置

![配置](http://images.akashi.org.cn/FkeirgmMNavwes07RDYgDhcbSJ_I)

![完成](http://images.akashi.org.cn/Snipaste_2019-08-29_12-35-41.png)

这样我们就可以开始使用了。

##### `GitHub` 搭建免费图床

<!-- 344c1f2fdf8a0ec5b1466e8edcdb94bf3751b0bf -->

当然我们还有更多的选择，还可以同样使用 `PicGo` + `Github` 实现自建图床。

- 创建仓库

<!-- ![创建仓库](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-34-19.png?token=AH3S4BH5CDVMGUT67NI7ADS5M6DAA) -->

![创建仓库](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-34-19.png)

- 设置

<!-- ![设置](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-35-17.png?token=AH3S4BGZVLHKDVMWRVBFMVC5M6DEG) -->

![设置](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-35-17.png)

- 拷贝仓库到本地（可省略）

<!-- ![get ssh](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-37-05.png?token=AH3S4BCFZ4TRAOOO4BYAGDC5M6DH2) -->

<!-- ![clone](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-42-06.png?token=AH3S4BDU4W622FHTWK25Q5C5M6DJE) -->

![ssh](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-37-05.png)

![clone](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-42-06.png)

- 获取 `token`

访问 `https://github.com/settings/tokens/new`，创建 `token`

<!-- ![创建](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-49-03.png?token=AH3S4BAZ2E6AQEDPQX6PQTC5M6DNO) -->

![创建](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-49-03.png)

获取到 `token`

<!-- ![保存](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-49-39.png?token=AH3S4BAJ47WBPPS52UIWW7K5M6DO2) -->

![保存](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-49-39.png)


- 设置 `PicGo`

配置 `PicGo` 的相关参数

<!-- ![github](https://raw.githubusercontent.com/AkashiGakki/image/master/markdown/Snipaste_2019-08-29_15-51-19.png?token=AH3S4BDREFBCAQULC6A6BJK5M6CEG) -->

![gitee](https://gitee.com/akashi_sai/image/raw/master/markdown/Snipaste_2019-08-29_15-51-19.png)

这样，一个 `Github` 的图床也创建好了。

但是，国内访问 `Github` 的速度还是比较缓慢，其实我们可以把 `Github` 换成国内的码云，这样速度就上来了，具体操作和搭建 `Github` 的图床大致相同。

