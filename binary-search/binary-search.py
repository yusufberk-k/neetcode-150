# Binary Search
# status: solo | retry: -
# note: l <= h with l = m+1 / h = m-1; 
# l + (h-l)//2 is a C++ overflow habit, plain (l+h)//2 is fine in Python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1

        while l <= h:
            m = l + (h-l)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else: 
                h = m-1

        return -1
