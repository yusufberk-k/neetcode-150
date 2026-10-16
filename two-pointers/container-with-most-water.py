# Container With Most Water
# status: solo | retry: -
# note: retry passed, solved in seconds; moving the shorter wall is now automatic
# (taller side can't help: width shrinks, height stays capped by the shorter wall)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        mw = 0
        while l < r:
            w = min(heights[l], heights[r]) * (r-l)
            if min(heights[l], heights[r]) == heights[r]:
                r -= 1
            else: l += 1
            mw = max(mw,w)

        return mw
