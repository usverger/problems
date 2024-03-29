import unittest
from typing import List
import python.leetcode as leetcode

class LinkedLists(unittest.TestCase):

    def test_mergeTwoLists(self):
        s = leetcode.DesignLinkedList.Solution()
        l1 = leetcode.DesignLinkedList.MyLinkedList([1,2,4])
        l2 = leetcode.DesignLinkedList.MyLinkedList([1,2,3])
        r = s.mergeTwoLists(l1.head, l2.head)
        self.assertEqual(r.next.next.next.next.val, 3) 
        self.assertEqual(r.next.next.next.next.next.val, 4) 

    def test_isPalindrome(self):
        l = leetcode.DesignLinkedList.MyLinkedList([1,2])
        self.assertEqual(l.isPalindrome(), False)

        l = leetcode.DesignLinkedList.MyLinkedList([1,2,2,1])
        self.assertEqual(l.isPalindrome(), True)

        l = leetcode.DesignLinkedList.MyLinkedList([1,2,5,2,1])
        self.assertEqual(l.isPalindrome(), True)

    def test_oddEvenList(self):
        l = leetcode.DesignLinkedList.MyLinkedList([1,2,3,4,5])
        l.oddEvenList()
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 3)
        self.assertEqual(l.get(2), 5)
        self.assertEqual(l.get(3), 2)
        self.assertEqual(l.get(4), 4) 

    def test_deleteNode(self):
        l = leetcode.DesignLinkedList.MyLinkedList([1,2,3,4,5])
        l.deleteNode(l.getNode(3))
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 5)

    def test_removeElements(self):
        l = leetcode.DesignLinkedList.MyLinkedList([6,1,2,6,3,4,5,6])
        l.removeElements(6)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 4)
        self.assertEqual(l.get(4), 5)

    def test_reverseList(self):
        l = leetcode.DesignLinkedList.MyLinkedList([1,2,3,4,5])
        l.reverseList()
        self.assertEqual(l.get(0), 5)
        self.assertEqual(l.get(1), 4)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 2)
        self.assertEqual(l.get(4), 1)

    def test_removeNthFromEnd(self):
        l = leetcode.DesignLinkedList.MyLinkedList([4,1,8,4,5]) 
        l.removeNthFromEnd(2)
        self.assertEqual(l.get(2), 8)
        self.assertEqual(l.get(3), 5)

        l = leetcode.DesignLinkedList.MyLinkedList()
        l.addAtTail(4)
        l.addAtTail(1)  
        l.removeNthFromEnd(3)
        self.assertEqual(l.get(0), 4)
        self.assertEqual(l.get(1), 1)

        l.removeNthFromEnd(2)
        self.assertEqual(l.get(0), 1)

        l.removeNthFromEnd(1)
        self.assertEqual(l.get(0), -1)

    def test_getIntersectionNode(self):
        l = leetcode.DesignLinkedList.MyLinkedList([4,1,8,4,5])

        l2 = leetcode.DesignLinkedList.MyLinkedList([5,6,1])
        l2.getNode(2).next = l.getNode(2)

        self.assertEqual(l.getIntersectionNode(l.head, l2.head), l.getNode(2))

    def test_getLength(self):
        l = leetcode.DesignLinkedList.MyLinkedList([3,2,0,-4])
        self.assertEqual(l.getLength(l.head), 4)

        l = leetcode.DesignLinkedList.MyLinkedList()
        self.assertEqual(l.getLength(l.head), 0)

    def test_detectCycle(self):
        l = leetcode.DesignLinkedList.MyLinkedList([3,2,0,-4])
        l.getNode(3).next = l.getNode(1)
        self.assertEqual(l.detectCycle(l.head), l.getNode(1))

        l = leetcode.DesignLinkedList.MyLinkedList([1,2,3])
        self.assertEqual(l.detectCycle(l.head), None)

    def test_hasCycle(self):
        l = leetcode.DesignLinkedList.MyLinkedList([3,2,0,-4])
        l.getNode(3).next = l.getNode(1)
        self.assertEqual(l.hasCycle(l.head), True)

        l = leetcode.DesignLinkedList.MyLinkedList()
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(3)
        self.assertEqual(l.hasCycle(l.head), False)

    def test_designLinkedList(self):
        l = leetcode.DesignLinkedList.MyLinkedList()
        
        self.assertEqual(l.get(0), -1) 
        self.assertEqual(l.get(1), -1)
        l.addAtHead(1)
        self.assertEqual(l.get(0), 1) 
        self.assertEqual(l.get(1), -1)
        l.addAtTail(3)
        self.assertEqual(l.get(0), 1) 
        self.assertEqual(l.get(1), 3)
        self.assertEqual(l.get(2), -1)
        l.addAtIndex(1, 2)
        self.assertEqual(l.get(0), 1) 
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), -1)
        l.deleteAtIndex(3)
        self.assertEqual(l.get(0), 1) 
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), -1)
        l.deleteAtIndex(1)
        self.assertEqual(l.get(0), 1) 
        self.assertEqual(l.get(1), 3)
        l.deleteAtIndex(1)
        self.assertEqual(l.get(0), 1) 
        self.assertEqual(l.get(1), -1)
        l.deleteAtIndex(0)
        self.assertEqual(l.get(0), -1)
        self.assertEqual(l.get(1), -1)




 
