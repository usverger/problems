import unittest
from typing import List
import python.leetcode as leetcode

class Numbers(unittest.TestCase):
        
    def test_singleNumber(self):
        s = leetcode.Numbers.Solution()
        self.assertEqual(s.singleNumber([2,2,1]), 1)
        self.assertEqual(s.singleNumber([2,3,1,2,3]), 1)
        self.assertEqual(s.singleNumber([4,3,1,1,3]), 4)

    def test_reverseInteger(self):
        s = leetcode.Numbers.Solution()
        r = s.reverse(123)
        self.assertEqual(r, 321)

    def test_palindromeNumber(self):
        s = leetcode.Numbers.Solution()

        r = s.isPalindrome(121)
        self.assertEqual(r, True)

        r = s.isPalindrome(10)
        self.assertEqual(r, False)


 
