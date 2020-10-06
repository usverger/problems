from typing import List
from collections import defaultdict

class MyNode:
    val = 0
    next = None

    def __init__(self, val: int, next):
        self.val = val
        self.next = next
        
class MyLinkedList:
    head = None
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = MyNode(0, None)
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        
        if self.head is None:
            return -1

        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr.val if curr else -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newHead = MyNode(val, self.head)
        self.head = newNead
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = MyNode(val)
            return
        
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = MyNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        curr = self.head
        i = 0
        while i < index - 1 and curr:
            curr = curr.next
            i += 1
        
        if not curr:
            return
        
        node = MyNode(val, curr.next)
        curr.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        i = 0
        while i < index - 1 and curr and curr.next:
            curr = curr.next
            i += 1
        
        if not curr:
            return
        
        curr.next = curr.next.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
                
            
                
        
                
                
            

