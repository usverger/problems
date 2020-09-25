import unittest
from typing import List
import python.problems as problems

class Numbers(unittest.TestCase):
        
    def test_singleNumber(self):
        s = problems.Numbers.Solution()
        self.assertEqual(s.singleNumber([2,2,1]), 1)
        self.assertEqual(s.singleNumber([2,3,1,2,3]), 1)
        self.assertEqual(s.singleNumber([4,3,1,1,3]), 4)

    def test_reverseInteger(self):
        s = problems.Numbers.Solution()
        r = s.reverse(123)
        self.assertEqual(r, 321)

    def test_palindromeNumber(self):
        s = problems.Numbers.Solution()

        r = s.isPalindrome(121)
        self.assertEqual(r, True)

        r = s.isPalindrome(10)
        self.assertEqual(r, False)


 
