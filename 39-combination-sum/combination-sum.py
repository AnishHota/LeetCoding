class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        curr = []
        def helper(ind,rem):
            if rem==0:
                ans.append(curr.copy())
                return
            if rem<0:
                return
            
            for i in range(ind,len(candidates)):
                if candidates[i]>rem:
                    continue
                curr.append(candidates[i])
                helper(i,rem-candidates[i])
                curr.pop()

        
        helper(0,target)
        return ans
        