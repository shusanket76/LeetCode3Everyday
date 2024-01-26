from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:

        queue = deque()
        queue.append(root)
        ans = root.val
        while queue:
            res = []
            qlen = len(queue)
            for x in range(qlen):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    res.append(node.val)
            ans = res[0]
        return ans
                
