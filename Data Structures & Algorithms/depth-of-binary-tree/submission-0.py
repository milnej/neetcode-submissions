# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth):

            if node is None:
                return depth

            p1 = dfs(node.left, depth + 1)
            p2 = dfs(node.right, depth + 1)

            if p1 > p2:
                return p1
            else:
                return p2
        
        return dfs(root, 0)