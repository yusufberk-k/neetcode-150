# Longest Substring Without Repeating Characters
# status: solo | retry: -
# note: started with r=1 and hand-coded the len<=1 special case, unnecessary with r=0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        sub = 0
        l, r = 0, 1
        
        if len(s) == 0 or len(s) == 1:
            return len(s)

        seen.add(s[l])
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                sub = max(sub, len(seen))
                r += 1
            else:
                seen.remove(s[l])
                l += 1

        return sub
