from collections import Counter
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # Check rows and columns
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid_set = set()
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] != '.':
                            if board[i + x][j + y] in subgrid_set:
                                return False
                            subgrid_set.add(board[i + x][j + y])

        return True



         



ss= Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(ss.isValidSudoku(board=board))