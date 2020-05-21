---
title: Redis 使用笔记
date: 2019-8-24
category:
    - 数据库
    - Redis
tag:
    - 数据库
    - Redis
thumbnail: /images/bg-23.jpg

---

#### `Redis` 使用笔记

> `Redis` 是一个开源的、高性能的、基于键值对的缓存与存储系统，通过提供多种键值数据类型来适应不同场景下的缓存与存储需求。同时， `Redis` 的诸多高级功能使其可以胜任消息队列、任务队列等不同的角色。

<!-- more -->

##### 简介

###### 存储结构

`Redis` 是 `Remote Dictionary Server` （远程字典服务器）的缩写，它以字典结构存储数据，并允许其他应用通过 `TCP` 协议读写字典中的内容。与大多数脚本语言中的字典一样， `Redis` 字典中的键值除了可以使字符串，还可以是其他数据类型。它支持的键值数据类型如下：

- 字符串类型

- 散列表类型

- 列表类型

- 集合类型

- 有序集合类型

###### 内存存储与持久化

`Redis` 数据库中的所有数据都存储在内存中。由于内存的读写速度远快于硬盘，因此 `Redis` 在性能上对比其他的基于硬盘存储的数据库有明显的优势，一台普通的笔记本电脑上， `Redis` 可以在一秒内读写超过 `10` 万个键值。

将数据存储在内存中也存在问题，比如程序退出后内存中的数据会丢失。不过 `Redis` 提供了对持久化的支持，即可以将内存中的数据异步写入到硬盘中，同时不影响继续提供服务。

###### 缓存、队列系统

由于 `Redis` 提供了丰富的功能，越来越多的人将其用作缓存、队列系统。

`Redis` 可以为每个键设置生存时间（`Time To Live TTL`），生存时间到期后键会自动被删除。可以限定数据占用的最大内存空间，在数据达到空间限制之后可以按照一定的规则自动淘汰掉不需要的键。用作缓存系统性能非常出色。

除此之外， `Redis` 的列表类型键可以用来实现队列，并且支持阻塞式读取，可以很容易的实现一个高性能的优先级队列。同时在更高的层面上，`Redis` 还支持 "`发布/订阅"` 的消息模式。

##### 准备

###### 安装

在 `OS X` 系统中安装：

```shell
brew install redis
```

###### 启动

```shell
redis-server
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g69qd2xmlxj21ts0pun0s.jpg)

可以重新打开一个终端窗口，查看 `redis`：

```shell
ps -ef | grep redis
```

或者通过端口号检查 `Redis` 服务器状态：

```shell
netstat -nlt|grep 6379
```

`Redis` 服务器默认使用 `6379` 端口，当然可以通过 `--port` 自定义端口号。

###### 启动 `Redis-client`

启动完服务器以后，重新打开一个窗口：

```shell
redis-cli
```

即可以启动 `Redis` 客服端。

查看连接：

```shell
redis-cli ping
```

如果连接正常，会输出 `PONG`

`redis-cli` 的一些使用：

自定义地址和端口号

```shell
redis-cli -h 127.0.0.1 -p 6379
```

测试连接（不带运行参数 `redis-cli`）

```shell
PING
```

```shell
echo hi
```

###### 停止

终端运行：

```shell
redis shutdown
```

考虑到 `Redis` 有可能正在将内存中的数据同步到硬盘中，强行终止 `Redis` 进程可能会导致数据丢失。通过 `SHUTDOWN` 命令， `Redis` 会先断开所有的客服端连接，然后根据配置执行持久化，最后完成退出。

###### `Redis` 可执行文件说明

名称 | 说明
--- | ---
`redis-server` | `Redis` 服务器
`redis-cli` | `Redis` 命令行客服端
`redis-benchmark` | `Redis` 性能测试工具
`redis-check-aof` | `AOF` 文件修复工具
`redis-check-dump` | `RDB` 文件检查工具
`redis-sentinel` | `Sentinel` 服务器

##### `Redis` 数据类型

###### 基础命令

以下我们在开启 `Redis` 服务器的情况下，另外再开一个终端启动 `redis-cli` 客户端进行下面的学习：

- 键值存储

语法：

```shell
set key value
```

`eg`:

```shell
set bar 1
```

存入了一个键为 `bar`，值为 `1` 的键值。

- 获取键名列表

语法：

```shell
keys pattern
```

`eg`:

```shell
keys *
```

使用上面的命令我们获得了 `Redis` 中所有的键。

> 注意：`keys` 命令需要遍历 `Redis` 中所有的键， 当键的数量较多时会影响性能，不建议在生产环境中使用。

- 判断键是否存储

语法：

```shell
exists key [key ...]
```

`eg`:

```shell
exists bar
```

如果存在，返回整数类型 `1`，否则返回 `0`。

- 获取数据类型

`type` 用来获取键值的数据类型，返回值可能是 `string` (字符串类型)、`hash`(散列类型)、`list`(列表类型)、`set`(集合类型)、`zset`(有序集合类型)

语法：

```shell
type key
```

`eg`:

```shell
type bar
```

返回的值是 `string`。

- 删除键

语法：

```shell
del key [key ...]
```

`eg`:

```shell
del bar
```

这样就删除了我们刚刚存入的 `{'bar': '1'}`

###### 字符串类型

- 赋值与取值

语法：

```shell
set key value
```

```shell
get key
```

`set` 和 `get` 是 `Redis` 里面最基础的两个命令，用来设置和获取键值。

- 递增

当存储的字符串是整数形式时，`Redis` 提供了一个实现当前键值递增的命名 `incr`，返回递增后的值。

语法：

```shell
incr key
```

`eg`:

```shell
incr num
```

当操作的键不存在时默认键值为 `0`，所以输出结果是递增后的 `1`。当键值不是整数时会提示错误。

- 增加指定的整数

语法：

```shell
incrby key increment
```

`incrby` 命令和 `incr` 命令基本一样，只不过前者可以通过参数 `increment` 指定一次增加的数值，如：

```shell
incrby num 3
```

在上一次（`1`） 的结果上再增加 `3`，那么输出应该为 `4`。

- 减少指定的整数

语法：

```shell
decr key
```

```shell
decrby key decrement
```

同样的，`decr` 和 `decrby` 可以实现让键值递减。

`eg`:

```shell
decrby num 2
```

继续使用上面的参数例子，在 `4` 的基础上减去 `2`，输出结果是 `2`。

- 增加指定浮点数

语法：

```shell
incrbyfloat key increment
```

`eg`:

```shell
incrbyflodt num 2.7
```

输出结果为 `4.7`。

- 向尾部追加值

语法：

```shell
append key value
```

`eg`:

```shell
set say hello
append say ' asuka!'
get say
```

![](http://ww1.sinaimg.cn/large/9c62a0cfly1g69qe12yrlj20vo05wab9.jpg)

`append` 的作用是向键值的末尾追加 `value`。例子中使用了引号是因为参数包含了空格，也可以输入类似于：

```shell
set name akashi
append name sai
get name
```

输出为： `akashisai`

- 获取字符串长度

语法：

```shell
strlen key
```

`strlen` 命令返回键值的长度，如果键不存在则返回 `0`。

`eg`:

```shell
strlen say
```

- 同时获取/设置多个键值

语法：

```shell
mget key [key ...]
mset key value [key value ...]
```

- 位操作

一个字节由 `8` 个二进制位组成， `Redis` 提供了 `4` 个命令可以直接对二进制位进行操作。

语法：

```shell
getbit key offset
setbit key offset value
bitcount key [start] [end]
bitop operation destkey key [key ...]
```

`getbit` 命令可以获得一个字符串类型键指定位置的二进制位的值（ `0` 或 `1`）。

`bitcount` 命令可以获得字符串类型键中值是 `1` 的二进制位个数。

###### 散列类型

> 散列表(`hash`)的键值是一种字典结构，其存储了字段(`field`)和字段值的映射，但字段值只能是字符串，不支持其他数据类型，也就是说，散列类型不能嵌套其他类型。

注意：其实 `Redis` 的其他数据类型同样不支持数据类型的嵌套。比如集合类型的每个元素都只能是字符串，不能是另一个集合或者散列表等。

散列类型适合存储对象。

- 赋值与取值

语法：

```shell
hset key field value
hget key field
hmset key field value [field value ...]
hmget key field [field ...]
hgetall key
```

`eg`:

```shell
hset user name akashi
hget user name
```

`hset` 的方便之处在于不区分插入和删除操作，这意味着不用事先判断字段是否存在来决定执行的是插入(`insert`)还是更新(`update`)操作。当字段不存在时，执行插入操作，返回 `1`，当字段存在时，执行更新操作，返回 `0`；当键本身不存在时，还会自动建立。

当需要设置/查找多个字段时：

```shell
hmset user age 21 email akashi_sai@163.com
hmget user name age email
```

如果想获取键中的所有字段和字段的值却不知道键中有哪些字段时，可以使用 `hgetall` 命令：

```shell
hgetall user
```

- 判断字段是否存在

语法:

```shell
hexists key field
```

`hexists` 用来判断一个字段是否存在，如果存在返回 `1`，否则返回 `0`。

- 当字段不存在时赋值

语法：

```shell
hsetnx key field value
```

`nx` 表示 `if not exisits`

`hsetnx` 与 `hset` 类似，区别在于如果字段已经存在，`hsetnx` 将不再执行任何操作。

- 增加数字

语法：

```shell
hincrby key field increment
```

`eg`:

```shell
hincrby user age 1
```

- 删除字段

语法：

```shell
hdel key field [field ...]
```

`hdel` 命令可以删除一个或多个字段，返回值是被删除的字段个数。

- 只获取字段名或字段值

语法：

```shell
hkeys key
hvals key
```

`eg`:

```shell
hkeys user
hvals user
```

- 获取字段数量

语法：

```shell
klen key
```

`eg`:

```shell
hlen user
```

###### 列表类型

> 列表类型(`list`)可以存储一个有序的字符串列表，常用的操作是向两端添加元素，或者获得列表的某一个片段。

- 向列表两端增加元素

语法：

```shell
lpush key value [value ...]
rpush key value [value ...]
```

`eg`:

```shell
lpush list 1
lpush list 0
```

在列表左边增加元素，完成后，列表 `list` 的元素为 `0 1`。

继续从右边增加元素：

```shell
rpush list 2 3
```

现在列表中的元素排列为: `0 1 2 3`。

- 从列表两端弹出元素

语法：

```shell
lpop key
rpop key
```

以上面声明的 `list` 为例：

```shell
lpop list
```

我们知道现在最左边的数字是 `0`，所以输入命令，返回了 `0`。

```shell
rpop list
```

同样，返回最右边的数字 `3`。现在我们弹出了列表两端的两个数字，还存在列表中的还有 `1 2`。

- 获取列表中元素的个数

语法：

```shell
llen key
```

当键不存在时返回 `0`。

```shell
llen list
```

返回了当前的列表元素个数 `2`。

- 获取列表片段

语法：

```shell
lrange key start stop
```

`Redis` 的列表索引从 `0`开始，返回包括两端的元素。为了演示，我们先往列表里添加一些元素：

```shell
rpush 3 4 5 6 7
lrange list 2 5
```

现在列表里的元素分别有 `1 2 3 4 5 6 7`，返回索引从 `2` 开始，`5` 结束的元素，有：`3 4 5 6`。

- 删除列表中指定的值

语法：

```shell
lrem key count value
```

`lrem` 会删除列表中前 `count` 个值为 `value` 的元素，返回值是实际删除的元素个数。根据 `count` 的值的不同，分为以下几种情况：

1. `count > 0` 时，`lrem` 会从列表左边开始删除前 `count` 个值为 `value` 的元素。

2. `count < 0` 时，`lrem` 会从列表右边开始删除前 `|count|` 个值为 `value` 的元素。

3. `count = 0` 时，`lrem` 会删除所有值为 `value` 的元素。

`eg`:

```shell
lrem key 0 7
```

以上例子删除了所有值为 `7` 的元素。

- 获取/设置指定索引的元素值

如果要将列表类型当做数组来用，`lindex` 是必不可少的，`lindex` 用来返回指定元素的索引，索引从 `0` 开始。

```shell
lindex key index
lset key index value
```

`eg`:

```shell
lindex list 1
lindex list -1
```

`-1` 表示最右边的索引，以此类推，`-2` 即为列表里面倒数第二个元素。

- 只保留列表指定片段

语法：

```shell
ltrim key start end
```

`ltrim` 可以删除指定索引范围之外的所有元素，其指定列表范围的方法和 `lrange` 相同。

- 向列表中插入元素

语法：

```shell
linsert key before|after pivot value
```

`linsert` 先从左到右查找 `pivot` 元素位置，然后根据参数决定在之前或者之后插入。

- 将元素从一个列表转到另一个列表

语法：

```shell
rpoplpush source destination
```

即先执行 `rpop` 再执行 `lpush`命令先从 `source` 列表类型键的右边弹出一个元素，然后将其加入到 `destination` 列表类型的左边，并返回这个元素的值。

当把列表类型当做队列使用时，`rpoplpush` 可以直观的在多个队列中传递数据；

当 `source` 和 `destination` 相同时，会不断执行队尾元素移到队首，借助这个特性可以实现一个网站监控系统。

###### 集合类型

> 集合类型的常用操作是向集合中加入或删除元素、判断某个元素是否存在等，由于集合类型在 `Redis` 内部是使用值为空的散列表实现的，所以这些操作的时间复杂度都是 `O(1)`。最方便的是多个集合类型之间还可以进行并集、交集和差集运算。

集合与列表类型的比较：

 | 集合类型 | 列表类型
--- | --- | ---
存储内容 | 字符串 | 字符串
有序性 | 否 | 是
唯一性 | 是 | 否

- 增加/删除元素

语法：

```shell
sadd key member [member ...]
srem key member [member ...]
```

`sadd` 用来向集合中增加一个或多个元素，如果键不存在则会自动创建。因为在一个集合中不能有相同的元素，所以如果加入的元素已经存在就会忽略这个元素，返回值是成功加入的元素的数量。


`eg`:

```shell
sadd letters a
sadd letters a b c
```

第一条成功加入一个元素，返回 `1`，第二条加入的 `a` 元素已经存在，忽略，新加入了 `2` 个元素，返回 `2`。

同理的 `srem` 用来从集合中删除一个或多个元素，并返回删除成功的个数。

`eg`:

```shell
srem letters a
```

- 获得集合中的所有元素

语法：

```shell
smembers key
```

- 判断元素是否在集合中

语法：

```shell
sismember key member
```

判断一个元素是否存在集合中的时间复杂度为 `O(1)`， 当存在时返回 `1`，否则返回 `0`。

- 集合间运算

语法：

```shell
sdiff key [key ...]
sinter key [key ...]
sunion key [key ...]
```

`sdiff` 表示执行集合的差集运算、`sinter` 表示执行集合的交集运算、`sunion` 表示执行集合的并集运算。

- 获取集合中元素个数

语法：

```shell
scard key
```
- 进行集合运算并将结果存储

语法：

```shell
sdiffstore destination key [key ...]
sinterstore destination key [key ...]
sunionstore destination key [key ...]
```

- 随机获取集合中的元素

语法；

```shell
srandmember key [count]
```

`eg`:

```shell
srandmember letters
srandmember letters 2
```

可选参数 `count` 用来随机获取多个元素，

当 `count` 为正数时，随机获取集合里 `count` 个不重复的元素；

当 `count` 为负数时，随机获取集合里 `|count|` 个元素，有可能相同；

- 从集合中弹出一个元素

语法：

```shell
spop key
```

`eg`:

```shell
spop letters
```

###### 有序集合

> 有序集合就是在集合类型的基础上将集合中的每个元素都关联到了一个分数，分数可以是相同的。

有序集合与列表有些类似，下面介绍它们的不同之处：

1. 列表类型是通过链表实现的，获取靠近两端的数据速度极快，而当元素增多以后，访问中间数据的速度会较慢，它合适实现如 "新鲜事","日志"等很少访问中间元素的应用，或者是时效性比较强的应用。

2. 有序集合类型是使用散列表和跳表(`skip list`)实现的，即使读取中间数据速度也很快(时间复杂度为`O(log(n))`)

3. 列表中不能简单地调整某个元素的位置，但是有序集合可以(通过更改元素关联的分数)

4. 有序集合要比列表类型更耗费内存

- 增加元素

语法：

```shell
zadd key score member [score member ...]
```

`zadd` 用来向有序集合加入一个元素和该元素的分数，如果该元素已存在则会用新的分数替换原有的分数，返回新加入到集合中的元素个数。

- 获得元素分数

```shell
zscore key member
```

- 获取排名在某个范围的元素列表

语法：

```shell
zrange key start stop [withscores]
zrevrange key start stop [withscores]
```

`zrevrange` 和 `zrange` 的唯一不同在于 `zrevrange` 是按照元素分数从大到小的顺序给出结果的。

- 获得指定分数范围内的元素

语法：

```shell
zrangebyscore key min max [withscores] [limit offset count]
```

第一个可选参数就和字面的意思一样，是带上分数返回，第二个可选参数表示在获得的元素列表的基础上向后偏移 `offset` 个元素，并且只获取前 `count` 个元素。

- 增加某个元素的分数

语法：

```shell
zincrby key increment member
```

`zincrby` 可以增加一个元素的分数，返回值是更改后的分数。

- 获取集合中元素的数量

语法：

```shell
zcard key
```

- 获得指定分数范围内的元素个数

语法：

```shell
zcount key min max
```

- 删除一个或多个元素

语法：

```shell
zrem key member [member ...]
```

- 按照排名范围删除元素

语法：

```shell
zremrangebyrank key start stop
```

- 按照分数范围删除元素

语法:

```shell
zremrangebyscore key min max
```

- 获得元素排名

语法：

```shell
zrank key member
zrevrank key member
```

`zrank` 会按照元素从小到大的顺序获得元素排名，相反， `zrevrank` 会按照从大到小的顺序排名。

- 计算有序集合的交集

语法:

```shell
zinterstore destination numkeys key [key ...] [weights weight [weight ...]] [aggregatesum|min|max]
```
