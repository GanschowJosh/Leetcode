#from math import prod
#class ProductOfNumbers:

#  def __init__(self):
#    self.nums = []
#    self.pref = []

#  def add(self, num: int) -> None:
#    self.nums.append(num)
#    if self.pref:
#        self.pref.append(self.pref[-1]*(num if num else 1))
#    else:
#        self.pref.append(num)

#  def getProduct(self, k: int) -> int:
#    #kth=self.pref[len(self.pref)-k-1]
#    return prod(self.nums[-k:])

class ProductOfNumbers:

  def __init__(self):
    self.pref = []

  def add(self, num: int) -> None:
    #print(num, self.pref)
    if num == 0:
      self.pref=[]
    else:
      if self.pref:
        self.pref.append(int(self.pref[-1]*num))
      else:
        self.pref.append(num)

  def getProduct(self, k: int) -> int:
    #print(self.pref, k)
    if len(self.pref) < k:
      return 0
    else:
      if len(self.pref) == k: kth = 1
      else: kth=self.pref[len(self.pref)-k-1]
      return self.pref[-1]//kth
    

sol=ProductOfNumbers()
sol.add(3)
sol.add(0)
sol.add(2)
sol.add(5)
sol.add(4)
print(sol.getProduct(2))
print(sol.getProduct(3))
print(sol.getProduct(4))
sol.add(8)
print(sol.getProduct(2))