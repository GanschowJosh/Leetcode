class Solution:
  def maxActiveSectionsAfterTrade(self, s: str) -> int:
    blocks=[]
    curr=s[0]
    clen=1
    num_ones = 0
    for i in range(len(s)-1):
      i+=1
      if s[i]==curr:
        clen+=1
      else:
        if clen==0: continue
        if curr=='1':
          num_ones+=clen
        blocks.append((curr,clen))
        curr=s[i]
        clen=1
    if clen!=0:
      blocks.append((curr,clen))
      if curr=='1':
        num_ones+=clen
    # print(blocks)

    longest=0
    lidx=None
    for i, block in enumerate(blocks):
      if i==0 or i>=len(blocks)-1: continue
      if block[0]=='0': continue
      if blocks[i-1][0]!='0' or blocks[i+1][0]!='0': continue
      cl=blocks[i-1][1]+blocks[i+1][1]
      #print(block, cl)
      if cl > longest:
        longest=cl
        lidx=i

    #print(lidx)
    if longest != 0:
      ll = blocks[lidx-1][1]
      lr = blocks[lidx+1][1]
      num_ones+=(ll+lr)
    return num_ones

sol=Solution()
print(sol.maxActiveSectionsAfterTrade("01"))
print(sol.maxActiveSectionsAfterTrade("0100"))
print(sol.maxActiveSectionsAfterTrade("1000100"))
print(sol.maxActiveSectionsAfterTrade("01010"))
print(sol.maxActiveSectionsAfterTrade("0100110110"))
print(sol.maxActiveSectionsAfterTrade("01101001"))
print(sol.maxActiveSectionsAfterTrade("00100111011"))