class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        stack = []
        def backtrack(nO,nC):
            if nO==nC==n:
                ans.append("".join(stack))
                return

            if nO<n:
                stack.append("(")
                backtrack(nO+1,nC)
                stack.pop()

            if nO>nC:
                stack.append(")")
                backtrack(nO,nC+1)
                stack.pop()
            
            
        backtrack(0,0)
        return ans