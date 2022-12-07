import unittest
from typing import List
import python.advent2022 as advent2022

class TestAdvent2022(unittest.TestCase):
    
    def test_day07(self):
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