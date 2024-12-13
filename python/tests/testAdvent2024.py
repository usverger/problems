import unittest
from typing import List
import python.advent2024 as advent2024
import os
from pathlib import Path

class TestAdvent2024(unittest.TestCase):
    
    def test_day01_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day01_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day01.Solution(text.read())
        self.assertEqual(11, s.part1())

    def test_day01_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day01.txt')
        text = open(filename, 'r')
        s = advent2024.Day01.Solution(text.read())
        self.assertEqual(1830467, s.part1())

    def test_day01_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day01_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day01.Solution(text.read())
        self.assertEqual(31, s.part2())

    def test_day01_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day01.txt')
        text = open(filename, 'r')
        s = advent2024.Day01.Solution(text.read())
        self.assertEqual(26674158, s.part2())

    def test_day02_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day02_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day02.Solution(text.read())
        self.assertEqual(2, s.part1())

    def test_day02_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day02.txt')
        text = open(filename, 'r')
        s = advent2024.Day02.Solution(text.read())
        self.assertEqual(510, s.part1())

    def test_day02_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day02_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day02.Solution(text.read())
        self.assertEqual(4, s.part2())

    def test_day02_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day02.txt')
        text = open(filename, 'r')
        s = advent2024.Day02.Solution(text.read())
        self.assertEqual(553, s.part2())

    def test_day03_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day03_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day03.Solution(text.read())
        self.assertEqual(161, s.part1())

    def test_day03_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day03.txt')
        text = open(filename, 'r')
        s = advent2024.Day03.Solution(text.read())
        self.assertEqual(184511516, s.part1())

    def test_day03_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day03_sample_2.txt')
        text = open(filename, 'r')
        s = advent2024.Day03.Solution(text.read())
        self.assertEqual(48, s.part2())

    def test_day03_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day03.txt')
        text = open(filename, 'r')
        s = advent2024.Day03.Solution(text.read())
        self.assertEqual(90044227, s.part2())

    def test_day04_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day04_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day04.Solution(text.read())
        self.assertEqual(18, s.part1())

    def test_day04_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day04.txt')
        text = open(filename, 'r')
        s = advent2024.Day04.Solution(text.read())
        self.assertEqual(2685, s.part1())

    def test_day04_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day04_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day04.Solution(text.read())
        self.assertEqual(9, s.part2())

    def test_day04_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day04.txt')
        text = open(filename, 'r')
        s = advent2024.Day04.Solution(text.read())
        self.assertEqual(2048, s.part2())

    def test_day05_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day05_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day05.Solution(text.read())
        self.assertEqual(143, s.part1())

    def test_day05_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day05.txt')
        text = open(filename, 'r')
        s = advent2024.Day05.Solution(text.read())
        self.assertEqual(4637, s.part1())

    def test_day05_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day05_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day05.Solution(text.read())
        self.assertEqual(123, s.part2())

    def test_day05_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day05.txt')
        text = open(filename, 'r')
        s = advent2024.Day05.Solution(text.read())
        self.assertEqual(6370, s.part2())

    def test_day06_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day06_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day06.Solution(text.read())
        self.assertEqual(41, s.part1())

    def test_day06_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day06.txt')
        text = open(filename, 'r')
        s = advent2024.Day06.Solution(text.read())
        self.assertEqual(4752, s.part1())

    def test_day06_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day06_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day06.Solution(text.read())
        self.assertEqual(6, s.part2())

    def test_day06_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day06.txt')
        text = open(filename, 'r')
        s = advent2024.Day06.Solution(text.read())
        self.assertEqual(1719, s.part2())

    def test_day07_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day07_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day07.Solution(text.read())
        self.assertEqual(3749, s.part1())

    def test_day07_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day07.txt')
        text = open(filename, 'r')
        s = advent2024.Day07.Solution(text.read())
        self.assertEqual(882304362421, s.part1())

    def test_day07_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day07_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day07.Solution(text.read())
        self.assertEqual(1224, s.concat_numbers_as_int(12, 24))
        self.assertEqual(11387, s.part2())

    def test_day07_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day07.txt')
        text = open(filename, 'r')
        s = advent2024.Day07.Solution(text.read())
        self.assertEqual(145149066755184, s.part2())

    def test_day08_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day08_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day08.Solution(text.read())
        self.assertEqual(14, s.part1())

    def test_day08_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day08.txt')
        text = open(filename, 'r')
        s = advent2024.Day08.Solution(text.read())
        self.assertEqual(336, s.part1())

    def test_day08_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day08_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day08.Solution(text.read())
        self.assertEqual(34, s.part2())

    def test_day08_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day08.txt')
        text = open(filename, 'r')
        s = advent2024.Day08.Solution(text.read())
        self.assertEqual(1131, s.part2())

    def test_day09_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day09_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day09.Solution(text.read())
        self.assertEqual(1928, s.part1())

    def test_day09_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day09.txt')
        text = open(filename, 'r')
        s = advent2024.Day09.Solution(text.read())
        self.assertEqual(6288707484810, s.part1())

    def test_day09_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day09_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day09.Solution(text.read())
        self.assertEqual(2858, s.part2())

    def test_day09_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day09.txt')
        text = open(filename, 'r')
        s = advent2024.Day09.Solution(text.read())
        self.assertEqual(6311837662089, s.part2())

    def test_day10_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day10_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day10.Solution(text.read())
        self.assertEqual(1, s.part1())

    def test_day10_part1_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day10_sample_2.txt')
        text = open(filename, 'r')
        s = advent2024.Day10.Solution(text.read())
        self.assertEqual(36, s.part1())

    def test_day10_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day10.txt')
        text = open(filename, 'r')
        s = advent2024.Day10.Solution(text.read())
        self.assertEqual(550, s.part1())

    def test_day10_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day10_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day10.Solution(text.read())
        self.assertEqual(16, s.part2())

    def test_day10_part2_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day10_sample_2.txt')
        text = open(filename, 'r')
        s = advent2024.Day10.Solution(text.read())
        self.assertEqual(81, s.part2())

    def test_day10_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day10.txt')
        text = open(filename, 'r')
        s = advent2024.Day10.Solution(text.read())
        self.assertEqual(1255, s.part2())

    def test_day11_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day11_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day11.Solution(text.read())
        self.assertEqual(1, s.blink_stone_many('0', 1))
        self.assertEqual(1, s.blink_stone_many('0', 2))
        self.assertEqual(2, s.blink_stone_many('0', 3))
        self.assertEqual(4, s.blink_stone_many('0', 4))
        self.assertEqual(2377, s.blink_stone_many('0', 20))
        self.assertEqual(1258125, s.blink_stone_many('0', 35))
        # self.assertEqual(10174278, len(s.blink_stone('0', 40)))
        # self.assertEqual(10174278, len(s.blink_stone('0', 50)))
        self.assertEqual(4, s.blink_stone_many('4022724', 5)) # ['333539', '121344', '382521', '880576']
        self.assertEqual(8, s.blink_stone_many('4022724', 6)) # ['333', '539', '121', '344', '382', '521', '880', '576']
        
        self.assertEqual(7, s.blink_all_stones_many(1))

    def test_day11_part1_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day11_sample_2.txt')
        text = open(filename, 'r')
        s = advent2024.Day11.Solution(text.read())
        self.assertEqual(22, s.blink_all_stones_many(6))
        self.assertEqual(55312, s.blink_all_stones_many(25))

    def test_day11_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day11.txt')
        text = open(filename, 'r')
        s = advent2024.Day11.Solution(text.read())
        self.assertEqual(211306, s.blink_all_stones_many(25))

    def test_day11_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day11.txt')
        text = open(filename, 'r')
        s = advent2024.Day11.Solution(text.read())
        self.assertEqual(250783680217283, s.blink_all_stones_many(75))

    def test_day12_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day12_sample.txt')
        text = open(filename, 'r')
        s = advent2024.Day12.Solution(text.read())
        self.assertEqual({(0, 1), (0, 2), (0, 3), (0, 0)}, s.find_region(0, 0))        
        self.assertEqual({(0, 1), (0, 2), (0, 3), (0, 0)}, s.find_region(0, 1))
        self.assertEqual(140, s.part1())

    def test_day12_part1_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day12_sample_2.txt')
        text = open(filename, 'r')
        s = advent2024.Day12.Solution(text.read())
        self.assertEqual(772, s.part1())

    def test_day12_part1_3(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day12_sample_3.txt')
        text = open(filename, 'r')
        s = advent2024.Day12.Solution(text.read())
        self.assertEqual(1930, s.part1())

    def test_day12_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2024/day12.txt')
        text = open(filename, 'r')
        s = advent2024.Day12.Solution(text.read())
        self.assertEqual(1374934, s.part1())        
