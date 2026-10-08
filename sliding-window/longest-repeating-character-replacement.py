# Longest Repeating Character Replacement
# status: looked | retry: 2026-10-11
# note: missed that window is valid iff (window length - maxFreq) <= k; 
# maxFreq never needs to shrink, since only a bigger maxFreq can grow the answer

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        maxFreq = 0
        ml = 0
        seen = {}

        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxFreq = max(maxFreq, seen[s[r]])

            while maxFreq+k < r-l+1:
                seen[s[l]] -= 1
                l += 1

            ml = max(ml, r-l+1)
            
            r += 1
        
        return ml
