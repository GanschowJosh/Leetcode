# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


def guess(n):
  ans = 1
  if n > ans:
    return -1
  if n < ans:
    return 1
  else:
    return 0

class Solution:
  def guessNumber(self, n: int) -> int:
    l,r=0,n
    while l <= r:
      m=l+((r-l)//2)
      g=guess(m)
      if g == -1:
        r=m-1
      if g == 1:
        l=m+1
      if g == 0:
        return m

sol=Solution()
print(sol.guessNumber(2))