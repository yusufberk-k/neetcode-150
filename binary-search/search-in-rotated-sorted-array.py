# Search in Rotated Sorted Array
# status: solo | retry: -
# note: retry passed, one half around m is always sorted (nums[m] < nums[r] -> right half sorted);
# if target is in the sorted half's range search there, otherwise go to the other half -> O(log n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                if nums[m] <= target <= nums[r]:
                    if nums[m] == target:
                        return m
                    elif nums[r] == target:
                        return r
                    else: l = m+1
                else: r = m-1
            
            else: 
                if nums[l] <= target <= nums[m]:
                    if nums[m] == target:
                        return m
                    elif nums[l] == target:
                        return l
                    else: r = m-1
                else: l = m+1

        return -1
