class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        ans = []

        def bfs(land,i,j):
            q = deque()
            q.append((i,j))
            land[i][j]=0
            maxA,maxB = i,j
            while q:
                a,b = q.popleft()
                if a+1<rows and land[a+1][b]==1:
                    maxA = max(maxA,a+1)
                    maxB = max(maxB,b)
                    land[a+1][b]=0
                    q.append((a+1,b))
                if b+1<cols and land[a][b+1]==1:
                    maxA = max(maxA,a)
                    maxB = max(maxB,b+1)
                    land[a][b+1]=0
                    q.append((a,b+1))
            return maxA,maxB
            
        for i in range(rows):
            for j in range(cols):
                if land[i][j]==1:
                    group = [i,j]
                    a,b = bfs(land,i,j)
                    group += [a,b]
                    ans.append(group)
        
        return ans

