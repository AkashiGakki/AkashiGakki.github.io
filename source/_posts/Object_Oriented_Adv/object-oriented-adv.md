---
title: 面向对象进阶
date: yyyy-mm-dd
category:
  - Java
tags:
  - Java
  - 面向对象
thumbnail: /images/bg-35.jpg
---

#### 面向对象进阶

> 类的继承、多态、抽象类与接口的具体使用。

<!-- more -->

##### 继承性

> 继承是面向对象的第二大特征，而继承性要解决的问题就是代码的重用问题，利用继承性可以从已有的类继续派生出新的子类，也可以利用子类扩展出更多的操作功能。

继承是为了增强代码的复用性，扩充类的功能，具体实现为：

```java
class 子类 extends 父类 {

}
```

- 子类又被称为派生类

- 父类又被称为超类

###### 基本实现

父类：`Person`：

```java
public class Person {
    private String name;
    private Integer age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
}
```

子类：`Student`:

```java
public class Student extends Person {
    private Integer sid;
    private String school;

    public Integer getSid() {
        return sid;
    }

    public void setSid(Integer sid) {
        this.sid = sid;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }
}
```

调用： `Main`:

```java
public class Main {
    public static void main(String[] args) {
        Student student = new Student();
        student.setName("Akashi");
        student.setAge(22);
        student.setSchool("SMU");
        student.setSid(123456);
        System.out.println("name: " + student.getName() + " age: " + student.getAge() + " school: " + student.getSchool() + " sid: " + student.getSid());
    }
}
```

子类实际上是将父类定义得更加具体化的一种手段。

###### 限制

虽然继承可以进行类功能的扩充，但是其在定义的时候也会存在若干限制：

- `Java` 不允许多继承，但是允许多层继承

虽然可以多层继承，但是从实际开发角度讲，类之间的继承最多不要超过三层，太多继承关系会让类过于复杂。

- 子类在继承父类的时候，严格上来讲会继承父类中的全部操作，但是对于所有的私有操作属于隐式继承，而所有的非私有操作属于显式继承。

隐式继承即只可以利用 `setter` 和 `getter` 方法间接的访问私有属性，子类也并不可以直接访问父类的私有属性。

- 在子类对象构造前一定会默认调用父类的构造(默认使用无参构造)，以保证父类的对象先实例化，子类的对象后实例化。

```java
class A {
    public A() {
        System.out.println("A类的构造方法");
    }
}

class B extends A {
    public B() {
        System.out.println("B类的构造方法");
    }
}

public class Main {
    public static void main(String[] args) {
        B b = new B();
    }
}
```

输出：

```
A类的构造方法
B类的构造方法
```

##### 覆写

> 继承性的主要特征是子类可以根据父类已有的功能进行功能的扩展，但是在子类定义属性或方法时，有可能出现定义的属性或方法与父类同名的情况，这样的操作被称为覆写。

当子类定义了和父类的方法名称、返回值类型、参数类型及个数完全相同的方法时，就称为方法的覆写。

###### 实现

```java
public class A {
    public void func() {
        System.out.println("A类中的func方法");
    }
}
```

```java
public class B extends A {
    public void func() {
        System.out.println("B类中的func方法");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        B b = new B();
        b.func();
    }
}
```

输出为：

```
B类中的func方法
```

###### 覆写的执行问题

- 观察实例化的是那一个类

- 观察这个实例化的类里面调用的方法是否已经被覆写过，如果没有覆写过则调用父类的方法

注意：父类方法中使用 `private` 声明的方法是无法被外部看见的，也是不能被覆写的。

##### `final` 关键字

- 使用 `final` 定义的类不能再有子类，即：任何类都不能继承以 `final` 声明的父类。

- 使用 `final`定义的方法不能被子类所覆写。

##### 多态性

- 方法的多态性
    - 重载：同一个方法名称，根据不同的参数类型及个数可以完成不同的功能
    - 覆写：同一个方法，根据实例化的子类不同，所完成的功能也不同

- 对象的多态性
    - 向上转型：子类对象变为父类对象，格式：`父类 父类对象 = 子类实例`(自动转换)
    - 向下转型：父类对象变为子类对象，格式：`子类 子类对象 = (子类)父类实例`(强制转换)

###### 实现

向下转型(自动完成)：

```java
public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.func();
    }
}
```

输出：

```
B类中的func方法
```

判断最终的输出，要看是实例化的那一个类。这里实例化的是 `B` (`new B()`)

向上转型(强制转换)

```java
public class Main {
    public static void main(String[] args) {
        A a = new B();
        B b = (B)a;
        b.func();
    }
}
```

先向上转型，再强制向下转型，同样输出 `B类中的func方法`，在强制向下转型时是有条件的，必须先向上转型，不然会抛出类型转换异常 `ClassCastException`。

```java
public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.func();
    }
}
```

向下转型是会存在安全隐患的，开发中应尽量避免此操作。

###### 转型意义

在实际开发中，对象向上转型的主要意义在于参数的统一，也是最为主要的用法。

而对象的向下转型指的是调用子类的个性化操作方法。

##### 抽象性

> 利用抽象类可以明确定义子类需要覆写的方法。

普通类可以直接产生实例化对象，并且在普通类中可以包含构造方法、普通方法、`static` 方法、常量、变量等内容。而抽象类就是指在普通类里面增加了抽象方法的组成部分，抽象方法指的是没有方法体的方法，同时抽象方法还必须使用 `abstract` 定义。

```java
public abstract class A {
    public void func() {
        System.out.println("A类中的func方法");
    }

    public abstract void print();
}
```

###### 抽象类不能直接实例化对象

- 抽象类必须有子类，即每一个抽象类一定要被子类所继承(使用`extends`)，但同样的因为单继承的原因，一个子类只能继承一个抽象类，这个问题会在之后的接口中提出解决办法。

- 抽象类的子类必须覆写抽象类中的全部抽象方法。

- 依靠对象的向上转型概念，可以通过抽象类的子类完成抽象类的实例化对象操作。

```java
public class B extends A {
    public void func() {
        System.out.println("B类中的func方法");
    }

    public void print() {
        System.out.println("覆写父类的抽象方法");
    }
}
```

```java
public class Demo {
    public static void main(String[] args) {
        B b = new B();
        b.print();
    }
}
```

###### 抽象类的相关限制

- 抽象类里面会存在一些属性，那么在抽象类里面一定会存在构造方法，目的是为了属性的初始化，并且子类对象实例化时依然满足先执行父类构造再调用子类构造的情况。

- 抽象类不能使用 `final` 定义，因为抽象类必须有子类，而 `final` 定义的类不能有子类。

- 抽象类中可以没有任何抽象方法，但是只要有抽象类，就不能直接使用关键字 `new` 实例化对象。

###### 抽象类应用 `——` 模板设计模式

抽象类的最主要特点相当于制约了子类必须覆写的方法，同时抽象类中也可以定义普通方法，而且最为关键的是，这些普通方法定义在抽象类时，可以直接调用类中定义的抽象方法，但是具体的抽象方法内容就必须由子类来提供。

```java
public abstract class A {

    public abstract void print();

    public void getPrint() {
        this.print();
    }
}
```

```java
public class B extends A {

    public void print() {
        System.out.println("覆写父类的抽象方法");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.getPrint();
    }
}
```

##### 接口

> 利用抽象类可以实现对子类覆写方法的控制，但是抽象类的子类存在单继承限制，所以需要 `Java` 的接口来解决。同时，在开发中为了将具体的代码的实现细节对调用者隐藏，也可以利用接口来进行方法视图的描述。

###### 定义接口

```java
public interface A {
    public abstract void func();
    
    public abstract void print();
}
```

- 接口必须要有子类，但是此时一个子类可以使用 `implements` 关键字实现多个接口，避免单继承局限。

- 接口的子类(如果不是抽象类)，必须要覆写接口中的全部抽象方法。

- 接口的对象可以利用子类对象的向上转型进行实例化操作。

```java
public class B implements A {
    public void func() {
        System.out.println("A接口的抽象方法");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.func();
    }
}
```

###### 接口的应用 `——` 工厂设计模式(`Factory`)

一个良好的代码编写风格要求遵从于以下两个标准：

- 客户端(示例中的主方法)调用简单，不需要关注具体的细节。

- 程序代码的修改，不影响客服端的调用，即：使用者可以不去关心代码是否变更。

我们来看以下的一个例子：

```java
public interface Fruit {
    public void eat();
}
```

```java
public class Apple implements Fruit {
    public void eat() {
        System.out.println("eating apple.");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        Fruit fruit = new Apple();
        fruit.eat();
    }
}
```

这时我们再添加一个新的子类，想要调用新的子类就需要去修改实例化接口的子类：

```java
public class Orange implements Fruit  {
    public void eat() {
        System.out.println("eating orange.");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        Fruit fruit = new Orange();
        fruit.eat();
    }
}
```

这种写法是不推荐的，为了解决耦合，需要引入工厂模式的概念，即想办法让客户端只看见接口，而不让其看见子类，这时需要一个中间的工具类来取得接口对象。

这样客户端就不用再关心接口的子类，只要通过 `Facroty` (工厂类)就可取得接口对象。

增加一个工厂类进行过渡：

```java
public class Factory {
    public static Fruit getInstance(String fruit) {
        if ("apple".equals(fruit)) {

            return new Apple();

        } else if ("orange".equals(fruit)) {

            return new Orange();

        } else {

            return null;

        }
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        Fruit fruit = Factory.getInstance("orange");
        fruit.eat();
    }
}
```

改写后，客户端的操作上取消了 `new` 关键字的使用，而使用 `Factory.getInstance()` 方法根据指定的子类的标记取得接口实例化对象，这时客户端不再需要关注具体的子类，也不需要关注 `Factory` 类是怎样处理的，只需要关注如何获取接口对象并操作。

这样的设计在开发中就称为工厂设计模式。

###### 接口的应用 `——` 代理设计模式(`Proxy`)

代理设计就是指一个代理主题来操作真实主题，真实主题执行具体的业务操作，而代理主题负责其他相关业务的处理。

就好比代理上网，客户通过网络代理连接网络，由代理服务器完成用户权限、访问限制等与上网操作相关的操作。

```java
public interface Network {
    public void browse();
}
```

```java
public class Proxy implements Network {
    private Network network;

    public Proxy(Network network) {
        this.network = network;
    }

    private void check() {
        System.out.println("检查用户是否合法");
    }

    public void browse() {
        this.check();
        this.network.browse();
    }
}
```

```java
public class Real implements Network {
    public void browse() {
        System.out.println("上网浏览信息");
    }
}
```

```java
public class Demo {
    public static void main(String[] args) {
        Network network = null;
        network = new Proxy(new Real());
        network.browse();
    }
}
```

##### 抽象类与接口的区别

比较：

区别 | 抽象类 | 接口
--- | --- | ---
关键字 | `abstract class` | `interface`
组成 | 构造方法、普通方法、抽象方法、`static` 方法、常量、变量 | 抽象方法、全局常量
子类使用 | `class 子类 extends 抽象类` | `class 子类 implements 接口, 接口...`
关系 | 抽象类可以实现多个接口 | 接口不能继承抽象类，却可以继承多个父接口
权限 | 可以使用各种权限 | 只能使用 `public` 权限
限制 | 单继承局限 | 没有单继承局限

相同：

子类：抽象类和子类都必须有子类，子类必须覆写全部的抽象方法
实例化对象：依靠子类对象的向上转型进行对象的实例化

建议；

- 在进行某些公共操作时一定要定义出接口

- 有了接口就需要利用子类完善方法

- 如果是自己写的方法，那么绝对不要使用关键字 `new` 直接实例化接口子类，应该使用工厂类完成

- 接口是在类之上的标准，接口比类更加灵活，在考虑用什么实现时，优先考虑接口

##### `Object` 类

`Object` 类是所有类的父类，也就是说任何一个类在定义时如果没有明确地继承一个父类，那么它就是 `Object` 的子类。

- `Object` 类的 `3` 个覆写方法

方法 | 描述
--- | ---
`public String toString()` | 取得对象信息
`public Boolean equals(Object obj)` | 对象比较
`public int hashCode()` | 取得对象哈希码
