# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from math import prod

import numpy as np
from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    puzzle_input = [list(map(int, x)) for x in puzzle_input.split("\n")]
    return np.array(puzzle_input)


def is_visible(x,y,grid):
    """Return whether or not tree with coordinates (x,y) is visible"""
    
    tree_height = grid[x,y]
    
    # horizontal
    left, right = grid[x,:y], grid[x,y+1:]
    horizontal = (tree_height > int(max(left))) | (tree_height > int(max(right)))
    
    # vertical
    top, bottom = grid[:x,y], grid[x+1:,y]
    vertical = (tree_height > int(max(top))) | (tree_height > int(max(bottom)))
    
    return bool(horizontal | vertical)


def count_trees(height, array):
    """Count number of trees until """
    result = np.argwhere(array >= height)
    return array.size if not result.size else int(result[0])+1


def scenic_score(x,y,grid):
    """Calculate the scenic score for a tree at coordinate (x,y)"""
    tree_height = grid[x,y]

    # horizontal
    left, right = grid[x,:y], grid[x,y+1:]
    # vertical
    top, bottom = grid[:x,y], grid[x+1:,y]

    return prod(list(map(count_trees, 
            (tree_height,)*4,
            (left[::-1], right, top[::-1], bottom),
            )))

def part1(data):
    """Solve part 1"""
    return sum(
        [is_visible(x,y,data) for x in range(1,data.shape[0]-1) 
                        for y in range(1,data.shape[1]-1)]
        ) + 2*(data.shape[0] + data.shape[1] - 2)


def part2(data):
    """Solve part 2"""
    
    return max(
        [scenic_score(x,y,data) for x in range(1,data.shape[0]-1)
                            for y in range(1,data.shape[0]-1)]
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2022, day=8).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part='a', day=8, year=2022)
    submit(answer2, part='b', day=8, year=2022)
