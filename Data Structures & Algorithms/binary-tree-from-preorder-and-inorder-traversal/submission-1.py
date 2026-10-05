# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        if n == 0:
            return []

        inorderNodes = dict()
        for i in range(n):
            inorderNodes[inorder[i]] = i

        self.preOrderIndex = -1
        def build(l, r):

            if l > r:
                return
        
            self.preOrderIndex += 1
            if self.preOrderIndex >= n:
                return
            currNodeVal = preorder[self.preOrderIndex]    
            currNode = TreeNode(currNodeVal)

            mid = inorderNodes[currNodeVal]

            currNode.left = build(l, mid-1)
            currNode.right = build(mid+1, r)

            return currNode
        return build(0, n-1)


