class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        r, c = len(matrix), len(matrix[0])
        dp = []
        for x in matrix:
            dp.append(x[::])
        
        count=0
        for i in range(1,r):
            for j in range(1,c):
                if dp[i][j]==1:
                    if dp[i-1][j]>0 and dp[i][j-1]>0 and dp[i-1][j-1]>0:
                        dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
                    else:
                        dp[i][j]=1
        for i in range(r):
            for j in range(c):
                count += dp[i][j]

        return count
        