# Longest Repeating Character Replacement
# status: solo | retry: -
# note: retry passed, sliding window: valid iff (r-l+1) - maxFreq <= k, else shrink from left;
# maxFreq never needs to decrease since only a bigger maxFreq can grow the answer, O(n) time O(1) space

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        ml = 0
        mf = 0
        l = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            mf = max(mf, seen[s[r]])

            while (r-l+1) > k+mf:
                seen[s[l]] -= 1
                l += 1
            ml = max(r-l+1, ml)
        return ml
