class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjmat = defaultdict(list)
        for s,d,w in edges:
            adjmat[s].append((d,w))
            adjmat[d].append((s,w))
        
        def dfs(i):
            dist = 0
            q = [(dist,i)]
            v = set()
            while q:
                dist_src,n = heappop(q)
                if n not in v:
                    v.add(n)
                    for d,w in adjmat[n]:
                        dist=dist_src+w
                        if dist<=distanceThreshold:
                            heappush(q,(dist,d))
            return len(v)-1
                    
        
        ans = -1
        min_nei = n
        for i in range(n):
            neigh = dfs(i)
            if neigh<=min_nei:
                min_nei = neigh
                ans = i
        
        return ans
        

        
         
                    


