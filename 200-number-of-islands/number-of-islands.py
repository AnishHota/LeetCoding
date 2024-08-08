class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r,c = len(grid), len(grid[0])

        def dfs(grid,i,j):
            di = [[0,1],[1,0],[0,-1],[-1,0]]
            q = deque()
            q.append([i,j])

            while q:
                a,b = q.popleft()
                for x,y in di:
                    if (a+x>=0 and a+x<r) and (b+y>=0 and b+y<c) and (grid[a+x][b+y]=="1"):
                        grid[a+x][b+y]="0"
                        q.append([a+x,b+y])

        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    ans +=1
                    dfs(grid,i,j)
        
        return ans
