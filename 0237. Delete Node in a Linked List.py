def deleteNode(self, node) -> None:
        """
        Deletes the given node (except the tail) in a singly linked list.
        NOT given the head of the list.
        """
        # copy value from the next node because we are not gonna access the first node in the head,
        node.val = node.next.val

        # skip over the next node
        node.next = node.next.next
