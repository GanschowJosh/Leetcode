def maxSubArray(nums) -> int:
  
  sum = 0
  max_sum = max(nums)
  # base case
  if len(nums) == 1:
    return nums[0]
  
  else:
    for num in nums:
      if sum < 0:
        sum = 0
      sum += num
      max_sum = max(max_sum, sum)
  
  return max_sum

print(maxSubArray([5,4,-1,7,8]))
