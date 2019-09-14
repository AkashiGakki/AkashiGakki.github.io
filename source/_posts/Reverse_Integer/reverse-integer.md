---
title: Leetcode 题解 - 整数反转
date: yyyy-mm-dd
category: 
    - Algorithm
    - Leetcode
tags:
    - Algorithm
    - Leetcode
thumbnail: /images/bg-34.jpg

---

#### `Leetcode` 题解 `-` 整数反转

> `Reverse Integer` 整数反转

<!-- more -->

##### 题目描述

给出一个 `32` 位的有符号整数，你需要将这个整数中每位上的数字进行`反转`。

示例 1:

输入: `123`
输出: `321`

 示例 2:

输入: `-123`
输出: `-321`

示例 3:

输入: `120`
输出: `21`

注意:

假设我们的环境只能存储得下 `32` 位的有符号整数，则其数值范围为 `[−231,  231 − 1]`。请根据这个假设，如果反转后整数溢出那么就返回 `0`。

##### 解题方案

首先判断输入是否为负，如果是负数就递归调用原函数转为整数，最后结果再取负返回。

之后使用字符串切片进行反转，判断是否溢出。

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        res = int(str(x)[::-1])
        return res if res <= (2**31-1) else 0
```

使用 `long` 类型，避免反转后出现溢出现象。

采用取模和取余操作，将数字进行反转然后存储到 `res` 中。

最后做溢出判断，满足条件然后返回 `int` 类型。

```java
class Solution {
    public int reverse(int x) {
        long res = 0;
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        if (res <= -Math.pow(2, 31) || res >= Math.pow(2, 31)-1) {
            res = 0;
        }
        return (int)res;
    }
}
```
