from collections import deque
class Solution:
  def shortestPathAllKeys(self, grid: list[str]) -> int:
    alphabet='abcdefghijklmnopqrstuvwxyz'
    neighbors=[
      [-1,0],
      [0,-1],[0,1],
      [1,0]
    ]
    n=len(grid)
    m=len(grid[0])
    k=0
    for i in range(n):
      for j in range(m):
        if grid[i][j]=='@': si,sj=i,j
        if grid[i][j] in alphabet: k += 1
    ss=(si,sj,"",0)
    seen=set()
    seen.add((si,sj,""))
    q=deque([ss])#ci,cj,#keys found,#moves
    while q:
      ci,cj,kf,mvs=q.popleft()
      #print(ci,cj,kf,mvs)
      if len(kf) == k: return mvs
      for di,dj in neighbors:
        ni,nj=di+ci,dj+cj
        if 0 <= ni < n and 0 <= nj < m:
          curr=grid[ni][nj]
          if curr=='#': continue
          if curr in alphabet.upper() and curr.lower() not in kf: continue
          nkf=kf
          if curr in alphabet and curr not in kf: nkf=kf+curr
          nkf="".join(sorted(nkf))
          nxt=(ni,nj,nkf,mvs+1)
          state=(ni,nj,nkf)
          if state in seen: continue
          seen.add(state)
          q.append(nxt)
    else:
      return -1

sol=Solution()
print(sol.shortestPathAllKeys(grid = ["@.a..","###.#","b.A.B"]))
print(sol.shortestPathAllKeys(grid = ["@..aA","..B#.","....b"]))
print(sol.shortestPathAllKeys(grid = ["@Aa"]))
print(sol.shortestPathAllKeys(grid = ["@...a",".###A","b.BCc"]))
print(sol.shortestPathAllKeys(grid = ["@abcdeABCDEFf"]))