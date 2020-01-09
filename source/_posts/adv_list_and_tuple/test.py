def removeDuplicates(nums):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)-1):
            if nums[i] == nums[j]:
                nums.pop(j)
    return len(nums)

if __name__ == "__main__":
    # nums = [1, 1, 2]
    nums = [0, 0, 0, 0]
    res = removeDuplicates(nums)
    print(res)
