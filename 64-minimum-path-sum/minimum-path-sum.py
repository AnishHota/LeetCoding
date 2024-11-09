class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.ans = float('inf')
        self.r, self.c = len(grid), len(grid[0])
        for i in range(self.r):
            for j in range(self.c):
                a = float('inf')
                b = float('inf')
                if i-1>=0:
                    a = grid[i-1][j]
                if j-1>=0:
                    b = grid[i][j-1]
                if min(a,b)!=float('inf'):
                    grid[i][j]+=min(a,b)
        
        return grid[self.r-1][self.c-1]