class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        OR = nums[0]
        for i in range(1,len(nums)):
            OR |= nums[i]
        
        return OR*(1<<(len(nums)-1))


        # Solution-2: Backtracking with/without including
        # def subsets(ind,xor):

        #     if ind>=len(nums):
        #         return xor
            
        #     a = subsets(ind+1,xor^nums[ind])
        #     b = subsets(ind+1,xor)
        #     return a+b
        
        # return subsets(0,0)

        # Solution-1: Backtracking: Subsets
        # self.ans = 0
        # self.res = []
        # def subsets(index, subset):
        #     temp_xor = subset[0] if subset else 0
        #     for i in range(1,len(subset)):
        #         temp_xor ^= subset[i]
        #     self.ans += temp_xor
        #     self.res.append(subset.copy())
        #     for i in range(index,len(nums)):
        #         subset.append(nums[i])
        #         subsets(i+1,subset)
        #         subset.pop()
            
        #     return self.res
            
        
        # subsets(0,[])
        # print(self.res)
        # return self.ans