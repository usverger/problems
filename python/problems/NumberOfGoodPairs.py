from typing import List
from collections import defaultdict

class Solution:
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
        
        def good(i: int, j: int, nums: List[int]) -> bool:
            return nums[i] == nums[j] and i < j

        histogram = [0] * 100 # according to problem statement

        for value in nums:
            histogram[value] += 1

        result = 0
        for count in histogram:
            # C of n elements by k = n! / (k! * (n - k)!)
            # in our case count! / (2! * (count - 2)!) = count * (count - 1) / 2
            result += count * (count - 1) // 2

        return result
                
                
            

