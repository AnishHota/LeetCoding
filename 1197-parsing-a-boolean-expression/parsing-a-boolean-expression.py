class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        op = []
        stack = []
        ans = False

        for x in expression:
            if x in '&!|':
                op.append(x)
            elif x in '(ft':
                if x=='f':
                    stack.append(False)
                elif x=='t':
                    stack.append(True)
                else:
                    stack.append(x)
            elif x==')':
                oper = op.pop()
                temp = []
                while stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop()
                curr = temp[0]
                if oper=='!':
                    stack.append(not curr)
                elif oper=='|':
                    for i in range(1,len(temp)):
                        curr = curr | temp[i]
                    stack.append(curr)
                elif oper=='&':
                    for i in range(1,len(temp)):
                        curr = curr & temp[i]
                    stack.append(curr)
        return stack[-1]