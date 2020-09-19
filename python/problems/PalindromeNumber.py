from typing import List
from collections import defaultdict

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        if x < 0:
            return False
                
        res = 0
        current = x
        
        while current != 0:
            digit = current % 10            
            current = current // 10
            res = res * 10 + digit
            
        return res == x
