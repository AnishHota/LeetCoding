class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        arr = sorted(candidates)
        self.ans = []
        def backtrack(path,curr,i):
            if curr==target:
                self.ans.append(path[::])
                return
            if curr>target:
                return
            for j in range(i,len(arr)):
                if j>i and arr[j]==arr[j-1]:
                    continue
                backtrack(path+[arr[j]],curr+arr[j],j+1)
        
        backtrack([],0,0)
        return self.ans