from typing import List
from collections import defaultdict

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negative = 1 if x > 0 else -1
        x = abs(x)
        maxint = 2147483647
        
        while x != 0:
            digit = x % 10            
            x = x // 10
            
            # check for overflows
            if res > maxint // 10 or (res == maxint // 10 and digit > 7):
                return 0
            
            res = res * 10 + digit
                
        return negative * res
