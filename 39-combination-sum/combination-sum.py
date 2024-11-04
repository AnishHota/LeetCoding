class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def helper(ind,curr):
            if sum(curr)==target:
                ans.append(curr.copy())
                return
            
            if sum(curr)>target:
                return
            if ind>=len(candidates):
                return
            curr.append(candidates[ind])
            helper(ind,curr)
            curr.pop()
            helper(ind+1,curr)
        
        helper(0,[])
        return ans
        