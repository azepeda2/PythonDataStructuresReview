def PairWithTargetSum(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[num] = i

    return [-1, -1]

print(PairWithTargetSum([1, 2, 3, 4, 6], 6))
print(PairWithTargetSum([2, 5, 9, 11], 11))