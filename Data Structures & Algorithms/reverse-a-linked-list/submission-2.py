# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list or a single node: already reversed
        if head is None or head.next is None:
            return head

        # Trust the recursion: reverse everything after head
        new_head = self.reverseList(head.next)

        # head.next used to be our neighbor; now it's the tail of the reversed part
        tail = head.next
        tail.next = head    # attach head to the end
        head.next = None    # head is now the last node

        return new_head
            




