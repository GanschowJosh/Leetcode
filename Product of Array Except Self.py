class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result_arr = [1]*n

        prefix = 1
        for i in range(n):
            result_arr[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            result_arr[i] *= suffix
            suffix *= nums[i]

        return result_arr