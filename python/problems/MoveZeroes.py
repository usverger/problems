from typing import List
from collections import defaultdict

class Solution:
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
                    
                
            
                
        
                
                
            

