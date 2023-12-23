class Solution:
    def hasCycle(self, head) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False
        