from collections import deque
from typing import List
class Solution:
  def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    parent=[i for i in range(n)]
    def find_set(v):
      if v!=parent[v]:
        parent[v]=find_set(parent[v])
      return parent[v]

    def union_sets(a,b):
      a=find_set(a)
      b=find_set(b)
      if a!=b:
        parent[b]=a

    def same_set(a,b):
      return find_set(a)==find_set(b)

    answer=[]
    
    for k in range(n-1):
      if nums[k+1]-nums[k]<=maxDiff: union_sets(k,k+1)

    for i, j in queries:
      answer.append(same_set(i,j))

    return answer

sol=Solution()
print(sol.pathExistenceQueries(n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]))
print(sol.pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]))