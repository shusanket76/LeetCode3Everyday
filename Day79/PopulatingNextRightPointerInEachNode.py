from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        queue = deque()
        res = []
        if root:
            queue.append(root)
            while queue:
                q = len(queue)
                for x in range(q):
                    
                    node = queue.popleft()
                    res.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        
                    if x+1!=q:
                        
                        node.next = queue[0]
        return root
        