from collections import deque, defaultdict
class Solution:
  def minCost(self, n: int, edges: list[list[int]]) -> int:
    start_state=(0,False,0) #node,used,cost
    q=deque([start_state])
    best=[float('inf') for _ in range(n)]
    best[0]=0
    graph=[[0]*n for _ in range(n)]
    for u,v,w in edges:
      graph[u][v]=w
    while q:
      curr_node, used, curr_cost = q.popleft()
      #print(curr_node, used, curr_cost)
      if best[curr_node]<curr_cost:
        continue
      for neighbor, w in enumerate(graph[curr_node]):
        if w==0: continue
        if best[neighbor]<curr_cost+w: continue
        new_state=(neighbor,used,curr_cost+w)
        best[neighbor]=curr_cost+w
        q.append(new_state)
      for neighbor,e in enumerate(graph):
        if neighbor==curr_node: continue
        if e[curr_node]==0: continue
        if best[neighbor]<curr_cost+(2*e[curr_node]): continue
        new_state=(neighbor,True,curr_cost+(2*e[curr_node]))
        best[neighbor]=curr_cost+(2*e[curr_node])
        q.append(new_state)
    return best[-1] if best[-1] < float('inf') else -1

sol=Solution()
print(sol.minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]))
print(sol.minCost(n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]))
print(sol.minCost(n = 4, edges = [[2,3,25],[2,1,18],[3,1,2]]))