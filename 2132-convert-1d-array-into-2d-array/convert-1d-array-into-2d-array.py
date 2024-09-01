class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        
        if len(original)==1:
            return [[original[0]]]
        
        ans = [[0 for _ in range(n)] for _ in range(m)]

        p = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[p]
                p+=1
        
        return ans