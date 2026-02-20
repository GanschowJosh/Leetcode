from bisect import bisect_left
class Solution:
    def minOperations(self, target, arr) -> int:
        m=len(target)
        n=len(arr)
        pos={v:i for i,v in enumerate(target)}
        seq=[pos[x] for x in arr if x in pos]

        t=[]
        for x in seq:
          k=bisect_left(t,x)
          if k==len(t):
            t.append(x)
          else:
            t[k]=x
        return m-len(t)
sol = Solution()
print(sol.minOperations([5,1,3],[9,4,2,3,4]))
print(sol.minOperations([6,4,8,1,3,2],[4,7,6,2,3,8,6,1]))
