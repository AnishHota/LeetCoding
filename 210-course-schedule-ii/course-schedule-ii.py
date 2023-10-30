class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = [[] for _ in range(numCourses)]
        inDegrees = [0]*numCourses
        def makeGraph(prereqs):
            for n in prereqs:
                graph[n[1]].append(n[0])
                inDegrees[n[0]]+=1
        
        makeGraph(prerequisites)
        queue = deque()
        for x in range(numCourses):
            if inDegrees[x]==0:
                queue.append(x)
        
        topSort = []
        while queue:
            node = queue.popleft()
            topSort.append(node)

            for neigh in graph[node]:
                inDegrees[neigh]-=1
                if inDegrees[neigh]==0:
                    queue.append(neigh)
        
        if len(topSort)!=numCourses:
            return []
        return topSort


        