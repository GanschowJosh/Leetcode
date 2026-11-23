class Solution:
  def minInsertions(self, s: str) -> int:
    lstack=0
    ct=0
    i=0
    while i < len(s):
      if s[i]=='(':
        lstack+=1
      elif s[i]==')':
        if lstack:
          lstack-=1
          if i+1 < len(s) and s[i+1] == ')':
            i+=2
            continue
          else:
            ct += 1
        else:
          if i+1 < len(s) and s[i+1] == ')':
            ct+=1
            i+=2
            continue
          else:
            ct += 2
      i+=1
    if lstack:
      ct+=lstack*2
    return ct
sol=Solution()
print(sol.minInsertions("(()))"))
print(sol.minInsertions("())"))
print(sol.minInsertions("))())("))