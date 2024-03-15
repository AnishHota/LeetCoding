class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1]
        post = [1]
        n = len(nums)
        for i,x in enumerate(nums):
            if i==0:
                pre.append(x)
                post.append(nums[n-i-1])
            else:
                pre.append(x*pre[i])
                post.append(post[i]*nums[n-i-1])
        
        ans = []
        post = post[::-1]
        for i in range(1,len(pre)):
            ans.append(pre[i-1]*post[i])
        return ans