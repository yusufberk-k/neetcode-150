# Koko Eating Bananas
# status: solo | retry: -
# note: retry passed, binary search on the answer (speed in 1..max(piles)).
# th > h means too slow, go right; otherwise m works, save it in pa and go left for a smaller one.

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        
        l, hi = 1, max(piles)
        pa = 0
        while l <= hi:
            m = l + (hi-l)//2
            th = 0
            for p in piles:
                th += ceil(p/m)
            
            if th > h:
                l = m+1

            else: 
                pa = m
                hi = m-1
        
        return pa
