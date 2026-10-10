# Permutation in String
# status: hint | retry: 2026-10-17
# note: couldn't see how to hold the ascii table as a list; [0] * 128 indexed by ord(c).
# shrink while fs[c] > f[c]; window length == len(s1) means it's a permutation

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f = [0] * 128

        l = 0

        for i in s1:
            f[ord(i)] += 1


        fs = [0] * 128
        for r in range(len(s2)):
            idx_r = ord(s2[r])
            idx_l = ord(s2[l])
            if f[idx_r] == 0:
                fs = [0] * 128
                l = r+1
                continue

            fs[idx_r] += 1

            while fs[idx_r] > f[idx_r]:
                fs[idx_l] -= 1
                l += 1
                idx_l = ord(s2[l])

            if r-l+1 == len(s1):
                return True

            
        return False
