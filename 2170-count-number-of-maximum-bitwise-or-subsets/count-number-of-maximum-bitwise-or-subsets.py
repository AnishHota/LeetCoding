class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.target = 0
        for x in nums:
            self.target |= x
        
        self.ans = 0

        def backtrack(ind,currOr):
            if currOr==self.target:
                self.ans+=1
            for i in range(ind,len(nums)):
                backtrack(i+1,currOr | nums[i])

        backtrack(0,0)
        return self.ans      