class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if not edges:
            return [0]
        
        graph = defaultdict(list)

        for x in edges:
            graph[x[0]].append(x[1])
            graph[x[1]].append(x[0])

        leaf_nodes = []
        for nodes in graph:
            if len(graph[nodes])==1:
                leaf_nodes.append(nodes)
        
        total_nodes_count = len(graph)

        leaf_nodes_remove = leaf_nodes

        while total_nodes_count>2:
            total_nodes_count -= len(leaf_nodes)

            leaf_nodes_remove = []

            for node in leaf_nodes:
                neigh = graph[node].pop()
                graph[neigh].remove(node)

                if len(graph[neigh])==1:
                    leaf_nodes_remove.append(neigh)
                
            
            leaf_nodes = leaf_nodes_remove[::]
        
        return leaf_nodes_remove
