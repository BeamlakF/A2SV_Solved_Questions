class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.left = Node(0)   
        self.right = Node(0)  
        self.left.next = self.right
        self.right.prev = self.left
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.left.next
        for _ in range(index):
            current = current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        first = self.left.next  
        new_node.next = first
        new_node.prev = self.left
        
        self.left.next = new_node
        first.prev = new_node
        
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        last = self.right.prev  
        new_node.next = self.right
        new_node.prev = last
        
        last.next = new_node
        self.right.prev = new_node
        
        self.length += 1 
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return            
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
            
        current = self.left.next
        for _ in range(index):
            current = current.next
        
        new_node = Node(val)
        prev_node = current.prev
        
        new_node.next = current
        new_node.prev = prev_node

        prev_node.next = new_node
        current.prev = new_node
        
        self.length += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
            
        current = self.left.next
        for _ in range(index):
            current = current.next
            
        prev_node = current.prev
        next_node = current.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.length -= 1