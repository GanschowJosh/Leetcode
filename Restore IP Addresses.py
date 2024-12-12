from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path, s):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            for i in range(1, 4):
                if start+i > len(s):
                    break
                if i > 1 and s[start] == '0':
                    break
                num = int(s[start:start+i])
                if num > 255:
                    break
                backtrack(start+i, path+[s[start:start+i]], s)
        res = []
        backtrack(0, [], s)
        return res

print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("0000"))
print(Solution().restoreIpAddresses("101023"))