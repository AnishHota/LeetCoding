class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*(len(nums)+1)
        post = [1]*(len(nums)+1)
        pre[0] = 1
        post[-1] = 1
        j = len(nums)-1
        res = []
        for i in range(len(nums)):
            pre[i+1] = (nums[i]*pre[i])
            post[j] = nums[j]*post[j+1]
            j-=1
        
        for i in range(1,len(nums)+1):
            res.append(pre[i-1]*post[i])

        return res