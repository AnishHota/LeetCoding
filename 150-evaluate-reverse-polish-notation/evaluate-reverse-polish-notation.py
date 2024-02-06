class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+','-','*','/']
        stack = []
        for tok in tokens:
            if tok not in ops:
                stack.append(tok)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if tok==ops[0]:
                    stack.append(a+b)
                elif tok==ops[1]:
                    stack.append(a-b)
                elif tok==ops[2]:
                    stack.append(a*b)
                else:
                    stack.append(a/b)
        return int(stack[-1])

