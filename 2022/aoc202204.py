# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    pairs = [(x.split(",")) for x in puzzle_input.split("\n")]
    pairs = [list(map(lambda x: x.split("-"),p)) for p in pairs]  
    return [(set(range(int(x[0][0]), int(x[0][1])+1)),
             set(range(int(x[1][0]), int(x[1][1])+1))) for x in pairs]
    


def part1(data):
    """Solve part 1"""

    return sum([1 for pair in data 
            if (pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]))])


def part2(data):
    """Solve part 2"""
    return sum([1 for pair in data
            if pair[0].intersection(pair[1])])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2022, day=4).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part='a', day=4, year=2022)
    submit(answer2, part='b', day=4, year=2022)
