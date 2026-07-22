from typing import List
class Solution:
  def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    l1=len(nums1)
    l2=len(nums2)
    
    b=0
    for i in range(l1):
      c=nums1[i]
      if nums2[i] < c: continue
      l,r=i,l2-1
      ans=None
      while l<=r:
        m=(l+r)//2
        if nums2[m]<c:
          r=m-1
        else:
          l=m+1
          ans=m
      if ans:
        b=max(ans-i,b)
    return b

sol=Solution()
print(sol.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))
print(sol.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))
print(sol.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))
