# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node):

            if node is None:
                return "N"
            
            return str(node.val) + serialize(node.left) + serialize(node.right)
        
        rootString = serialize(root)
        subRootString = serialize(subRoot)
        
        return subRootString in rootString