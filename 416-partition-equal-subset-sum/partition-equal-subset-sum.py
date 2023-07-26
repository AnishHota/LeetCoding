class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totSum = sum(nums)
        if totSum%2!=0:
            return False
        
        sumFind = totSum//2
        dp = [[False for x in range(sumFind+1)] for y in range(len(nums))]

    #1st Column
        for i in range(len(nums)):
            dp[i][0] = True
    
    #1st row everything false except that number
        for j in range(sumFind):
            if j==nums[0]:
                dp[0][j]=True

        for i in range(len(nums)):
            for j in range(sumFind+1):
                if (j-nums[i])>=0:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[-1][-1]
        