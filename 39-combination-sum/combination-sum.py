class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        comb,curr = [],[]
        def btrack(i,candidates,comb,curr):
            if sum(curr)>target:
                return
            elif sum(curr)==target and curr not in comb:
                comb.append(curr.copy())
            if i>=len(candidates):
                return
            curr.append(candidates[i])
            btrack(i,candidates,comb,curr)
            curr.pop()
            btrack(i+1,candidates,comb,curr)
        
        btrack(0,candidates,comb,curr)
        return comb