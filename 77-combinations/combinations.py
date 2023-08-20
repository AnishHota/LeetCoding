class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        comb,curr = [],[]
        def btrack(i,n,comb,curr):
            if len(curr)==k:
                comb.append(curr[:])
                return
            if i>n:
                return 
            
            for j in range(i,n+1):
                curr.append(j)
                btrack(j+1,n,comb,curr)
                curr.pop()
        
        btrack(1,n,comb,curr)
        return comb