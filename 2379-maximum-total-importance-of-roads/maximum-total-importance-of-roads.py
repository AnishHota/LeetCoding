class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)

        for x,y in roads:
            graph[x]+=1
            graph[y]+=1
        
        graph = dict(sorted(graph.items(), key = lambda x: x[1], reverse=True))
        
        ans = 0
        for x,y in graph.items():
            ans += graph[x]*n
            n-=1
        

        return ans
