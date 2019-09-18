---
title: Leetcode 题解 - 最长公共前缀
date: yyyy-mm-dd
category: 
    - Algorithm
    - Leetcode
tags:
    - Algorithm
    - Leetcode
thumbnail: /images/bg-38.jpg

---

#### `Leetcode` 题解 `-` 最长公共前缀

> `Longest Common Prefix` 最长公共前缀

<!-- more -->

##### 题目描述

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

示例 1:

输入: `["flower","flow","flight"]`
输出: `"fl"`

示例 2:

输入: `["dog","racecar","car"]`
输出: `""`

解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 `a-z` 。

思路 1：

利用 `Python` 里面字符串可以比较大小的优势，只需要比较最大和最小的字符串的公共前缀就是整个数组的公共前缀。

`Python`:

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        for i, v in enumerate(s1):
            if v != s2[i]:
                return s2[:i]
        return s1
```

比较取巧的做法：

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)
```

思路 2：

假设第一个是字符数组的公共子串，分别与之后的进行比较，如果不相等，将字符串从末尾减去一个字符，重新进行比较，如果相等，与下一个字符串进行比较，最后得到的就是整个字符数组的公共子串。

`Java`:

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        String str = strs[0];
        for (int i = 0; i < strs.length; i++) {
            while (strs[i].indexOf(str) != 0) {
                str = str.substring(0, str.length()-1);
                if (str.isEmpty()) {
                    return "";
                }
            }
        }
        return str;
    }
}
```
