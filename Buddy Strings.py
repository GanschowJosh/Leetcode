"""
Not difficult, but harder than I was expecting given
that it's an easy problem
"""
from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_length = len(s)
        goal_length = len(goal)
        if s_length != goal_length:
            return False
        
        swap_num = 0
        s_counter = Counter(s)
        goal_counter = Counter(goal)

        if s_counter != goal_counter:
            return False
        
        differences = sum(1 for i in range(s_length) if s[i] != goal[i])

        return differences == 2 or (differences == 0 and any(v > 1 for k, v in s_counter.items()))