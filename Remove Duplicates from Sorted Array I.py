class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nextUnique = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[nextUnique - 1]:
                nums[nextUnique] = nums[i]
                nextUnique+=1
        
        return nextUnique