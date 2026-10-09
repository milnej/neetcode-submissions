class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        class node:
            def __init__(self, val):
                self.val = val
                self.children = []
            
            def addEdge(self, node):
                self.children.append(node)
        
        nodes = dict()
        for edge in edges:
            if edge[0] not in nodes:
                nodes[edge[0]] = node(edge[0])
            if edge[1] not in nodes:
                nodes[edge[1]] = node(edge[1])
        
            nodes[edge[0]].addEdge(nodes[edge[1]])
            nodes[edge[1]].addEdge(nodes[edge[0]])
        
        seen = set()
        components = 0

        def search(node):

            if node in seen:
                return
            seen.add(node)

            for child in node.children:
                search(child)

        for val in nodes:
            node = nodes[val]
            if node in seen:
                continue
            
            search(node)
            components += 1
        
        return components + (n - len(seen))
            
            
