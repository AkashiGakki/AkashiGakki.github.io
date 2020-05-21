---
title: 典型算法处理实现
date: 2019-9-12
category: 
    - Algorithm
tags:
    - Algorithm
    - 算法
thumbnail: /images/bg-31.jpg

---

#### 典型算法处理实现

> 记录几个常见算法实现。

<!-- more -->

##### 典型的数组处理

###### 找出数组中最大的元素

```java
class Max {

    public static double max(double[] list) {
        double max = list[0];
        for (int i = 0; i < list.length; i++) {
            if (list[i] > max) {
                max = list[i];
            }
        }
        return max;
    }

    public static void main(String args[]) {
        double[] list = new double[] {1.2, 3.0, 5, 0.4, 9, 6.8, 7};
        System.out.println(max(list));
    }
}
```

###### 计算数组元素的平均值

```java
class Avg {
    public static double avg(double[] list) {
        int N = list.length;
        double sum = 0;
        for (int i = 0; i < N; i++) {
            sum += list[i];
        }
        double average = sum / N;
        return average;
    }

    public static void main(String args[]) {
        double[] list = new double[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
        double avg = avg(list);
        System.out.println(avg);
    }
}
```

###### 复制数组

```java
class CopyArray {
    public static int[] copy(int[] list) {
        int N = list.length;
        int[] list_new = new int[N];
        for (int i = 0; i < N; i++) {
            list_new[i] = list[i];
        }
        return list_new;
    }

    public static void main(String[] args) {
        int[] list1 = new int[] {1, 2, 3, 4, 5, 6, 7};
        int[] list2 = copy(list1);
        for (int i : list2) {
            System.out.println(i);
        }
    }
}
```

###### 颠倒数组元素的顺序

```java
class Reverse {
    public static double[] rev(double[] list) {
        int N = list.length;
        for (int i = 0; i < N / 2; i++) {
            double temp = list[i];
            list[i] = list[N-1-i];
            list[N-1-i] = temp;
        }
        return list;
    }

    public static void main(String[] args) {
        double[] list = new double[] {1, 2, 3, 4, 5, 6, 7};
        double[] rev_list = rev(list);
        for (int i = 0; i < rev_list.length; i++) {
            System.out.println(rev_list[i]);
        }
    }
}
```

###### 矩阵相乘

```java
class MatrixMult {
    public static double[][] multip(double[][] array1, double[][] array2) {
        int N = array1.length;
        double[][] matrix = new double[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    matrix[i][j] += array1[i][k] * array2[k][j];
                }
            }
        }
        return matrix;
    }

    public static void main(String[] args) {
        double[][] array1 = new double[][] {
            {1, 2, 3}, {3, 2, 1}
        };
        double[][] array2 = new double[][] {
            {1, 2, 3}, {3, 2, 1}
        };
        double[][] matrix = multip(array1, array2);
        int M = array1.length;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                System.out.println(matrix[i][j]);
            }
        }
    }
}
```

##### 典型的静态方法的实现

###### 计算一个整数的绝对值

```java
class Abs {
    public static int abs(int x) {
        if (x < 0) {
            return -x;
        } else {
            return x;
        }
    }

    public static void main(String[] args) {
        int x = -2;
        System.out.println(abs(x));
    }
}
```

###### 计算一个浮点数的绝对值

```java
class AbsDouble {
    public static double abs(double x) {
        if (x < 0) {
            return -x;
        } else {
            return x;
        }
    }

    public static void main(String[] args) {
        double x = -2.3;
        System.out.println(abs(x));
    }
}
```

###### 判定一个数是否是素数

```java
class Prime {
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int x = 123;
        System.out.println(isPrime(x));
    }
}
```

###### 计算平方根

```java
class Sqrt {
    public static double sqrt(double x) {
        if (x < 0) {
            return Double.NaN;
        }
        double err = 1e-15;
        double t = x;
        while(Math.abs(t - x / t) > err * t) {
            t = (x / t + t) / 2.0;
        }
        return t;
    }

    public static void main(String[] args) {
        double x = 9;
        System.out.println(sqrt(x));
    }
}
```

###### 计算直角三角形的斜边

```java
class Hypotenuse {
    public static double hypotense(double a, double b) {
        return Math.sqrt(a * a + b * b);
    }

    public static void main(String[] args) {
        double x = 3;
        double y = 4;
        System.out.println(hypotense(x,y));
    }
}
```
