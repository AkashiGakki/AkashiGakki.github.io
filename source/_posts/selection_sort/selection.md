---
title: SelectionSort
date: yyyy-mm-dd
category: Algorithm
tags: 
    - Python
    - Algorithm
thumbnail: /images/asuka/asu-10.jpg

---

### SelectionSort

> 选择排序 - 前一位和后面的数组进行比较。

<!-- more -->

#### 选择排序的思想

指定两个指针，从数组头部开始，将第一个与数组后面的数字逐一进行比较，如果第一个元素小于后面相比较的元素时，交换他们的位置，否则，位置不变，直到数组末尾，完成一轮比较。

结束一轮比较之后，数组第一个元素即为数组中最小的元素，指针向前移动一个位置，继续重复过程比较，直到最终获得一个有序的数组。

#### 代码示例

- `Java` 实现

```java
import java.util.Arrays;

public class Selection {
    public void sort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    swap(nums, i, j);
                }
            }
        }
    }

    private static void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public static void main(String[] args) {
        int[] nums = new int[] {3, 2, 6, 4, 1, 9 ,7};
        Selection sort = new Selection();
        sort.sort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```

外部循环控制第一个比较元素，即循环次数，内部循环控制第二个元素，并与第一个元素进行比较，符合条件，则进行交换。

- `Python` 实现

```python
class Selection():
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        for i in range(self.length):
            for j in range(i+1, self.length):
                if self.nums[i] > self.nums[j]:
                    self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def show(self):
        print(self.nums)


if __name__ == "__main__":
    nums = [2, 3, 1, 6, 4, 9, 7]
    sort = Selection(nums)
    sort.sort()
    sort.show()
```

- 简化版

```python
def sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == "__main__":
    nums = [2, 3, 1, 6, 4, 9, 7]
    res = sort(nums)
    print(res)
```

选择排序在第一次外部循环找到数组中最小的元素，将它和数组中第一个的元素位置交换(如果第一个元素最小就和自己交换)，然后，进入第二次外部循环，在剩下的元素中，找到最小的元素，与第二个元素的位置交换，如此往复，完成数组排序。

因为每一次遍历一遍找出的都是最小的元素，并不能为下一次扫描提供什么信息，一个有序的数组和一个元素随机的数组排列所需的时间是一样的。

交换次数和数组大小是线性关系，数据的移动是最少的。
