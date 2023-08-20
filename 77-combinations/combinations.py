class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        comb,curr = [],[]
        def btrack(i,n,comb,curr,k):
            if k==0:
                comb.append(curr.copy())
                return
            if i>n:
                return 
            
            for j in range(i,n+1):
                curr.append(j)
                btrack(j+1,n,comb,curr,k-1)
                curr.pop()
        
        btrack(1,n,comb,curr,k)
        return comb