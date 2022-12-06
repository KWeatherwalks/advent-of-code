# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

import re

import numpy as np
from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    stacks, procedure = [(x.split("\n")) for x in puzzle_input.split("\n\n")]
    
    ## Transform input so stacks is a list of crate stacks with the bottom-most
    ##  element on the left of each stack
    stacks.reverse()
    stacks = np.array([list(x) for x in stacks]).transpose().tolist()
    stacks = ["".join(x[1:]) for x in stacks]
    stacks = [x.replace("[","").replace("]","").replace(" ","") for x in stacks]
    stacks = [x for x in stacks if x]

    ## Transform input so procedure is list of 3-tuples
    procedure = [list(map(int, re.findall(r'\d+', x))) for x in procedure]

    return stacks, procedure


def part1(data):
    """Solve part 1"""

    # assign variables to lists
    stacks, moves = data
    

    def move_crates(move):
        '''Helper function to move crates from one stack to another'''   
        n, origin, destination = move

        # pick up crates
        crates = stacks[origin-1][-n:]
        stacks[origin-1] = stacks[origin-1][:-n]
        # drop crates
        stacks[destination-1] += crates[::-1]


    # perform moving operation
    for move in moves:
        move_crates(move)

    # Return the crates at the top of each stack
    return "".join([x[-1] for x in stacks])


def part2(data):
    """Solve part 2"""
    # assign variables to lists
    stacks, moves = data


    def move_crates(move):
        '''Helper function to move crates from one stack to another'''   
        n, origin, destination = move

        # pick up crates
        crates = stacks[origin-1][-n:]
        stacks[origin-1] = stacks[origin-1][:-n]
        # drop crates
        stacks[destination-1] += crates


    # perform moving operation
    for move in moves:
        move_crates(move)

    # Return the crates at the top of each stack
    return "".join([x[-1] for x in stacks])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    solution1 = part1(parse(puzzle_input))
    solution2 = part2(parse(puzzle_input))

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2022, day=5).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part='a', day=5, year=2022)
    submit(answer2, part='b', day=5, year=2022)
