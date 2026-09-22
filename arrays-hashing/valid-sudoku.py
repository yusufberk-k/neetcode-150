# Valid Sudoku
# status: solo | retry: -
# note: [set()] * 3 creates 3 references to the same set; use a comprehension.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_seen = [[set() for _ in range(3)] for _ in range(3)]
        row_seen = [set() for _ in range(9)]
        col_seen = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                
                if val not in row_seen[row]:
                    row_seen[row].add(val)
                else: return False

                if val not in col_seen[col]:
                    col_seen[col].add(val)
                else: return False

                if val not in box_seen[row//3][col//3]:
                    box_seen[row//3][col//3].add(val)
                else: return False

        return True        
