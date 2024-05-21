class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        
        def sub(index, subs):
            if index>=len(nums):
                self.res.append(subs.copy())
                return
            subs.append(nums[index])
            sub(index+1,subs)
            subs.pop()
            sub(index+1,subs)
            return subs

        sub(0,[])
        return self.res