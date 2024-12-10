# Given an array of integers, nums, and an integer target, return two numbers such
# that they add up to target.
# Assume there’s only one unique pair of numbers that will sum up to the target and
# you may not use the same element twice.
# You can return the answer in any order.
# Example:
# Input: nums = [1, 2, 3, 7, 5], target = 10
# Output: [3, 7]

def two_sum(arr, target):
    if len(arr) < 2:
        return

    pair_dict = {}
    for num in arr:
        pair = target - num
        if pair not in pair_dict:
            pair_dict[num] = True
        else:
            return [num, pair]

print(two_sum([1, 2, 3, 7, 5], 10))