class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        maxGold = 0
        def dfs(i,j,visited,gold):
            nonlocal maxGold            
            visited.add((i,j))
            gold+=grid[i][j]
            maxGold = max(maxGold,gold)

            add = [(0,1),(1,0),(-1,0),(0,-1)]

            for x,y in add:
                if (i+x>=0 and i+x<rows) and (j+y>=0 and j+y<cols) and ((i+x,j+y) not in visited) and grid[i+x][y+j]!=0:
                    dfs(i+x,y+j,visited,gold)

            visited.remove((i,j))
            return maxGold
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0:
                    ans = max(ans,dfs(i,j,set(),0))
        
        return ans