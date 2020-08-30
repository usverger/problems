from typing import List
from collections import defaultdict

class Solution:
    
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # the easiest solution is to calculate manhattan distances, then sort by it and then output
        # ideally we should put them to a storage that is already sorted
        # a simple array actually works because distance is naturally the index of array

        # initialize the array        
        result = [[] for i in range(R + C - 1)]
        
        # enumerate all cells, the order does not matter
        for i in range(R):
            for j in range(C):
                result[abs(i - r0) + abs(j - c0)].append([i, j])
                
        # output in the same order
        flattened = []
        for e in result:
            for e2 in e:
                flattened.append(e2)
            
        return flattened