class Solution:
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i+1)]