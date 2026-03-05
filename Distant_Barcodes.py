from collections import Counter
class Solution:
  def rearrangeBarcodes(self, barcodes):
    counter = Counter(barcodes)
    idx, n = 0, len(barcodes)
    out=[0]*n
    for k,v in counter.most_common():
      for _ in range(v):
        out[idx]=k
        idx+=2
        if idx>=n: idx=1
    return out
sol=Solution()
print(sol.rearrangeBarcodes([1,1,1,2,2,2]))