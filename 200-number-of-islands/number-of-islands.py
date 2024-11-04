class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.r, self.c = len(grid), len(grid[0])
        def helper(i,j):
            if grid[i][j]=="0":
                return
            
            grid[i][j]="#"

            d = [(0,1),(1,0),(0,-1),(-1,0)]

            for x,y in d:
                if 0<=i+x<self.r and 0<=j+y<self.c and grid[i+x][y+j]!="#":
                    helper(i+x,j+y)
        
        ans = 0
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j]=="1":
                    ans+=1
                    helper(i,j)
        
        return ans
