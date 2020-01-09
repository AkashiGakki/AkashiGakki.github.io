---
title: Leetcode 题解 - 回文数
date: yyyy-mm-dd
category: 
    - Algorithm
    - Leetcode
tags:
    - Algorithm
    - Leetcode
thumbnail: /images/bg-36.jpg

---

#### `Leetcode` 题解 `-` 回文数

> `Palindrome Num` 回文数

<!-- more -->

##### 题目描述

判断一个整数是否是`回文数`。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: `121`
输出: `true`

示例 2:

输入: `-121`
输出: `false`
解释: 从左向右读, 为 `-121` 。 从右向左读, 为 `121-` 。因此它不是一个回文数。

示例 3:

输入: `10`
输出: `false`
解释: 从右向左读, 为 `01` 。因此它不是一个回文数。

##### 解题方案

思路 `1`:

判断是否为负数，如果是负数直接返回 `false`

对字符串进行反转，判断是否与之前的值相等，若不等返回 `false`，否则返回 `true`


`Python`:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if int(str(x)[::-1]) == x:
            return True
```

`Java`:

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        String str = String.valueOf(x);
        int n = str.length();
        for (int i = 0; i < n; i++) {
            if (str.charAt(i) != str.charAt(n-1-i)) {
                return false;
            }
        }
        return true;
    }
}
```

```java
class Solution {
    public boolean isPalindrome(int x) {
        String string = String.valueOf(x);
        StringBuilder stringBuilder = new StringBuilder(string);
        if (string.equals(stringBuilder.reverse().toString())) {
            return true;
        } else {
            return false;
        }
    }
}
```

思路 `2`:

直接将整数反转过来，与之前的值进行比较，如果相等，返回 `true`

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int temp = x;
        long res = 0;
        while(x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        return temp == res;
    }
}
```
