def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        while dummy:
            while dummy.next and dummy.next.val ==val:
                dummy.next = dummy.next.next

            dummy = dummy.next

        return res.next