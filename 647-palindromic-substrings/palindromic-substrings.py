class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        ans = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):

                if i==j:
                    dp[i][j]=1
                
                elif i+1==j:
                    if s[i]==s[j]:
                        dp[i][j]=1
                    else:
                        dp[i][j]=0
                
                elif dp[i+1][j-1]==1 and s[i]==s[j]:
                    dp[i][j]=1
                
                if dp[i][j]==1:
                    ans+=1
        
        return ans
        