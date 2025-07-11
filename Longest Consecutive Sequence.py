class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0

        for i in nums:
            if i-1 not in nums:
                curr_length = 1
                while(i+curr_length in nums):
                    curr_length += 1
                max_length = max(max_length, curr_length)
            
        return max_length