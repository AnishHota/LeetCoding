class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # adjmat = defaultdict(list)
        # for s,d,w in edges:
        #     adjmat[s].append((d,w))
        #     adjmat[d].append((s,w))
        
        # def dfs(i):
        #     dist = 0
        #     q = [(dist,i)]
        #     v = set()
        #     while q:
        #         dist_src,n = heappop(q)
        #         if n not in v:
        #             v.add(n)
        #             for d,w in adjmat[n]:
        #                 dist=dist_src+w
        #                 if dist<=distanceThreshold:
        #                     heappush(q,(dist,d))
        #     return len(v)-1
                    
        
        # ans = -1
        # min_nei = n
        # for i in range(n):
        #     neigh = dfs(i)
        #     if neigh<=min_nei:
        #         min_nei = neigh
        #         ans = i
        
        # return ans

        graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        for node in range(n):
            graph[node][node] = 0

        for s,d,dist in edges:
            graph[s][d] = dist
            graph[d][s] = dist
        
        for middle in range(n):
            for src in range(n):
                for dest in range(n):
                    graph[src][dest] = min(graph[src][dest],graph[src][middle]+graph[middle][dest])
        
        min_n = float('inf')
        res = -1
        for src in range(n):
            count=0
            for dest in range(n):
                if graph[src][dest]<=distanceThreshold:
                    count+=1
            
            if count<=min_n:
                min_n = count
                res = src
        
        return res




        

        
         
                    


