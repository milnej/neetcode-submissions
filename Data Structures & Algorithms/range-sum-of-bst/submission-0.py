# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):

            if node is None:
                return 0

            curr = 0
            if node.val >= low and node.val <= high:
                curr = node.val
            
            p1 = dfs(node.left)
            p2 = dfs(node.right)

            return p1 + p2 + curr
        

        return dfs(root)

