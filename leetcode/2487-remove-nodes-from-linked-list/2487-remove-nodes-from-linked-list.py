# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(node):
            if not node:
                return None

            node.next = solve(node.next)
            if node.next and node.val < node.next.val:
                return node.next
            return node

        return solve(head)        