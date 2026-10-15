# Longest Consecutive Sequence
# status: solo | retry: -
# note: retry passed, first try TLE'd from looping over nums instead of seen;
# a duplicated head re-scans the whole run every time (0 x50k + 1..49999 -> 150s). loop over the set.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            seen.add(n)

        ml = 0
        for n in seen:
            if n-1 not in seen:
                l = 0
                i = n
                while i in seen:
                    i += 1
                    l += 1
                ml = max(l, ml)
        return ml
