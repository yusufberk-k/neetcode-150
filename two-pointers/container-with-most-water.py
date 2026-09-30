# Container With Most Water
# status: hint | retry: 2026-10-07
# note: missed why moving the shorter side is safe; 
# the taller side can't help since width shrinks and height stays capped by the shorter wall

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0 
        while(l < r):
            lv = heights[l]
            rv = heights[r]
            max_area = max(max_area, (r-l)*min(rv,lv))
            if min(rv,lv) == rv:
                r -= 1
            else: l += 1
        return max_area
