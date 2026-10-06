# 3Sum
# status: solo | retry: -
# note: retry passed 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        seen = set()
        triplets = []
        for m in range(1, len(nums)-1):
            l, r = 0, len(nums) - 1
            target = -nums[m]
            while l < m and r > m:
                if target < nums[l] + nums[r]:
                    r -= 1
                elif target > nums[l] + nums[r]:
                    l += 1
                else:
                    if (nums[l], nums[r]) not in seen:
                        seen.add((nums[l], nums[r]))
                        triplets.append([nums[l], nums[m], nums[r]])
                    r -= 1
                    l += 1
        return triplets
