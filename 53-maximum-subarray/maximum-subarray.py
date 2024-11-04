class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        s = curr

        for x in nums[1:]:
            curr += x
            curr = max(curr,x)
            s = max(curr,s)
        
        return s