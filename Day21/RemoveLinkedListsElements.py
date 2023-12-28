# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        first = head
        dummy=ListNode(0)
        tail = dummy
        tail.next=head
        while first:
           
            if first.val==val:
                tail.next =tail.next.next
                first=first.next
            else:
                first = first.next
                tail=tail.next
        return dummy.next
            
        