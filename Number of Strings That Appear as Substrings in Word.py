class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """num = 0
        for item in patterns:
            if item in word:
                num+=1
        return num"""
        return sum(1 for pattern in patterns if pattern in word)
