# Search a 2D Matrix
# status: solo | retry: -
# note: retry passed, treat matrix as one sorted array of rows*cols;
# row = m // cols, col = m % cols, then plain binary search -> O(log(m*n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        t = rows*cols

        l, r = 0, t-1
        while l <= r:
            m = l + (r-l)//2

            row = m//cols
            col = m%cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m-1
            else:
                l = m+1
        return False
