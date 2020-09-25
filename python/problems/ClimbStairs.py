from typing import List
from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def rec(i: int, n: int, cache) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            
            if i not in cache:
                cache[i] = rec(i+1, n, cache) + rec(i+2, n, cache)
            
            return cache[i]
        
        c = dict()
        return rec(0, n, c)
                
