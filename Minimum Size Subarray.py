class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    l, r = 0, 0
    smallest = float('inf')
    curr_sum = nums[0]
    while(True):
      if curr_sum >= target:
        smallest = min(smallest, r-l+1)
          curr_sum -= nums[l]
          l += 1
      else:
        if r == len(nums)-1:
          break
        r += 1
        curr_sum += nums[r]
    return smallest if smallest != float('inf') else 0