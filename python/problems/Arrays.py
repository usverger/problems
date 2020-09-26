from typing import List
from collections import defaultdict

class Solution:

    def sumOddLengthSubarrays_BruteForce(self, arr: List[int]) -> int:
        
        result = 0
        for l in range(1, len(arr) + 1, 2): # iterate over all odd lengths
            for i in range(0, len(arr) - l + 1):
                result += sum(arr[i:i + l])
        
        return result

    def moveZeroes(self, nums: List[int]) -> None:
        
        def swap(i: int, j: int, nums: List[int]):
            k = nums[j]
            nums[j] = nums[i]
            nums[i] = k
        
        last = 0
        for i in range(len(nums)):          
            if nums[i] != 0:
                swap(i, last, nums)
                last += 1

    def pivotIndex(self, nums: List[int]) -> int:
        
        # corner case when list is empty
        if len(nums) == 0:
            return -1
        
        total = sum(nums)

        # check leftmost element since it is not part of the cycle
        if total - nums[0] == 0:
            return 0
        
        leftSum = 0
        rightSum = total - nums[0]
        
        for i in range(1, len(nums)):
            leftSum += nums[i - 1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        
        return -1
                    
    def numIdenticalPairs_BruteForce(self, nums: List[int]) -> int:
        
        def good(i: int, j: int, nums: List[int]) -> bool:
            return nums[i] == nums[j] and i < j
        
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if good(i, j, nums):
                    count += 1
        return count
                                  
    def numIdenticalPairs_Linear(self, nums: List[int]) -> int:

        histogram = [0] * 100 # according to problem statement

        for value in nums:
            histogram[value] += 1

        result = 0
        for count in histogram:
            # C of n elements by k = n! / (k! * (n - k)!)
            # in our case count! / (2! * (count - 2)!) = count * (count - 1) / 2
            result += count * (count - 1) // 2

        return result
                
            
                
        
                
                
            

