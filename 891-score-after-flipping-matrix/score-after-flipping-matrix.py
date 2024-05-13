class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            if grid[i][0]==0:
                for j in range(cols):
                    grid[i][j]=1-grid[i][j]

        for j in range(cols):
            count_zeros = 0
            for i in range(rows):
                if grid[i][j]==0:
                    count_zeros+=1
            
            if count_zeros > rows/2:
                for i in range(rows):
                    grid[i][j]=1-grid[i][j]
        
        ans = 0
        for x in grid:
            str_x = ''.join(list(map(str,x)))
            str_x = int(str_x,2)
            ans+=str_x
        
        return ans