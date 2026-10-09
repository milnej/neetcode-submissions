from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()
        def search(node):
            if node in seen:
                return
            seen.add(node)
            for child in adj[node]:
                search(child)

        comp = 0
        for node in adj:
            if node in seen:
                continue
            search(node)
            comp += 1
        return comp + (n - len(seen))

            
