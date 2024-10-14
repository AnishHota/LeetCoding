class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,x in enumerate(rooms):
            graph[i] += x
        
        n = len(rooms)
        visited = set()
        q = deque([0])

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    q.append(neigh)
        
        if len(visited)!=n:
            return False
        
        return True