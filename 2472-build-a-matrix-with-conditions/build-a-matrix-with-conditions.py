class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        

        def dfs(node, graph, curr_path, visited, res):
            if node in curr_path:
                return False
            
            if node in visited:
                return True
            
            visited.add(node)
            curr_path.add(node)

            for neigh in graph[node]:
                if not dfs(neigh,graph,curr_path,visited,res):
                    return False
            
            curr_path.remove(node)
            res.append(node)
            return True
        
        def topo(edges):
            graph = defaultdict(list)

            for src,dest in edges:
                graph[src].append(dest)
            
            visited = set()
            curr_path = set()
            res = []
            for node in range(1,k+1):
                if not dfs(node,graph,curr_path,visited,res):
                    return []
            
            return res[::-1]
        
        row_order = topo(rowConditions)
        col_order = topo(colConditions)


        if not row_order or not col_order:
            return []

        val_pos = {}
        for i in range(1,k+1):
            val_pos[i] = [0,0]

        for ind,val in enumerate(row_order):
            val_pos[val][0] = ind
        for ind,val in enumerate(col_order):
            val_pos[val][1] = ind
        
        ans = [[0 for _ in range(k)] for _ in range(k)]

        for val in range(1,k+1):
            row, col = val_pos[val]
            ans[row][col] = val
        
        return ans

