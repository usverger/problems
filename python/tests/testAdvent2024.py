import unittest
from typing import List
import python.advent2024 as advent2024
import os
from pathlib import Path
from itertools import permutations, combinations, combinations_with_replacement

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