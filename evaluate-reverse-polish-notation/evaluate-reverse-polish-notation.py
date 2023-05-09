class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x.replace('-','',1).isdigit():
                stack.append(x)
            
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if x=='+':
                    temp = a+b
                if x=='*':
                    temp = a*b
                if x=='/':
                    temp = int(a/b)
                if x=='-':
                    temp = a-b
                stack.append(temp)
        
        return int(stack[0])