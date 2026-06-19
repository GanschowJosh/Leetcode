from collections import deque
class Solution:
  def minOperations(self, k: int) -> int:
    if k == 1: return 0
    s=[1]
    q=deque([(s,0,1)])
    seen=set([1])
    while q:
      s,moves,su=q.popleft()
      # print(s,moves,su)
      seen.add(su)
      if su >= k: return moves
      for i,val in enumerate(s):
        # print(i)
        new_s=s[:]
        new_s[i]+=1
        if su+1 not in seen:
          q.append((new_s,moves+1,su+1))
          seen.add(su)
        new_s=s[:]
        new_s.append(s[i])
        if su+s[i] not in seen:
          q.append((new_s,moves+1,su+s[i]))
          seen.add(su)
    else:
      return -1
  
sol=Solution()
print(sol.minOperations(11))
print(sol.minOperations(1))