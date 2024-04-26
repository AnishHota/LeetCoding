class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for i in range(rows-2,-1,-1):
            for j in range(cols-1,-1,-1):
                temp_arr = grid[i+1][:j]+grid[i+1][j+1:]
                grid[i][j]+=min(temp_arr)
        
        return min(grid[0])