# Find Minimum in Rotated Sorted Array
# status: looked | retry: 2026-10-21
# note: compare nums[m] with nums[hi], not nums[lo] (m can equal lo, so the check gives no info);
# use hi = m, not m-1, since m itself can be the minimum

'''
kanka fikir en buyuk ve en kucugu karsilastirip eger duzgun sira bozulduysa 
ortadaki kendinden onceki indeksteki sayidan kucuk olan sayiyi 
bulmak ama kodu yazamiyorum kendimi s***cem deliricem A**

SDOIHFPASOUIDHFASPUODIFASDF
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        if len(nums) <= 2:
            return min(nums)

        while nums[lo] > nums[hi]:
            m = lo + (hi-lo)//2
            if nums[m] > nums[hi]:
                lo = m+1
            else: 
                hi = m
        return nums[lo]
