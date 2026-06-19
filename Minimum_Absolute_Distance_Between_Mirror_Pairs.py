class Solution:
  def minMirrorPairDistance(self, nums: list[int]) -> int:
    def reverse(num):
      return int(str(num)[::-1])
    best=10**18
    mirr=dict() #mirrored val at idx -> idx
    for i,num in enumerate(nums):
      if num in mirr:
        best=min(best, abs(i-mirr[num]))
      mirr[reverse(num)]=i
    return best if best < 10**18 else -1