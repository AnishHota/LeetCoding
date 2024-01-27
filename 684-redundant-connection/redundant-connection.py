class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent=[-1]*(len(edges)+1)
        def find(elem):
            while parent[elem]>0:
                elem=parent[elem]
            return elem
        
        def union(u,v):
            par_u = find(u)
            par_v = find(v)
            if par_u == par_v:
                return False
            parent[par_u]=par_v
            return True
        
        for edge in edges:
            x = union(edge[0],edge[1])
            if not(x):
                return edge

        