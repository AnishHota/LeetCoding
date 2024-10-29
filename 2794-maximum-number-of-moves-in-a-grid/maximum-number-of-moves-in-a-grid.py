class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.count = 0
        self.ans = 0
        self.r, self.c = len(grid),len(grid[0])
        def move(i,j,seen,mov):
            seen.add((i,j))
            self.count = max(self.count,mov)
            if (i-1>=0 and j+1<self.c) and (grid[i][j]<grid[i-1][j+1]) and (i-1,j+1) not in seen:
                move(i-1,j+1,seen,mov+1)
            
            if (i>=0 and j+1<self.c) and (grid[i][j]<grid[i][j+1]) and (i,j+1) not in seen:
                move(i,j+1,seen,mov+1)
            
            if (i+1<self.r and j+1<self.c) and (grid[i][j]<grid[i+1][j+1]) and (i+1,j+1) not in seen:
                move(i+1,j+1,seen,mov+1)
        
        for i in range(self.r):
            self.count = 0
            move(i,0,set(),0)
            self.ans = max(self.ans,self.count)
        return self.ans
        