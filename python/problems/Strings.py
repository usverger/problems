from typing import List
import string
from collections import defaultdict

class Solution:

    def generateParenthesis_BruteForce(self, n: int) -> List[str]:
        
        def isBalanced(s):
            balance = 0
            for c in s:
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                
                if balance < 0:
                    return False
            
            return balance == 0
        
        def generateBruteForce(n, result: List[str], s: List[str]):
            if len(s) == 2*n:
                if isBalanced(s):
                    result.append(''.join(s))
                return
            
            s.append('(')
            generateBruteForce(n, result, s)
            s.pop()
            
            s.append(')')
            generateBruteForce(n, result, s)
            s.pop()
            
        result = []
        generateBruteForce(n, result, [])
        
        return result

    def generateParenthesis_WithCounters(self, n: int) -> List[str]:

        def isBalanced(s):
            balance = 0
            for c in s:
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                
                if balance < 0:
                    return False
            
            return balance == 0

        def generate(s: str, result: List[str], left: int, right: int):
            if len(s) == 2*n:
                if isBalanced(s):
                    result.append(s)
                return

            if left < n:
                generate(s + '(', result, left + 1, right)

            if left > right:
                generate(s + ')', result, left, right + 1)

        result = []
        generate('', result, 0, 0)
        return result


    def validParentheses(self, s: str) -> bool:
        
        if not s:
            return True
        
        stack = []
        
        for c in s:
            
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                t = stack.pop()
                if not ((c == ')' and t == '(') or (c == '}' and t == '{') or (c == ']' and t == '[')):
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

    def lengthOfLastWord(self, s: str) -> int:        
        words = s.split()
        if not words:
            return 0
        
        return(len(words.pop()))

    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i in range(len(s)):
            result[indices[i]] = s[i]
            
        return "".join(result)

    def maxNumberOfBalloons(self, text: str) -> int:
        
        # initialize the histogram
        histogram = {}
        for c in string.ascii_lowercase:
            histogram[c] = 0
            
        # count the characters
        for c in text:
            histogram[c] += 1
        
        b = histogram['b']
        a = histogram['a']
        l = histogram['l']
        o = histogram['o']
        n = histogram['n']
        
        return min(b, a, n, l // 2, o // 2)
            