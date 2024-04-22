class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        visited = set()
        graph = defaultdict(list)
        for x in edges:
            graph[x[0]].append(x[1])
            graph[x[1]].append(x[0])
        q = deque()
        q.append(source)
        visited.add(source)
        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            for x in graph[node]:
                if x not in visited:
                    q.append(x)
                    visited.add(x)
        
        return False
        