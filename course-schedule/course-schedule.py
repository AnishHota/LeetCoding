class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses

        for x,y in prerequisites:
            graph[y].append(x)
            inDegrees[x]+=1

        queue = collections.deque([x for x in range(numCourses) if inDegrees[x]==0])
        topOrder = []
        while queue:
            node = queue.popleft()
            topOrder.append(node)
            for x in graph[node]:
                inDegrees[x]-=1
                if inDegrees[x]==0:
                    queue.append(x)

        return len(topOrder)==numCourses
        


        