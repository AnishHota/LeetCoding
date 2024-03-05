class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {"(":")", "{":"}","[":"]"}
        for x in s:
            if x in "({[":
                stack.append(x)
            elif not stack or x!=op[stack[-1]]:
                return False
            else:
                stack.pop()
        
        if stack:
            return False
        return True
        