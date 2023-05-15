class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def helper(i,j):
            queue = collections.deque()
            queue.append([i,j])
            grid[i][j]="0"
            while queue:                
                cell = queue.popleft()
                i=cell[0]
                j=cell[1]
                if i-1>=0 and grid[i-1][j]=="1":
                    grid[i-1][j]="0"
                    queue.append([i-1,j])
                if i+1<len(grid) and grid[i+1][j]=="1":
                    grid[i+1][j]="0"
                    queue.append([i+1,j])
                if j-1>=0 and grid[i][j-1]=="1":
                    grid[i][j-1]="0"
                    queue.append([i,j-1])
                if j+1<len(grid[0]) and grid[i][j+1]=="1":
                    grid[i][j+1]="0"
                    queue.append([i,j+1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    helper(i,j)
        
        return count