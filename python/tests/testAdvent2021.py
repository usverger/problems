import unittest
from typing import List
import python.advent2021 as advent2021
import os
from pathlib import Path
from itertools import permutations, combinations, combinations_with_replacement

class TestAdvent2021(unittest.TestCase):
    
    def test_day01_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day01_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day01.Solution(list(map(int, text.read().splitlines())))
        result = s.part1()
        self.assertEqual(7, result)

    def test_day01_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day01.txt')
        text = open(filename, 'r')
        s = advent2021.Day01.Solution(list(map(int, text.read().splitlines())))
        result = s.part1()
        self.assertEqual(1139, result)

    def test_day01_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day01_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day01.Solution(list(map(int, text.read().splitlines())))
        result = s.part2()
        self.assertEqual(5, result)

    def test_day01_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day01.txt')
        text = open(filename, 'r')
        s = advent2021.Day01.Solution(list(map(int, text.read().splitlines())))
        result = s.part2()
        self.assertEqual(1103, result)

    def test_day02_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day02_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day02.Solution(text.read().splitlines())
        result = s.work()
        self.assertEqual(150, result)

    def test_day02_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day02.txt')
        text = open(filename, 'r')
        s = advent2021.Day02.Solution(text.read().splitlines())
        result = s.work()
        self.assertEqual(1427868, result)

    def test_day02_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day02_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day02.Solution(text.read().splitlines())
        result = s.part2()
        self.assertEqual(900, result)

    def test_day02_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day02.txt')
        text = open(filename, 'r')
        s = advent2021.Day02.Solution(text.read().splitlines())
        result = s.part2()
        self.assertEqual(1568138742, result)

    def test_day03_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day03_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day03.Solution()
        result = s.part1(text.read().splitlines())
        self.assertEqual(198, result)

    def test_day03_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day03.txt')
        text = open(filename, 'r')
        s = advent2021.Day03.Solution()
        result = s.part1(text.read().splitlines())
        self.assertEqual(4174964, result)

    def test_day03_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day03_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day03.Solution()
        result = s.part2(text.read().splitlines())
        self.assertEqual(230, result)

    def test_day03_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day03.txt')
        text = open(filename, 'r')
        s = advent2021.Day03.Solution()
        result = s.part2(text.read().splitlines())
        self.assertEqual(4474944, result)

    def test_day04_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day04_sample.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day04.Solution(lines)
        result = s.first_winning()
        self.assertEqual(4512, result)

    def test_day04_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day04.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day04.Solution(lines)
        result = s.first_winning()
        self.assertEqual(21607, result)

    def test_day04_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day04_sample.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day04.Solution(lines)
        result = s.last_winning()
        self.assertEqual(1924, result)

    def test_day04_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day04.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day04.Solution(lines)
        result = s.last_winning()
        self.assertEqual(19012, result)

    def test_day05_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day05_sample.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day05.Solution(lines)
        result = s.solve()
        self.assertEqual(5, result)

    def test_day05_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day05.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day05.Solution(lines)
        result = s.solve()
        self.assertEqual(6710, result)

    def test_day05_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day05_sample.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day05.Solution(lines)
        result = s.solve_part2()
        self.assertEqual(12, result)

    def test_day05_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day05.txt')
        text = open(filename, 'r')
        lines = text.read().splitlines()
        s = advent2021.Day05.Solution(lines)
        result = s.solve_part2()
        self.assertEqual(20121, result)

    def test_day06_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day06_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day06.Solution(text.read())
        self.assertEqual(5, s.solve(0))
        self.assertEqual(5, s.solve(1))
        self.assertEqual(6, s.solve(2))
        self.assertEqual(26, s.solve(18))
        self.assertEqual(73, s.solve(29))
        self.assertEqual(5934, s.solve(80))
        self.assertEqual(6358, s.solve(81))
        self.assertEqual(7087, s.solve(82))
        # self.assertEqual(26984457539, s.solve(256))

    def test_day06_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day06.txt')
        text = open(filename, 'r')
        s = advent2021.Day06.Solution(text.read())
        self.assertEqual(362639, s.solve(80))

    def test_day06_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day06_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day06.Solution(text.read())

        self.assertEqual(5, s.solve_part2(0))
        self.assertEqual(5, s.solve_part2(1))
        self.assertEqual(6, s.solve_part2(2))
        self.assertEqual(26, s.solve_part2(18))
        self.assertEqual(73, s.solve_part2(29))
        self.assertEqual(5934, s.solve_part2(80))
        self.assertEqual(6358, s.solve_part2(81))
        self.assertEqual(7087, s.solve_part2(82))
        self.assertEqual(26984457539, s.solve_part2(256))

    def test_day06_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day06.txt')
        text = open(filename, 'r')
        s = advent2021.Day06.Solution(text.read())
        self.assertEqual(362639, s.solve_part2(80))
        self.assertEqual(1639854996917, s.solve_part2(256))        

    def test_day07_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day07_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day07.Solution(text.read())
        self.assertEqual(37, s.align_crabs())

    def test_day07_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day07.txt')
        text = open(filename, 'r')
        s = advent2021.Day07.Solution(text.read())
        self.assertEqual(344605, s.align_crabs())

    def test_day07_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day07_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day07.Solution(text.read())
        self.assertEqual(168, s.align_crabs_part2())

    def test_day07_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day07.txt')
        text = open(filename, 'r')
        s = advent2021.Day07.Solution(text.read())
        self.assertEqual(93699985, s.align_crabs_part2())

    def test_day08_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day08_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day08.Solution(text.read())
        self.assertEqual(26, s.part1())

    def test_day08_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day08.txt')
        text = open(filename, 'r')
        s = advent2021.Day08.Solution(text.read())
        self.assertEqual(274, s.part1())

    def test_day08_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day08_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day08.Solution(text.read())

        map = {'a': 'g', 'b': 'f', 'c': 'e', 'd': 'c', 'e': 'd', 'f': 'a', 'g': 'b'}
        self.assertEqual('abdefg', s.translate(map, 'facegb'))
        self.assertEqual(61229, s.part2_bruteforce())

    def test_day08_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day08.txt')
        text = open(filename, 'r')
        s = advent2021.Day08.Solution(text.read())
        self.assertEqual(1012089, s.part2_bruteforce())

    def test_day09_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day09_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day09.Solution(text.read())
        self.assertEqual(15, s.part1())

    def test_day09_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day09.txt')
        text = open(filename, 'r')
        s = advent2021.Day09.Solution(text.read())
        self.assertEqual(498, s.part1())

    def test_day09_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day09_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day09.Solution(text.read())
        self.assertEqual(1134, s.part2())

    def test_day09_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day09.txt')
        text = open(filename, 'r')
        s = advent2021.Day09.Solution(text.read())
        self.assertEqual(1071000, s.part2())
    
    def test_day10_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day10_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day10.Solution(text.read())
        self.assertEqual(26397, s.part1())

    def test_day10_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day10.txt')
        text = open(filename, 'r')
        s = advent2021.Day10.Solution(text.read())
        self.assertEqual(216297, s.part1())

    def test_day10_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day10_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day10.Solution(text.read())
        self.assertEqual(288957, s.part2())

    def test_day10_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day10.txt')
        text = open(filename, 'r')
        s = advent2021.Day10.Solution(text.read())
        self.assertEqual(2165057169, s.part2())

    def test_day11_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day11_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day11.Solution(text.read())
        self.assertEqual(1656, s.part1())

    def test_day11_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day11.txt')
        text = open(filename, 'r')
        s = advent2021.Day11.Solution(text.read())
        self.assertEqual(1688, s.part1())

    def test_day11_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day11_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day11.Solution(text.read())
        self.assertEqual(195, s.part2())

    def test_day11_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day11.txt')
        text = open(filename, 'r')
        s = advent2021.Day11.Solution(text.read())

        self.assertEqual(403, s.part2())

    def test_day12_part1(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(10, s.part1())

    def test_day12_part1_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12_sample_2.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(19, s.part1())

    def test_day12_part1_3(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12_sample_3.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(226, s.part1())

    def test_day12_part1_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(3463, s.part1())

    def test_day12_part2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12_sample.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(36, s.part2())

    def test_day12_part2_2(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12_sample_2.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(103, s.part2())

    def test_day12_part2_3(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12_sample_3.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(3509, s.part2())

    def test_day12_part2_puzzle(self):
        filename = os.path.join(os.path.dirname(__file__), 'testAdvent2021/day12.txt')
        text = open(filename, 'r')
        s = advent2021.Day12.Solution(text.read())
        self.assertEqual(91533, s.part2())




