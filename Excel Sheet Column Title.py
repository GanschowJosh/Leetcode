class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            result = chr(65 + remainder) + result
        return result

print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))