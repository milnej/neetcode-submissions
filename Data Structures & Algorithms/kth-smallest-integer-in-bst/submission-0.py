# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        allVals = [False]*10001

        def explore(node):
            if not node:
                return
            allVals[node.val] = True
            explore(node.left)
            explore(node.right)
        
        explore(root)

        count = 0
        for i in range(10001):
            if allVals[i]:
                count += 1
                if count == k:
                    return i