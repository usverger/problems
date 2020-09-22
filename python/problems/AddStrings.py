from typing import List
from collections import defaultdict

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if len(num1) < len(num2):
            shorter = num1
            longer = num2
        else:
            shorter = num2
            longer = num1

        result = str('')
        carry = 0
        i = 0
        while i < len(shorter):
            a = shorter[len(shorter) - 1 - i]
            b = longer[len(longer) - 1 - i]
            c = (int(a) + int(b) + carry) % 10
            carry = (int(a) + int(b) + carry) // 10
            result = str(c) + result
            i += 1
        
        while i < len(longer):
            b = longer[len(longer) - 1 - i]
            c = (int(b) + carry) % 10
            carry = (int(b) + carry) // 10
            result = str(c) + result
            i += 1
            
        if carry == 1:
            result = '1' + result
            
        return result
        
                    
                
            
                
        
                
                
            

