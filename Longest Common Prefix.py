class Solution:
    def longestCommonPrefix(self, strs):
        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        return shortest_str
            