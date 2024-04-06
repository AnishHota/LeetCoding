class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i,x in enumerate(s):
            if x=="(":
                stack.append((x,i))
            elif x==")":
                if stack and stack[-1][0]=="(":
                    stack.pop()
                else:
                    stack.append((x,i))
        
        rem_ind = []
        for x in stack:
            rem_ind.append(x[1])
        ans = ""
        for i,x in enumerate(s):
            if i not in rem_ind:
                ans+=str(x)
        
        return ans

