class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i,nums,subset,currset):
            if i>=len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            helper(i+1,nums,subset,currset)
            currset.pop()
            helper(i+1,nums,subset,currset)
            
        subset, currset = [],[]
        helper(0,nums,subset,currset)
        return subset

        
        