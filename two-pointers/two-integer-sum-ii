# Two Sum II - Input Array Is Sorted
# status: solo | retry: -
# note: no l < r guard, works only because a solution is guaranteed

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while l < len(numbers):
            while (target - numbers[l] <= numbers[r]):
                if target - numbers[l] == numbers[r]:
                    return [l+1,r+1]
                r -= 1
            l += 1
