---
title: Leetcode 题解 - 两数之和
date: yyyy-mm-dd
category: 
    - Algorithm
    - Leetcode
tags:
    - Algorithm
    - Leetcode
thumbnail: /images/bg-32.jpg

---

#### `Leetcode` 题解 `-` 两数之和

> `Two Sum` 两数之和

##### 题目描述

给定一个整数数组 `nums` 和一个目标值 `target` ，请你在该数组中找出和为目标值的那 `两个` 整数，并返回他们的`数组下标`。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 `nums = [2, 7, 11, 15]`, `target = 9`

因为 `nums[0] + nums[1] = 2 + 7 = 9`
所以返回 `[0, 1]`


##### 解题方案

1. 暴力解法，双重循环遍历

时间复杂度： `O(N^2)` 空间复杂度：`O(1)`

外层循环从数组中取出下标为 `i` 的元素 `nums[i]`，内层循环取出 `i` 之后的元素 `nums[j]`，与下标为 `i` 的元素进行相加操作，判断结果是否为 `target`。

`Python`:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

`Java`:

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}
```

2. 牺牲空间来换取时间

时间复杂度：`O(N)` 空间复杂度：`O(N)`

我们希望在第一次遍历时就可以进行判断，新开一个字典进行存储。

通过字典存储当前数字，判断 `target - num` 是否在字典中，如果存在，返回对应值字典的值和当前 `index`，如果不存在，以当前数字为键，当前下标为值存入字典中。

`Python`:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target-num], i]
            else:
                dict[num] = i
```

`Java`:

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = target - nums[i];
            if (map.containsKey(num)) {
                return new int[] {map.get(num), i};
            }
            map.put(nums[i], i);
        }
        return null;
    }
}
```
