class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for x,y in stones:
            adj[x].append(~y)
            adj[~y].append(x)
        
        self.visited = set()

        def dfs(i):
            self.visited.add(i)
            for neigh in adj[i]:
                if neigh not in self.visited:
                    dfs(neigh)
        
        count=0
        for x,y in stones:
            if x not in self.visited:
                dfs(x)
                count+=1
        
        return len(stones)-count

        
