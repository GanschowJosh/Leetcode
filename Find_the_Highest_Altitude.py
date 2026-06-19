from typing import List

class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    curr = 0
    max = 0
    for i, g in enumerate(gain):
      curr+=g
      if curr > max:
        max = curr

    return max

sol = Solution()

print(sol.largestAltitude([-5,1,5,0,-7]))
print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))
