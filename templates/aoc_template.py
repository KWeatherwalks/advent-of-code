# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""


def part1(data):
    """Solve part 1"""
    return


def part2(data):
    """Solve part 2"""
    return


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2021, day=2).input_data.split('\n')
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part='a', day=None, year=2021)
    submit(answer2, part='b', day=None, year=2021)
