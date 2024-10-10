class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i,x in enumerate(nums):
            if not stack or nums[stack[-1]]>x:
                stack.append(i)
 
        n = len(nums)
        res = 0
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                res = max(res,i-stack.pop())
        
        return res