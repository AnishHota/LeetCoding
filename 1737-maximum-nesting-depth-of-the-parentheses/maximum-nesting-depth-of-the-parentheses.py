class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for x in s:
            if x=="(":
                stack.append("(")
                if len(stack)>ans:
                    ans = len(stack)
            elif x==")":
                stack.pop()
        return ans
