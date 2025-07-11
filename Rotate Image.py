class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # analogous to mirroring the matrix along diagonal then mirroring along vertical
        n = len(matrix)
        # mirror along diagonal
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # mirror along vertical line
        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n-c-1] = matrix[r][n-c-1], matrix[r][c]