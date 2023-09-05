class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        area = 0
        n = len(grid)
        m = len(grid[0])
        print(n,m)

        def helper(grid,i,j):
            queue=deque()
            queue.append([i,j])
            count=1
            while queue:
                for p in range(len(queue)):
                    x,y = queue.popleft()
                    grid[x][y]=-1
                    for upd in ([0,1],[0,-1],[1,0],[-1,0]):
                        new_i = x+upd[0]
                        new_j = y+upd[1]
                        if (new_i>=0 and new_i<n) and (new_j>=0 and new_j<m) and grid[new_i][new_j]==1:
                            queue.append([new_i,new_j])
                            grid[new_i][new_j]=-1
                            count+=1
            return count

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    temp_area = helper(grid,i,j)
                    if temp_area>area:
                        area=temp_area
        
        return area

        