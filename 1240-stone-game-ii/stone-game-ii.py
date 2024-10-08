class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        dp = [[0] * (n+1) for _ in range(n)]

        suf = [0]*n
        suf[-1] = piles[-1]

        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1]+piles[i]
        
        for i in range(n-1,-1,-1):
            for m in range(1,n+1):
                if i+2*m>=n:
                    dp[i][m] = suf[i]
                else:
                    for x in range(1,2*m+1):
                        dp[i][m] = max(dp[i][m],suf[i]-dp[i+x][max(x,m)])
        
        return dp[0][1]