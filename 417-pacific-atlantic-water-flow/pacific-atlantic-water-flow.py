class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        def dfs(heights,i,j):
            stack = []
            stack.append([i,j])
            pac,atl = 0,0
            visited = []
            while stack:
                height = stack.pop()
                visited.append([height[0],height[1]])
                if height[0]==0 or height[1]==0:
                    pac=1
                if height[0]==n-1 or height[1]==m-1:
                    atl=1
                if pac==1 and atl==1:
                    return True
                for (x,y) in [[0,1],[0,-1],[1,0],[-1,0]]:
                    new_i = height[0]+x
                    new_j = height[1]+y

                    if (new_i>=0 and new_i<n) and (new_j>=0 and new_j<m) and heights[height[0]][height[1]]>=heights[new_i][new_j] and [new_i,new_j] not in visited:
                        stack.append([new_i,new_j])
            
            return False



        ans = []
        for i in range(n):
            for j in range(m):
                if dfs(heights,i,j):
                    ans.append([i,j]) 
        
        return ans
        