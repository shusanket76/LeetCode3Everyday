# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root, val):
            if not root:
                root = TreeNode(val)
                return root

            if root.val<val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root
                else:
                    insert(root.right, val)
                    return root
            else:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root
                else:
                    insert(root.left, val)
                    return root


        return insert(root, val) 
         
        