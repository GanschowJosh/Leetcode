class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nextUnique = 2

        count = 1 #count of current element
        for i in range(2, len(nums)):
            if nums[i] == nums[nextUnique - 1] and nums[i] == nums[nextUnique - 2]:
                continue
            
            if nums[i] != nums[nextUnique - 1]: #current element is different from previous unique element
                nums[nextUnique] = nums[i]
                nextUnique += 1
                count = 1
            
            else: #current element is the same as the previous unique element
                nums[nextUnique] = nums[i]
                nextUnique += 1
                count += 1
                if count > 2:
                    nextUnique -= 1
        
        return nextUnique
            