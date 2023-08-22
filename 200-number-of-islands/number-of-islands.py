class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r,c = len(grid),len(grid[0])
        def dfs(grid,i,j):
            if i>=0 and i<r and j>=0 and j<c:
                if grid[i][j]=='1':
                    grid[i][j]='2'
                    dfs(grid,i-1,j)
                    dfs(grid,i,j-1)
                    dfs(grid,i+1,j)
                    dfs(grid,i,j+1)
                else:
                    return
            else:
                return
        
        count = 0
        for x in range(r):
            for y in range(c):
                if grid[x][y]=='1':
                    count+=1
                    dfs(grid,x,y)
        
        return count

        