# https://leetcode.com/problems/maximum-matrix-sum

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        neg = 0
        min_abs = float('inf')
        total = 0
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                total += abs(num)
                if num < 0:
                    neg += 1
                min_abs = min(min_abs, abs(num))
        if neg % 2 == 0:
            return total
        return total - 2 * min_abs

sol = Solution()
print(sol.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))
print(sol.maxMatrixSum([[1,-1],[-1,1]]))