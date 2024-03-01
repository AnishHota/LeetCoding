class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = 1
        post = 1
        result = [1 for _ in range(len(nums))]
        k = len(nums)
        for i in range(k):
            result[i]*=pre
            pre = pre*nums[i]
            result[k-i-1]*=post
            post*=nums[k-i-1]
    
        return result