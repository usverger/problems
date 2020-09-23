import unittest
from typing import List
import python.problems as problems

class Strings(unittest.TestCase):

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

 
