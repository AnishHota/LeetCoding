from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(set)
        inEdges = [0]*numCourses
        def makeGraph(prereqs):

            for x in prereqs:
                graph[x[1]].add(x[0])
                inEdges[x[0]]+=1
        
        makeGraph(prerequisites)
        queue = deque()
        for i in range(numCourses):
            if inEdges[i]==0:
                queue.append(i)

        topSort = []
        while queue:
            node = queue.popleft()
            topSort.append(node)
            for neigh in graph[node]:
                inEdges[neigh]-=1
                if inEdges[neigh]==0:
                    queue.append(neigh)

        if len(topSort)!=numCourses:
            return False
        return True

        