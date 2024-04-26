class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])


        def find_min(arr):
            dp = []
            for ind,x in enumerate(arr):
                if len(dp)<2:
                    dp.append((x,ind))
                    dp.sort()
                elif x<=dp[1][0]:
                    dp.pop()
                    dp.append((x,ind))
                    dp.sort()
            return dp
        
        dp = find_min(grid[rows-1])

        for i in range(rows-2,-1,-1):
            for j in range(cols-1,-1,-1):
                if j!=dp[0][1]:
                    grid[i][j]+=dp[0][0]
                else:
                    grid[i][j]+=dp[1][0]
            dp = find_min(grid[i])
        
        return min(grid[0])