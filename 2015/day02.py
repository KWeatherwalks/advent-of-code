# aoc_template.py
# Modified from https://realpython.com/python-advent-of-code/#a-starting-template

from aocd import submit
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""
    wrapping_paper_needed = 0
    for box in data:
        # get dimensions
        l, w, h = [int(side_length) for side_length in box.split("x")]
        # calculate surface areas
        side1 = l * w
        side2 = w * h
        side3 = l * h
        extra_piece = min([side1, side2, side3])

        wrapping_paper_needed += 2 * (side1 + side2 + side3) + extra_piece

    return wrapping_paper_needed


def part2(data):
    """Solve part 2"""
    ribbon_needed = 0
    for box in data:
        # get dimensions
        l, w, h = [int(side_length) for side_length in box.split("x")]
        # calculate the ribbon needed to wrap the present
        ribbon_present = 2 * sum(sorted([l, w, h])[:2])
        # calculate the ribbon needed for the bow
        ribbon_bow = l * w * h
        # add to the total
        ribbon_needed += ribbon_bow + ribbon_present

    return ribbon_needed


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Connect to the API
    puzzle_input = Puzzle(year=2015, day=2).input_data
    # Solve
    answer1, answer2 = solve(puzzle_input)
    # Submit answers
    submit(answer1, part="a", day=2, year=2015)
    submit(answer2, part="b", day=2, year=2015)
