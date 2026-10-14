# Search a 2D Matrix
# status: hint | retry: 2026-10-21
# note: treat matrix as one sorted array of m*n; 
# row = mid // n, col = mid % n. first try walked rows linearly -> O(m + log n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix[0])-1
        print(h)

        row = 0
        while l <= h and row < len(matrix):
            mid = l + (h-l) // 2
            r = matrix[row]
            if r[h] < target:
                row += 1
                l, h = 0, len(matrix[0])-1
                continue

            if r[mid] == target:
                return True

            elif r[mid] < target: 
                l = mid + 1
            
            else: 
                h = mid - 1
        return False
