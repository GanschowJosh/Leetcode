class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mod_map = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 0: 'Z'
        }
        result = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            result = chr(65 + remainder) + result
        return result