import unittest
from typing import List
import python.problems as problems

class LinkedLists(unittest.TestCase):

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




 