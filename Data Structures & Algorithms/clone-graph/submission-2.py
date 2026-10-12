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
        def dfs(curr):

            if curr in nodes:
                return nodes[curr]
            
            nodes[curr] = Node(curr.val)
            for n in curr.neighbors:
                copied = dfs(n)
                nodes[curr].neighbors.append(copied)
            
            return nodes[curr]
        
        dfs(node)
        return nodes[node]

