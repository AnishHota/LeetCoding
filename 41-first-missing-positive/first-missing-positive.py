class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,x in enumerate(nums):
            if x<0:
                nums[i]=0
        
        n = len(nums)
        for i,x in enumerate(nums):
            ind = abs(x)
            if ind<=n and ind!=0:
                if nums[ind-1]>=0:
                    nums[ind-1] = -1*nums[ind-1] if nums[ind-1]!=0 else -1*ind
        
        for i,x in enumerate(nums):
            if x>=0:
                return i+1
        return n+1