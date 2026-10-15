# Koko Eating Bananas
# status: looked | retry: 2026-10-22
# note: binary search on the answer (speed in 1..max(piles)), not on the array;
# if hours <= h, save m and go left to find a smaller speed

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo, hi = 1, max(piles)

        while lo <= hi:
            m = lo + (hi-lo)//2
            hours = 0
            for p in piles:
                hours += ceil(p/m)

            if hours <= h:
                hi = m-1
                pot = m
            else: 
                lo = m+1

        return pot
