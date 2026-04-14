def removeElements(self, head, val: int) :
        res = (0, head)
        dummy = res

        while dummy:
            while dummy.next and dummy.next.val ==val:
                dummy.next = dummy.next.next

            dummy = dummy.next

        return res.next