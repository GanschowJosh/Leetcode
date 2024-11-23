from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates and use two-pointer
        out = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate elements for the first number of the triplet
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            curr = nums[i]
            target = -curr
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    out.append([curr, nums[left], nums[right]])
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return out

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 1, 1]))
print(sol.threeSum([0, 0, 0, 0]))
