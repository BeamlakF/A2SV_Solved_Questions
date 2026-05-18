def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_temp = curr.next # this is to save the continuing List from being lost other wise, curr.next will have nothing to point at,
            curr.next = prev # this is the reversal point
            prev =curr # save the reverses node in to the current one
            curr = next_temp # update the saved list

        return prev