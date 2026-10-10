# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = dict()
        curr = head
        while curr:
            if curr not in nodes:
                nodes[curr] = 1
                curr = curr.next
            else:
                return True
        return False
