---
title: MongoDB 初探
date: yyyy-mm-dd
category:
    - 数据库
    - MongoDB
tags:
    - 数据库
    - MongoDB
thumbnail: /images/bg-16.jpg

---

#### `MongoDB` 初探

> `MongoDB` 是由 `C++` 语言编写的非关系型数据库，是一个基于分布式文件存储的开源数据库系统，其内容存储形式类似 `JSON` 对象，它的字段值可以包含其他文档、数组及文档数组，非常灵活。

<!-- more -->

##### 准备工作

###### 安装

这里使用 `Mac OS` 的包管理工具 `Homebrew` 进行下载安装，其他系统请自行搜索正确安装姿势。

```shell
brew install mongodb
```

然后创建一个新文件夹 `/data/db`，用于存放 `MongoDB` 数据。

注意：默认 `MongoDB` 数据文件是放到根目录 `data/db` 文件夹下,如果没有这个文件,需要自行创建。

###### 启动

```shell
brew services start mongodb
```

或者：

```shell
sudo mongodb
```

###### 停止、重启

停止:

```shell
brew services stop mongodb
```

重启:

```shell
brew serbices restart mongodb
```

###### 可视化工具

> 推荐两个可视化工具。

- `RoboMongo/Robo 3T`

    - `https://robomongo.org/`

- `Studio 3T`

    - `https://studio3t.com/`


##### 简介和使用

> `MongoDB` 是一个非关系型的数据库，什么叫非关系型？就是把数据直接放进一个大仓库，不标号、不连线、单纯的堆起来。传统数据库由于受到各种关系的累赘，各种数据形式的束缚，特有的约束和关联成为性能瓶颈，难以处理海量数据以及超高并发的业务场景。为了应对海量数据的存储，出现了非关系型数据库，它不支持外键，不支持事务，不支持数据类型约定，就这样松散的数据结构，成就了数据量的扩展。

###### 面向集合的存储

在 `MongoDB` 中，一个数据库包含多个集合，类似于 `MySQL` 中一个数据库包含多个表；一个集合包含多个文档，类似于 `MySQL` 中一个表包含多条数据。

可以把集合记为表，文档记为一条记录。

这样命名是有原因的，因为 `MongoDB` 没有行列统一的表格式排列，而是采用一个大仓库的形式将所有数据包纳其中。文档也一样，它是一段自由独立的数据，受外部限制少，所以区别于关系型数据库的记录。

###### 数据库

- 一个 `MongoDB` 可以创建多个数据库

- 使用 `show dbs` 可以查询所有数据库的列表

- 执行 `db` 命令则可以查看当前数据库对象或者集合

- 运行 `use` 命令可以连接到指定的数据库

注意：数据库名可以是任何字符，但是不能有`空格`、`点号`和 `$` 字符。

下面实际操作一次，在启动了 `MongoDB` 服务以后，在终端运行 `mongo` 可以进入 `MongoDB` 环境。

```shell
mongo
```

接下来我们`查看`所有的`数据库列表`：

```shell
show dbs
```

使用 `use` 命令`创建`数据库

```shell
use test
```

查询当前的`数据库对象`

```shell
db
```

再次查看所有数据库

```shell
show dbs
```

列出的所有数据库中看不到 `test` 或者显示 `test(empty)` ，因为 `test` 为空，里面没有任何东西，`MongoDB` 不显示或显示 `test(empty)`。

`销毁`数据库

```shell
db.dropDatabase()
```

这样，刚刚创建的数据库就被销毁了。

使用 `exit` 退出 `MongoDB` 环境

```shell
exit
```

###### 集合

集合就是一组文档的组合，就相当于是 `关系数据库中的表`，在 `MongoDB` 中可以存储不同的文档结构的文档。

例如：

```json
{"user": "akashi"} {"idol": "nogizaka", "member": "asuka"}
```

上面的两个文档就可以存储在同一个集合中，在关系型数据库中是很难实现上述数据结构的，要么需要定义大量的字段，对于一些字段名不确定的属性，关系型数据库会更加力不从心。

###### 文档

文档是 `MongoDB` 的核心，类似于`关系型数据库的每一条数据`，多个键及其关联的值放在一起就是文档。在 `Mongodb` 中使用一种类 `json` 的 `bson` 存储数据，`bson` 数据可以理解为在 `json` 的基础上添加了一些 `json` 中没有的数据类型。

- 文档的逻辑关系

例如有以下两个文档：

```json
# user文档
{
    "name": "akashi",
    "age": 22,
    "sex": "male"
}

# address文档
{
    "building": "22 A, Indiana Apt",
    "pincode": 123456,
    "city": "chengdu",
    "state": "sichuan"
}
```

1. 嵌入式关系:

```json
{
    "name": "akashi",
    "age": 22,
    "sex": "male",
    "address":
    [{
        "building": "22 A, Indiana Apt",
        "pincode": 123456,
        "city": "chengdu",
        "state": "sichuan"
    },{
        "building": "170 A, Acropolis Apt",
        "pincode": 456789,
        "city": "beijing",
        "state": "beijing"
   }]
}
```

2. 引用式关系:

> 将两个文档分开，通过引用文档的_id 字段来建立关系。

```json
{
    "name": "akashi",
    "age": 22,
    "sex": "male",
    "address_ids": [
        ObjectId("52ffc4a5d85242602e000000")    #对应address文档的id字段
    ]
}
```

在实际应用的时候，`嵌入式` 关系比较适合 `一对一` 的关系，`引用式` 关系比较适合 `一对多` 或者 `多对多` 的情况。

###### 原数据

数据库的信息存储在集合中，他们统一使用系统的命名空间：`DBNAME.system.*`。

`DBNAME` 可用 `db` 或数据库名替代：

- `DBNAME.system.namespaces` ：列出所有名字空间

- `DBNAME.system.indexs` ：列出所有索引

- `DBNAME.system.profile` ：列出数据库概要信息

- `DBNAME.system.users` ：列出访问数据库的用户

- `DBNAME.system.sources` ：列出服务器信息


###### 集合的创建和删除

- 创建集合

在数据库 `test` 中创建一个集合 `users`:

```mongo
use test
db.createCollection("users")
```

查看创建的集合：

```shell
show collections
```

- 删除集合

删除刚刚创建的集合 `users`:

```shell
db.users.drop()
```

查看是否删除成：

```shell
show collections
```

###### 向集合中插入数据

- 使用 `insert()`

插入数据时，如果 `users` 集合没有创建会自动创建。

```json
db.users.insert([
    {
        "name": "akashi",
        "email": "akashisai@163.com"
    }, {
        "name": "asuka",
        "email": "asuka@163.com"
    }
])
```

- 使用 `save()`

插入数据时，如果 `users` 集合没有创建会自动创建。

```json
db.users.save({
    "name": "akashi",
    "email": "akashi_sai@163.com"
})
```

`insert` 和 `save` 的区别：`insert` 是插入，侧重于新增一个记录的含义；`save` 是保存，可以保存一个新的记录，也可以保存对一个记录的修改。因此，`insert` 不能插入一条已经存在的记录，如果已经有了一条记录(以主键为准)，`insert` 操作会报错，而使用 `save` 指令则会更新原记录。

##### 阶段小结

到这里我们大致了解了非关系型数据库和关系型数据库的差异，现在我们来做一个阶段小结。

关系型数据库的结构一般是 `数据库database` => `表table` => `字段field`，就像下面这样：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5rb519ad6j20rs02y0sp.jpg)

而非关系型数据库的结构一般是 `数据库database` => `集合collection` => `文档document`，像下面这样：

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g5rbb2cb5hj20rs03kjre.jpg)

在充分理解差异之后，才能很好的将两者区分开来，不至于混淆。

##### 数据查询

###### `find()`

语法如下：

```mongo
db.COLLECTION_NAME.find()
```

以之前创建的 `users` 集合为例：

- 查询所有文档

查询数据，不加任何参数默认返回所有数据记录

```mongo
db.users.find()
```

- 添加查询条件

```mongo
db.users.find({"name": "akashi"})
```

###### `pretty()`

> `pretty()` 可以使查询输出的结果更美观。

```mongo
db.users.find().pretty()
```

如果你想让 `mongo shell` 始终以 `pretty` 的方式显示返回数据，可以通过下面的指令实现（退出环境，在终端输入）：

```shell
echo "DBQuery.prototype._prettyShell = true" >> ~/.mongorc.js
```

这样就把默认的显示方式设置为 `pretty` 了。

###### `AND`

> `MongoDB` 不需要类似于其他数据库的 `AND` 运算符，当 `find()` 中传入多个键值对时，`MongoDB` 就会将其作为 `AND` 查询处理。

用法：

```mongo
db.mycol.find({ key1: value1, key2: value2 })
```

###### `OR`

> `MongoDB` 中，`OR` 查询语句以 `$or` 作为关键词，用法如下：

```mongo
db.users.find({
    $or: [
        {key1: value1}, {key2:value2}
    ]
})
```

###### 更多

`$gt` 表示`大于`、`$lt` 表示`小于`、`$gte` 表示`大于等于`、`$lte` 表示`小于等于`、`$ne` 表示`不等于`。

可以这样记忆：

表达式 | 意义 | 描述
--- | --- | ---
`gt`： | 大于 |  `greater than`
`lt`： | 小于 |  `less than`
`gte`： | 大于或等于 |  `greater than equal`
`lte`： | 小于或等于 | `less than equal`

##### 文档基本操作

###### 删除数据库

语法：

- `db.dropDatabase()`：删除数据库

在当前数据库对象下执行语句，即可删除数据库。

```mongo
# 使用 db 查询当前数据库对象
db

# 删除当前数据库
db.dropDatabase
```

###### 创建集合

语法：

- `createCollection(name,options)`：创建集合

参数描述:

- `name`：创建的集合名称
- `options`：是一个作为初始化的文档(可选)

之前我们创建过无参数的集合，下面我们尝试创建一个带参数的集合：

```mongo
db.createCollection("user", { capped : 1, autoIndexId : 1, size : 6142800, max : 10000 } ) #带参数
```

参数描述：

- `capped`：类型为 `Boolean`，如果为 `true` 则创建一个固定大小的集合，当其条目达到最大时可以自动覆盖以前的条目。在设置其为 `true` 时也要指定参数大小；注意：固定集合的数据不能被修改，只能查找 => 删除 => 再插入；
- `autoIndexId`：类型为 `Boolean`，默认为 `false`，如果设置为 `true`，则会在 `_id` 字段上自动创建索引；
- `size`：如果 `capped` 为 `true` 则需要指定，指定参数的最大值，单位为 `byte`；
- `max`：指定最大的文档数。

在 `Mongodb` 中也可以不用创建集合，因为在创建文档的时候也会自动的创建集合。

###### 删除集合

语法：

- `db.COLLECTION.drop()`：删除集合

以下我们依然以之前创建的 `test` 数据库为例：

```mongo
use test    # 选择数据库
show collections    # 查看集合列表
db.users.drop()     # 删除test数据库下的users集合
```

###### 插入文档

语法：

- `db.COLLECTION_NAME.insert(document)`：插入文档

我们以下面的例子实际演示：

```json
# 先定义文档
user = ([
    {
        "user_id": 1,
        "name": "akashi",
        "email": "akashisai@163.com"
    }, {
        "user_id": 2,
        "name": "asuka",
        "email": "asuka@163.com"
    }
])

# 创建集合test的同时，插入文档数据
db.test.insert(user)
```

###### 更新文档

语法：

- `db.COLLECTION_NAME.update(SELECTION_CRITERIA,UPDATED_DATA)`：更新文档

我们将 `user_id=1` 文档中 `email` 进行更新：

```json
db.test.update({
    "user_id": 1
}, {
    $set:{
        "email": "akashi_sai@163.com"
    }
})
```

查询更新效果：

```json
db.test.find()
```

- 括号内第一个参数标识查找的内容的条件，第二个参数标识更新后的数据
- 默认的 `update` 函数只对一个文档更新，如果想作用所有文档，则需要加入 `multi:true`

```json
db.test.update({
    "user_id": 1,
    "name": "akashi",
    "email": "akashisai.163.com"
}, {
    $set:{
        "email": "akashi_sai@163.com"
    }
}, {
    "multi": true
})
```

###### 替换文档

语法：

- `db.COLLECTION_NAME.save({_id:ObjectId(),NEW_DATA})`：替换已存在的文档

```json
db.test.save({
    "_id" : ObjectId("5d4ba3240d800ad42ba1f8b8"), 
    "user_id": 2,
    "name": "sito_asuka", 
    "email": "sito_asuka@163.com"
})
```

前面提到过一下 `save` 的用法，它在存入数据的过程中，如果数据存在(通过主键`_di`进行区分)，则会替换原来的数据，如果不存在，则会新建一条数据。

我们也可以使用它插入一条文档：

```josn
db.test.save({
    "user_id": 3,
    "name": "gakki",
    "email": "gakki@163.com"
})
```

###### 删除文档

语法：

- `db.COLLECTION_NAME.remove(DELECTION_CRITERIA)`：删除文档

其实 `remove` 函数的参数跟 `update` 函数的第一个参数一样，相当于查找条件，注意，不要误删！

```mongo
db.test.remove({
    "name": "gakki"
})
```

删除后可以用查找命令确认数据:

```mongo
db.test.find()
```

##### 查询、索引与聚合

###### 查询语句 `find()`

语法：

- `db.COLLECTION_NAME.find(Parameter)`

已经使用过好多次了，这里不再介绍。

- 条件操作符

`$gt`：大于
`$lt`：小于
`$gte`：大于等于
`$lte`：小于等于

- `$type:[key]`:

可选的 `key` 值如下：

`1`: 双精度型(`Double`)
`2`: 字符串(`String`)
`3`: 对象(`Object`)
`4`: 数组(`Array`)
`5`: 二进制数据(`Binary data`)
`7`: 对象 `ID`(`Object id`)
`8`: 布尔类型(`Boolean`)
`9`: 数据(`Date`)
`10`: 空(`Null`)
`11`: 正则表达式(`Regular Expression`)
`13`: `JS` 代码(`Javascript`)
`14`: 符号(`Symbol`)
`15`: 有作用域的 `JS` 代码(`JavaScript with scope`)
`16`: `32` 位整型数(`32-bit integer`)
`17`: 时间戳(`Timestamp`)
`18`: `64` 位整型数(`64-bit integer`)
`-1`: 最小值(`Min key`)
`127`: 最大值(`Max key`)

```mongo
db.test.find({"name": {$type:2}})
```

上面的命令是用于查找 `name` 是字符串的文档记录，它等同于下面的命令：

```mongo
db.test.find({"name": {$type:'string'}})
```

- `limit()` 与 `skip()`

读取指定数量的数据记录 `limit()`。

```mongo
db.test.find().limit(1)
```

读取一条记录，默认是排在最前面的那一条被读取。

读取时跳过指定数量的数据记录 `skip()`。

```mongo 
db.test.find().limit(1).skip(1)
```

当然，还可以添加 `find` 的查找条件的参数，以便进行更精确的查找。

- 排序 `sort()`

标识升序和降序，其中升序用 `1` 表示，降序用 `-1` 表示。

语法：

- `db.COLLECTION_NAME.find().sort({KEY:1|-1})`

```mongo
db.test.find().sort({"user_id":-1})
```

###### 索引 `ensureIndex()`

> 索引通常能够极大的提高查询的效率，如果没有索引，`MongoDB` 在读取数据时必须扫描集合中的每个文件并选取那些符合查询条件的记录。这种扫描全集合的查询效率是非常低的，特别在处理大量的数据时，查询可能要花费几十秒甚至几分钟，这无疑对网站的性能是非常致命的。

索引是特殊的数据结构，索引存储在一个易于遍历读取的数据集合中，索引是对数据库集合中一个文档或多个文档的值进行排序的一种结构。

语法：

- `db.COLLECTION_NAME.ensureIndex({KEY:1|-1})`

同样 `1` 代表升序，`-1` 代表降序

```mongo
db.test.ensureIndex({"name": 1})
```

`ensureIndex()` 的可选参数：

参数 |	类型 |	描述
--- | --- | ---
`background`	| `Boolean` |	建立索引要不要阻塞其他数据库操作，默认为 `false`
`unique` | 	`Boolean` |	建立的索引是否唯一，默认 `false`
`name` |	`string` |	索引的名称，若未指定，系统自动生成
`dropDups` |	`Boolean` |	建立唯一索引时，是否删除重复记录，默认 `flase`
`sparse` |	`Boolean` |	对文档不存在的字段数据不启用索引，默认 `false`
`expireAfterSeconds` |	`integer` |	设置集合的生存时间，单位为秒
`v` |	`index version` |	索引的版本号
`weights` |	`document` |	索引权重值，范围为 `1` 到 `99999`
`default-language` |	`string` |	默认为英语
`language_override` |	`string` |	默认值为 `language`

```mongo
db.test.ensureIndex({"user_id":1,"name":1},{background:1})
```

###### 聚合 `aggregate()`

语法：

```json
db.COLLECTION_NAME.aggregate({
    $match:{x:1},
    {limit:NUM},
    $group:{_id:$age}
})
```

这些参数都可选：

- `$match`：查询，跟 `find` 一样；
- `$limit`：限制显示结果数量；
- `$skip`：忽略结果数量；
- `$sort`：排序；
- `$group`：按照给定表达式组合结果。

- 聚合表达式

名称 |	描述
--- | ---
`$sum` |	计算总和
`$avg` |	计算平均值
`min` 和 `min` 和 `max` |	计算最小值和最大值
`$push` |	在结果文档中插入值到一个数组
`$addToSet` |	在结果文档中插入值到一个数组，但不创建副本
`$first` |	根据资源文档的排序获取第一个文档数据
`$last` |	根据资源文档的排序获取最后一个文档数据

- 管道

> `MongoDB` 的聚合管道将 `MongoDB` 文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的。

表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。

聚合框架中常用的几个操作：

- `$project`：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
- `$match`：用于过滤数据，只输出符合条件的文档。`$match` 使用 `MongoDB` 的标准查询操作。
- `$limit`：用来限制 `MongoDB` 聚合管道返回的文档数。
- `$skip`：在聚合管道中跳过指定数量的文档，并返回余下的文档。
- `$unwind`：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
- `$group`：将集合中的文档分组，可用于统计结果。
- `$sort`：将输入文档排序后输出。
- `$geoNear`：输出接近某一地理位置的有序文档。
