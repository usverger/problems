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



