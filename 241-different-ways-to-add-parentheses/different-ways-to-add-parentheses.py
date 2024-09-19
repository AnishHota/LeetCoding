class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        for i in range(len(expression)):
            if expression[i] in ["*","-","+"]:
                sub1 = expression[:i]
                sub2 = expression[i+1:]
                r1 = self.diffWaysToCompute(sub1)
                r2 = self.diffWaysToCompute(sub2)
                for x in r1:
                    for y in r2:
                        if expression[i]=="*":
                            res.append(int(x)*int(y))
                        elif expression[i]=="-":
                            res.append(int(x)-int(y))
                        else:
                            res.append(int(x)+int(y))
        
        if not res:
            res.append(int(expression))
    
        return res