class Solution:
    def longestPalindrome(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    d[s[i:j]] = len(s[i:j])
        maximum = max(d, key=d.get)
        return maximum