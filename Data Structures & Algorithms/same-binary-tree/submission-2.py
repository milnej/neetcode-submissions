# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 or queue2:
            n1 = queue1.popleft()
            n2 = queue2.popleft()

            if not n1 and not n2:
                continue
            if n1 and not n2:
                return False
            if n2 and not n1:
                return False
            if n1.val != n2.val:
                return False
            
            queue1.append(n1.left)
            queue2.append(n2.left)
            queue1.append(n1.right)
            queue2.append(n2.right)
        
        return True

            