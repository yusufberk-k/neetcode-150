# Product of Array Except Self
# status: solo | retry: -
# note: retry passed, suff filled at its own index so no n-1-i mapping needed;
# O(1) extra space follow-up (reuse output as pref, running suffix var) not done yet

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        
        s = 1
        for i, n in enumerate(nums):
            
            pref[i] = s
            s *= n

        s = 1
        for i in range(len(nums)-1, -1, -1):
            
            suff[i] = s
            s *= nums[i]

        return [pref[i] * suff[i] for i in range(len(nums))]
