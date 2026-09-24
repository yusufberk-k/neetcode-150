# Two Sum
# status: solo | retry: -
# note: store num -> index, check complement with `in` (not get() == 0, since 0 is a valid index)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] not in seen:
                seen[nums[i]] = i
            else:
                return [seen[target-nums[i]], i]
