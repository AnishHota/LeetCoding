class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def bfs(grid,i,j):
            q = deque()
            q.append((i,j))
            while q:
                a,b = q.popleft()
                grid[a][b]='x'
                if a-1>=0 and grid[a-1][b]=='1':
                    grid[a-1][b]='x'
                    q.append((a-1,b))
                if a+1<rows and grid[a+1][b]=='1':
                    grid[a+1][b]='x'
                    q.append((a+1,b))
                if b-1>=0 and grid[a][b-1]=='1':
                    grid[a][b-1]='x'
                    q.append((a,b-1))
                if b+1<cols and grid[a][b+1]=='1':
                    grid[a][b+1]='x'
                    q.append((a,b+1))
        cnt =0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    cnt+=1
                    bfs(grid,i,j)
        return cnt