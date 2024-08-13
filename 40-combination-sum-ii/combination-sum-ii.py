class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.ans = []
        def backtrack(path,curr,i):
            if curr==target:
                self.ans.append(path[::])
                return
            if curr>target:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                backtrack(path+[candidates[j]],curr+candidates[j],j+1)
        
        backtrack([],0,0)
        return self.ans