# Trapping Rain Water
# status: solo | retry: -
# note: retry passed; excluded i from pref/suff max fearing it'd break,
# but including it is fine: min(pref, suff) >= height[i] so water never goes negative, no `if a > 0` or edge skipping needed

class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0] * len(height)
        suff = [0] * len(height)

        mp = 0
        for i in range(1, len(height)-1):
            p = height[i-1]
            mp = max(mp, p)
            pref[i] = mp

        
        ms = 0
        for i in range(len(height)-2, 0, -1):
            s = height[i+1]
            ms = max(ms, s)
            suff[i] = ms


        ta = 0
        for i in range(1, len(height)-1):
            a = min(pref[i], suff[i]) - height[i]
            if a > 0:
                ta += a

        return ta
