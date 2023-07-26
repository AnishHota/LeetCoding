class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totSum = sum(nums)
        if totSum%2!=0:
            return False
        
        sumFind = totSum//2
        dp = [False] * (sumFind+1)
        dp[0]=True
        for num in nums:
            for i in range(sumFind,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[-1]
        