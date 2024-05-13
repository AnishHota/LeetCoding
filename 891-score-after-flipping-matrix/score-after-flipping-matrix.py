class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            flag = False
            for j in range(cols):
                if j==0 and grid[i][j]==0:
                    flag=True
                if flag:
                    if grid[i][j]==0:
                        grid[i][j]=1
                    elif grid[i][j]==1:
                        grid[i][j]=0
                        
        for j in range(cols):
            count_zeros = 0
            for i in range(rows):
                if grid[i][j]==0:
                    count_zeros+=1
            
            if count_zeros > rows/2:
                for i in range(rows):
                    if grid[i][j]==0:
                        grid[i][j]=1
                    else:
                        grid[i][j]=0
        
        print(grid)
        ans = 0
        for x in grid:
            str_x = ''.join(list(map(str,x)))
            str_x = int(str_x,2)
            ans+=str_x
        
        return ans