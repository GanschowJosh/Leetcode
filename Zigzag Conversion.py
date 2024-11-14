class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        curr = 0
        if numRows == 1:
            return s
        direction = -1

        for char in s:
            rows[curr] += char
            if curr == 0 or curr == numRows - 1: #reached the top or bottom
                direction *= -1
            curr += direction
    
        return ''.join(rows)