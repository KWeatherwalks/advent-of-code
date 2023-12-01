# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    return data.count("(") - data.count(")")


def part2(data):
    """Solve part 2"""
    counts = [0, 0]
    for position, p in enumerate(data, start=1):
        if p == "(":
            counts[0] += 1
        if p == ")":
            counts[1] += 1
        if counts[0] < counts[1]:
            return position


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2015, day=1).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part="a", day=1, year=2015)
    submit(answer2, part="b", day=1, year=2015)
