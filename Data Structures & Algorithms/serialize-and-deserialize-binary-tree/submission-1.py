# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        encoded = []


        def traverse(node):

            if not node:
                encoded.append("N")
                return

            encoded.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return '|'.join(encoded)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split('|')
        self.i = 0

        def dfs():
            val = vals[self.i]
            if val == "N":
                self.i += 1
                return
            curr = TreeNode(int(val))
            self.i += 1

            curr.left = dfs()
            curr.right = dfs()
            return curr

        return dfs()

        