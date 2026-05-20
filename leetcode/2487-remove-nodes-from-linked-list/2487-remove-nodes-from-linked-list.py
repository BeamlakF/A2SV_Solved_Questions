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
                # does a bigger node exists on the side, because the recursion already checked the ones on the left, 
                so this is to check if the biggest on the right is bigger than the node I have now
                return node.next
            return node

        return solve(head)        
