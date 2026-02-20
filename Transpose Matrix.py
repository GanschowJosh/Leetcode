class Solution:
    def transpose(self, matrix):
        n=len(matrix); m=len(matrix[0])
        out=[[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
          for j in range(n):
            out[i][j]=matrix[j][i]
        return out
sol=Solution()
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.transpose([[1,2,3],[4,5,6]]))