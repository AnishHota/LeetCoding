class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[(i//3)*3+(j//3)]:
                        return False
                    else:
                        rows[i].append(board[i][j])
                        cols[j].append(board[i][j])
                        box[(i//3)*3+(j//3)].append(board[i][j])
        
        return True


        