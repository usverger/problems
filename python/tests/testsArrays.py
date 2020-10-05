import unittest
from typing import List
import python.problems as problems

class Arrays(unittest.TestCase):

    def test_heightChecker(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.heightChecker([1,1,4,2,1,3]), 3)
        self.assertEqual(s.heightChecker([5,1,2,3,4]), 5)
        self.assertEqual(s.heightChecker([1,2,3,4,5]), 0)

    def test_sortArrayByParity(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.sortArrayByParity([3,1,2,4]), [4,2,1,3])

    def test_replaceElements(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.replaceElements([17,18,5,4,6,1]), [18,6,6,6,1,-1])

    def test_validMountainArray(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.validMountainArray([1,2]), False)
        self.assertEqual(s.validMountainArray([1]), False)
        self.assertEqual(s.validMountainArray([]), False)
        self.assertEqual(s.validMountainArray([3,5,5]), False)
        self.assertEqual(s.validMountainArray([1,2,1,0]), True)
        self.assertEqual(s.validMountainArray([1,2,2,1]), False)
        self.assertEqual(s.validMountainArray([0,3,2,1]), True)

    def test_checkIfExist(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.checkIfExist([10,2,5,3]), True)
        self.assertEqual(s.checkIfExist([7,1,14,11]), True)
        self.assertEqual(s.checkIfExist([3,1,7,11]), False)
        self.assertEqual(s.checkIfExist([-2,0,10,-19,4,6,-8]), False)

    def test_mergeSorted(self):
        s = problems.Arrays.Solution()
        input = [1,2,3,0,0,0]
        s.mergeSorted(input, 3, [2,5,6], 3)
        self.assertEqual(input, [1,2,2,3,5,6])

        input = [0]
        s.mergeSorted(input, 0, [1], 1)
        self.assertEqual(input, [1])

    def test_duplicateZeroes(self):
        s = problems.Arrays.Solution()
        input = [1,0,2,3,0,4,5,0]
        s.duplicateZeros(input)
        self.assertEqual(input, [1,0,0,2,3,0,0,4])

        input = [1,2,3]
        s.duplicateZeros(input)
        self.assertEqual(input, [1,2,3])

        input = [0,0,0]
        s.duplicateZeros(input)
        self.assertEqual(input, [0,0,0])

    def test_sortedSquares(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(s.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

    def test_findNumbers(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.findNumbers([555,901,482,1771]), 1)
        self.assertEqual(s.findNumbers([12,345,2,6,7896]), 2)

    def test_removeDuplicates(self):
        s = problems.Arrays.Solution()
        input = [0,0,1,1,1,2,2,3,3,4]
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [0,1,2,3,4])

        input = [0,0,1]
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [0,1])

        input = []
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [])

        input = [1,2,3,4,5]
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [1,2,3,4,5])

    def test_getPascalRow(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.getPascalRow(1), [1,1])
        self.assertEqual(s.getPascalRow(2), [1,2,1])
        self.assertEqual(s.getPascalRow(3), [1,3,3,1])
        self.assertEqual(s.getPascalRow(7), [1,7,21,35,35,21,7,1])

    def test_rotate(self):
        s = problems.Arrays.Solution()

        p = [1]
        s.rotate(p, 2)
        self.assertEqual(p, [1])

        p = [1,2,3,4,5,6,7]
        s.rotate(p, 3)
        self.assertEqual(p, [5,6,7,1,2,3,4])

    def test_minSubArrayLen(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.minSubArrayLen(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(s.minSubArrayLen_BruteForce(7, [2,3,1,2,4,3]), 2)

    def test_findMaxConsecutiveOnes(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.findMaxConsecutiveOnes([1]), 1)
        self.assertEqual(s.findMaxConsecutiveOnes([1, 1, 0]), 2)
        self.assertEqual(s.findMaxConsecutiveOnes([0, 1, 1, 0, 1]), 2)

    def test_removeElement(self):
        s = problems.Arrays.Solution()
        input = [3,2,2,3]
        l = s.removeElement(input, 3)
        self.assertEqual(input[:l], [2,2])

        input = [4,1,2,3,5]
        l = s.removeElement(input, 4)
        self.assertEqual(input[:l], [1,2,3,5])

    def test_twoSum(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.twoSum([2,7,11,15], 9), [0,1])

    def test_twoSumSorted(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.twoSumSorted([2,7,11,15], 9), [1,2])
        self.assertEqual(s.twoSumSorted([-1, 0], -1), [1,2])
        self.assertEqual(s.twoSumSorted([2, 3, 4], 6), [1,3])

    def test_arrayPairSum(self):
        s = problems.Arrays.Solution()

        self.assertEqual(s.arrayPairSum([1,4,3,2]), 4) 
        self.assertEqual(s.arrayPairSum([1,1,2,3,4,5]), 7)

    def test_addBinary(self):
        s = problems.Arrays.Solution()

        self.assertEqual(s.addBinary('0', '0'), '0') 
        self.assertEqual(s.addBinary('11', '1'), '100')
        self.assertEqual(s.addBinary('1010', '1011'), '10101')

    def test_addStrings(self):
        s = problems.Arrays.Solution()

        self.assertEqual(s.addStrings('0', '0'), '0') 
        self.assertEqual(s.addStrings('1', '9'), '10')
        self.assertEqual(s.addStrings('9', '9'), '18')
        self.assertEqual(s.addStrings('9', '999'), '1008')

    def test_plusOne(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(s.plusOne([0]), [1])
        self.assertEqual(s.plusOne([1]), [2])
        self.assertEqual(s.plusOne([9,9,9]), [1,0,0,0])

    def test_dominantIndex(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.dominantIndex([3, 6, 1, 0]), 1)
        self.assertEqual(s.dominantIndex([1,2,3,4]), -1)
        self.assertEqual(s.dominantIndex([]), -1)

    def test_pivotIndex(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.pivotIndex([1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex([1,2,3]), -1)
        self.assertEqual(s.pivotIndex([]), -1)

    def test_numIdenticalPairs(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,2,3,1,1,3]), 4)
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,1,1,1]), 6)
        self.assertEqual(s.numIdenticalPairs_BruteForce([1,2,3]), 0)
        self.assertEqual(s.numIdenticalPairs_Linear([1,2,3,1,1,3]), 4)
        self.assertEqual(s.numIdenticalPairs_Linear([1,1,1,1]), 6)
        self.assertEqual(s.numIdenticalPairs_Linear([1,2,3]), 0)

    def test_sumOddLengthSubarrays(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([1,4,2,5,3]), 58)
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([1,2]), 3)
        self.assertEqual(s.sumOddLengthSubarrays_BruteForce([10,11,12]), 66)

    def test_moveZeroes(self):
        s = problems.Arrays.Solution()

        arr = [0,1,0,3,12]
        s.moveZeroes(arr)
        self.assertEqual(arr, [1,3,12,0,0])

        arr = [0,1]
        s.moveZeroes(arr)
        self.assertEqual(arr, [1,0])
