class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])

        def checkMatrix(r,c):
            if grid[r+1][c+1]!=5:
                return 0
            if grid[r][c]%2!=0 or grid[r+2][c+2]%2!=0 or grid[r+2][c]%2!=0 or grid[r][c+2]%2!=0:
                return 0
            rsum1 = sum(grid[r][c:c+3])
            rsum2 = sum(grid[r+1][c:c+3])
            rsum3 = sum(grid[r+2][c:c+3])
            if rsum1!=rsum2 or rsum2!=rsum3 or rsum3!=rsum1:
                return 0
            csum = []
            for i in range(c,c+3):
                s = 0
                for j in range(r,r+3):
                    if grid[j][i]==0 or grid[j][i]>9:
                        return 0
                    s += grid[j][i]
                if i>c and csum[-1]!=s:
                    return 0
                csum.append(s)
            return 1
                    
        ans = 0
        for i in range(r-2):
            for j in range(c-2):
                ans += checkMatrix(i,j)

        return ans