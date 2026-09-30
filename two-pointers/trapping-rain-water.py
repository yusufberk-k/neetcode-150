# Trapping Rain Water
# status: hint | retry: 2026-10-07
# note: missed the core idea: water at i = min(max left, max right) - height[i]; prefix/suffix max arrays give it in O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        suffix = [0] * len(height)
        prefix = []

        max_suffix = 0
        for i in range(len(height)-1, -1 ,-1):
            max_suffix = max(max_suffix, height[i])
            suffix[i] = max_suffix

        max_prefix = 0
        for i in range(len(height)):
            max_prefix = max(max_prefix, height[i])
            prefix.append(max_prefix)

        total_water = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            total_water += water

        return total_water
        