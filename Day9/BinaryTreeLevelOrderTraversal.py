from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        queue = deque()
        queue.append(root)
        res =[]
        while queue:
            qlen = len(queue)
            r1 = []
            for x in range(qlen):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    r1.append(node.val)
            if len(r1)!=0:
                res.append(r1)
        return res

        