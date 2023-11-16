class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        n = len(nums)
        pre.append(1)
        post.append(1)
        for i in range(1,n):
            pre.append(pre[i-1]*nums[i-1])
            post.append(post[i-1]*nums[n-i])
        
        post = post[::-1]
        ans = []
        for i in range(n):
            ans.append(pre[i]*post[i])
        
        return ans

        