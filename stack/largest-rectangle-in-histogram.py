# Largest Rectangle in Histogram
# status: solo | retry: -
# note: retry passed; monotonic increasing stack, popper = right boundary, run it reversed for left;
# n / -1 sentinels drop the leftover-stack loops. if/else was redundant again, just while-pop then append

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pref = [len(heights)] * len(heights)
        suff = [-1] * len(heights)
        
        pst = []
        for i,n in enumerate(heights):
            if len(pst) == 0 or heights[pst[-1]] <= n:
                pst.append(i)

            else:
                while len(pst) != 0 and heights[pst[-1]] > n:
                    pref[pst.pop()] = i
                pst.append(i)

        sst = []
        for i in range(len(heights)-1, -1, -1):
            if len(sst) == 0 or heights[sst[-1]] <= heights[i]:
                sst.append(i)

            else:
                while len(sst) != 0 and heights[sst[-1]] > heights[i]:
                    suff[sst.pop()] = i
                sst.append(i)

        lr = 0
        for i in range(len(heights)):
            r = (pref[i]-suff[i]-1)*heights[i]
            lr = max(lr, r)

        return lr
