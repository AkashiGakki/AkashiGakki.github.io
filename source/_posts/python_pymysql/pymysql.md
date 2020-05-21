---
title: pymysql 操作关系型数据库
date: 2019-09-25
category: 
    - Python
    - 工具
tags:
    - Python
    - 工具
thumbnail: /images/bg-39.jpg

---

#### `pymysql` 操作关系型数据库

> 关系型数据库 `MySQL` 的数据存储操作。

<!-- more -->

##### 数据库连接

```python
import pymysql

# 创建一个连接，新建数据库并且输出版本

db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('Database version: ', data)
cursor.execute('create database spiders default character set utf8mb4')
db.close()
```

这里使用 `connect()` 方法声明一个 `MySQL` 连接对象 `db`，传入对应参数

连接成功后，调用 `cursor()` 方法获得 `MySQL` 的操作游标，利用游标来执行 `SQL` 语句，

执行操作使用 `execute()` 方法实现，首先获取了 `MySQL` 当前的版本，使用 `fetchone()` 获取结果的第一条数据，

然后创建一个数据库，命名为 `spider`，使用 `utf8mb4` 编码，

最终关闭数据库。

##### 创建表

```python
import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
sql = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))'
cursor.execute(sql)
db.close()
```

##### 插入数据

```python
import pymysql

id = '20190001'
user = 'Akashi'
age = 22

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
sql = 'insert into students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
```

这里最终需要执行对 `db` 对象的 `commit()` 方法才可以实现数据的插入，对于数据的插入、更新、删除操作都需要使用提交数据库才会保存生效。

我们还加入了异常处理，如果执行失败，打印异常并且执行数据回滚，保证了数据的一致性。

##### 事务

一个事务中的命令，要么全部执行，要么都不执行，这样确保了数据的一致性。事务包括原子性、一致性、隔离性、和持久性。

属性 | 解释
--- | ---
原子性 | 事务是一个不可分割的工作单位，事务中的所有操作，要么都执行，要么都不执行。
一致性 | 事务必须使数据库从一个一致性状态变到另一个一致性状态。
隔离性 | 一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
持久性 | 也称永久性，指一个事务一旦提交，它对数据库中的数据的改变就应该是永久性的，接下来的其他操作或故障不应该对其有任何影响。

下面对插入进一步的改进，使用字典进行传入，对 `sql` 语句做更好的封装：

```python
import pymysql

data = {
    'id': '20190002',
    'name': 'Asuka',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'insert into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
try:
    cursor.execute(sql, tuple(data.values()))
    print('Successful')
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
```

##### 更新数据

```python
sql = 'update students set age = %s where name = %s'
try:
    cursor.execute(sql, (21, 'Akashi'))
    db.commit()
except:
    db.rollback()
db.close()
```

如果数据存在，则更新数据，如果数据不存在，则插入数据：

```python
import pymysql

data = {
    'id': '20190001',
    'name': 'Akashi',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'insert into {table}({keys}) values({values}) on duplicate key update'.format(table=table, keys=keys, values=values)

update = ','.join([" {key} = %s".format(key=key) for key in data])

sql += update

try:
    cursor.execute(sql, tuple(data.values())*2)
    print('Successful')
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
```

##### 删除数据

```python
import pymysql

table = 'students'
condition = 'age > 20'

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)

try:
    cursor.execute(sql)
    print('Successful')
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
```

##### 查询数据

```python
import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students where age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
except Exception as e:
    print(e)
```

推荐逐条取数据:

```python
import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

sql = 'select * from students where age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except Exception as e:
    print(e)
```

利用内部的指针偏移获取查询结果。
