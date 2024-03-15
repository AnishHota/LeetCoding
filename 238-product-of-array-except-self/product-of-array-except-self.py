class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = 1
        post = 1
        ans = [1 for _ in range(len(nums))]
        n = len(nums)
        for i,x in enumerate(nums):
            ans[i]*=pre
            ans[n-i-1]*=post
            pre *= x
            post *= nums[n-i-1]
        return ans
      