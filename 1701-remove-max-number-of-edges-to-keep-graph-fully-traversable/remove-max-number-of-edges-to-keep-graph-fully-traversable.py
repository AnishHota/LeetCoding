class UF:
    def __init__(self,n):
        self.n = n
        self.par = [i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self,x):
        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self,x1,x2):
        par1 = self.find(x1)
        par2 = self.find(x2)
        if par1==par2:
            return 0
        elif self.rank[par1]>self.rank[par2]:
            self.rank[par1]+=self.rank[par2]
            self.par[par2] = par1
        else:
            self.rank[par2]+=self.rank[par1]
            self.par[par1]=par2
        self.n-=1
        return 1
    
    def isConnected(self):
        return self.n==1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
       
        alice = UF(n)
        bob = UF(n)
        cnt = 0
        for t,u,v in edges:
            if t==3:
                cnt+= (alice.union(u,v) | bob.union(u,v))
        
        for t,u,v in edges:
            if t==1:
                cnt+=alice.union(u,v)
            elif t==2:
                cnt+=bob.union(u,v)
        
        if bob.isConnected() and alice.isConnected():
            return len(edges)-cnt
        
        return -1