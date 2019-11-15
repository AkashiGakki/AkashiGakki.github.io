---
title: MergeSort
date: yyyy-mm-dd
category: Algorithm
tags: 
    - Python
    - Algorithm
thumbnail: /images/asuka/asu-12.jpg

---

### MergeSort

> 归并排序 - 分治为子数组进行比较，然后归并。

<!-- more -->

#### 归并排序的思想

归并，即将两个有序的数组归并成一个更大的有序数组。归并排序算法：要将一个数组排序，可以先递归的将它们分成两半进行排序，然后再将结果合并起来。合并时需要额外的空间进行操作。

#### 原地归并排序

将原数组递归分治为两个子数组进行比较，使用一个辅助数组进行归并。

在归并时，左半边用尽，取右半边元素；右半边用尽，取左半边元素；右半边当前元素小于左半边当前元素，取右半边元素，以及右半边当前元素大于左半边元素，取左半边元素。

- `Java` 实现

```java
import java.util.Arrays;

public class Merge {
//    原地归并排序
    public void sort(int[] a, int lo, int hi) {
        if (lo >= hi)
            return;

        int mid = lo + (hi - lo) / 2;

        sort(a, lo, mid);
        sort(a, mid+1, hi);

        merge(a, lo, mid, hi);
    }

    public static void merge(int[] nums, int lo, int mid, int hi) {
        int i = lo, j = mid + 1;
        int[] aux = new int[nums.length];

        for (int k = lo; k <= hi; k++) {
            aux[k] = nums[k];
        }

        for (int k = lo; k <= hi; k++) {
            if (i > mid)
                nums[k] = aux[j++];
            else if (j > hi)
                nums[k] = aux[i++];
            else if (aux[j] < aux[i])
                nums[k] = aux[j++];
            else
                nums[k] = aux[i++];
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[] {3, 2, 6, 4, 1, 9 ,7};
        Merge sort = new Merge();
        sort.sort(nums, 0, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }
}
```

- `Python` 实现

```python
def sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    sort(left)
    sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j] 
        j += 1
        k += 1

if __name__ == "__main__":
    nums = [3, 2, 6, 4, 1, 9 ,7]
    sort(nums)
    print(nums)
```

另一种实现方式(个人感觉更简洁)：

```python
def sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2

    left = sort(nums[:mid])
    right = sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    aux = list()

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            aux.append(left[i])
            i += 1
        else:
            aux.append(right[j])
            j += 1
    aux += left[i:]
    aux += right[j:]
    return aux


if __name__ == "__main__":
    nums = [3, 2, 6, 4, 1, 9 ,7]
    res = sort(nums)
    print(res)
```

#### 自顶向下的归并排序

```java
import java.util.Arrays;

public class MergeUB {
//    自顶向下的归并排序
    private static int[] aux;

    public void sort(int[] a) {
        aux = new int[a.length];
        sort(a, 0, a.length-1);
    }

    public static void sort(int[] a, int lo, int hi) {
        if (hi <= lo)
            return;
            
        int mid = lo + (hi - lo) / 2;
        sort(a, lo, mid);
        sort(a, mid+1, hi);
        merge(a, lo, mid, hi);
    }

    public static void merge(int[] nums, int lo, int mid, int hi) {
        int i = lo, j = mid + 1;

        for (int k = lo; k <= hi; k++) {
            aux[k] = nums[k];
        }

        for (int k = lo; k <= hi; k++) {
            if (i > mid)
                nums[k] = aux[j++];
            else if (j > hi)
                nums[k] = aux[i++];
            else if (aux[j] < aux[i])
                nums[k] = aux[j++];
            else
                nums[k] = aux[i++];
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[] {3, 2, 6, 4, 1, 9 ,7};
        MergeUB sort = new MergeUB();
        sort.sort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```

#### 自底向上的归并排序

```java
import java.util.Arrays;

public class MergeBU {
//    自底向上的归并排序
    private static int[] aux;

    public void sort(int[] a) {
        int N = a.length;
        aux = new int[N];

        for (int size = 1; size < N; size = size + size) {
            for (int lo = 0; lo < N-size; lo += size + size) {
                merge(a, lo, lo+size-1, Math.min(lo+size+size-1, N-1));
            }
        }
    }

    public static void merge(int[] nums, int lo, int mid, int hi) {
        int i = lo, j = mid + 1;

        for (int k = lo; k <= hi; k++) {
            aux[k] = nums[k];
        }

        for (int k = lo; k <= hi; k++) {
            if (i > mid)
                nums[k] = aux[j++];
            else if (j > hi)
                nums[k] = aux[i++];
            else if (aux[j] < aux[i])
                nums[k] = aux[j++];
            else
                nums[k] = aux[i++];
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[] {3, 2, 6, 4, 1, 9 ,7};
        MergeBU sort = new MergeBU();
        sort.sort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
```
