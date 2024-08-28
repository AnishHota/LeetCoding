class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        r,c = len(grid1), len(grid1[0])

        def dfs(i,j):
            grid2[i][j]=0
            d =[[1,0],[0,1],[-1,0],[0,-1]]
            for x,y in d:
                if i+x>=0 and i+x<r and j+y>=0 and j+y<c and grid2[i+x][j+y]==1:
                    if grid1[i+x][j+y]==0:
                        self.flag=0
                    dfs(i+x,j+y)
                
        
        count=0
        for i in range(r):
            for j in range(c):
                if grid2[i][j]==1 and grid1[i][j]==1:
                    self.flag=1
                    dfs(i,j)
                    count+=self.flag
        
        return count