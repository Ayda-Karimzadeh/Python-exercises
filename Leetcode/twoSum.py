# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#            for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
# O(n^2)

class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

# O(n)
# Hash map: save data as key -> value so we can find values quickly.
# For each number, check if we've already seen the value needed to reach target.
# If not, store the current number and its index for future lookups.