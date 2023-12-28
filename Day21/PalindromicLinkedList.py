from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        queue = deque()
        prev, curr = None, head
        while curr:
            queue.append(curr.val)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        while prev:
            if queue.popleft()!=prev.val:
                return False
            prev = prev.next
        return True
        