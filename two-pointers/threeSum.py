# 3Sum
# status: looked | retry: 2026-09-28
# note: missed reducing to Two Sum II by fixing one element; 
# first try never moved l/r (infinite loop), then deduped by index instead of value


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        m = 1
        seen = set()
        while m < len(nums) - 1:
            l, r = 0, len(nums)-1
            
            while l < m and m < r:
                target = -nums[m]
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    if (nums[l],nums[r]) not in seen:
                        triplets.append([nums[l],nums[m],nums[r]])
                        seen.add((nums[l],nums[r]))

                    l+=1
                    r-=1
            m += 1
        return triplets
