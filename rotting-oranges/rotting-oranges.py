class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = collections.deque()

        freshO = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append([i,j])
                if grid[i][j]==1:
                    freshO +=1
        
        levels=0
        while queue and freshO>0:
            levels+=1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for i,j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                        freshO -= 1
                        grid[i][j]=2
                        queue.append([i,j])
        
        return -1 if freshO!=0 else levels
