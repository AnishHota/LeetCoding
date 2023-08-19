class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i,nums,subset,currset):
            if i>=len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            helper(i+1,nums,subset,currset)

            currset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1,nums,subset,currset)
        
        nums.sort()
        subset,currset = [],[]
        helper(0,nums,subset,currset)
        return subset