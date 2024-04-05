class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for x in s:
            if stack and x.lower()==stack[-1].lower() and x!=stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        
        return ''.join(stack)
        