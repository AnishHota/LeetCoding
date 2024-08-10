class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        square = [[0 for _ in range(n*3)] for _ in range(n*3)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]=='/':
                    square[i*3][j*3+2] = square[i*3+1][j*3+1] = square[i*3+2][j*3] = 1
                elif grid[i][j]=='\\':
                    square[i*3][j*3] = square[i*3+1][j*3+1] = square[i*3+2][j*3+2] = 1
        
        def dfs(i,j):
            if i<0 or i>=n*3 or j<0 or j>=n*3 or square[i][j]!=0:
                return
            square[i][j] = "#"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        ans = 0
        for i in range(n*3):
            for j in range(n*3):
                if square[i][j]==0:
                    ans += 1
                    dfs(i,j)
        
        return ans