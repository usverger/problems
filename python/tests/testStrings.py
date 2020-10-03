import unittest
from typing import List
import python.problems as problems

class Strings(unittest.TestCase):

    def test_removeDuplicates(self):
        s = problems.Strings.Solution()
        input = [0,0,1,1,1,2,2,3,3,4]
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [0,1,2,3,4])

        input = [0,0,1]
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [0,1])

        input = []
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [])

        input = [1,2,3,4,5]
        r = s.removeDuplicates(input)
        self.assertEqual(input[:r], [1,2,3,4,5])

    def test_reverseWordsII(self):
        s = problems.Strings.Solution()
        self.assertEqual(s.reverseWordsII_Naive('Alice does not even like bob'), 'bob like even not does Alice')
        self.assertEqual(s.reverseWordsII_Naive('  Bob    Loves  Alice   '), 'Alice Loves Bob')
        self.assertEqual(s.reverseWordsII_Naive('    Alice   '), 'Alice')
        self.assertEqual(s.reverseWordsII_Naive('the sky is blue'), 'blue is sky the')
        self.assertEqual(s.reverseWordsII('  Bob    Loves  Alice   '), 'Alice Loves Bob')
        self.assertEqual(s.reverseWordsII('    Alice   '), 'Alice')
        self.assertEqual(s.reverseWordsII('the sky is blue'), 'blue is sky the')

    def test_reverseString(self):
        s = problems.Strings.Solution()
        input = ['h','e','l','l','o']
        s.reverseString(input)
        self.assertEqual(input, ['o','l','l','e','h'])

    def test_longestCommonPrefix(self):
        s = problems.Strings.Solution()
        self.assertEqual(s.longestCommonPrefix(["flower", "flow", "flight"]), 'fl')
        self.assertEqual(s.longestCommonPrefix([]), '')
        self.assertEqual(s.longestCommonPrefix(["dog","racecar","car"]), '')
        self.assertEqual(s.longestCommonPrefix(['leet', 'leeds', 'leetcode', 'leets']), 'lee')

    def test_strStr(self):
        s = problems.Strings.Solution()
        self.assertEqual(s.strStr('mississippi', 'issip'), 4)
        self.assertEqual(s.strStr('hello', 'll'), 2)
        self.assertEqual(s.strStr('a', 'a'), 0)
        self.assertEqual(s.strStr('aaaaaaa', 'bba'), -1)

    def test_firstUniqChar(self):
        s = problems.Strings.Solution()
        self.assertEqual(s.firstUniqChar('leetcode'), 0)
        self.assertEqual(s.firstUniqChar('loveleetcode'), 2)

    def test_generateParentheses(self):
        s = problems.Strings.Solution()
        self.assertEqual(s.generateParenthesis_BruteForce(3), ["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(s.generateParenthesis_WithCounters(3), ["((()))","(()())","(())()","()(())","()()()"])

    def test_validParentheses(self):
        s = problems.Strings.Solution()
        self.assertEqual(s.validParentheses("()"), True)
        self.assertEqual(s.validParentheses("()[]"), True)
        self.assertEqual(s.validParentheses("()[]{}"), True)
        self.assertEqual(s.validParentheses("(]"), False)
        self.assertEqual(s.validParentheses("([)]"), False)
        self.assertEqual(s.validParentheses("{[]}"), True)
        
    def test_lengthOfLastWord(self):
        s = problems.Strings.Solution()
        r = s.lengthOfLastWord("")
        self.assertEqual(r, 0)
        r = s.lengthOfLastWord(" ")
        self.assertEqual(r, 0)
        r = s.lengthOfLastWord("  ")
        self.assertEqual(r, 0)
        r = s.lengthOfLastWord("Hello World")
        self.assertEqual(r, 5)
        r = s.lengthOfLastWord("Hello   World   ")
        self.assertEqual(r, 5)

    def test_restoreString(self):
        s = problems.Strings.Solution()
        r = s.restoreString("codeleet", [4,5,6,7,0,2,1,3])
        self.assertEqual(r, "leetcode")

    def test_maxNumberOfBalloons(self):
        s = problems.Strings.Solution()
        r = s.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw")
        self.assertEqual(r, 10)

        r = s.maxNumberOfBalloons("leetcode")
        self.assertEqual(r, 0)

        r = s.maxNumberOfBalloons("loonbalxballpoon")
        self.assertEqual(r, 2)

 
