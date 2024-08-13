class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        arr = sorted(candidates)
        self.ans = []
        def backtrack(path,curr,i):
            if curr==target:
                self.ans.append(path[::])
                return
            if i>=len(arr) or curr>target:
                return
            backtrack(path + [arr[i]],curr+arr[i],i+1)
            while i+1<len(arr) and (arr[i+1]==arr[i]):
                i+=1
            if i<len(arr):
                backtrack(path,curr,i+1)
            return
        
        backtrack([],0,0)
        return self.ans