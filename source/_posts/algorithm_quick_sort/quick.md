---
title: LeetCode-QuickSort
date: 2019-11-16
category: Algorithm
tags: 
    - Python
    - Algorithm
thumbnail: /images/asuka/asu-13.jpg

---

### QuickSort

> 快速排序 - 递归分治为两个子数组，独立进行排序，主要在于切分元素的选择，左边子数组元素小于切分元素，右边子数组元素大于切分元素。

<!-- more -->

#### 快速排序的思想

对于双边循环法，以两个指针和切分元素将数组进行递归切分，左边子数组元素小于切分元素，右边子数组元素大于切分元素，递归切分至最小元素时，自然实现排序(最小时包括一个左边元素，一个切分元素，一个右边元素，它们是有序的)。

对于单边循环法，只使用一个指针和切分元素将数组进行递归切分，并且使用一个标记指针记录切分边界的位置，当元素小于切分元素，移动标记元素并且与比较元素交换位置。

#### 代码示例

##### 单边循环法

- `Java` 实现

```java
import java.util.Arrays;

public class QuickSort {
    public static void sort(int[] nums, int lo, int hi) {
        if (hi <= lo)
            return;

        int j = partition(nums, lo, hi);
        sort(nums, lo, j - 1);
        sort(nums, j + 1, hi);
    }

    private static int partition(int[] nums, int lo, int hi) {
        int pivot = nums[lo];
        int mark = lo;

        for (int i = lo + 1; i <= hi; i++) {
            if (nums[i] < pivot) {
                mark++;
                swap(nums, mark, i);
            }
        }

        swap(nums, lo, mark);
        return mark;
    }

    private static void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{3, 2, 6, 4, 1, 9, 7};
        QuickSort sort = new QuickSort();
        sort.sort(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));
    }
}
```
- `Python` 实现

```python
def sort(nums, low, high):
    if low < high:
        key = partition(nums, low, high)
        sort(nums, low, key-1)
        sort(nums, key+1, high)

def partition(nums, low, high):
    mark, key = low, nums[low]
    for i in range(low+1, high+1):
        if nums[i] < key:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]

    nums[low], nums[mark] = nums[mark], nums[low]
    return mark

if __name__ == "__main__":
    nums = [3, 2, 6, 4, 1, 9 ,7]   
    sort(nums, 0, len(nums)-1)
    print(nums)
```

##### 双边循环法

- `Java` 实现

```java
import java.util.Arrays;

public class Quick {
    public static void sort(int[] nums, int lo, int hi) {
        if (lo >= hi)
            return;

        int pivot = partition(nums, lo, hi);

        sort(nums, lo, pivot-1);
        sort(nums, pivot+1, hi);
    }

    public static int partition(int[] nums, int lo, int hi) {
        int pivot = nums[lo];
        int left = lo + 1;
        int right = hi;
        boolean done = true;

        while (done) {
            while (left <= right && nums[left] < pivot)
                left++;
            while (left <= right && nums[right] > pivot)
                right--;
            if (left > right)
                done = false;
            else
                swap(nums, left, right);
        }

        swap(nums, lo, right);
        return right;
    }

    private static void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public static void main(String[] args) {
        int[] nums = new int[] {3, 2, 6, 4, 1, 9 ,7};
        Quick sort = new Quick();
        sort.sort(nums, 0, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }
}
```

- `Python` 实现

```python
def sort(nums, low, high):
    if low < high:
        key = partition(nums, low, high)
        sort(nums, low, key-1)
        sort(nums, key+1, high)

def partition(nums, low, high):
    left, right, key = low + 1, high, nums[low]
    done = True

    while done:
        while left <= right and nums[left] < key:
            left += 1
        while left <= right and nums[right] > key:
            right -= 1
        if left > right:
            done = False
        else:
            nums[left], nums[right] = nums[right], nums[left]
    
    nums[low], nums[right] = nums[right], nums[low]
    return right

if __name__ == "__main__":
    nums = [3, 2, 6, 4, 1, 9 ,7]   
    sort(nums, 0, len(nums)-1)
    print(nums)
```
