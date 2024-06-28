class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        graph = dict(sorted(graph.items(), key = lambda x: len(x[1]), reverse=True))
        
        for x,y in graph.items():
            graph[x]=n
            n-=1
        ans = 0
        for x,y in roads:
            ans += graph[x]+graph[y]

        return ans
