class UnionFind:

    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self,x):

        while x!=self.par[x]:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
    
    def union(self,x1,x2):

        p1, p2 = self.find(x1), self.find(x2)

        if p1==p2:
            return False

        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        
        return True

class Solution:
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))

        emailAcc = {}

        for i,(_,*emails) in enumerate(accounts):
            for email in emails:
                if email in emailAcc:
                    uf.union(i,emailAcc[email])
                else:
                    emailAcc[email]=i
        
        emailGroup = defaultdict(list)

        for e,i in emailAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i,e in emailGroup.items():
            res.append([accounts[i][0]]+sorted(emailGroup[i]))
        
        return res






