# Sliding Window Maximum
# status: looked | retry: 2026-10-14
# note: keep the running max, re-sort the window only when the max slides out (O(nk log k) worst case);
# optimal is a monotonic decreasing deque of indices, O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= k:
            return [max(nums)]
        if k == 1:
            return nums
        l = 0
        r = k
        
        sub = sorted(nums[l:r])
        m = sub[-1]
        ms = []
        for r in range(k, len(nums)+1):

            
            if nums[r-1] > m:
                m = nums[r-1]
            ms.append(m)

            if nums[l] == m:
                m = sorted(nums[l:r])[-2]
            l+=1
            
            
        return ms
