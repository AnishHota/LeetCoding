class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])


        def dfs(i,j,ind):
            if board[i][j]==word[ind] and ind==len(word)-1:
                return True

            if board[i][j]!=word[ind]:
                return False
            
            temp, board[i][j] = board[i][j],"*"
            inc = [(0,1),(0,-1),(1,0),(-1,0)]
            for x,y in inc:
                if (i+x>=0 and i+x<rows) and (j+y>=0 and j+y<cols) and (board[i+x][j+y]!="*"):
                    result = dfs(i+x,j+y,ind+1)
                    if result:
                        return True
            board[i][j]=temp

        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False
        