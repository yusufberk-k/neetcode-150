# Minimum Window Substring
# status: solo | retry: -
# note: retry passed; need/have counters, shrink while valid, k only moves when fs crosses f exactly;
# chars not in t have f = 0 so no f > 0 check needed. use r-l+1 for length, not len(s[l:r+1])

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ms = ''
        ml = float('inf')
        f = [0] * 128
        n = 0
        for c in t:
            if f[ord(c)] == 0:
                n+= 1
            f[ord(c)] += 1

        l = 0
        k = 0
        fs = [0] * 128
        for r, c in enumerate(s):
            fs[ord(c)] += 1
            if fs[ord(c)] == f[ord(c)]:
                k += 1

            while k == n:
                if r-l+1 < ml:
                    ml = r - l + 1
                    ms = s[l:r+1]
                
                fs[ord(s[l])] -= 1
                if fs[ord(s[l])] < f[ord(s[l])]:
                    k -= 1
                
                l += 1
        
        return ms
