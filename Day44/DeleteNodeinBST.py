# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):


        def dfs(root, key):
            if not root:
                return root
            if root.val<key:
                root.right = dfs(root.right, key)
            elif root.val>key:
                root.left = dfs(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                else:
                    curr = root.right
                    while curr.left:
                        curr = curr.left
                    root.val = curr.val
                    root.right = dfs(root.right, root.val)
            return root

        return dfs(root, key)
        