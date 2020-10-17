import unittest
from typing import List
import python.problems as problems

class LinkedLists(unittest.TestCase):

    def test_oddEvenList(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(3)
        l.addAtTail(4)
        l.addAtTail(5)
        l.oddEvenList()
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 3)
        self.assertEqual(l.get(2), 5)
        self.assertEqual(l.get(3), 2)
        self.assertEqual(l.get(4), 4) 

    def test_deleteNode(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(3)
        l.addAtTail(4)
        l.addAtTail(5)
        l.deleteNode(l.getNode(3))
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 5)

    def test_removeElements(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(6)
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(6)
        l.addAtTail(3)
        l.addAtTail(4)
        l.addAtTail(5)
        l.addAtTail(6)
        l.removeElements(6)
        self.assertEqual(l.get(0), 1)
        self.assertEqual(l.get(1), 2)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 4)
        self.assertEqual(l.get(4), 5)

    def test_reverseList(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(3)
        l.addAtTail(4)
        l.addAtTail(5)
        l.reverseList()
        self.assertEqual(l.get(0), 5)
        self.assertEqual(l.get(1), 4)
        self.assertEqual(l.get(2), 3)
        self.assertEqual(l.get(3), 2)
        self.assertEqual(l.get(4), 1)

    def test_removeNthFromEnd(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(4)
        l.addAtTail(1)
        l.addAtTail(8)
        l.addAtTail(4)
        l.addAtTail(5)     
        l.removeNthFromEnd(2)
        self.assertEqual(l.get(2), 8)
        self.assertEqual(l.get(3), 5)

        l = problems.DesignLinkedList.MyLinkedList()
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
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(4)
        l.addAtTail(1)
        l.addAtTail(8)
        l.addAtTail(4)
        l.addAtTail(5)

        l2 = problems.DesignLinkedList.MyLinkedList()
        l2.addAtTail(5)
        l2.addAtTail(6)
        l2.addAtTail(1)
        l2.getNode(2).next = l.getNode(2)

        self.assertEqual(l.getIntersectionNode(l.head, l2.head), l.getNode(2))

    def test_getLength(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(3)
        l.addAtTail(2)
        l.addAtTail(0)
        l.addAtTail(-4)
        self.assertEqual(l.getLength(l.head), 4)

        l = problems.DesignLinkedList.MyLinkedList()
        self.assertEqual(l.getLength(l.head), 0)

    def test_detectCycle(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(3)
        l.addAtTail(2)
        l.addAtTail(0)
        l.addAtTail(-4)
        l.getNode(3).next = l.getNode(1)
        self.assertEqual(l.detectCycle(l.head), l.getNode(1))

        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(3)
        self.assertEqual(l.detectCycle(l.head), None)

    def test_hasCycle(self):
        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(3)
        l.addAtTail(2)
        l.addAtTail(0)
        l.addAtTail(-4)
        l.getNode(3).next = l.getNode(1)
        self.assertEqual(l.hasCycle(l.head), True)

        l = problems.DesignLinkedList.MyLinkedList()
        l.addAtTail(1)
        l.addAtTail(2)
        l.addAtTail(3)
        self.assertEqual(l.hasCycle(l.head), False)

    def test_designLinkedList(self):
        l = problems.DesignLinkedList.MyLinkedList()
        
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




 
