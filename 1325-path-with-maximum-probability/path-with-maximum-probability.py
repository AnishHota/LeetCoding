class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for i,(x,y) in enumerate(edges):
            graph[x].append((y,succProb[i]))
            graph[y].append((x,succProb[i]))
        
        has = defaultdict(int)
        
        heap = []

        heapq.heappush(heap,(-1,start_node))
 
        while heap:
            cost,node = heapq.heappop(heap)
            if node==end_node:
                return -1*cost
            if node in has:
                continue
            has[node] = -1*cost
            for neigh,prob in graph[node]:
                if neigh not in has:
                    heapq.heappush(heap,(cost*prob,neigh))
        
        return has[end_node]

