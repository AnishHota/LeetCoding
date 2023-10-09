
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j))
        
        if not queue:
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1:
                        return -1
            return 0
        
        def bfs(queue):
            visited = set()
            mins=0
            while queue:
                qlen = len(queue)
                mins+=1
                for i in range(qlen):
                    a,b = queue.popleft()
                    visited.add((a,b))   
                    for (x,y) in [[0,-1],[0,1],[1,0],[-1,0]]:
                        if (0<=x+a<n and 0<=y+b<m) and (x+a,y+b) not in visited and grid[x+a][y+b]==1:
                            grid[x+a][y+b]=2
                            queue.append((x+a,y+b))
            return mins
        
        ans=bfs(queue)-1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return ans
        
