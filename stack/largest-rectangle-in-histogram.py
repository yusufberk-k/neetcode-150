# Largest Rectangle in Histogram
# status: hint | retry: 2026-10-11
# note: couldn't see how to get both boundaries from a stack; 
# monotonic increasing stack, popper = right boundary, run it reversed for left

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        pref = [0] * len(heights)
        suff = [0] * len(heights)

        for i in range(len(heights)):
            while len(st) != 0 and heights[st[-1]] > heights[i]:
                pref[st[-1]] = i-1
                st.pop()
            st.append(i)

        while len(st) != 0:
            pref[st[-1]] = len(heights) - 1
            st.pop()
        

        for i in range(len(heights)-1, -1, -1):
            while len(st) != 0 and heights[st[-1]] > heights[i]:
                suff[st[-1]] = i+1
                st.pop()
            st.append(i)
        
        while len(st) != 0:
            suff[st[-1]] = 0
            st.pop()

        areas = [(pref[i] - suff[i] + 1)*heights[i] for i in range(len(heights))]

        return max(areas)
