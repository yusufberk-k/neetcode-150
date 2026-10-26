# Permutation in String
# status: solo | retry: -
# note: retry passed, fixed-size window of len(s1) with need/have counters.
# have counts chars with m[c] >= mp[c]; no decrement on overshoot needed, since the window
# is at most len(s1) long, every char at >= means every char is exactly equal.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = {}
        need = 0
        for c in s1:
            if c not in mp:
                need += 1
            mp[c] = mp.get(c, 0) + 1
        k = len(s1)
        
        l = 0
        m = {}
        have = 0
        for r in range(len(s2)):
            m[s2[r]] = m.get(s2[r], 0) + 1
            if s2[r] in mp and m[s2[r]] == mp[s2[r]]:
                have += 1
            
            if r-l+1 > k:
                if s2[l] in mp and m[s2[l]] == mp[s2[l]]:
                    have -= 1
                m[s2[l]] -= 1
                l+=1
            if have == need: return True
        return False
