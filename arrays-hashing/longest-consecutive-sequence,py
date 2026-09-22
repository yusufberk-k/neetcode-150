# Longest Consecutive Sequence
# status: hint | retry: -
# note: only start counting from a sequence head (num - 1 not in set). 
# Without that check every element restarts a scan and it degrades to O(n^2).

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)

        
        max_seq = 0
        for num in num_set:
            if num-1 not in num_set:
                st = num
                seq = 0
                while st in num_set:
                    seq += 1
                    st += 1
                max_seq = max(max_seq, seq)
            
        return max_seq
