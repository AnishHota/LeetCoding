class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]

        inEdges = [0]*n
        parents_kids = defaultdict(list)
        for parent,kid in edges:
            ans[kid].add(parent)
            inEdges[kid]+=1
            parents_kids[parent].append(kid)
        
        dq = deque([i for i in range(n) if inEdges[i]==0])
        
        while dq:
            parent = dq.popleft()
            for kids in parents_kids[parent]:
                ans[kids].update(ans[parent])
                inEdges[kids]-=1
                if inEdges[kids]==0:
                    dq.append(kids)
        
        return [sorted(x) for x in ans]