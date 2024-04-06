# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        first = head
        if head and head.next:
            second = head.next
            while first and second:
                temp = second.next
                second.next = first
                tail.next = second
                first.next = temp
                first = first.next
                if first and first.next:
                    second = first.next
                    tail = tail.next.next
                else:
                    break
            return dummy.next
        return head
