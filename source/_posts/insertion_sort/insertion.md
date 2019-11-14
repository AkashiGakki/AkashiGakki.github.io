---
title: InsertionSort
date: yyyy-mm-dd
category: Algorithm
tags: 
    - Python
    - Algorithm
thumbnail: /images/asuka/asu-11.jpg

---

### InsertionSort

> 插入排序 - 后一位与前面数组进行比较。

<!-- more -->

#### 插入排序的思想

指定两个指针，从数组头部开始，第一个指针控制有序数组的边界，从 `1` 开始，另一个指针进行比较操作，控制子数组(有序数组)边界的元素，与前面有序数组进行比较，如果小于前一个元素，就和前一个元素交换位置，完成一次比较。

#### 代码示例

- `Java` 实现

```java
import java.util.Arrays;

public class Insertion {
    public void sort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            for (int j = i; j > 0 && nums[j] < nums[j-1]; j--) {
                swap(nums, j, j-1);
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
        Insertion sort = new Insertion();
        sort.sort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```

外层循环确定有序数组的边界和循环次数(从 `1` 开始)，内层循环控制子数组中的比较操作，将新加入子数组中的元素与之前的元素进行比较，并插入到数组中的合适位置。

- `Python` 实现

```python
class Insertion():
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)

    def sort(self):
        for i in range(1, self.length):
            j = i
            while j and self.nums[j] < self.nums[j-1]:
                self.nums[j], self.nums[j-1] = self.nums[j-1], self.nums[j]
                j -= 1

    def show(self):
        print(self.nums)


if __name__ == "__main__":
    nums = [3, 2, 6, 4, 1, 9 ,7]
    sort = Insertion(nums)
    sort.sort()
    sort.show()
```

- 简化版

```python
def sort(nums):
    length = len(nums)
    for i in range(1, length):
        j = i
        while j and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums


if __name__ == "__main__":
    nums = [3, 2, 6, 4, 1, 9 ,7]
    res = sort(nums)
    print(res)
```

插入排序所需的时间取决于输入中元素的初始位置。如果对一个有序或接近有序的数组进行排序，效率会比随机数组有效的多。
