from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        
        temp_k = abs(k)
        n = len(code)
        temp_k %= n
        if k > 0:
            res = []
            n = len(code)
            for i in range(n):
                total = 0
                for j in range(temp_k):
                    next_index = (i+j+1) % n
                    total += code[next_index]
                res.append(total)
            return res
        else:
            res = []
            for i in range(n):
                total = 0
                for j in range(temp_k):
                    prev_index = (i-j-1)%n
                    total += code[prev_index]
                res.append(total)
            return res
        