from collections import deque
from typing import List
class Solution:
    def rightShift(self, nums, num_rotations):
        a = deque(nums)

        for _ in range(num_rotations):
            a.rotate()
        
        return list(a)

    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        length_of_nums = len(nums)
        start = min(nums)
        end = max(nums)
        shifts = (length_of_nums - nums.index(start)) % length_of_nums
        if self.rightShift(nums, shifts) == sorted_nums:
            return shifts
        else:
            return -1

sol = Solution()
print(sol.minimumRightShifts([3, 4, 5, 1, 2]))
print(sol.minimumRightShifts([1, 3, 5]))
print(sol.minimumRightShifts([2, 1, 4]))

"""from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        
        min_index = nums.index(min(nums))
        
        shifts = (n - min_index) % n
        
        rotated_nums = nums[-shifts:] + nums[:-shifts]
        
        if rotated_nums == sorted_nums:
            return shifts
        else:
            return -1

sol = Solution()
print(sol.minimumRightShifts([3, 4, 5, 1, 2]))
print(sol.minimumRightShifts([1, 3, 5]))
print(sol.minimumRightShifts([2, 1, 4]))
"""