class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        ans = ""
        for x in s:
            temp = ""
            if x!=")":
                stack.append(x)
            else:
                while stack[-1]!="(":
                    temp += stack.pop()[::-1]
                stack.pop()
                stack.append(temp)
        
        return ''.join(stack)
                
                