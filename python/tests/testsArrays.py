import unittest
import bisect
from typing import List
import python.problems as problems

class Arrays(unittest.TestCase):

    def test_maxSubArray(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.maxSubArray_BruteForce([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(s.maxSubArray_DP([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(s.maxSubArray_BruteForce([-2]), -2)
        self.assertEqual(s.maxSubArray_DP([-2]), -2)     

    def test_firstBadVersion(self):
        s = problems.Arrays.Solution()
        def isBadVersion4(i): return i >= 4
        def isBadVersion2(i): return i >= 2
        def isBadVersion1(i): return i >= 1
        self.assertEqual(s.firstBadVersion(5, isBadVersion4), 4)
        self.assertEqual(s.firstBadVersion(2, isBadVersion1), 1)
        self.assertEqual(s.firstBadVersion(2, isBadVersion2), 2)

    def test_intersect(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.intersect_Naive([1,2,2,1], [2,2]), [2,2])
        self.assertEqual(s.intersect_Naive([4,9,5], [9,4,9,8,4]), [4,9]) 
        self.assertEqual(s.intersect_SortedSearch([1,2,2,1], [2,2]), [2,2])
        self.assertEqual(s.intersect_SortedSearch([4,9,5], [9,4,9,8,4]), [4,9])
        self.assertEqual(s.intersect_Counters([1,2,2,1], [2,2]), [2,2])
        self.assertEqual(s.intersect_Counters([4,9,5], [9,4,9,8,4]), [4,9]) 

    def test_containsNearbyDuplicate(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.containsNearbyDuplicate([1,2,3,1,2,3], 3), True)
        self.assertEqual(s.containsNearbyDuplicate([1,2,3,1,2,3], 2), False)

    def test_containsDuplicate(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.containsDuplicate([7,1,5,3,6,4]), False)
        self.assertEqual(s.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(s.containsDuplicate([1,1,1,2,3,3,4]), True)

    def test_maxProfitManyTradesWithCooldown(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.maxProfitManyTradesWithCooldown([1,2,3,0,2]), 3)
        self.assertEqual(s.maxProfitManyTradesWithCooldown([7]), 0)
        self.assertEqual(s.maxProfitManyTradesWithCooldown([]), 0)

    def test_maxProfitWithFee(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.maxProfitWithFee([1,3,2,8,4,9], 2), 8)
        self.assertEqual(s.maxProfitWithFee([1,2,3,4,5], 2), 2)
        self.assertEqual(s.maxProfitWithFee([7,6,4,3,1], 2), 0)
        self.assertEqual(s.maxProfitWithFee([7], 2), 0)
        self.assertEqual(s.maxProfitWithFee([], 2), 0)

    def test_maxProfitOneTrade(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.maxProfitOneTrade([7,1,5,3,6,4]), 5)
        self.assertEqual(s.maxProfitOneTrade([1,2,3,4,5]), 4)
        self.assertEqual(s.maxProfitOneTrade([7,6,4,3,1]), 0)
        self.assertEqual(s.maxProfitOneTrade([6,7]), 1)
        self.assertEqual(s.maxProfitOneTrade([6]), 0)
        self.assertEqual(s.maxProfitOneTrade([]), 0)

    def test_maxProfitManyTrades(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.maxProfitManyTrades([7,1,5,3,6,4]), 7)
        self.assertEqual(s.maxProfitManyTrades([1,2,3,4,5]), 4)
        self.assertEqual(s.maxProfitManyTrades([7,6,4,3,1]), 0)
        self.assertEqual(s.maxProfitManyTrades([7]), 0)
        self.assertEqual(s.maxProfitManyTrades([]), 0)

    def test_partition(self):
        s = problems.Arrays.Solution()
        arr = [12,5,3,19,7,8,2]
        pos = s.partition(arr, 0, 4)
        self.assertEqual(pos, 2)
        self.assertEqual(arr, [5,3,7,19,12,8,2])

    def test_findDisappearedNumbers(self):
        s = problems.Arrays.Solution()
        #self.assertEqual(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6])
        self.assertEqual(s.findDisappearedNumbers([4,3,2,7,7,2,3,1]), [5,6,8])

    def test_thirdMax(self):
        s = problems.Arrays.Solution()
        self.assertEqual(s.thirdMax([1,2,3]), 1)
        self.assertEqual(s.thirdMax([3,2,1]), 1)
        self.assertEqual(s.thirdMax([1,2]), 2)
        self.assertEqual(s.thirdMax([2,2,3,1]), 1)

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
