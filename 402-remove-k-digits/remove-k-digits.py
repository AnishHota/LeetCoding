class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for x in num:
            if stack:
                while stack and x<stack[-1] and k!=0:
                    k-=1
                    stack.pop()
            stack.append(x)
        
        stack = stack[:-k] if k!=0 else stack

        stack = ''.join(stack).lstrip('0')

        return stack if stack else "0"
        