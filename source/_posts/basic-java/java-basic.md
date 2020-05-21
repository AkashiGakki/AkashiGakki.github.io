---
title: Java 基本概念
date: 2019-9-11
category: 
    - Java
tags:
    - Java
    - 基础
thumbnail: /images/bg-30.jpg

---

#### `Java` 基本概念

> 从 `Java` 语法开始，理解面向对象的基本概念。

<!-- more -->

##### 数据类型划分

- 数据类型
    - 基本数据类型
        - 数值型
            - 整数类型(`byte`、`short`、`int`、`long`)
            - 浮点类型(`float`、`double`)
        - 字符型(`char`)
        - 布尔型(`boolean`)
    - 引用数据类型
        - 类(`class`)
        - 接口(`interface`)
        - 数组(`[]`)

##### 方法的定义

> 方法也被称为函数，是一段可以重复调用的代码块。

方法的主要功能是封装可执行的一段代码，这样不仅仅可以进行重复调用，更可以方便的实现代码的维护，定义如下：

```
public[权限修饰符] static[属性] 返回值类型[关键字] 方法名称(参数类型, 参数变量, ...) 抛出异常类型 {
    方法体 (本方法要执行的若干操作);
    [return [返回值];]
}
```

##### 方法重载

> 方法重载是指方法名称相同，参数的类型不同或个数不同，调用的时候将会按照传递的参数类型和个数完成不同方法体的执行。

```java
public class FuncOverload {
    /**
     * 实现两个整型类型的相加
     * @param x
     * @param y
     * @return
     */
    public static int add(int x, int y) {
        return x + y;
    }

    /**
     * 实现三个整型类型的相加
     * @param x
     * @param y
     * @param z
     * @return
     */
    public static int add(int x, int y, int z) {
        return x + y + z;
    }

    /**
     * 实现两个小数类型的相加
     * @param x
     * @param y
     * @return
     */
    public static double add(double x, double y) {
        return x + y;
    }

    public static void main(String[] args) {
        System.out.println("两个整型参数相加：" + add(10, 20));
        System.out.println("三个整型参数相加：" + add(10, 20, 30));
        System.out.println("两个浮点型参数相加：" + add(10.2, 20.3));
    }
}
```

##### 方法的递归调用

> 递归调用是一种特殊的调用形式，指的是方法自己调用自己的形式。

注意：在项目应用的开发中避免过多的使用递归，因为如果处理不当，就有可能出现内存溢出问题。

```java
public class RecursiveCall {
    /**
     * 实现从 1 到 n 的累加
     * @param num
     * @return
     */
    public static int sum(int num) {
        if (num == 1) {
            return 1;
        } else {
            return num + sum(num - 1);
        }
    }

    public static void main(String[] args) {
        System.out.println(sum(100));
    }
}
```

##### 面向对象程序设计的特性

###### 封装性

一层含义是指把对象的属性和行为看成一个密不可分的整体，将两者封装在一个不可分割的独立单位(即对象)中；

另一层含义指信息隐蔽，把不需要让外界知道的信息隐藏起来，有些对象的属性和行为允许外界知道或使用，但不允许更改，而另一些对象的属性及行为，则不允许外界知晓，或只允许使用对象的功能，而尽可能隐蔽对象的功能实现细节。

###### 继承性

继承性是指首先拥有反应事物一般性质的类，然后在其基础上派生出反应特殊事物的类。

面向对象程序设计的继承机制，大大增强了程序代码的可复用性，提高了软件开发的效率，降低了程序产生错误的可能，也为程序的修改扩展提供了便利。

若一个子类只允许继承一个父类，称为单继承；若允许继承多个父类，称为多继承。目前许多面向对象程序设计语言不支持多继承。`Java` 通过接口 `interface` 的方式弥补由于 `Java` 不支持多继承而带来的子类不能使用多个父类成员的缺憾。

###### 多态性

多态是指允许程序中出现重名现象。 `Java` 中含有方法重载和对象多态两种形式的多态。

1. 方法重载：在一个类中，允许多个方法使用同一个名字，但方法的参数不同，完成的功能也不同。

2. 对象多态：子类对象可以与父类对象相互转换，而且根据其使用的子类不同完成不同的功能也不同。

多态的特性使程序的抽象程度和简洁程度更高，有助于程序设计人员对程序的分组协同开发。

##### 类与对象

###### 类与对象的基本定义

```java
class 类名称 {
    数据类型 属性(变量);

    权限修饰符 返回值的数据类型 方法名称 (形式参数列表) {
        执行语句;
        [return 返回值;]
    }
}
```

`eg`:

```java
class Book {
    String title;
    double price;

    public void getInfo() {
        System.out.printLn("图书名称：" + title, "价格：" +price);
    }
}
```

类定义完成之后，需要使用还需要对象声明和实例化：

```java
类名称 对象名称 = new 类名称();
```

分步完成：

```java 
类名称 对象名称 = null;     // 声明对象
对象名称 = new 类名称();    // 实例化对象
```

因为类属于引用数据类型，而引用数据类型和基本数据类型最大的不同就在于需要内存的开辟及使用，关键字 `new` 的主要功能就是开辟内存空间，只要使用引用数据类型，就必须使用 `new` 关键字来开辟空间。

对象实例化后可进行的操作：

对象.属性： 表示操作类中的属性的内容；
对象.方法()： 表示调用类中的方法。

```java
public class BookClass {

    public static void main(String[] args) {
        Book book = new Book();
        book.title = "Java";
        book.price = 89.0;
        book.getInfo();
    }
}
```

###### 引用数据的初步分析

引用传递是整个 `Java` 中的精髓所在，而引用传递的核心概念也只有一点：一块堆内存空间(保存对象的属性信息)可以同时被多个栈内存共同指向，则每一个栈内存都可以修改同一块堆内存空间的属性值。

- 堆内存(`heap`)：保存每一个对象的属性内容，堆内存需要用关键字 `new` 才可以开辟，如果一个对象没有对应的堆内存指向，将无法使用。

- 栈内存(`stack`)：保存的是一块堆内存的地址数值，每一块栈内存只能保存一块堆内存地址。

对象引用传递：

```java
public class BookClass {

    public static void main(String[] args) {
        Book book1 = new Book();
        book1.title = "Java";
        book1.price = 89.0;

        Book book2 = new Book();
        book2 = book1;
        book2.price = 69.8;

        book1.getInfo();
    }
}
```

这里打印 `book1` 的结果，价格变成了 `69.8`，这就是两个不同的栈内存指向了同一块堆内存空间(引用传递)，所以当 `book2` 修改属性内容时，会直接影响 `book1`对象的内容。

我们还可以发现，我们开始为 `book2` `new` 了一个内存空间，但是没有使用，而是使用引用传递(`book2 = book1`)，这样原本 `book2` 的内存空间没有任何指向，就会成为垃圾空间。

所有的垃圾会不定期的被垃圾收集器(`Garbage Collector`)回收，回收后会被释放掉其所占用的空间。

##### 封装性初步分析

需要让用户看不见操作的东西，就需要使用 `private` 关键字进行封装，将类中的属性进行私有化操作。

`Book.java`:

```java
public class Book {
    private String title;
    private double price;
    public void getInfo() {
        System.out.println("图书名称：" + title + "，价格：" + price);
    }
}
```

`Main.java`:

```java
public class Main {
    public static void main(String[] args) {
        Book book = new Book();
        book.title = "Java";
        book.pirce = 89.9;
        book.getInfo();
    }
}
```

这样运行项目是会报错的，在声明了 `private` 关键字之后，属性只能在 `Book` 类中被访问，就不可以对属性进行直接调用了，所以主类需要使用，就需要定义 `setter`、`getter` 方法。

下面改写 `Book` 类：

```java
public class Book {
    private String title;
    private double price;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void getInfo() {
        System.out.println("图书名称：" + title + "，价格：" + price);
    }
}
```

在 `Main` 中调用：

```java
public class Main {
    public static void main(String[] args) {
        Book book = new Book();
        book.setTitle("Java");
        book.setPrice(89.9);
        book.getInfo();
    }
}
```

##### 构造方法

如果实例化新的对象，需要使用关键字 `new` 来完成，但是除了 `new` 这个关键字之外，还有可能在对象实例化时为其进行一些初始化操作，直观时候就需要构造方法的支持。

构造方法是一种特殊的方法，它只在新对象实例化的时候调用，其定义原则是：方法名称与类名称相同，没有返回类型声明，同时构造方法也可以进行重载。

与普通方法的区别：

- 构造方法是在实例化新对象(`new`)的时候只调用一次；

- 普通方法是在实例化对象产生之后，通过 `Object.function` 的方式多次调用。

利用构造方法为属性赋值：

```java
public class Book {
    private String title;
    private double price;

    public Book(String title, double price) {
        this.title = title;
        this.price = price;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void getInfo() {
        System.out.println("图书名称：" + title + "，价格：" + price);
    }
}
```

`Main` 调用:

```java
public class Main {
    public static void main(String[] args) {
        Book book = new Book("Java", 89.8);
        book.getInfo();
    }
}
```

构造方法重载：

```java
public class Book {
    private String title;
    private double price;

    public Book() {
    }

    public Book(String title) {
        this.title = title;
    }

    public Book(String title, double price) {
        this.title = title;
        this.price = price;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void getInfo() {
        System.out.println("图书名称：" + title + "，价格：" + price);
    }
}
```

现在方法被我们重载了 `3` 次，我们可传入不同的形参：

```java
public class Main {
    public static void main(String[] args) {
        Book book = new Book("Java", 89.8);
        book.getInfo();
        Book book1 = new Book("Python");
        book1.getInfo();
        Book book2 = new Book();
        book2.getInfo();
    }
}
```

![方法重载](http://images.akashi.org.cn/FlH5UJS2ItY-VJKCOGwGckSx6a1V)

##### 匿名对象

按之前的内存关系来讲，对象的名字可以解释为在栈内存中保存，而对象的具体内容(属性)在堆内存中保存，这样一来，没有栈内存指向堆内存空间，就是一个匿名对象。

- 匿名对象

```java
public class Main {
    public static void main(String[] args) {
        new Book("Java", 89.9).getInfo();
    }
}
```

通过匿名对象调用了类中的方法，但由于匿名对象没有对应的栈内存指向，所以只能使用一次，一次之后就将成为垃圾，并且等待被 `GC` 回收释放。

