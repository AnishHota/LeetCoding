class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            isConnected[i][i]=0
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1:
                    isConnected[i][j]=0
                    dfs(j)

        r,c = len(isConnected),len(isConnected[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if isConnected[i][j]==1:
                    count+=1
                    dfs(i)
        
        return count