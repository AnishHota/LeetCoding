class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i,x in enumerate(nums):
            if nums[abs(x)-1]<0:
                ans.append(abs(x))
            nums[abs(x)-1]*=-1
        
        return ans
        