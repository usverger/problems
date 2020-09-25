from typing import List
from collections import defaultdict
import itertools

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def area(a: List[int], b: List[int], c:List[int]) -> float:
            
            # area is determinant of matrix divided by 2, absolute value
            # S = abs 1/2 * | x1 - x3   y1 - y3 |
            #               | x2 - x3   y2 - y3 |
            
            return 0.5 * abs(  (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0])  )
        
        # enumerate all possible combinations by 3 points
        combinations = itertools.combinations(points, 3)
        # return max
        return max([area(c[0], c[1], c[2]) for c in combinations])
                    
                
            
                
        
                
                
            

