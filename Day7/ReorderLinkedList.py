class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head

        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next =None
        prev  = None
        while second:
            nxt = second.next
            second.next = prev 
            prev = second
            second = nxt
        first = head
        while prev:
           
            temp1, temp2 = first.next, prev.next
            first.next = prev
            prev.next = temp1
            first=temp1
            prev = temp2
           
