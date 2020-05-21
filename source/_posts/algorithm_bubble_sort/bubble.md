---
title: BubbleSort
date: yyyy-mm-dd
category: Algorithm
tags: 
    - Python
    - Algorithm
thumbnail: /images/asuka/asu-9.jpg

---

### BubbleSort

> 冒泡排序 - 相邻两个元素进行比较。

<!-- more -->

#### 冒泡排序的思想

指定两个指针，从数组头部开始，把相邻的两个元素进行比较，当前一个元素大于后一个元素时，交换他们的位置，否则，位置不变，直到数组末尾，完成一轮比较。

结束一轮比较，获得数组中最大的元素，在数组末尾。接下来重复这个过程，在剩下的元素中进行比较，最终得到一个有序的数组。

#### 代码示例

- `Java` 实现

```java
import java.util.Arrays;

public class Bubble {
    public void sort(int[] nums) {
//        标记每轮遍历中数字是否发生了交换
        boolean hasChange = true;

        for (int i = 0; i < nums.length-1 && hasChange; i++) {
            hasChange = false;

            for (int j = 0; j < nums.length-1-i; j++) {
                if (nums[j] > nums[j+1]) {
                    swap(nums, j, j+1);
                    hasChange = true;
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
        int[] nums = new int[] {2, 3, 1, 6, 4, 9, 7};
        Bubble sort = new Bubble();
        sort.sort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```

外部循环控制循环次数，内部循环实现每一轮冒泡处理：先元素比较，然后进行元素交换。

加入一个有序标记，如果元素没有发生交换，证明数组已经是有序的，结束循环。

- `Python` 实现

```python
class Bubble():
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.has_change = True

    def sort(self):
        for i in range(self.length-1):
            if self.has_change:
                self.has_change = False
                for j in range(self.length-1-i):
                    if self.nums[j] > self.nums[j+1]:
                        self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                        self.has_change = True

    def show(self):
        print(self.nums)


if __name__ == "__main__":
    nums = [2, 3, 1, 6, 4, 9, 7]
    sort = Bubble(nums)
    sort.sort()
    sort.show() 
```

- 简化版

```python
def sort(nums):
    length = len(nums)
    for i in range(length-1):
        for j in range(length-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__":
    nums = [2, 3, 1, 6, 4, 9, 7]
    res = sort(nums)
    print(res)
```
