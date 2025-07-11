class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_idx = {}
        maxlen = 0
        start = 0
        for i, char in enumerate(s):
            if char in seen_idx and seen_idx[char] >= start:
                start = seen_idx[char] + 1
            seen_idx[char] = i
            maxlen = max(maxlen, i - start + 1)
        
        return maxlen