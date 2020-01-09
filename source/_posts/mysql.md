---
title: SQL 基础笔记
date: yyyy-mm-dd
category:
    - 数据库
tags:
    - 数据库
    - MySQL
thumbnail: /images/bg-14.jpg

---

#### `SQL` 基础笔记

> 对 `SQL` 语句的基础复习

<!-- more -->

开始学习之前，我们需要正确安装 `MySQL`， 各系统的安装稍有差异，这里不另行赘述，自行百度正确的安装姿势。以下内容以我的环境为主：

- 系统：`Mac OS`
- 包管理工具：`Homebrew`
- `MySQL` 版本：`8.0.16`

##### 连接 `MySQL`

###### 确认正确安装

在终端输入

```shell
mysql --version
```

若可以正确打印安装的 `MySQL` 版本，则安装成功

###### 启动/终止服务

`Mac` 下使用 `Homebrew` 包管理工具可以运行

```shell
brew services start mysql
```

和

```shell
brew services restart mysql
```

其他系统可以尝试

```shell
net start mysql5
```

和

```shell
net stop mysql5
```

或者是

```shell
service mysql start
```

和

```shell
service mysql stop
```

来进行启动和关闭服务。

###### 连接到服务器

确保服务启动状态下终端运行

```shell
mysql -uroot -p
```

以上命令 `mysql` 代表客户端命令，`-u` 后边跟连接数据库的用户，这里是 `root`，`-p` 表示输入密码，回车后输入密码即可。`MySQL` 默认用户为 `root`，密码为空，如果没有修改，直接回车就可以连接到 `MySQL` 服务器，也可以使用下面的命令实现快速登录：

```sql
mysql -uroot
```

##### `DDL` 语句

> 数据定义语言，简单来说，就是对数据库的内部对象进行创建、删除、修改等操作的语言。

###### 创建数据库

语法：

```sql
CREATE DATABASE dbname;
```

现在，我们来创建一个数据库 `demo`:

```sql
create database demo;
```

注意，如果数据库名称已存在，系统将不再允许创建同名的数据库，这时，我们可以删除已存在的数据库或另取一个名称再创建。

这样，一个数据库就创建成功了。我们可以通过以下命令查看：

```sql
show databases;     // 不要忘了分号(;)
```

注意，是 `databases` 不是 `database`；还有 `sql` 以分号结束。

查看数据库之后，可以选择要操作的数据库，使用命令：

```sql
USE dbname;
```

这里我们查看刚刚创建的数据库 `demo`:

```sql
use demo;
```

然后再查看数据库中创建的所有数据表：

```sql
show tables;
```

因为我们创建的是一个空数据库，里面还没有表。

###### 删除数据库

语法：

```sql
DROP DATABASE dbnaem;
```

这里我们删除刚创建的 `demo` 数据库：

```sql
drop database demo;
```

###### 创建表

语法：

```sql
CREATE TABLE tablename(
    name type constraints,
    name type constraints,
    ....
); 
```

`constraints` （约束）可以为空，不写就行。一般的约束条件有：主键约束（`primary key`），外键约束（`foreign key`），唯一约束（`unique`），非空约束（`not null`）和默认值（`default`）

约束 | 描述
--- | ---
主键约束（`primary key`） | 主键约束列不允许重复，也不允许出现空值。相当于唯一约束+非空约束，每个表最多只允许一个主键
外键约束（`foreign key`） | 外键约束是保证一个或两个表之间的参照完整性，外键是构建于一个表的两个字段或是两个表的两个字段之间的参照关系
唯一约束（`unique`） | 指定`table`的列或列组合不能重复，保证数据的唯一性
非空约束（`not null`） | 确保当前列的值不为空值
默认值（`default`） | 可以设置一个当前字段的默认值

现在我们实际创建一个新的表，首先，创建一个数据库:

```sql
create database emp;
```

然后，使用它：

```sql
use emp;
```

接下来，就是创建表：

```sql
create table emp(ename varchar(10), hiredate date, sal decimal(10, 2), deptno int(2));
```

这时，我们便创建了一张新表（`emp`)，我们可以查看表的定义：

```sql
DESC tablename;
```

即

```sql
desc emp;
```

如果需要更全面的表信息，可以使用 `SQL` 语句：

```sql 
SHOW CREATE TABLE tablename \G;
```

我们来尝试一下：

```sql
show create table emp \G
```

这里的"`\G`"的含义是使记录能够按照字段竖向排列，以便更好地显示内容，也可以选择不写，不过一旦选择传入，切记是大写的，不然无效。

###### 删除表

语法：

```sql
DROP TABLE tablename;
```

可自行尝试。

###### 修改表

> 对于已经创建好的表，尤其是已经有大量数据的表，如果需要做一些结构上的改变，可以先将表删除（`drop`），然后再重新定义表，这样做没有问题，但是就必须重新对数据进行加载，因此，大多数情况下，表结构的更改都使用 `alter table` 语句，以下是一些常用命令。

- 修改表类型

语法如下：

```sql
ALTER TABLE tablename MODIFY [COLUMN] column_definition [FIRST|AFTER col_name];
```

接下来我是实际进行尝试：

```sql
alter table emp modify ename varchar(20);
```

重新查看表结构，可以发现我们把 `ename` 字段的类型从 `varchar(10)` 修改成了 `varchar(20)`。

```sql
desc emp;
```

- 增加表字段

语法如下：

```sql
ALTER TABLE tablename ADD [COLUMN] column_definition [FIRST|AFTER col_name];
```

例如，我们增加一个字段 `age`，类型为 `int(3)`：

```sql
alter table emp add age int(3);
```

可以自己利用`desc`语句查看一下表结构的变化。

- 删除表字段

语法如下：

```sql
ALTER TABLE tablename DROP [COLUMN] col_name;
```

以下，我们删除 `age` 字段：

```sql
alter table emp drop age;
```

自行查看表结构的变化。

- 更改字段名

语法如下：

```sql
ALTER TABLE tablename CHANGE [COLUMN] old_col_name column_definition [FIRST|AFTER col_name];
```

我们先将刚才删除的字段添加回来：

```sql
alter table emp add age int(3);
```

然后修改名称为 `age_1`，同时修改字段类型为 `int(4)`:

```sql
alter table emp change age age_1 int(4);
```

查看表结构的变化：

```sql
desc emp;
```

注意：`change` 和 `modify` 都可以修改表的定义，不同的是 `change` 后面需要写两次列名，但 `change` 的优点是可以修改列名称， `modify` 则不能。

- 修改字段排列顺序

前面介绍的方法都有一个可选项， `first|after cloumn_name`，这个选项可以修改字段在表中的位置。 `add` 默认是加在表的最后位置，`change` 和 `modify` 默认不会改变字段的位置。

下面我们将添加 `birth` 字段在 `ename` 之后：

```sql
alter table emp add birth date after ename;
```

自行查看。

- 更改表名

语法如下：

```sql
ALTER TABLE tablename RENAME [TO] new_name;
```

我们将表名 `emp` 改为 `emp1`:

```sql
alter table emp reanme emp1;
```

查看变化：

```sql
show tables;
```

##### `DML` 语句

> `DML` 即数据操作语句，是指对数据库中表记录的操作，主要包括插入(`insert`)、更新(`update`)、删除(`delete`)和查询(`select`)，是开发人员日常使用最频繁的操作。

开始之前，先将表进行调整，将表名改回 `emp`，并且删除 `age_1` 字段：

```sql
alter table emp1 rename emp;
alter table emp drop age_1;

```

###### 插入记录

语法如下：

```sql
INSERT INTO tablename (field_1, field_2,..., field_n) VALUES(value_1, value_2,...,value_n);
```

实际尝试：

```sql
insert into emp (ename, birth, hiredate, sal, deptno) values('akashi', '1997-09-28', '2019-08-01', '5000', 01);
```

也可以不指定字段名，但是 `value` 后面的顺序要和字段的排列顺序一致：

```sql
insert into emp values('asuka', '1998-08-10', '2019-08-01', '5000', 1);
```

可以通过以下语法进行查看插入情况：

```sql
select * from emp;
```

###### 更新记录

语法如下：

```sql
UPDATE tablename SET field_1 = value_1, field_2 = value_2,...,field_n = value_n [WHERE CONDITION]
```

例如:

```sql
update emp set sal = '6000' where ename = 'asuka';
```

查看：

```sql
select * from emp;
```

###### 删除记录

语法如下：

```sql 
DELETE FROM tablename [WHERE CONDITION]
```

例如：

```sql
delete from emp where ename = 'akashi';
```

使用别名的一个参考例子：

```sql
delete a, b from emp a, dept b where a.depton = b.depton and a.depton = 3;
```

###### 查询记录

其实上面有使用过最基础的查询，语法如下：

```sql 
SELECT * FROM tablename [WHERE CONDITION]
```

即：

```sql
select * from emp;
```

`*` 表示全部，等价于：

```sql
select ename, birth, hiredate, sal, deptno from emp;
```

注意：考虑到性能和效率问题，在大型的数据库查询中，并不提倡使用 `*` 来查询，要养成良好的习惯。

- 查询不重复的记录

> 有时候需要将表中的记录去掉重复后显示出来，可以用 `distinct` 关键字来实现。

一个例子：

```sql
select distinct depno from emp;
```

- 条件查询

> 在很多情况下，不需要查询全部记录，而只是需要根据限定条件来查询一部分的数据，用 `where` 来实现。

一个例子：

```sql
select ename, birth, hiredate, sal, deptno from emp where deptno = 1;
```

- 排序和限制

> 当需要取出按照某个字段进行排序后的记录结果集，可以使用关键字 `order by` 来实现。

语法如下：

```sql
SELECT * FROM tablename [WHERE CONDITION] [ORDEY BY field_1 [DESC|ASC],...,field_2 [DESC|ASC]]
```

其中，`desc` 和 `asc` 排序顺序关键字， `desc` 表示按照字段进行降序排序， `asc` 表示升序排序，如果不写，默认是升序。

一个例子：

```sql
select ename, birth, hiredate, sal, deptno from emp order by sal;
```

稍微再复杂一点：(先按部门升序，再按奖金降序排序)

```sql
select ename, birth, hiredate, sal, deptno from emp order by deptno, sal desc;
```

对于排序后的记录，如果只希望显示部分，可以使用 `limit` 关键字。

语法如下：

```sql
SELECT ... [LIMIT offset_start, row_count]
```

其中， `offset_start` 表示记录的起始偏移量， `row_count` 表示显示的行数。默认起始偏移量为 `0`，这时，实际显示的就是前 `n` 条记录。

具体例子：

```sql
select ename, birth, hiredate, sal, deptno from emp order by sal limit 3;
```

这里显示了 `3` 条记录。

另一个例子：

```sql
select ename, birth, hiredate, sal, deptno from emp order by sal limit 1, 3;
```

表示排序后从第`2`条记录开始，显示`3`条记录。

`limit` 经常和 `order by` 一起配合使用，来进行记录的分页显示。

- 聚合

语法如下：

```sql 
SELECT [field_1, field_2,...,field_n] fun_name
FROM tablenaem
[WHERE where_contition]
[GROUP BY field_1, field_2,...field_n
[WITH ROLLUP]]
[HAVING where_contition]
```

参数说明：

- `fun_naem` 表示要做的聚合参数，也就是聚合函数，常用的有 `sum`-求和, `count(*)`-记录数, `max`-最大值, `min`-最小值。

- `group by` 关键字表示要进行分类聚合的字段。

- `with rollup` 是可选字段（在`[]`里面表示可选参数），表明是否对分类聚合后的结果进行再汇总。

- `having` 关键字表示对分类后的结果再进行条件的过滤。

注意：`having` 和 `where` 的区别在于， `having` 是对聚合后的结果进行再过滤，而 `where` 是在聚合前就对记录进行过滤， 如果逻辑允许，我们尽可能的用 `where` 先过滤记录， 因为这样结果集会减小，提高聚合效率，最后再根据情况看是否用 `having` 进行再过滤。


统计人数大于 `1` 的部门：

```sql
select deptno count(1) from emp group by deptno having count(1) > 1;
```

再看一些具体的函数：

```sql
select sum(sal), max(sal), min(sal) from emp;
```

- 表连接

> 当需要同时显示多个表中的字段时，就可以通过表连接来实现。表连接分为外连接和内连接，他们最主要的区别是，内连接仅选出两张表中相互匹配的记录；而外连接会选出其他不匹配的记录。我们最常用的是内连接。

一个例子(内连接)：

```sql
select ename, deptname from emp.dept where emp.deptno = dept.deptno;
```

外连接又分为左连接和右连接：

左连接： 包含所有的左边表中的记录甚至是右边表中没有和它匹配的记录。

右连接： 包含所有的右边表中的记录甚至是左边表中没有和它匹配的记录。

左连接：

```sql
select ename, deptname from emp left join dept on emp.deptno = dept.deptno;
```

右连接：

```sql
select ename, deptname from emp right join emp on dept.deptno = emp.deptno;
```

两者效果相同，可以相互转化。


- 子查询

> 有些情况下，查询时需要的条件是另外一个 `select` 语句的结果，这个时候，就需要子查询。用于子查询的关键字主要包括： `in`, `not in`, `=`, `!=`, `exists`, `not exists` 等。

一个例子：

```sql
select * from emp where deptno in (select deptno from dept);
```

如果子查询的记录唯一，还可以用 `=` 代替 `in`:

```sql
select * from emp where deptno = (select deptno from dept);
```

- 记录联合

> 我们常常需要将两个表的数据按一定的查询条件查询出来以后，将结果合并到一起显示出来，这时候，需要 `union` 和 `union all` 关键字来实现。

语法如下：

```sql 
SELECT * FROM t1
UNION | UNION ALL
SELECT * FROM t2
...
UNION | UNION ALL
SELECT * FROM tn
```

`union` 和 `union all` 的主要区别是 `union all` 是直接把结果合并在一起，而 `union` 是在 `union all` 的基础上进行了一次 `distinct`，去除了重复的记录。

一个例子：

```sql
select deptno from emp
union all
select deptno from dept;
```

去重：

```sql
select deptno from emp
union 
select deptno from dept;
```


##### `DCL` 语句

> `DCL` 即数据控制语句，主要是DBA用来管理系统中的对象权限时使用，一般开发人员很少使用。

###### 创建数据库用户，添加权限

```sql
create user 'akashi'@'localhost' identified by '123';
```

```sql
grant select, insert on emp.* to 'akashi'@'localhost';
```

###### 收回权限

```sql
revoke insert on emp.* from 'akashi'@'localhost';
```


##### 实战

一些实例：

```sql
-- 1. 查询第三个字母为A的员工记录
select ename from emp where ename like '__A%';

-- 2. 输出员工人数大于等于5的部门
select deptno, count(empno) 
from emp 
group by deptno 
having count(empno) >= 5;

-- 3. 以部门编号为统计单位，统计(聚合函数)
select deptno, count(empno), max(sal), min(sal), avg(sal)
from emp
group by deptno;

-- 4. 查询没有奖金的员工信息
-- select * from emp where comm = 'NULL'
select * from emp
where comm = 0 or comm is NULL;

-- 如果字段为空，字段置零，如果为零，同样置零
select * from emp 
where ifnull(comm, 0) = 0;

-- 5. 不重复的部门编号
select distinct deptno from emp

-- 6. 查询工资和奖金的和大于2000的员工信息(注意：奖金为空时，不参与运算)
select * from emp 
where ifnull(sal, 0) + ifnull(comm, 0) > 2000

-- 7. 公式化：分页查询，n为开始的下标，m为显示的个数
select * from emp limit n, m;

-- select * from emp limit （当前页码数-1）* 每页显示条数, 每页显示条数(实时分页，不再利用缓存，满足高并发的数据实时变化)
select * from emp limit （index-1）* pageSize, pageSize;

-- 8. 添加
-- 语法规则：
-- 主键（自增长）
-- 字段的类型
-- 字段的长度
-- 日期（表单传入（应用程序）、系统传入、数据库获取）
-- 实体间的依赖关系
-- 添加字段顺序

insert into emp(empno, ename, job, hiredate, sal, comm, deptno) 
values(9999, 'AKASHI', 'STUDENT', now(), 5000.56, 1000, 40);

insert into emp(ename, job, hiredate, sal, comm, deptno) 
values('AKASHI', 'STUDENT', now(), 5000.56, 1000, 40);

delete from emp where empno = 10000;
-- 增删改===> 注意事务的提交和回滚
-- 所有的关系型数据库，存在自动提交和手动提交；Oracle需要手动提交，MySQL自动提交，无需commit，rollback；

-- 9. 删除
-- 考虑临界值
-- 先检索语句确认是否满足要求，再删除
select * from emp where sal >= 800 and sal <= 3000;
delete from emp where sal >= 800 and sal <= 3000;
delete from emp where sal between 800 and 3000;

-- 10. 更新
-- 先检索
-- 考虑非空
update emp 
set sal = ifnull(sal, 0) + 1000, comm = ifnull(comm, 0) + 500
where ifnull(comm,0) = 0;

```

