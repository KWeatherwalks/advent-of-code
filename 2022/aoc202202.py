# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return [round.replace(" ", "") for round in puzzle_input]


def part1(data):
    """Solve part 1"""
    print(data[:5])

    # comparison dictionary
    evaluator = {'AX': 1+3, 'AY': 2+6, 'AZ': 3+0,
                 'BX': 1+0, 'BY': 2+3, 'BZ': 3+6,
                 'CX': 1+6, 'CY': 2+0, 'CZ': 3+3}

    score = 0
    for round in data:
        score += evaluator[round]

    return score


def part2(data):
    """Solve part 2"""

    # comparison dictionary
    evaluator = {'AX': 3+0, 'AY': 1+3, 'AZ': 2+6,
                 'BX': 1+0, 'BY': 2+3, 'BZ': 3+6,
                 'CX': 2+0, 'CY': 3+3, 'CZ': 1+6}

    score = 0
    for round in data:
        score += evaluator[round]

    return score


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2022, day=2).input_data.split('\n')
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    # submit(answer1, part='a', day=2, year=2022)
    submit(answer2, part='b', day=2, year=2022)
