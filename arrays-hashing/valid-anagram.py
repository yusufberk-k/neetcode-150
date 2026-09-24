# Valid Anagram
# status: solo | retry: -
# note: early len(s) != len(t) check makes final empty-check unnecessary

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(l, 0) + 1

        for c in t:
            if freq.get(c, 0):
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
                continue
            return False
        
        if len(freq):
            return False
        return True
