class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        self.res = []
        def subsets(index, subset):
            temp_xor = subset[0] if subset else 0
            for i in range(1,len(subset)):
                temp_xor ^= subset[i]
            self.ans += temp_xor
            self.res.append(subset.copy())
            for i in range(index,len(nums)):
                subset.append(nums[i])
                subsets(i+1,subset)
                subset.pop()
            
            return self.res
            
        
        subsets(0,[])
        print(self.res)
        return self.ans