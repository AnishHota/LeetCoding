class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        pre=1
        post=1
        ans = [1]*n
        for i in range(1,n):
            pre=pre*nums[i-1]
            ans[i]=ans[i]*pre
            post=post*nums[n-i]
            ans[n-i-1]=ans[n-i-1]*post
        
        return ans

        