# Search in Rotated Sorted Array
# status: looked | retry: 2026-10-24
# note: one half around m is always sorted (nums[l] <= nums[m] -> left half); check if target is inside
# the sorted half's range, otherwise go to the other half. first try: found pivot like 153, then binary searched one side

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:              # sol yarı sıralı
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:                               # sağ yarı sıralı
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1


        while nums[lo] > nums[hi]:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else: 
                hi = mid

        if target > nums[-1]:
            l, h = 0, len(nums[:lo])-1
            while l <= h:
                m = l + (h-l)//2
                if nums[m] > target:
                    h = m-1
                elif nums[m] < target:
                    l = m+1
                elif target == nums[m]:
                    return m
        
        
        else: 
            l, h = lo, len(nums[lo:])+lo-1
            while l <= h:
                m = l + (h-l)//2
                if nums[m] > target:
                    h = m-1
                elif nums[m] < target:
                    l = m+1
                elif nums[m] == target:
                    return m
        return -1
'''
