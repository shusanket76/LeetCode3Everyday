# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root1,root2):
            if not root1 and not root2:
                return
            val1=0
            val2=0
            if root1:
                val1=root1.val
            if root2:
                val2=root2.val
            val = val1+val2
            
            root = TreeNode(val)
            print(root)
            
            root.left = dfs(root1.left if root1 else None, root2.left if root2 else None)
            root.right = dfs(root1.right if root1 else None, root2.right if root2 else None)
      
            return root
        return dfs(root1, root2)

            