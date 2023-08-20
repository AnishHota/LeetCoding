class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x in "([{":
                stack.append(x)
            if x in ")]}" and not stack:
                return False
            if x==")":
                if stack[-1]!="(":
                    return False
                else:
                    stack.pop()
            if x=="]":
                if stack[-1]!="[":
                    return False
                else:
                    stack.pop()
            if x=="}":
                if stack[-1]!="{":
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True