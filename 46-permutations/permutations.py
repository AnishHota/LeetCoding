class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(used, path):
            nonlocal ans
            if len(path)==len(nums):
                ans += [path[:]]
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    backtrack(used,path)
                    path.pop()
                    used[i]=False
        backtrack([False]*len(nums),[])

        return ans

        