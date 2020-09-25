from typing import List
from collections import defaultdict
import itertools

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def combinationsOfThree(arr: List[int]) -> List[List[int]]:
            for i in range(len(arr) - 2):
                for j in range(i + 1, len(arr) - 1):
                    for k in range(j + 1, len(arr)):
                        yield (arr[i], arr[j], arr[k])

        def area(a: List[int], b: List[int], c:List[int]) -> float:
            
            # area is determinant of matrix divided by 2, absolute value
            # S = abs 1/2 * | x1 - x3   y1 - y3 |
            #               | x2 - x3   y2 - y3 |
            
            return 0.5 * abs(  (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0])  )
    
        # just for the sake of comparing the implementation
        arr = [1,2,3,4,5]
        print(list(itertools.combinations(arr, 3)))
        print(list(combinationsOfThree(arr)))
        
        # enumerate all possible combinations by 3 points
        iterator = itertools.combinations(points, 3)
        # return max
        return max([area(c[0], c[1], c[2]) for c in iterator])
                    
                
            
                
        
                
                
            

