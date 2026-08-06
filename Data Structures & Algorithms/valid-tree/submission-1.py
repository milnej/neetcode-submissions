class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Create the graph from the edges
        graph = {i: [] for i in range(n)}
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)
    
        seen = set()
        def search(graph, seen, node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            children = graph[node]
            for child in children:
                if child != prev and not search(graph, seen, child, node):
                    return False
            
            return True

        return search(graph, seen, 0, None) and len(seen) == n