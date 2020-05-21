---
title: Python 上手指南之标准库
date: yyyy-mm-dd
category: Python
tags: Python
thumbnail: /images/asuka/asu-8.jpg

---

### 标准库

> 标准库：一些常用的模块。

<!-- more -->

#### 探索模块

- 使用 `dir`

要查明模块包含哪些东西，可以使用函数 `dir`，它列出对象的所有属性

```python
>>> import copy
>>> dir(copy)
['Error', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_copy_dispatch', '_copy_immutable', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', 'copy', 'deepcopy', 'dispatch_table', 'error']
```

为方便阅读，可以去掉下划线打头的不提供外部使用的函数：

```python
[n for n in dir(copy) if not n.startswith('_')]
```

- 变量 `__all__`

查看模块具体导入可用的内容

```python
>>> import copy
>>> copy.__all__
['Error', 'copy', 'deepcopy']
```

这样就可以看到模块 `copy` 可以使用的公有接口

- 使用 `help`

函数 `help` 提供一些你需要的信息

```python
>>> import sys
>>> help(sys)
```

- 查看文档

```python
>>> import sys
>>> print(sys.__doc__)
```

#### `sys`

访问和 `Python` 解释其相关的变量和函数。

函数 | 描述
--- | ---
`argv` | 获取命令行参数，返回值是List，第一个元素是程序本身路径
`exit([arg])` | 退出当前程序，可以通过可选参数指定返回值或错误消息
`modules` | 一个字典，将模块名映射到加载的函数
`path` | 一个列表，返回模块的搜索路径
`platform` | 返回操作系统的名称
`stdin` | 标准输入流
`stdout` | 标准输出流
`stderr` | 标准错误流
`version` | 解释器版本信息

1. `argv`

命令行执行，实现从外部传入参数

`python3 test.py arg1 arg2`

```python
import sys

print(sys.argv)
```

输出：

```python
['test.py', 'arg1', 'arg2']
```

2. `exit([arg])`

```python
import sys

print(sys.exit("运行结束."))
```

#### `os`

访问和操作系统相关的变量和函数。

模块 | 描述
--- | ---
`getcwd` | 获取当前的工作目录
`chdir` | 修改当前工作目录
`listdir` | 获取指定文件夹中的所有文件和文件夹组成的列表
`mkdir` | 创建一个目录/文件夹
`makedirs` | 递归创建文件夹
`rmdir` | 移除一个目录（必须是空目录）
`removedirs` | 递归删除文件夹
`rename` | 修改文件和文件夹的名称
`stat` | 获取文件的相关信息
`system` | 执行系统命令
`getenv` | 获取系统环境变量
`putenv` | 设置系统环境变量
`exit` | 退出当前执行命令，直接关闭当前操作
`unlink` | 删除文件
`open` | 新建文件

- `path` 模块

```python
>>> os.path.__all__
['normcase', 'isabs', 'join', 'splitdrive', 'split', 'splitext', 'basename', 'dirname', 'commonprefix', 'getsize', 'getmtime', 'getatime', 'getctime', 'islink', 'exists', 'lexists', 'isdir', 'isfile', 'ismount', 'expanduser', 'expandvars', 'normpath', 'abspath', 'samefile', 'sameopenfile', 'samestat', 'curdir', 'pardir', 'sep', 'pathsep', 'defpath', 'altsep', 'extsep', 'devnull', 'realpath', 'supports_unicode_filenames', 'relpath', 'commonpath']
```

函数 | 描述
--- | ---
`abspath()` | 将一个相对路径转化为绝对路径
`basename()` | 获取路径中的文件夹或者文件名称（只要路径的最后一部分）
`dirname()` | 获取路径中的路径部分(除去最后一部分)
`join()` | 将两个路径合并为一个路径
`split()` | 将一个路径切割成文件夹和文件名部分
`splitext()` | 将一个文件名切成名字和后缀两个部分
`getsize()` | 获取一个文件的大小
`isfile()` | 检测一个路径是否是一个文件
`isdir()` | 检测一个路径是否是一个文件夹
`getctime()` | 获取文件的创建时间
`getmtime()` | 获取文件的修改时间
`getatime()` | 获取文件的访问时间
`exists()` | 检测指定的路径是否存在 
`isabs()` | 检测一个路径是否是绝对路径
`islink()` | 检测一个路径是否是链接
`samefile()` | 检测两个路径是否指向同一个文件

参考： [os path](https://blog.csdn.net/jamfiy/article/details/88175302)

#### `fileinput`

迭代多个文件或流的内容行。

```python
>>> import fileinput
>>> fileinput.__all__
['input', 'close', 'nextfile', 'filename', 'lineno', 'filelineno', 'fileno', 'isfirstline', 'isstdin', 'FileInput', 'hook_compressed', 'hook_encoded']
```

#### `shutil`

拷贝、移动文件。

```python
>>> import shutil
>>> shutil.__all__
['copyfileobj', 'copyfile', 'copymode', 'copystat', 'copy', 'copy2', 'copytree', 'move', 'rmtree', 'Error', 'SpecialFileError', 'ExecError', 'make_archive', 'get_archive_formats', 'register_archive_format', 'unregister_archive_format', 'get_unpack_formats', 'register_unpack_format', 'unregister_unpack_format', 'unpack_archive', 'ignore_patterns', 'chown', 'which', 'get_terminal_size', 'SameFileError', 'disk_usage']
```

函数 | 描述
--- | ---
`copyfileobj(f1, f2)` | 将 `f1` 的数据覆盖 `copy` 给 `f2`，需打开文件
`copyfile(f1, f2)` | 不用打开文件，直接用文件名进行覆盖 `copy`
`copymode(f1, f2)` | 拷贝权限，内容组，用户，均不变
`copystat(f1, f2)` | 只拷贝了权限
`copy(f1, f2)` | 拷贝文件和权限都进行 `copy`
`copy2(f1, f2)` | 拷贝了文件和状态信息
`rmtree(dir)` | 可以递归删除目录下的目录及文件
`move(dir, f)` | 递归移动一个文件

参考： [shutil](https://www.cnblogs.com/xiangsikai/p/7787101.html)

#### `time`

获取时间、操作时间和日期以及设置它们格式。

时间的表示方式：

1. 时间戳 `timestamp` - 新纪元开始后的秒数(1970年1月1日00:00:00开始按秒计算的偏移量)

2. 格式化的时间字符串

3. 结构化时间元组 - `struct_time`

函数 | 描述
--- | ---
`localtime([secs])` | 将秒数(时间戳)转换为表示当地时间的结构化时间元组
`gmtime()` | 将时间戳转换为结构化时间
`mktime(tuple)` | 将结构化时间转换为时间戳
`sleep(ses)` | 休眠，什么都不做
`asctime([tuple])` | 将结构化时间转换为字符串
`strptime(string[, format])` | 将字符串转换为结构化时间
`time()` | 当前时间戳(浮点类型)
`ctime()` | 当前时间字符串
```
graph TB

A[struct_time] -->|strftime| B[Format string]

B[Format string] -->|strptime| A[struct_time]

A[struct_time] -->|mktime| C[Timestamp]

C[Timestamp] -->|localtime, gmtime| A[struct_time]

```

1. 当前时间戳 - `time()`

```python
>>> import time
>>> time.time()
1573438880.298209
```

2. 当前时间字符串 - `ctime()`

```python
>>> import time
>>> time.ctime()
'Mon Nov 11 10:21:08 2019'
```

3. 当前结构化时间元组

```python
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=11, tm_hour=10, tm_min=23, tm_sec=28, tm_wday=0, tm_yday=315, tm_isdst=0)
```

4. 休眠 

```python
>>> import time
>>> time.sleep(10)
```

#### `datetime`

`tiem` 模块的高级封装，接口更加直观。

首先查看模块下面的类：

```python
import datetime
>>> [n for n in dir(datetime) if not n.startswith('_')]
['MAXYEAR', 'MINYEAR', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

`datetime` 模块中包含的类：

类名 | 功能说明
--- | ---
`date` | 日期对象,常用的属性有 `year`, `month`, `day`
`time` | 时间对象
`datetime` | 日期时间对象,常用的属性有 `hour`, `minute`, `second`, `microsecond`
`datetime_CAPI` | 日期时间对象C语言接口
`timedelta` | 时间间隔，即两个时间点之间的长度
`tzinfo` | 时区信息对象

- `datetime`

1. 获取当前结构化时间 - `today()`、`now()`

```python
>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2019, 11, 11, 11, 9, 38, 648690)
>>> datetime.datetime.now()
datetime.datetime(2019, 11, 11, 11, 9, 43, 735714)
```

可用函数：

```python
>>> import datetime
>>> [n for n in dir(datetime.datetime) if not n.startswith('_')]
['astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
```

#### `random`

生成随机数。

```python
>>> import random
>>> random.__all__
['Random', 'seed', 'random', 'uniform', 'randint', 'choice', 'sample', 'randrange', 'shuffle', 'normalvariate', 'lognormvariate', 'expovariate', 'vonmisesvariate', 'gammavariate', 'triangular', 'gauss', 'betavariate', 'paretovariate', 'weibullvariate', 'getstate', 'setstate', 'getrandbits', 'choices', 'SystemRandom']
```

函数 | 描述
--- | ---
`random()` | 返回一个 `[0, 1)` 的随机实数
`uniform(a, b)` | 返回一个 `[a, b]` 的随机实数
`randrange([start], stop, [step])` | 从 `range(start, stop, step)` 中随机选择一个数
`choice(seq)` | 从序列中随机选择一个元素
`shuffle(seq[, random])` | 就地打乱序列 `seq`
`sample(seq, n)` | 从序列 `seq` 中随机选择 `n` 个不同的元素值

#### `json`

序列化。

```python
>>> import json
>>> json.__all__
['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecodeError', 'JSONEncoder']
```

函数 | 描述
--- | ---
`dump(fileobj)` | 字典转成 `json` 字符串，用于文件
`dumps(str)` | 字典转成 `json` 字符串
`load(fileobj)` | `json` 字符串转成字典，用于文件
`loads(str)` | `json` 字符串转成字典

#### `re`

正则表达式。

```python
>>> import re
>>> re.__all__
['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'findall', 'finditer', 'compile', 'purge', 'template', 'escape', 'error', 'Pattern', 'Match', 'A', 'I', 'L', 'M', 'S', 'X', 'U', 'ASCII', 'IGNORECASE', 'LOCALE', 'MULTILINE', 'DOTALL', 'VERBOSE', 'UNICODE']
```

函数 | 描述
--- | ---
`match(pattern, string[, flags])` | 在字符串开头匹配模式
`search(pattern, string[, flags])` | 在字符串中查找模式
`sub(pat, repl, string[, count=0])` | 将字符串中与模式 `pat` 匹配的子串都替换为 `repl`
`split(pattern, string[, maxsplit=0])` | 根据模式来分割子串
`findall(pattren, string)` | 返回一个列表，其中包含字符串中所有与模式匹配的子串
`compile(pattern[, flags])` | 根据包含正则表达式的字符串创建模式对象

#### `logging`

日志。

```python
>>> import logging
>>> logging.__all__
['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'NOTSET', 'NullHandler', 'StreamHandler', 'WARN', 'WARNING', 'addLevelName', 'basicConfig', 'captureWarnings', 'critical', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogger', 'getLoggerClass', 'info', 'log', 'makeLogRecord', 'setLoggerClass', 'shutdown', 'warn', 'warning', 'getLogRecordFactory', 'setLogRecordFactory', 'lastResort', 'raiseExceptions']
```

#### `collections`

内建集合模块，提供多个集合类。

```python
>>> import collections
>>> collections.__all__
['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList', 'UserString', 'Counter', 'OrderedDict', 'ChainMap']
```

函数 | 描述
--- | ---
`namedtuple()` | 创建一个自定义的 `tuple` 对象
`deque()` | 高效实现插入和删除操作的双向列表，适合用于队列和栈
`defaultdict()` | 字典，当 `key` 不存在时，返回一个默认值
`OrderedDict()` | 有序字典
`Counter()` | 计数器

1. `namedtuple`

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
```

2. `deque`

```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```

参考：[collections](https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456)
