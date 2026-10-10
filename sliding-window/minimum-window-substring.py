# Minimum Window Substring
# status: looked | retry: 2026-10-13
# note: need/have counters with shrink-while-valid; 
# decrement have before removing s[l] from the window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = 0
        
        f = [0] * 128
        for i in t:
            ind = ord(i)
            f[ind] += 1
        
        for j in f:
            if j > 0:
                need += 1
        
        fs = [0] * 128
        have = 0
        l = 0
        ms = ""
        ml = 99999999999999999999
        for r in range(len(s)):
            ind_r = ord(s[r])
            print(ind_r)
            fs[ind_r] += 1
            if f[ind_r] > 0 and f[ind_r] == fs[ind_r]:
                have += 1
            while have == need:
                ind_l = ord(s[l])
                if f[ind_l] > 0 and fs[ind_l] == f[ind_l]:
                    have -= 1
                if ml != min(ml, r-l+1):
                        ml = r-l+1
                        ms = s[l:r+1]
                fs[ind_l] -= 1
                l += 1
        
        return ms
