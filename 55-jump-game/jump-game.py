class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        steps = nums[0]

        for curr in nums[1:]:
            if steps==0:
                return False
            steps-=1
            steps = max(curr, steps)
        
        return True
