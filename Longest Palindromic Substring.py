#O(n^3) solution
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    d[s[i:j]] = len(s[i:j])
        maximum = max(d, key=d.get)
        return maximum
"""

#O(n) solution using Manacher's algorithm
class Solution:
    def longestPalindrome(s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]