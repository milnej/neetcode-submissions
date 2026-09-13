# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        l = []

        def createList(node):
            
            if node.left:
                createList(node.left)
            l.append(node.val)
            if node.right:
                createList(node.right)
        
        createList(root)

        return l[k-1]