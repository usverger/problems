from typing import List
from collections import defaultdict

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        emptyLeftovers = 0
        while numBottles > 0:
            result += numBottles # drink all converting full to empty
            emptyBottles = numBottles + emptyLeftovers
            emptyLeftovers = emptyBottles % numExchange # save unused bottles for future use
            numBottles = emptyBottles // numExchange # exchange empty bottles to fill
            
        return result
                
            
                
        
                
                
            

