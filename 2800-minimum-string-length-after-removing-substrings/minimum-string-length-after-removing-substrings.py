class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for x in s:
            if x == 'B':
                if stack and stack[-1]=='A':
                    stack.pop()
                else:
                    stack.append(x)
            elif x == 'D':
                if stack and stack[-1]=='C':
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        
        return len(stack)