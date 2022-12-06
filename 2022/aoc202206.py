# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")[0]


def part1(data):
    """Solve part 1"""
    
    # Window function
    window = data[:4]
    characters = 4
    while len(set(window)) != 4:
        # move window to the right
        window = window[1:] + data[characters]
        characters += 1

    return characters


def part2(data):
    """Solve part 2"""
    # Window function
    window = data[:14]
    characters = 14
    while len(set(window)) != 14:
        # move window to the right
        window = window[1:] + data[characters]
        characters += 1

    return characters


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2022, day=6).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part='a', day=6, year=2022)
    submit(answer2, part='b', day=6, year=2022)
