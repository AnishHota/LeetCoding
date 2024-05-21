class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        
        def sub(index, subs):
            self.res.append(subs.copy())

            for i in range(index,len(nums)):
                subs.append(nums[i])
                sub(i+1,subs)
                subs.pop()

        sub(0,[])
        return self.res