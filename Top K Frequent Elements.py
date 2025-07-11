from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        d = {ke: v for ke, v in sorted(d.items(), key = lambda item: item[1], reverse=True)}

        out = []
        for ke, v in d.items():
            out.append(ke)
            if len(out) == k:
                break
        
        return out        