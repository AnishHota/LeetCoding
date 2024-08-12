class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])

        def count_islands():
            v = set()
            def dfs(i,j):
                if i<0 or i>=r or j<0 or j>=c or (i,j) in v or grid[i][j]!=1:
                    return
                v.add((i,j))
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
            
            count = 0
            for i in range(r):
                for j in range(c):
                    if grid[i][j]==1 and (i,j) not in v:
                            count+=1
                            dfs(i,j)
            
            return count
        
        count_first = count_islands()
        if count_first>1 or count_first==0:
            return 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    grid[i][j]=0
                    count = count_islands()
                    if count>1 or count==0:
                        return 1
                    grid[i][j]=1
        return 2

        


