# --- Day 9: Smoke Basin ---
# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves
# that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer.
# The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations.
# Most locations have four adjacent locations (up, down, left, and right);
# locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5),
# and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6.
# The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

# --- Part Two ---
# Next, you need to find the largest basins so you know what areas are most important to avoid.

# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin,
# although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations
# will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

# The top-left basin, size 3:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The top-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The middle basin, size 14:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The bottom-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

# What do you get if you multiply together the sizes of the three largest basins?

from typing import List
from collections import Counter
from itertools import permutations
from copy import deepcopy

class Solution:

    def __init__(self, file: str):
        lines = file.splitlines()
        self.heightmap = [list(map(int, list(l))) for l in lines]

    def get_low_points(self) -> List[tuple]:
        low_points = []
        for i in range(len(self.heightmap)):
            for j in range(len(self.heightmap[i])):
                if self.is_low_point(i, j):
                    low_points.append((self.heightmap[i][j], i, j))
        return low_points
    
    def is_low_point(self, i: int, j: int) -> bool:
        left = self.heightmap[i-1][j] if i > 0 else 9
        right = self.heightmap[i+1][j] if i < len(self.heightmap)-1 else 9
        top = self.heightmap[i][j-1] if j > 0 else 9
        bottom = self.heightmap[i][j+1] if j < len(self.heightmap[i])-1 else 9
        
        if self.heightmap[i][j] < min(left, right, top, bottom):
            return True
        return False
    
    def part1(self) -> int:
        return sum([x[0]+1 for x in self.get_low_points()])
    
    def get_basin(self, i: int, j: int) -> List[tuple]:
        """ (i, j) is expected to be a low point
        """

        visited = set()
        queue = [(i, j)]
        basin = []
        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited: continue

            visited.add((x, y))
            basin.append((x, y))

            if x > 0 and self.heightmap[x-1][y] > self.heightmap[x][y] and self.heightmap[x-1][y] < 9 and (x-1, y) not in visited:
                queue.append((x-1, y))
            if x < len(self.heightmap)-1 and self.heightmap[x+1][y] > self.heightmap[x][y] and self.heightmap[x+1][y] < 9 and (x+1, y) not in visited:
                queue.append((x+1, y))
            if y > 0 and self.heightmap[x][y-1] > self.heightmap[x][y] and self.heightmap[x][y-1] < 9 and (x, y-1) not in visited:
                queue.append((x, y-1))
            if y < len(self.heightmap[x])-1 and self.heightmap[x][y+1] > self.heightmap[x][y] and self.heightmap[x][y+1] < 9 and (x, y+1) not in visited:
                queue.append((x, y+1))

        return basin

    def part2(self) -> int:
        lengths = []
        for low_point in self.get_low_points():
            basin = self.get_basin(low_point[1], low_point[2])
            lengths.append(len(basin))
        lengths.sort()

        m = 1
        for i in range(min(3, len(lengths))):
            m *= lengths[-i-1]
        return m


