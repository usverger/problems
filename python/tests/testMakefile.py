import unittest
from typing import List
import python.leetcode as leetcode

class Makefile(unittest.TestCase):

    def test_case1(self):
        parsed = leetcode.Makefile.parse('''a: b,c
b: d,e
c: f
d:
e: f
f:''')
        self.assertEqual(['d', 'f', 'e', 'b', 'c', 'a'], leetcode.Makefile.build_order(parsed, 'a'))

    def test_case2(self):
        parsed = leetcode.Makefile.parse('''10: 11,3
9: 11,8
2: 11
8: 7,3
11: 5,7
3:
7:
5:''')
        self.assertEqual(['5', '7', '11', '3', '8', '9'], leetcode.Makefile.build_order(parsed, '9'))

    def test_case3(self):
        parsed = leetcode.Makefile.parse('''10: 11,3,9
9: 11,8
2: 11
8: 7,3
11: 5,7
3:
7:
5:''')
        self.assertEqual(['5', '7', '11', '3', '8', '9', '10'], leetcode.Makefile.build_order(parsed, '10'))

    def test_case4(self):
        parsed = leetcode.Makefile.parse('''a: b,c
b: d,e,f
c: f
d: 
e: f
f: ''')
        self.assertEqual('Circular dependency detected', leetcode.Makefile.build_order(parsed, 'a'))

    def test_case5(self):
        parsed = leetcode.Makefile.parse('''a: b,c
b: d,e
c: f
d: 
e: f
f: b''')
        self.assertEqual('Circular dependency detected', leetcode.Makefile.build_order(parsed, 'a'))


