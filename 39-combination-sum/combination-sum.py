class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        comb,curr = [],[]
        def btrack(i,candidates,comb,curr,target):
            if target<0:
                return
            if target==0:
                comb.append(curr.copy())
                return
            if i>len(candidates)-1:
                return
            
            for j in range(i,len(candidates)):
                curr.append(candidates[j])
                btrack(j,candidates,comb,curr,target-candidates[j])
                curr.pop()

        btrack(0,candidates,comb,curr,target)
        return comb