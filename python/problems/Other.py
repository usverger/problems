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
                
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(1, n + 1):
            if i % 15 == 0: r.append("FizzBuzz")
            elif i % 3 == 0: r.append("Fizz")
            elif i % 5 == 0: r.append("Buzz")
            else: r.append(str(i))
        return r

        
            
                
        
                
                
            

