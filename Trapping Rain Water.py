"""
FIRST HARD PROBLEM!!!!
kinda slow but uses a different approach than I found online
two dp arrays for all the left and right maxes
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        height_length = len(height)

        maxes_l = [0] * height_length
        maxes_l[0] = height[0]
        for i in range(1, height_length):
            maxes_l[i] = max(maxes_l[i-1], height[i])
        
        maxes_r = [0] * height_length
        maxes_r[-1] = height[-1]
        for i in range(height_length-2, -1, -1):
            maxes_r[i] = max(maxes_r[i+1], height[i])
        for i in range(1, len(height)-1):
            max_left = maxes_l[i]
            max_right = maxes_r[i]
            trapped += max(0, min(max_left, max_right)-height[i])
        
        return trapped