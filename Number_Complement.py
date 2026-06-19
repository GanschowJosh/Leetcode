class Solution:
  def findComplement(self, num: int) -> int:
    b=bin(num)[2:]
    o=[]
    for i,val in enumerate(b):
      if val=="1":
        o.append("0")
      if val=="0":
        o.append("1")
    return int("".join(o), base=2)

sol=Solution()
print(sol.findComplement(5))
print(sol.findComplement(1))