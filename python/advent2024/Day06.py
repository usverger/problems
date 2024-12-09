# --- Day 6: Guard Gallivant ---
# The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab...
# in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

# You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief.
# Unfortunately, a single guard is patrolling this part of the lab.

# Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

# You start by making a map (your puzzle input) of the situation. For example:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map).
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

# Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.
# Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

# ....#.....
# ....^....#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...
# Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

# ....#.....
# ........>#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#...
# Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#......v.
# ........#.
# #.........
# ......#...
# This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#........
# ........#.
# #.........
# ......#v..
# By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path.
# Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

# ....#.....
# ....XXXXX#
# ....X...X.
# ..#.X...X.
# ..XXXXX#X.
# ..X.X.X.X.
# .#XXXXXXX.
# .XXXXXXX#.
# #XXXXXXX..
# ......#X..
# In this example, the guard will visit 41 distinct positions on your map.

# Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?


# --- Part Two ---
# While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab.
# From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post
# on the walls of the closet.

# Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large
# for them to safely search the lab without getting caught.

# Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox.
# They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

# To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction.
# The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

# In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop.
# The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show
# a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

# Option one, put a printing press next to the guard's starting position:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ....|..#|.
# ....|...|.
# .#.O^---+.
# ........#.
# #.........
# ......#...
# Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:


# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ......O.#.
# #.........
# ......#...
# Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----+O#.
# #+----+...
# ......#...
# Option four, put an alchemical retroencabulator near the bottom left corner:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ..|...|.#.
# #O+---+...
# ......#...
# Option five, put the alchemical retroencabulator a bit to the right instead:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ....|.|.#.
# #..O+-+...
# ......#...
# Option six, put a tank of sovereign glue right next to the tank of universal solvent:

# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----++#.
# #+----++..
# ......#O..
# It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing.
# The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example,
# there are 6 different positions you could choose.

# You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?

from typing import List
import copy

class Solution:

    def __init__(self, input: str):
        lines = input.splitlines()
        self.map = []
        for line in lines:
            self.map.append(list(line))

        self.guard = self.locate_guard(self.map)

    def locate_guard(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] in '^<>v':
                    return (i,j)

    def print_map(self, map):
        for line in map:
            print(''.join(line))

    def move_one_up(self, map, guard) -> tuple:
        r,c = guard
        if r-1 < 0:
            # exit the map
            map[r][c] = 'X'
            return None
            
        elif map[r-1][c] == '#':
            # turn right
            map[r][c] = '>'
            return guard
            
        else:
            # move up
            map[r][c] = 'X'
            map[r-1][c] = '^'
            return (r-1,c)

    def move_one_right(self, map, guard) -> tuple:
        r,c = guard
        if c+1 >= len(map[r]):
            # exit the map
            map[r][c] = 'X'
            return None
            
        elif map[r][c+1] == '#':
            map[r][c] = 'v'
            return guard
            
        else:
            # move right
            map[r][c] = 'X'
            map[r][c+1] = '>'
            return (r,c+1)

    def move_one_down(self, map, guard) -> tuple:
        r,c = guard
        if r+1 >= len(map):
            # exit the map
            map[r][c] = 'X'
            return None
            
        elif map[r+1][c] == '#':
            map[r][c] = '<'
            return guard
            
        else:
            # move down
            map[r][c] = 'X'
            map[r+1][c] = 'v'
            return (r+1,c)

    def move_one_left(self, map, guard) -> tuple:
        r,c = guard
        if c-1 < 0:
            # exit the map
            map[r][c] = 'X'
            return None
            
        elif map[r][c-1] == '#':
            # turn right
            map[r][c] = '^'
            return guard
            
        else:
            # move left
            map[r][c] = 'X'
            map[r][c-1] = '<'
            return (r,c-1)

    def move_one(self, map, guard, path: set) -> tuple:
        r,c = guard
        d = map[r][c]
        path.add((r,c,d)) # store the path, coordinates and direction

        if d == '^':
            guard = self.move_one_up(map, guard)

        elif d == '>':
            guard = self.move_one_right(map, guard)
            
        elif d == 'v':
            guard = self.move_one_down(map, guard)
                
        elif d == '<':
            guard = self.move_one_left(map, guard)
        
        return guard

    def move_until_exit_or_loop(self, map, guard):
        path = set()
        while guard:
            r,c = guard
            truple = (r, c, map[r][c])
            if truple in path: # the guard has been here before, so it is a loop
                break
            
            guard = self.move_one(map, guard, path)
            #self.print_map(map)
            #print('')

        return guard

    def part1(self):
        self.move_until_exit_or_loop(self.map, self.guard)
        return sum([1 for line in self.map for c in line if c == 'X'])
    
    # def part2(self):
    #     path = set()
    #     guard = self.guard
    #     map = self.map
    #     possible_blocks = set()

    #     while guard:
    #         r,c = guard
            
    #         if map[r][c] == '^' and r-1 >= 0 and map[r-1][c] != '#':
    #             # create a copy of the map and move untul exit or loop is identified
    #             map_copy = [row[:] for row in map]
    #             map_copy[r-1][c] = '#'
    #             result = self.move_until_exit_or_loop(map_copy, (r,c))
    #             if result:
    #                 possible_blocks.add((r-1,c))

    #         elif map[r][c] == '>' and c+1 < len(map[r]) and map[r][c + 1] != '#':
    #             map_copy = [row[:] for row in map]
    #             map_copy[r][c+1] = '#'
    #             result = self.move_until_exit_or_loop(map_copy, (r,c))
    #             if result:
    #                 possible_blocks.add((r,c+1))

    #         elif map[r][c] == 'v' and r+1 < len(map) and map[r+1][c] != '#':
    #             map_copy = [row[:] for row in map]
    #             map_copy[r+1][c] = '#'
    #             result = self.move_until_exit_or_loop(map_copy, (r,c))
    #             if result:
    #                 possible_blocks.add((r+1,c))
            
    #         elif map[r][c] == '<' and c-1 >= 0 and map[r][c-1] != '#':
    #             map_copy = [row[:] for row in map]
    #             map_copy[r][c-1] = '#'
    #             result = self.move_until_exit_or_loop(map_copy, (r,c))
    #             if result:
    #                 possible_blocks.add((r,c-1))            

    #         self.print_map(map_copy)
    #         print('')
    #         guard = self.move_one(map, guard, path)

    #     return len(possible_blocks)

    def part2(self):
        '''
        just try all possible positions to place and simply simulate again
        '''

        possible_blocks = set()

        # run once first to see what coordinates we never visited anyway
        first_run_map = [row[:] for row in self.map]
        self.move_until_exit_or_loop(first_run_map, self.guard)

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):

                if self.map[i][j] == '#': continue
                if (i,j) == self.guard: continue
                if first_run_map[i][j] == '.': continue
                
                map_copy = [row[:] for row in self.map]
                map_copy[i][j] = '#'

                result = self.move_until_exit_or_loop(map_copy, self.guard)
                if result:
                    possible_blocks.add((i,j))

        # print(possible_blocks)
        return len(possible_blocks)