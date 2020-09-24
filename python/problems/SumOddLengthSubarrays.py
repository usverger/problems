from typing import List
from collections import defaultdict

class Solution:
    def sumOddLengthSubarrays_BruteForce(self, arr: List[int]) -> int:
        
        result = 0
        for l in range(1, len(arr) + 1, 2): # iterate over all odd lengths
            for i in range(0, len(arr) - l + 1):
                result += sum(arr[i:i + l])
        
        return result
                    
                
            
                
        
                
                
            

