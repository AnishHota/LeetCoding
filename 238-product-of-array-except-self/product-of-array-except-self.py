class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1]
        post = [1]

        k = len(nums)-1
        for i in range(k):
            if i==0:
                pre.append(nums[i])
                post.append(nums[k-i])
            else:
                pre.append(nums[i]*pre[i])
                post.append(nums[k-i]*post[i])
        post = post[::-1]
        return [pre[i]*post[i] for i in range(len(pre))]