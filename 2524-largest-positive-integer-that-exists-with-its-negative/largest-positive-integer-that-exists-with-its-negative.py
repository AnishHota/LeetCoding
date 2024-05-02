class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = set()
        ans = float('-inf')
        for x in nums:
            if x*-1 in d:
                if x<0 and x*-1>ans:
                    ans = x*-1
                elif x>ans:
                    ans = x
            d.add(x)

        if ans==float('-inf'):
            return -1
        return ans

        