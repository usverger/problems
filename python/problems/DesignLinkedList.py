class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def getNode(self, index: int) -> ListNode:
        if index < 0: return None
        if self.head is None: return None
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.getNode(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = ListNode(val, self.head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.addAtHead(val)
            return
        
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return

        prev = self.getNode(index - 1)
        if not prev: return
        node = ListNode(val, prev.next)
        prev.next = node
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next if self.head else None
            return

        prev = self.getNode(index - 1)
        if not prev: return
        if not prev.next: return
        
        prev.next = prev.next.next
        
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        if not head.next: return False

        sp = head
        fp = head.next.next
        while sp and fp and sp != fp:
            sp = sp.next
            fp = fp.next.next if fp.next else None
            
        if sp and fp and sp == fp: return True
        return False
        