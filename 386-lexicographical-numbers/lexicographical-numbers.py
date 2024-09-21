class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        self.ans = []

        def dfs(i):
            if i>n:
                return
            self.ans.append(i)
            for x in range(10):
                temp = i*10+x
                dfs(temp)
            
            return
        
        end = min(n+1,10)
        for i in range(1,end):
            # self.ans.append(i)
            dfs(i)
        return self.ans
