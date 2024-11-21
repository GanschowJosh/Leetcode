class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_height = 0, len(height)-1, max(height)
        max_area = 0

        while l < r:
            max_area = max(max_area, min(height[l], height[r])*(r-l))

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
            if (r-l) * max_height < max_area: break
    
        return max_area