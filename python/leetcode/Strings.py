from typing import List
import string
from collections import defaultdict
from collections import Counter

class Solution:

    def countAndSay(self, n: int) -> str:
         
        def say(s: str) -> str:
            if len(s) == 0: return ''
            if len(s) == 1: return "1" + s
            
            i = 0
            c = 1
            res = ''
            for j in range(1, len(s)):
                if s[j] == s[i]:
                    c += 1
                else:
                    res = res + str(c) + s[i]
                    c = 1
                    i = j
                    
            res = res + str(c) + s[i]
            return res
        
        if n == 1: return '1'
        s = self.countAndSay(n - 1)
        return say(s)   

    def myAtoi(self, s: str) -> int:
        if not s: return 0
        i = 0
        n = len(s)

        # skip all spaces, test if it was all just spaces
        while i < n and s[i] == ' ': i += 1
        if i == n: return 0

        # parse the sign if any
        negative = 1
        if s[i] == '-':
            i += 1
            negative = -1
        elif s[i] == '+':
            i += 1
        elif not s[i].isnumeric():
            return 0

        # build the number intil the end of numeric numbers or the string
        # ignoring the dot?
        result = 0
        maxint = 2**31 - 1
        minint = -2**31
        while i < n and s[i].isnumeric():
            if result > maxint // 10 or (result == maxint // 10 and int(s[i]) > maxint % 10):
                return maxint if negative > 0 else minint

            result = result * 10 + int(s[i])
            i += 1

        return negative * result

    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if len(s) != len(t): return False
        
        c = Counter(s)
        for x in t:
            if c[x] == 0:
                return False
            c[x] -= 1
        
        return True

    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        i = 0
        j = len(s) - 1
        while i < j:

            # skip all non-alphanumeric
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            # upper case are from 65 to 90, lower case 97 to 122
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def reverseWordsII(self, s: str) -> str:
        
        # in-place reverse from start to end
        def reverse(a: List[str], start: int, end: int) -> None:
            while start < end:
                k = a[end]
                a[end] = a[start]
                a[start] = k
                start += 1
                end -= 1

        def reverseByWord(a: List[str]) -> None:
            i, j = 0, 0 # i would be the start of a word, j would be the end of a word
            while i < len(a):
                while i < j or (i < len(a) and a[i] == ' '): i += 1 # skip all spaces after last known end of a word
                while j < i or (j < len(a) and a[j] != ' '): j += 1 # skip all non-spaces after last known start of a word
                reverse(a, i, j - 1)

        def removeSpaces(a: List[str]) -> None:
            i, j = 0, 0 # i would be the slow pointer, j would be the main iterator
            while j < len(a):
                while j < len(a) and a[j] == ' ': j += 1 # skip any spaces before a word
                while j < len(a) and a[j] != ' ': # copy all non-spaces to the end of the reduced string
                    a[i] = a[j]
                    i += 1 # change the end of new reduced string
                    j += 1
                while j < len(a) and a[j] == ' ': j += 1 # skip any spaces before a word
                if j < len(a): # if still not the end of the string, preserve one space
                     a[i] = ' '
                     i += 1

            # now all the rest should be stripped, we will fill it with spaces to strip later
            while i < len(a):
                a[i] = ' '
                i += 1

        result = list(s)
        reverse(result, 0, len(result) - 1)
        reverseByWord(result)
        removeSpaces(result)
        return ''.join(result).strip()

    def reverseWordsII_Naive(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            k = s[i]
            s[i] = s[j]
            s[j] = k
            i += 1
            j -= 1

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        
        n = min(map(len, strs))
        maxIndex = -1
        for index in range(n):     
            if all(strs[0][index] == s[index] for s in strs):
                maxIndex = index
            else:
                break
            
        return strs[0][:maxIndex + 1]

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(needle) > len(haystack): return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
                
        return -1

    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(int)
        for c in s:
            h[c] += 1

        for i in range(len(s)):
            if h[s[i]] == 1:
                return i
            
        return -1

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
            