class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0]*numCourses
        for c,pre in prerequisites:
            graph[pre].append(c)
            inDegree[c]+=1
        
        q = deque([i for i in range(len(inDegree)) if inDegree[i]==0])
        visited = set()
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neigh in graph[node]:
                inDegree[neigh]-=1
                if inDegree[neigh]==0:
                    q.append(neigh)

        return len(visited)==numCourses
        
