"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return
        
        nodes = dict()
        edges = []

        queue = [node]
        seen = set()

        while queue:
            curr = queue.pop()
            if curr in seen:
                continue
            
            newNode = Node(curr.val)
            nodes[curr.val] = newNode
            seen.add(curr)

            for n in curr.neighbors:
                queue.append(n)
                edges.append((curr.val, n.val))
        
        for edge in edges:
            nodes[edge[0]].neighbors.append(nodes[edge[1]])
        return nodes[node.val]

