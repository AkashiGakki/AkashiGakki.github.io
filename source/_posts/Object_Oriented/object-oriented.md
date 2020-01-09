---
title: 面向对象
date: yyyy-mm-dd
category: 
    - Java
tags:
    - Java
    - 面向对象
thumbnail: /images/bg-33.jpg

---

#### 面向对象

> 定义简单 `Java` 类，`static` 与 `this` 的理解。

<!-- more -->

##### 简单 `Java` 类

基本要求：

1. 类名称必须存在意义

2. 类中的所有属性必须 `private` 封装，封装之后的属性必须提供 `setter`、`getter`

3. 类中可以提供任意多个构造方法，但是必须保留一个无参构造方法

4. 类中不允许出现任何输出语句，所有信息输出必须交给被调用处输出

5. 类中需要提供一个可以取得对象完整信息的方法，一般叫做 `getInfo()`，返回 `String` 型数据

- 创建 `Emp` 类

```java
public class Emp {
    private int empno;          // 编号
    private String ename;       // 姓名
    private String job;         // 职位
    private double sal;         // 工资
    private double comm;        // 奖金

    // 定义一个无参构造方法
    public Emp() {
    }

    // 有参构造
    public Emp(int empno, String ename, String job, double sal, double comm) {
        this.empno = empno;
        this.ename = ename;
        this.job = job;
        this.sal = sal;
        this.comm = comm;
    }

    public int getEmpno() {
        return empno;
    }

    public void setEmpno(int empno) {
        this.empno = empno;
    }

    public String getEname() {
        return ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public double getSal() {
        return sal;
    }

    public void setSal(double sal) {
        this.sal = sal;
    }

    public double getComm() {
        return comm;
    }

    public void setComm(double comm) {
        this.comm = comm;
    }

    public String getInfo() {
        return  "empno: " + empno + '\n' +
                "ename: " + ename + '\n' +
                "job: " + job + '\n' +
                "sal: " + sal + '\n' +
                "comm: " + comm;
    }
}
```

- 调用

```java
public class Main {
    public static void main(String[] args) {
        Emp emp = new Emp(7936, "akashi", "Engineer", 5000, 3000);
        System.out.println(emp.getInfo());
    }
}
```

##### 数组

> 数组属于引用类型，所以在数组的操作过程中，以有内存分配问题。

- 声明并开辟数组

```java
数据类型 数组名称 [] = new 数据类型 [长度];
数据类型 [] 数组名称 = new 数据类型 [长度];
```

- 分步完成

```java
数据类型 [] 数组名称 = null;    // 声明
数组名称 = new 数据类型 [长度]; // 开辟空间
```

内存分配中和对象保存唯一的区别在于：对象中的堆内存是保存属性，而数组中的堆内存保存的是一组信息。

数组长度不允许改变，所以使用时需注意数组越界。

不能使用未开辟空间的数组。

- 初始化

```java
数据类型 [] 数组名称 = {value, value, ....};
数据类型 [] 数组名称 = new 数据类型 [] {value, value, ....};
```

`eg`:

```java
int[] data = new int[] {1, 2, 3, 4};
```

###### 二维数组

```java
public class Array {
    public static void main(String[] args) {
        int[][] data = new int[][] {
                {1, 2, 3}, {4, 5, 6}, {7, 8, 9}
        };

        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[i].length; j++) {
                System.out.print(data[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
```

从二维数组开始其实就进入了一个多维数组的概念范畴，一维数组表示一行数据，二维数组描述一张表的数据，三维数据就可以描述一个三维图形的结构，也就是说数组维度越多概念越复杂。在开发中只有很少的情况会涉及多维开发，尽量使用一维数组来进行简洁高效的开发。

###### 数组操作

- 数组冒泡排序

```java
public class BubbleSort {
    public static void sort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length - 1; j++) {
                if (array[j] > array[j+1]) {
                    int temp =array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
        show(array);
    }

    private static void show(int[] array) {
        for (int i : array) {
            System.out.print(i + "\t");
        }
    }

    public static void main(String[] args) {
        int[] array = new int[] {2, 1, 9, 0, 5, 3, 7, 4, 63, 8, 6};
        BubbleSort sorter = new BubbleSort();
        sorter.sort(array);
    }
}
```

- 数组转置

```java
public class Reverse {
    public static void reverse(int[] array) {
        int N = array.length;
        for (int i = 0; i < N/2; i++) {
            int temp = array[i];
            array[i] = array[N-1-i];
            array[N-1-i] = temp;
        }
        show(array);
    }

    private static void show(int[] array) {
        for (int i : array) {
            System.out.print(i + "\t");
        }
    }

    public static void main(String[] args) {
        int[] array = new int[] {1, 2, 3, 4, 5, 6, 7};
        Reverse sorter = new Reverse();
        sorter.reverse(array);
    }
}
```

###### 对象数组

数组是引用类型，而类也是引用类型，如果是对象数组的话表示一个引用类型里面嵌套其他的引用类型。

- 对象数组动态初始化

```java
类名称 [] 对象数组名称 = new 类名称 [长度];
```

- 对象数组的静态初始化

```java
类名称 [] 对象数组名称 = new 类名称[] {实例化对象, 实例化对象,....};
```

`eg`:

```java
public static void main(String[] args) {
    Book[] books = new Book[] {
            new Book("Java"), new Book("Python"), new Book("JavaScript")
    };

    for (int i = 0; i < books.length; i++) {
        books[i].getInfo();
    }
}
```

##### `String` 类的基本概念

> `String` 是字符串的描述类型，虽然 `String` 本身不属于引用数据类型，但是可以像基本数据类型那要直接赋值，是一个特殊的类。

###### 常用 `API`

`public class String` |||
--- | --- | ---
| `String()` | 创建一个空字符串
`int` | `length()` | 获取字符串长度
`int` | `charAt(int i)` | 获取第 `i` 个字符 
`int` | `indexOf(String p)` | 获取 `p` 第一次出现的位置(没有则返回 `-1`)
`int` | `indexOf(String p, int i)` | 获取 `p` 在 `i` 个字符后第一次出现的位置(没有则返回 `-1`)
`String` | `concat(String t)` | 将 `t` 附在该字符串末尾(字符串连接)
`String` | `sbustring(int i, int j)` | 使用字符串的子字符串(第 `i` 个字符到第 `j-1` 个字符)
`String[]` | `split(String delim)` | 使用 `delim` 分隔符切分字符串
`int` | `compareTo(String t)` | 比较字符串
`boolean` | `equals(String t)` | 该字符串的是和 `t` 的值是否相同
`int` | `hashCode()` | 散列值
`boolean` | `contains(String t)` | 判断字符串是否存在
`String` | `trim()` | 去掉字符串两边空格
`String` | `replaceAll(String t, String rep_t)` | 用新的内容替换全部旧的内容

##### `this` 关键字

> `this` 可以完成 `3` 中方法：调用本类属性，调用本类方法，表示当前对象。

###### 调用本类属性

```java
public class Book {
    private String title;
    private double price;

    public Book(String title, double price) {
        this.title = title;
        this.price = price;
    }
}
```

这里为类中的属性赋值，如果参数名与属性名相同，在 `Java` 里会采用 `就近取用` 的原则，若没有对属性进行 `this` 的指定，就不能标记为属性，函数会把形参里面的值赋给形参，就无法对属性赋值了。

用 `this` 表示本类的属性，与形参区分，在名称相同的情况下也可以明确定位并赋值。

###### 调用本类方法

`this` 本质上就是明确进行本类结构的标记，而除了访问类中的属性外，也可以进行类中的方法调用。

```java
public class Book {
    public void getInfo() {
        this.show();
        System.out.println("图书名称：" + title + "，价格：" + price);
    }

    public void show() {
        System.out.println("this 调用本类方法");
    }
}
```

```java
public class Book {
    private String title;
    private double price;

    public Book() {
        System.out.println("new 了一个新对象");
    }

    public Book(String title) {
        this();
        this.title = title;
    }

    public Book(String title, double price) {
        this();
        this.title = title;
        this.price = price;
    }

    public void getInfo() {
        System.out.println("图书名称：" + title + "，价格：" + price);
    }
}
```

###### 表示当前对象

当前对象就是指当前正在调用的类中的方法的实例化对象。


##### 数据表与 简单 `Java` 类映射

> 简单 `Java` 类在实际的开发中都是根据其数据表的定义来实现的。

下面我们需要实现主表与部门表的对应关系，即：一个部门可以有多个员工

我们使用一个外键 `deptno` 进行关联。

`Dept`:

```java
public class Dept {
    private int deptno;
    private String dname;
    private String loction;

    public Dept() {
    }

    public Dept(int deptno, String dname, String loction) {
        this.deptno = deptno;
        this.dname = dname;
        this.loction = loction;
    }

    public int getDeptno() {
        return deptno;
    }

    public void setDeptno(int deptno) {
        this.deptno = deptno;
    }

    public String getDname() {
        return dname;
    }

    public void setDname(String dname) {
        this.dname = dname;
    }

    public String getLoction() {
        return loction;
    }

    public void setLoction(String loction) {
        this.loction = loction;
    }

    public String getInfo() {
        return  "deptno = " + deptno + '\n' +
                "dname = " + dname + '\n' +
                "loction = " + loction;
    }
}
```

`Emp`:

```java
public class Emp {
    private int empno;          // 编号
    private String ename;       // 姓名
    private String job;         // 职位
    private double sal;         // 工资
    private double comm;        // 奖金
    private int deptno;         // 部门编号

    // 定义一个无参构造方法
    public Emp() {
    }

    // 有参构造
    public Emp(int empno, String ename, String job, double sal, double comm, int deptno) {
        this.empno = empno;
        this.ename = ename;
        this.job = job;
        this.sal = sal;
        this.comm = comm;
        this.deptno = deptno;
    }

    public int getEmpno() {
        return empno;
    }

    public void setEmpno(int empno) {
        this.empno = empno;
    }

    public String getEname() {
        return ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public double getSal() {
        return sal;
    }

    public void setSal(double sal) {
        this.sal = sal;
    }

    public double getComm() {
        return comm;
    }

    public void setComm(double comm) {
        this.comm = comm;
    }

    public int getDeptno() {
        return deptno;
    }

    public void setDeptno(int deptno) {
        this.deptno = deptno;
    }

    public String getInfo() {
        return  "empno: " + empno + '\n' +
                "ename: " + ename + '\n' +
                "job: " + job + '\n' +
                "sal: " + sal + '\n' +
                "comm: " + comm + '\n' +
                "deptno: " + deptno;
    }
}
```

`Main`:

```java
public class Main {
    public static void main(String[] args) {

        Emp emp1 = new Emp(7936, "akashi", "Engineer", 5000, 3000, 10);
        Emp emp2 = new Emp(7937, "asuka", "Engineer", 5000, 3000, 20);

        Dept dept = new Dept(10, "IT", "Chengdu");
        emp2.setDeptno(10);

        System.out.println("=========================");
        System.out.println(emp1.getInfo());
        System.out.println("=========================");
        System.out.println(emp2.getInfo());
        System.out.println("=========================");
        System.out.println(dept.getInfo());
    }
}
```

##### `static` 关键字

> `static` 关键字可以用于定义属性及方法。

###### `static` 定义属性

如果类中的属性希望定义为公共属性(所有对象都可以使用的属性)，则可以在声明属性前加上 `static` 关键字。

`eg`:

```java
static String pub = "人民邮电出版社";
```

既然 `static` 是一个公共属性的概念，那么如果只是简单的由一个对象去修改 `static` 的做法不是很适合，最好的做法是由类来进行访问。

```java
Book.pub = "电子工业出版社";
```

`static` 属性与非 `static` 属性最大的一个区别，所有非 `static` 属性必须产生实例化对象才可以进行访问，但是 `static` 属性不受实例化对象的控制，在没有实例化对象产生的情况下，也可以使用 `static` 属性。

在实际的开发中， `static` 定义的属性出现几率并不是很高。

###### `static` 定义方法

使用 `static` 定义的方法也可以在没有实例化对象的情况下由类名称直接进行调用。

- `static` 方法不能直接访问非 `static` 属性或方法，只能调用 `static` 属性或方法。

- 非 `static` 方法可以访问 `static` 的属性和方法，不受任何限制。

当一个类中没有属性产生，就没有必要开辟堆内存保存属性内容了，这时候就可以考虑类中的方法使用 `static` 进行声明。

###### 主方法

- `public`

主方法是程序的入口，所以这个方法对任何操作都一定是可见的，所以就必须使用 `public`

`类修饰符`

访问包位置 | `private` | `protected` | `public`
--- | --- | --- |---
本类 | 可见 | 可见 | 可见
同包其他类或子类 | 不可见 | 可见 | 可见
其他包的类或子类 | 不可见 | 不可见 | 可见

- `static`

证明此方法是由类名称调用的

- `void`

没有返回值

- `main`

是一个系统规定好的方法名称，不能修改

- `String[] args`

指的是程序运行时传递的参数

