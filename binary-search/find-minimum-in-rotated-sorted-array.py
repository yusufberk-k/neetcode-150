# Find Minimum in Rotated Sorted Array
# status: hint | retry: 2026-11-14
# note: retry solved it but took a hint for the optimal version.
# compare nums[m] with nums[r], not nums[l] (m can equal l, so the check gives no info);
# loop while l < r and use r = m, not m-1, since m itself can be the minimum

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m+1
            else: r = m
        return nums[l]
