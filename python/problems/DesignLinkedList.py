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

        sp = head.next
        fp = head.next.next
        while sp and fp and sp != fp:
            if not sp: return False
            if not fp or not fp.next: return False
            sp = sp.next
            fp = fp.next.next

        if not sp: return False
        if not fp: return False

        return True

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return None

        sp = head.next
        fp = head.next.next
        while sp and fp and sp != fp:
            if not sp: return None
            if not fp or not fp.next: return None
            sp = sp.next
            fp = fp.next.next

        if not sp: return None
        if not fp: return None

        # now move the slow pointer from the beginning and move the fast pointer in the cycle
        sp = head
        while sp != fp:
            sp = sp.next
            fp = fp.next
        return sp

    def getLength(self, head: ListNode) -> int:
        c = head
        counter = 0
        while c:
            c = c.next
            counter += 1

        return counter

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        
        # find out which one is longer
        lA = self.getLength(headA)
        lB = self.getLength(headB)
        
        if lA > lB:
            a = headA
            b = headB
        else:
            a = headB
            b = headA
            
        # move the pointer on the longer one to make the same length
        i = 0
        while i < abs(lA - lB):
            a = a.next
            i += 1
            
        # now move both lists until meet (or not meet)
        while a != b:
            if not a or not b: return None
            a = a.next
            b = b.next
            
        return a

    def removeNthFromEnd(self, n: int) -> ListNode:
        if n <= 0: return self.head

        # move first pointer n elements forward
        i = self.head
        while n > 0:
            if not i: return self.head
            i = i.next
            n -= 1
        
        # corner case when we need to delete the head
        if i == None:
            self.head = self.head.next
            return self.head
        
        # second pointer is n elements behind
        j = self.head
        prevj = None
        while i:
            i = i.next
            prevj = j
            j = j.next
        
        # now j is subject to removal
        prevj.next = j.next
        return self.head

    def reverseList(self) -> ListNode:
        if not self.head: return self.head
        if not self.head.next: return self.head
        
        cur = self.head.next
        prev = self.head
        while cur:
            temp = cur.next
            cur.next = self.head
            self.head = cur
            prev.next = temp
            cur = temp
            
        return self.head

    def removeElements(self, val: int) -> ListNode:
        dummy = ListNode(0, self.head)
        slow = dummy
        fast = self.head
        
        while fast:
            if fast.val == val: # remove the value, special attn to head
                slow.next = fast.next
                if fast == self.head:
                    self.head = self.head.next
            else:
                slow = fast
            
            fast = fast.next
            
        return self.head