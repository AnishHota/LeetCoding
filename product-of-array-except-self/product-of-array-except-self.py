class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [None]*len(nums)
        res[0] = 1
        for i in range(1,len(nums)):
            res[i]=pre*nums[i-1]
            pre = pre*nums[i-1]

        for i in range(len(nums)-1,-1,-1):
            res[i]=post*res[i]
            post = post*nums[i]
        
        return res
