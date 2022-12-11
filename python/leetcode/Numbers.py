from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
            
        return nums[0]

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
