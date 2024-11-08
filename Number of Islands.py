class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == "1":
                visited[x][y] = True
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count+=1
        
        return count