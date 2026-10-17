# Longest Repeating Character Replacement
# status: hint | retry: 2026-10-31
# note: missed that window is valid iff (window length - maxFreq) <= k; 
# maxFreq never needs to shrink, since only a bigger maxFreq can grow the answer

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        ml = 0
        
        maxFreq = 0
        l = 0
        for r, c in enumerate(s):
            seen[c] = seen.get(c, 0) + 1
            maxFreq = max(maxFreq, seen[c])

            while maxFreq + k < r-l+1:
                seen[s[l]] -= 1
                l += 1
            ml = max(ml, r-l+1)

        return ml
