class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sub(s):
            if s<0: return 0
            l=0
            res=0
            for r in range(len(nums)):
                s-=nums[r]
                while s<0:
                    s+=nums[l]
                    l+=1
                res+=r-l+1
            return res
        
        return sub(goal)-sub(goal-1)
