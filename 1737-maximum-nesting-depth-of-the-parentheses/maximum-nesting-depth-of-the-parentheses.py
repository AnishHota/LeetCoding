class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        ans = 0
        for x in s:
            if x=="(":
                stack+=1
                ans = max(ans,stack)
            elif x==")":
                stack-=1
        return ans
