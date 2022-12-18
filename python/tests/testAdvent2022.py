import unittest
from typing import List
import python.advent2022 as advent2022
import os
from pathlib import Path


class TestAdvent2022(unittest.TestCase):
    
    def test_day01_part1(self):
        text = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        s = advent2022.Day01.Solution(text.splitlines())
        s.parseInput()
        result = s.findMax()
        print('max is ' + str(result))

        self.assertEqual(24000, result)

    def test_day01_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day01.txt')
        text = open(filename, 'r')
        s = advent2022.Day01.Solution(text.read().splitlines())

        s.parseInput()
        result = s.findMax()

        print('\n')
        print('max is ' + str(result))

        self.assertEqual(68923, result)

    def test_day01_part2(self):
        text = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        
        s = advent2022.Day01.Solution(text.splitlines())
        s.parseInput()
        result = s.sumTop3()

        print('\n')
        print('sum of top 3 is ' + str(result))

        self.assertEqual(45000, result)

    def test_day01_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day01.txt')
        text = open(filename, 'r')
        s = advent2022.Day01.Solution(text.read().splitlines())

        s.parseInput()
        result = s.sumTop3()

        print('\n')
        print('sum of top 3 is ' + str(result))

    def test_day02_part1(self):
        text = '''A Y
B X
C Z'''
        s = advent2022.Day02.Solution(text.splitlines())
        score = s.scorePart1()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(15, score)

    def test_day02_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day02.txt')
        text = open(filename, 'r')
        s = advent2022.Day02.Solution(text.read().splitlines())

        score = s.scorePart1()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(12794, score)

    def test_day02_part2(self):
        text = '''A Y
B X
C Z'''
        s = advent2022.Day02.Solution(text.splitlines())
        score = s.scorePart2()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(12, score)

    def test_day02_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day02.txt')
        text = open(filename, 'r')
        s = advent2022.Day02.Solution(text.read().splitlines())

        score = s.scorePart2()
        print('\n')        
        print('score is ' + str(score))

        self.assertEqual(14979, score)

    def test_day03_part1(self):
        text = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
        s = advent2022.Day03.Solution(text.splitlines())

        print('\n')
        sum = s.findPart1()
        print('sum is ' + str(sum))
        self.assertEqual(157, sum)

    def test_day03_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day03.txt')
        text = open(filename, 'r')
        s = advent2022.Day03.Solution(text.read().splitlines())

        print('\n')
        sum = s.findPart1()
        print('sum is ' + str(sum))
        self.assertEqual(7997, sum)

    def test_day03_part2(self):
        text = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
        s = advent2022.Day03.Solution(text.splitlines())

        print('\n')
        groups = s.findGroupBadges()
        print(groups)

        result = s.findPart2()
        self.assertEqual(70, result)

    def test_day03_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day03.txt')
        text = open(filename, 'r')
        s = advent2022.Day03.Solution(text.read().splitlines())

        print('\n')
        groups = s.findGroupBadges()
        print(groups)

        result = s.findPart2()
        self.assertEqual(2545, result)

    def test_day04_part1(self):
        text = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
        s = advent2022.Day04.Solution(text.splitlines())

        print('\n')
        c = s.countFullyContained()
        print(c)

        self.assertEqual(2, c)

    def test_day04_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day04.txt')
        text = open(filename, 'r')
        s = advent2022.Day04.Solution(text.read().splitlines())

        print('\n')
        c = s.countFullyContained()
        print(c)

        self.assertEqual(584, c)

    def test_day04_part2(self):
        text = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
        s = advent2022.Day04.Solution(text.splitlines())

        print('\n')
        c = s.countOverlap()
        print(c)

        self.assertEqual(4, c)

    def test_day04_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day04.txt')
        text = open(filename, 'r')
        s = advent2022.Day04.Solution(text.read().splitlines())

        print('\n')
        c = s.countOverlap()
        print(c)

        self.assertEqual(933, c)

    def test_day05_part1(self):
        text = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
        s = advent2022.Day05.Solution(text.splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart1(s.instructions)
        print(s.stacks)
        self.assertEqual('CMZ', s.result(s.stacks))

    def test_day05_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day05.txt')
        text = open(filename, 'r')
        s = advent2022.Day05.Solution(text.read().splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart1(s.instructions)
        result = s.result(s.stacks)
        self.assertEqual('FRDSQRRCD', result)

    def test_day05_part2(self):
        text = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
        s = advent2022.Day05.Solution(text.splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart2(s.instructions)
        print(s.stacks)
        self.assertEqual('MCD', s.result(s.stacks))

    def test_day05_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day05.txt')
        text = open(filename, 'r')
        s = advent2022.Day05.Solution(text.read().splitlines())

        print('\n')
        s.readStacks()
        s.readInstructions()
        s.executeInstructionsPart2(s.instructions)
        result = s.result(s.stacks)
        self.assertEqual('HRFTQVWNN', result)

    def test_day06_part1(self):
        s = advent2022.Day06.Solution()
        text = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''
        print('\n')
        result = s.resultOption1(text, 4)
        print(result)
        self.assertEqual(7, result)

    def test_day06_part1_puzzle(self):
        s = advent2022.Day06.Solution()
        text = '''vftfrfcrfrpptffhnnnsznzgngqgsssczcjcdcssmgmtmnmqnmmfttbdttqtggmgpmmqrqzrzttptpdtpddqfdffgjgzjzczjcjjvttvmmrwmrwwjtwjttnccgbcbjbgjjcvvsqshszhzvhvsstjjljcczmzjmzzdtzzhfhvvvflljtllfqqdmmmhmfhffzhhtgtssqppgcppfjjrnngwwrvrvqvpppcspsrrsqqqlmmpcmcjmmjhmhzzpnnggmjjrprptpccdggcrrwfwggsfggbbqlqflqqcsqqccqzqbbnbmmlzllnhnwwsjsgstgttfdtffzfvzvbzzrlzlppcsctcncrncnjnfnqnvngnzzscslsppdqdbbthhqvqfvqqvccvdcddsllnwnqwwsccjmcjmmfmppnzpzffslffjrfjftftrffwcwppfsftssdwdzzffnwndnvnggbbfbgfbbfmbbjzzdqdtqtfqqpzzqpzpllvrrbqqbcqqzvznzmmwcwtwftwfwtftvtddhldldblbzlbzlllcjjwllvcllqplqplpzlzqzsqzsznnqwnqqrcqqnrrhmmqbqqlbqqrhrrdgrrsqssnwsnswsgsfsbbdhbdbqqtsqsbsmmbtmmghhcththrrnvvnlvvdvwwjwmwbmmvtvztzmtmrmprpvvmbmrbrsbbpsbbtccwgccbctbccjrjcjtccrrdnnwwqrwwjpjtptcpcfpfvfjjtqtnqqvzqqfhfrftrrgqgbqqtwwthwhqwqjqmmlglnlrnlrnnshsmspmmfnnqwqgwqqprpbbjbhjbbfqftfwwjhhcpcgcpcvppgfgcfgffbzbfzbzqzccmppndppspbssnbbpdpjpgpngpnggtztjzjdjhjmmwrmmqhhcvvvltvllvmvpvlplwplpmllgpllczlzpzczwzswwqgqbqppcjjhjddgccfmmctcjcscczzzjzwzjjsccdmdppdrdccmttjpttqvqdqtdqtqhqchhhtbbddmhhwdhdwdjdccnhcnndpdldvldlvddbjdbjbppjbpbssqnqnmmmclcggrmmdnnwmwddvjvdvrvzzglzlnnllhqqrbbcvvdtttdvvnfnqqstszsjsrscspszppfjjfttgqttdpdbbbvnndbdcdqdrdhhdhhdjjjzzhqqrcrvccrvrtvtnvnpppccpdpccjgjmjzzbsbgsbstsbbtdttrqtrrsrdrdcdjcddbcbjcbjbwbbslbbbbnmmtsmmrwrnwwqtqzqpprhrzhrhhldddrpdrpdpwdpwdpwwlmmzssbwswppldlmddphhnfhhczhhqrrdgdjjdttztftzffdvddqnqvvlbbncnffssbnbfnnzbnznhzhdzzrqzzptzppsnsnzntzzfwfzzvrzrbzrbzrbzrrqqltqlqppbwppmvpmvpmmbnnbhbmbdmbbhmmngmgmhgmghhvttzzfvfggrrchrrbffzjzlzsllbqqhqrrmqrrlzzsqzqqmhhmnmtntstnsnhsnnwwpdphhgjhjccbcqcjcbjbttmssqffjzjmzmqqrbbfnffcbfcfzfrzztftntbntttlddvwdvdcdhcdhdbbjfjzjwpbcvlqvcwjrcjssdfmgwrhrjvhpgqsbtzqqdwjrqsjplqjdzdcrtvqlcrfpcgwpjnbpcmbwnwbzhcvjvzzpvqnzdqdgpfrvdpfdmpprmzmghdfjjzfqjqcbplwntzmsrpqclgrqzhlsgwffqqntswnjsmrcpjlsvdrmcwdgqzsbsbvhbszqgwqffcgbqmjrfjdvbpwbrzwbjgvvjchwfscrhrtzbghjlcnsqqhdgqtdcqrrpsbzqvjwptblszrtffhwcvbngnsdjgpscfzwrncwlpfqgwdzffsqmjcbrlffftpvhjchmgmgqvjnpfsjnfzddqjsfqcpjgfrfgrtlmtfqphjfmdcvmghrdqvbbbhlstgpcgmqnwpdjwbrdbntbpncnztmnmzmsjzrwjmccqslngrvbjcjjgcvnvhsslfhwpwtjjcwgzqpdvqrlbttnnwdphztmwcdlvlqggrdprmzdfpbfhmsgqznzjhdqpmhfphqcvbfqmhnfpcvstrhdbtmljnnhqtfnpdwnszfrflsbbqjsvbvggzfhlcljwlrlfnlwlzzllzbqftlwzqsvwlldslnfnnbhlwmhqhrjlqzpdsjlhjncpwtnpnqvjtzzjnmdntmbjbcwphplbcwdfcqbhhnjnjsfplgwbrqpqmghnzvdprtlmgvwhdgpdwfvdtqtnqdvbntmsrhftwvrgwcbvhnwmhfggdzfgbdfqsbngmvjgssclqlhqggwndzzhcrzrmnzggnvbbbpzfdjtnlvlnprjtlljhtdqjlddmjdswjrwhwdbbbrmpwsgpfgnplbtzfzlvgnfrvvnbjtsglbzmtmcjbbjclmjgtdrrbpbbqzqnvrgqssfrwhrtpsbgsvnnfbmqgbvhshmpqtqljlpwptqzprdbgnzmlgtrvgnmmfhtccsvbmsfnlnzwhrmcnwmmhgwclghgmspwjvbgqrbbhhrglstdntwnvcgdcmwgbwrwhsqzsdnqsvmcbzrvtztspshrfmqbtrdtnsqdllqzdcbmvbdswzrrzchqgpgmhvjgwgnpqfwcmchsnqssnnslzwtwvbqjfbhlbdjzjrqjvsshcvcbwhsvvwtmjwjfgszmvfzclbqjhnczqcznprwzjnlgmdgbfjnrqfgvstcldnttbjmhsqgqlmzqtsqngvmdvrwcjtfljzdmnndnrbqnlqtmsqngflwsghzzsfcdnttpblqqhmtgnqmcdfmclsvgnsfpnnfssqzjtdsjbjnnmqhfctlddtwrqlpczlzvhddrtjfwgqhfcvchzqgfhdbfpbvtqcjvchqmwhvwjrbtcjgbfqjdsbfpgjrzvlgqwphshnqrvqsppgsnfswvrzpwmdfmmwntnsddzppffjvbnshhqgwclvtpjzvlbdzblhhmhrmjrpmltglsdffnstsdqwjhnjccqhbdrgnwmpwczflfvsbznpphgpbfzffbcdnbrqbwddlhvgqsdmdhmlzbdztrrswsbvdgptvhhcdtwzqqhzqpswwvftppwvwhrspfqwppjbdlhcchlftjhrpwhtvqhmwwtcbfhgbqzvzdlwlzwcsqgvmmsnhrfmwwpcrjlsgzmgdqstlwbzrzbqfnpqffmjqbqqzcnsqrfstnwjflwlpfgcjwjdvtjslrcpgwsvrbvjtzqvnjlqrvvwjhzbzqqjhcrbdtwqjbtmwfrmcgnbdcrhrvlcgrgtglpfmvpgwbzccddlrbsjzwbgwthhdmjjtpchtsbnnpgqfcpmsrgvqwhcdqzmtzlzbfdgmvtqzzdcrnhtlcwnmhdjtwdsrfnlmwpnfwdrptclvwrnwrnntwwqvfmjgswbtqcvmbfbgstvsntndzhjjnjfblqdqrgchchtgdwtvlqzrlpsqgbltjzjngdscdczwzhnlszpdnvnbrmfmjpdzvjfgvtwtpwdjjfgspbvtdjrwzncdpbsthgcwvvdbbvpvqdqpzjmlzhtjmjwmzsmrcstrsvbccqhppwrtmslggqbgglgrgffrbwzmbghfqclwwgssgghqjgfjgvwjhhwnntnrnhmfslqpmwzlggsbmrjjgfzfpjlvmshfsdjtshdlfzvjtlqwjbbgmnjhrhtpbgvcsjvwzlqvfchhpfwsbhcztmdgfzgsmszwfbvvgmgpqsrbzvtpmpqdvhgrjmmspnswjrjnjqfgjwsfbzhwhtlfwjfdhgsvcwqlbznqlnhsmzwltfwclcwgjdbhqvjbbchmcpptmpdqzwpfwrbmchpbqndtmdrwtcvlmrrnvhnpzwqcwwgmcblzvnzbzsspwchtqvjmphqtzgwdzqlbvgdjbssdjwljhlsjwzrdvqtrzcdwszqgfdwgnqdrmssqqhtblqzdhtqtqmlbbfhzvlbrphcjhzpvvshjffnsjcbgvngnsjmfdbgfzphjc'''
        print('\n')
        result = s.resultOption1(text, 4)
        print(result)
        self.assertEqual(1640, result)

    def test_day06_part2(self):
        s = advent2022.Day06.Solution()
        self.assertEqual(19, s.resultOption1('''mjqjpqmgbljsphdztnvjfqwrcgsmlb''', 14))
        self.assertEqual(23, s.resultOption1('''bvwbjplbgvbhsrlpgdmjqwftvncz''', 14))
        self.assertEqual(23, s.resultOption1('''nppdvjthqldpwncqszvftbrmjlhg''', 14))
        self.assertEqual(29, s.resultOption1('''nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg''', 14))
        self.assertEqual(26, s.resultOption1('''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw''', 14))

    def test_day06_part2_puzzle(self):
        s = advent2022.Day06.Solution()
        text = '''vftfrfcrfrpptffhnnnsznzgngqgsssczcjcdcssmgmtmnmqnmmfttbdttqtggmgpmmqrqzrzttptpdtpddqfdffgjgzjzczjcjjvttvmmrwmrwwjtwjttnccgbcbjbgjjcvvsqshszhzvhvsstjjljcczmzjmzzdtzzhfhvvvflljtllfqqdmmmhmfhffzhhtgtssqppgcppfjjrnngwwrvrvqvpppcspsrrsqqqlmmpcmcjmmjhmhzzpnnggmjjrprptpccdggcrrwfwggsfggbbqlqflqqcsqqccqzqbbnbmmlzllnhnwwsjsgstgttfdtffzfvzvbzzrlzlppcsctcncrncnjnfnqnvngnzzscslsppdqdbbthhqvqfvqqvccvdcddsllnwnqwwsccjmcjmmfmppnzpzffslffjrfjftftrffwcwppfsftssdwdzzffnwndnvnggbbfbgfbbfmbbjzzdqdtqtfqqpzzqpzpllvrrbqqbcqqzvznzmmwcwtwftwfwtftvtddhldldblbzlbzlllcjjwllvcllqplqplpzlzqzsqzsznnqwnqqrcqqnrrhmmqbqqlbqqrhrrdgrrsqssnwsnswsgsfsbbdhbdbqqtsqsbsmmbtmmghhcththrrnvvnlvvdvwwjwmwbmmvtvztzmtmrmprpvvmbmrbrsbbpsbbtccwgccbctbccjrjcjtccrrdnnwwqrwwjpjtptcpcfpfvfjjtqtnqqvzqqfhfrftrrgqgbqqtwwthwhqwqjqmmlglnlrnlrnnshsmspmmfnnqwqgwqqprpbbjbhjbbfqftfwwjhhcpcgcpcvppgfgcfgffbzbfzbzqzccmppndppspbssnbbpdpjpgpngpnggtztjzjdjhjmmwrmmqhhcvvvltvllvmvpvlplwplpmllgpllczlzpzczwzswwqgqbqppcjjhjddgccfmmctcjcscczzzjzwzjjsccdmdppdrdccmttjpttqvqdqtdqtqhqchhhtbbddmhhwdhdwdjdccnhcnndpdldvldlvddbjdbjbppjbpbssqnqnmmmclcggrmmdnnwmwddvjvdvrvzzglzlnnllhqqrbbcvvdtttdvvnfnqqstszsjsrscspszppfjjfttgqttdpdbbbvnndbdcdqdrdhhdhhdjjjzzhqqrcrvccrvrtvtnvnpppccpdpccjgjmjzzbsbgsbstsbbtdttrqtrrsrdrdcdjcddbcbjcbjbwbbslbbbbnmmtsmmrwrnwwqtqzqpprhrzhrhhldddrpdrpdpwdpwdpwwlmmzssbwswppldlmddphhnfhhczhhqrrdgdjjdttztftzffdvddqnqvvlbbncnffssbnbfnnzbnznhzhdzzrqzzptzppsnsnzntzzfwfzzvrzrbzrbzrbzrrqqltqlqppbwppmvpmvpmmbnnbhbmbdmbbhmmngmgmhgmghhvttzzfvfggrrchrrbffzjzlzsllbqqhqrrmqrrlzzsqzqqmhhmnmtntstnsnhsnnwwpdphhgjhjccbcqcjcbjbttmssqffjzjmzmqqrbbfnffcbfcfzfrzztftntbntttlddvwdvdcdhcdhdbbjfjzjwpbcvlqvcwjrcjssdfmgwrhrjvhpgqsbtzqqdwjrqsjplqjdzdcrtvqlcrfpcgwpjnbpcmbwnwbzhcvjvzzpvqnzdqdgpfrvdpfdmpprmzmghdfjjzfqjqcbplwntzmsrpqclgrqzhlsgwffqqntswnjsmrcpjlsvdrmcwdgqzsbsbvhbszqgwqffcgbqmjrfjdvbpwbrzwbjgvvjchwfscrhrtzbghjlcnsqqhdgqtdcqrrpsbzqvjwptblszrtffhwcvbngnsdjgpscfzwrncwlpfqgwdzffsqmjcbrlffftpvhjchmgmgqvjnpfsjnfzddqjsfqcpjgfrfgrtlmtfqphjfmdcvmghrdqvbbbhlstgpcgmqnwpdjwbrdbntbpncnztmnmzmsjzrwjmccqslngrvbjcjjgcvnvhsslfhwpwtjjcwgzqpdvqrlbttnnwdphztmwcdlvlqggrdprmzdfpbfhmsgqznzjhdqpmhfphqcvbfqmhnfpcvstrhdbtmljnnhqtfnpdwnszfrflsbbqjsvbvggzfhlcljwlrlfnlwlzzllzbqftlwzqsvwlldslnfnnbhlwmhqhrjlqzpdsjlhjncpwtnpnqvjtzzjnmdntmbjbcwphplbcwdfcqbhhnjnjsfplgwbrqpqmghnzvdprtlmgvwhdgpdwfvdtqtnqdvbntmsrhftwvrgwcbvhnwmhfggdzfgbdfqsbngmvjgssclqlhqggwndzzhcrzrmnzggnvbbbpzfdjtnlvlnprjtlljhtdqjlddmjdswjrwhwdbbbrmpwsgpfgnplbtzfzlvgnfrvvnbjtsglbzmtmcjbbjclmjgtdrrbpbbqzqnvrgqssfrwhrtpsbgsvnnfbmqgbvhshmpqtqljlpwptqzprdbgnzmlgtrvgnmmfhtccsvbmsfnlnzwhrmcnwmmhgwclghgmspwjvbgqrbbhhrglstdntwnvcgdcmwgbwrwhsqzsdnqsvmcbzrvtztspshrfmqbtrdtnsqdllqzdcbmvbdswzrrzchqgpgmhvjgwgnpqfwcmchsnqssnnslzwtwvbqjfbhlbdjzjrqjvsshcvcbwhsvvwtmjwjfgszmvfzclbqjhnczqcznprwzjnlgmdgbfjnrqfgvstcldnttbjmhsqgqlmzqtsqngvmdvrwcjtfljzdmnndnrbqnlqtmsqngflwsghzzsfcdnttpblqqhmtgnqmcdfmclsvgnsfpnnfssqzjtdsjbjnnmqhfctlddtwrqlpczlzvhddrtjfwgqhfcvchzqgfhdbfpbvtqcjvchqmwhvwjrbtcjgbfqjdsbfpgjrzvlgqwphshnqrvqsppgsnfswvrzpwmdfmmwntnsddzppffjvbnshhqgwclvtpjzvlbdzblhhmhrmjrpmltglsdffnstsdqwjhnjccqhbdrgnwmpwczflfvsbznpphgpbfzffbcdnbrqbwddlhvgqsdmdhmlzbdztrrswsbvdgptvhhcdtwzqqhzqpswwvftppwvwhrspfqwppjbdlhcchlftjhrpwhtvqhmwwtcbfhgbqzvzdlwlzwcsqgvmmsnhrfmwwpcrjlsgzmgdqstlwbzrzbqfnpqffmjqbqqzcnsqrfstnwjflwlpfgcjwjdvtjslrcpgwsvrbvjtzqvnjlqrvvwjhzbzqqjhcrbdtwqjbtmwfrmcgnbdcrhrvlcgrgtglpfmvpgwbzccddlrbsjzwbgwthhdmjjtpchtsbnnpgqfcpmsrgvqwhcdqzmtzlzbfdgmvtqzzdcrnhtlcwnmhdjtwdsrfnlmwpnfwdrptclvwrnwrnntwwqvfmjgswbtqcvmbfbgstvsntndzhjjnjfblqdqrgchchtgdwtvlqzrlpsqgbltjzjngdscdczwzhnlszpdnvnbrmfmjpdzvjfgvtwtpwdjjfgspbvtdjrwzncdpbsthgcwvvdbbvpvqdqpzjmlzhtjmjwmzsmrcstrsvbccqhppwrtmslggqbgglgrgffrbwzmbghfqclwwgssgghqjgfjgvwjhhwnntnrnhmfslqpmwzlggsbmrjjgfzfpjlvmshfsdjtshdlfzvjtlqwjbbgmnjhrhtpbgvcsjvwzlqvfchhpfwsbhcztmdgfzgsmszwfbvvgmgpqsrbzvtpmpqdvhgrjmmspnswjrjnjqfgjwsfbzhwhtlfwjfdhgsvcwqlbznqlnhsmzwltfwclcwgjdbhqvjbbchmcpptmpdqzwpfwrbmchpbqndtmdrwtcvlmrrnvhnpzwqcwwgmcblzvnzbzsspwchtqvjmphqtzgwdzqlbvgdjbssdjwljhlsjwzrdvqtrzcdwszqgfdwgnqdrmssqqhtblqzdhtqtqmlbbfhzvlbrphcjhzpvvshjffnsjcbgvngnsjmfdbgfzphjc'''
        print('\n')
        result = s.resultOption1(text, 14)
        print(result)
        self.assertEqual(3613, result)

    def test_day07_part1(self):
        text = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

        s = advent2022.Day07.Solution(text.splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        s.printTree(s.root, 0)

        sum = s.findPart1()
        print('Sum: ' + str(sum))

    def test_day07_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day07.txt')
        text = open(filename, 'r')
        s = advent2022.Day07.Solution(text.read().splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        s.printTree(s.root, 0)

        sum = s.findPart1()
        print('Sum: ' + str(sum))
        self.assertEqual(sum, 2104783)

    def test_day07_part2(self):
        text = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

        s = advent2022.Day07.Solution(text.splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        
        minSize = s.findPart2()
        print('Min size: ' + str(minSize))
        self.assertEqual(minSize, 24933642)

    def test_day07_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day07.txt')
        text = open(filename, 'r')
        s = advent2022.Day07.Solution(text.read().splitlines())

        s.buildTree()
        s.calculateTotalSize(s.root)
        print('\n')
        
        minSize = s.findPart2()
        print('Min size: ' + str(minSize))
        self.assertEqual(minSize, 5883165)

    def test_day08_part1(self):
        text = '''30373
25512
65332
33549
35390'''
        s = advent2022.Day08.Solution(text.splitlines())
        result = s.countVisible()
        print('\n')
        print(result)
        self.assertEqual(21, result)

    def test_day08_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day08.txt')
        text = open(filename, 'r')
        s = advent2022.Day08.Solution(text.read().splitlines())
        result = s.countVisible()
        print('\n')
        print(result)
        self.assertEqual(1782, result)

    def test_day08_part2(self):
        text = '''30373
25512
65332
33549
35390'''
        s = advent2022.Day08.Solution(text.splitlines())
        self.assertEqual(4, s.scenicScore(2, 1))
        self.assertEqual(8, s.scenicScore(2, 3))
        self.assertEqual(8, s.scenicScoreMax())        

    def test_day08_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day08.txt')
        text = open(filename, 'r')
        s = advent2022.Day08.Solution(text.read().splitlines())
        result = s.scenicScoreMax()
        print('\n')
        print(result)
        self.assertEqual(474606, result)

    def test_day09_part1(self):
        text = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
        s = advent2022.Day09.Solution(text.splitlines(), 2)
        s.execute()
        result = len(s.trail)
        print('\n')
        print(result)
        self.assertEqual(13, result)

    def test_day09_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day09.txt')
        text = open(filename, 'r')
        s = advent2022.Day09.Solution(text.read().splitlines(), 2)

        s.execute()
        result = len(s.trail)
        print('\n')
        print(result)
        self.assertEqual(5902, result)

    def test_day09_part2(self):
        text = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''
        s = advent2022.Day09.Solution(text.splitlines(), 10)
        s.execute()
        result = len(s.trail)
        self.assertEqual(36, result)

        text2 = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
        s = advent2022.Day09.Solution(text2.splitlines(), 10)
        s.execute()
        result = len(s.trail)
        self.assertEqual(1, result)        

    def test_day09_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day09.txt')
        text = open(filename, 'r')
        s = advent2022.Day09.Solution(text.read().splitlines(), 10)

        s.execute()
        result = len(s.trail)
        print('\n')
        print(result)
        self.assertEqual(2445, result)

    def test_day10_part1_1(self):
        text = '''noop
addx 3
addx -5'''
        s = advent2022.Day10.Solution(text.splitlines())
        s.run(1)
        self.assertEqual(1, s.x)
        s.run(1)
        self.assertEqual(1, s.x)
        s.run(1)
        self.assertEqual(4, s.x)
        s.run(1)
        self.assertEqual(4, s.x)
        s.run(1)
        self.assertEqual(-1, s.x)

    def test_day10_part1_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day10-1.txt')
        text = open(filename, 'r')
        s = advent2022.Day10.Solution(text.read().splitlines())
        s.run(19)
        self.assertEqual(21, s.x)
        self.assertEqual(20, s.cycle)
        s.run(40)
        self.assertEqual(19, s.x)
        self.assertEqual(60, s.cycle)
        s.run(40)
        self.assertEqual(18, s.x)
        self.assertEqual(100, s.cycle)
        s.run(40)
        self.assertEqual(21, s.x)
        self.assertEqual(140, s.cycle)
        s.run(40)
        self.assertEqual(16, s.x)
        self.assertEqual(180, s.cycle)
        s.run(40)
        self.assertEqual(18, s.x)
        self.assertEqual(220, s.cycle)

    def test_day10_part1_3(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day10-1.txt')
        text = open(filename, 'r')
        s = advent2022.Day10.Solution(text.read().splitlines())
        result = s.part1()
        print('\n')
        print(result)
        self.assertEqual(13140, result)
        
    def test_day10_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day10-2.txt')
        text = open(filename, 'r')
        s = advent2022.Day10.Solution(text.read().splitlines())
        result = s.part1()
        print('\n')
        print(result)
        self.assertEqual(13920, result)

    def test_day10_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day10-1.txt')
        text = open(filename, 'r')
        s = advent2022.Day10.Solution(text.read().splitlines())
        result = s.part2()
        print('\n')
        print(result)

    def test_day10_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2022/day10-2.txt')
        text = open(filename, 'r')
        s = advent2022.Day10.Solution(text.read().splitlines())
        result = s.part2()
        # EGLHBLFJ        
        print('\n')
        print(result)



