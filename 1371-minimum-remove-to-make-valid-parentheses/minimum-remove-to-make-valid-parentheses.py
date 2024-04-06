class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rem_ind = set()
        for i,x in enumerate(s):
            if x=="(":
                stack.append(i)
            elif x==")":
                if stack:
                    stack.pop()
                else:
                    rem_ind.add(i)
        
        rem_ind.update(stack)
        ans = ""
        for i,x in enumerate(s):
            if i not in rem_ind:
                ans+=str(x)
        
        return ans

