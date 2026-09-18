# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node, val):

            if not node:
                return False
            
            if node.val == val:
                isEqual = checkEqual(node, subRoot)
            else:
                isEqual = False
            
            p1 = dfs(node.left, val)
            p2 = dfs(node.right, val)

            return p1 or p2 or isEqual
    
        def checkEqual(node1, node2):

            if not node1 and not node2:
                return True

            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                print(node1, node2)
                return False

            if node1.val != node2.val:
                return False

            return checkEqual(node1.left, node2.left) and checkEqual(node1.right, node2.right)
        
        return dfs(root, subRoot.val)
            