class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(list)

        for i,(s,d,w) in enumerate(edges):
            graph[s].append([d,w,i])
            graph[d].append([s,w,i])
        
        distances = [[float("inf")]*2 for _ in range(n)]
        distances[source][0]=distances[source][1]=0

        def djikstra(graph,edges,distances,source,diff,run):
            n = len(graph)
            h = [(0,source)]
            distances[source][run]=0
            while h:
                d,n = heappop(h)
                if d>distances[n][run]:
                    continue
                
                for neigh,w,i in graph[n]:
                    weigh = edges[i][2]
                    if weigh==-1:
                        weigh = 1
                    
                    if run==1 and edges[i][2]==-1:
                        new_w = diff+distances[neigh][0]-distances[n][1]
                        if new_w>weigh:
                            edges[i][2]=weigh=new_w
                    
                    if distances[neigh][run]>distances[n][run]+weigh:
                        distances[neigh][run] = distances[n][run]+weigh
                        heappush(h,(distances[neigh][run],neigh))

        djikstra(graph,edges,distances,source,0,0)
        difference = target-distances[destination][0]
        if difference<0:
            return []
        
        djikstra(graph,edges,distances,source,difference,1)
        
        if distances[destination][1]<target:
            return []

        for edge in edges:
            if edge[2]==-1:
                edge[2]=1
        
        return edges