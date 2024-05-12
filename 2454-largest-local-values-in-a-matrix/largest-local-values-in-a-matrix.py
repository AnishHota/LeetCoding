class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(grid), len(grid[0])

        ans = [[0 for _ in range(rows-2)] for _ in range(cols-2)]
        for i in range(rows-2):
            for j in range(cols-2):
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        ans[i][j] = max(ans[i][j], grid[x][y])
        
        return ans
